#!/usr/bin/env python3
"""Pre-release audit for the public Finite Contact Theory repository.

The audit is intentionally conservative. It catches common release hygiene
failures without trying to decide whether a theory claim is correct.
"""

from __future__ import annotations

import re
import subprocess
import sys
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SELF = Path("scripts/release_audit.py")

TEXT_SUFFIXES = {
    ".cff",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}

SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    ".venv",
    "venv",
}

REQUIRED_FILES = [
    "README.md",
    "LICENSE.md",
    "CITATION.cff",
    "RELEASE-NOTES-v0.1.0.md",
    "docs/mathematical-core.md",
    "docs/public-claim-register.md",
    "docs/theorem-bank.md",
    "docs/correction-ledger.md",
    "docs/release-roadmap.md",
    "papers/finite-contact-theory-v0.1.md",
    "verification/evidence-manifest.md",
    "verification/scripts/run_all.py",
]

STALE_HOLD_STATUS = [
    "pending campaign 10",
    "hold pending campaign 10",
    "until campaign 10",
    "final wording pending campaign 10",
]

# Internal-process codenames that must never appear in the public repository.
CODENAME_PATTERNS = [
    r"\bfable\b",
]

PRIVATE_PATH_PATTERNS = [
    r"[A-Za-z]:\\",
    r"appdata",
    r"\.codex",
    r"claude",
    r"scratchpad",
    r"\bfable/",
]

OVERCLAIM_PATTERNS = [
    (
        "all quantum mechanics",
        {
            Path("README.md"),
            Path("docs/how-to-read.md"),
            Path("docs/public-claim-register.md"),
            Path("docs/release-roadmap.md"),
            Path("docs/theorem-bank.md"),
            Path("papers/finite-contact-theory-v0.1.md"),
        },
    ),
    (
        "floor derives all quantum theory",
        {
            Path("docs/public-claim-register.md"),
        },
    ),
    (
        "floor selects the quantum boundary in every scenario",
        {
            Path("docs/hold-register.md"),
        },
    ),
    ("solves gravity", {Path("docs/release-roadmap.md")}),
    ("complete theory", {Path("docs/release-roadmap.md")}),
    ("selects the boundary", {Path("docs/release-roadmap.md")}),
]

ALLOWLIST = {
    "private_path": {
        Path("docs/release-roadmap.md"),
        SELF,
    },
    "stale_hold_status": {
        Path("docs/release-roadmap.md"),
        SELF,
    },
    "codename": {
        SELF,
    },
}


class AuditFailure(Exception):
    """Raised when a release audit check fails."""


def rel(path: Path) -> Path:
    return path.relative_to(ROOT)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def run_command(name: str, command: list[str]) -> None:
    print(f"[RUN] {name}: {' '.join(command)}")
    proc = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.stdout:
        print(proc.stdout.rstrip())
    if proc.returncode != 0:
        raise AuditFailure(f"{name} failed with exit code {proc.returncode}")
    print(f"[PASS] {name}")


def check_required_files() -> None:
    missing = [file for file in REQUIRED_FILES if not (ROOT / file).is_file()]
    if missing:
        raise AuditFailure("missing required files: " + ", ".join(missing))
    print(f"[PASS] required files present ({len(REQUIRED_FILES)})")


def check_metadata() -> None:
    citation = read_text(ROOT / "CITATION.cff")
    license_text = read_text(ROOT / "LICENSE.md")

    required_citation_bits = [
        'title: "Finite Contact Theory v0.1: Growing the Bell/CHSH Quantum Boundary from a Finite One-Use Floor"',
        'family-names: "Douglas"',
        'given-names: "Seth"',
        'orcid: "https://orcid.org/0009-0007-4708-3252"',
        'repository-code: "https://github.com/Apsiape/finite-contact-theory-public"',
    ]
    # Version may be the pre-release (0.1.0-pre) or the DOI-stamped tag (0.1.0).
    # This tolerates the planned bump so the mint step does not fail the gate.
    if not re.search(r'^version: "0\.1\.0(-pre)?"$', citation, flags=re.MULTILINE):
        raise AuditFailure('CITATION.cff version must be "0.1.0-pre" or "0.1.0"')
    missing = [bit for bit in required_citation_bits if bit not in citation]
    if missing:
        raise AuditFailure("CITATION.cff missing expected fields: " + "; ".join(missing))

    if "CC BY-NC-ND 4.0" not in license_text:
        raise AuditFailure("LICENSE.md does not state the CC BY-NC-ND 4.0 license")

    print("[PASS] citation and rights metadata")


def scan_for_terms(
    label: str,
    terms: list[str],
    *,
    allowed_files: set[Path],
    regex: bool = False,
) -> None:
    hits: list[str] = []
    allowed_hits: list[str] = []

    for path in iter_text_files():
        relative = rel(path)
        if relative == SELF:
            continue
        text = read_text(path)
        haystack = text.lower()

        for term in terms:
            found = bool(re.search(term, haystack, flags=re.IGNORECASE)) if regex else term in haystack
            if not found:
                continue
            target = allowed_hits if relative in allowed_files else hits
            target.append(f"{relative}: {term}")

    for hit in allowed_hits:
        print(f"[ALLOW] {label}: {hit}")

    if hits:
        raise AuditFailure(f"{label} hits outside allowlist:\n  " + "\n  ".join(hits))

    print(f"[PASS] {label}")


CANONICAL_CEILING = (
    "Finite Contact Theory is a finite reconstruction program with a scoped "
    "theorem stack — from one-use contact to counting, to one-receiver gluing, "
    "to rational Born weights, to the CHSH/Pell boundary, to a carrier grammar "
    "grown from one-use contact — under which the quantum boundary is a floor "
    "theorem at binary-Bell finite-carrier scope, with every unearned "
    "generalization left open by name."
)

CEILING_FILES = [
    "README.md",
    "papers/finite-contact-theory-v0.1.md",
    "docs/public-claim-register.md",
    "RELEASE-NOTES-v0.1.0.md",
]


def check_canonical_ceiling() -> None:
    """The one-claim ceiling must appear verbatim in every advertised location."""
    def normalize(text: str) -> str:
        text = text.replace("**", "").replace("> ", " ")
        return re.sub(r"\s+", " ", text)

    target = normalize(CANONICAL_CEILING)
    missing = [f for f in CEILING_FILES if target not in normalize(read_text(ROOT / f))]
    if missing:
        raise AuditFailure("canonical ceiling missing/altered in: " + ", ".join(missing))
    print(f"[PASS] canonical ceiling verbatim in {len(CEILING_FILES)} files")


def check_overclaims() -> None:
    hits: list[str] = []
    allowed_hits: list[str] = []

    for path in iter_text_files():
        relative = rel(path)
        if relative == SELF:
            continue
        haystack = read_text(path).lower()
        for phrase, allowed_files in OVERCLAIM_PATTERNS:
            if phrase in haystack:
                target = allowed_hits if relative in allowed_files else hits
                target.append(f"{relative}: {phrase}")

    for hit in allowed_hits:
        print(f"[ALLOW] overclaim caveat/example: {hit}")

    if hits:
        raise AuditFailure("overclaim phrase hits outside allowlist:\n  " + "\n  ".join(hits))

    print("[PASS] overclaim phrase scan")


def check_markdown_links() -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    broken: list[str] = []

    for path in iter_text_files():
        if path.suffix.lower() != ".md":
            continue
        relative = rel(path)
        text = read_text(path)
        for match in link_pattern.finditer(text):
            target = match.group(1).strip("<>")
            target_lower = target.lower()
            if (
                target.startswith("#")
                or target_lower.startswith("http://")
                or target_lower.startswith("https://")
                or target_lower.startswith("mailto:")
                or "://" in target
            ):
                continue

            clean_target = urllib.parse.unquote(target.split("#", 1)[0])
            if not clean_target:
                continue

            resolved = (path.parent / clean_target).resolve()
            if not str(resolved).lower().startswith(str(ROOT).lower()):
                broken.append(f"{relative}: link escapes repository: {target}")
            elif not resolved.exists():
                broken.append(f"{relative}: missing local link target: {target}")

    if broken:
        raise AuditFailure("local Markdown link failures:\n  " + "\n  ".join(broken))

    print("[PASS] local Markdown links")


def main() -> int:
    try:
        check_required_files()
        check_metadata()
        scan_for_terms(
            "stale hold-status language",
            STALE_HOLD_STATUS,
            allowed_files=ALLOWLIST["stale_hold_status"],
        )
        scan_for_terms(
            "internal-process codename",
            CODENAME_PATTERNS,
            allowed_files=ALLOWLIST["codename"],
            regex=True,
        )
        scan_for_terms(
            "private path/scratchpad language",
            PRIVATE_PATH_PATTERNS,
            allowed_files=ALLOWLIST["private_path"],
            regex=True,
        )
        check_canonical_ceiling()
        check_overclaims()
        check_markdown_links()
        run_command("shipped verification", [sys.executable, "verification/scripts/run_all.py"])
        run_command("git whitespace check", ["git", "diff", "--check"])
    except AuditFailure as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    print("\nPUBLIC RELEASE AUDIT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
