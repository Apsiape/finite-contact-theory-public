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
    "EVOLUTION.md",
    "RELEASE-NOTES-v0.1.0.md",
    "RELEASE-NOTES-v0.2.0.md",
    "RELEASE-NOTES-v0.3.0.md",
    "RELEASE-NOTES-v0.4.0.md",
    "RELEASE-NOTES-v0.5.0.md",
    "RELEASE-NOTES-v0.6.0.md",
    "RELEASE-NOTES-v0.7.0.md",
    "RELEASE-NOTES-v0.8.0.md",
    "RELEASE-NOTES-v0.9.0.md",
    "RELEASE-NOTES-v0.10.0.md",
    "RELEASE-NOTES-v0.11.0.md",
    "RELEASE-NOTES-v0.12.0.md",
    "docs/mathematical-core.md",
    "docs/public-claim-register.md",
    "docs/theorem-bank.md",
    "docs/correction-ledger.md",
    "docs/release-roadmap.md",
    "docs/release-checklist.md",
    "papers/finite-contact-theory-v0.1.md",
    "papers/02-behavior-conditioned-capacity/paper.md",
    "papers/02-behavior-conditioned-capacity/claims.md",
    "papers/02-behavior-conditioned-capacity/RELEASE.md",
    "papers/03-identifiability-and-debt/paper.md",
    "papers/03-identifiability-and-debt/claims.md",
    "papers/03-identifiability-and-debt/RELEASE.md",
    "papers/04-inquiry-calculus/paper.md",
    "papers/04-inquiry-calculus/claims.md",
    "papers/04-inquiry-calculus/RELEASE.md",
    "papers/05-becoming-webs/paper.md",
    "papers/05-becoming-webs/claims.md",
    "papers/05-becoming-webs/RELEASE.md",
    "papers/06-measured-floor/paper.md",
    "papers/06-measured-floor/claims.md",
    "papers/06-measured-floor/RELEASE.md",
    "papers/07-program-map/paper.md",
    "papers/07-program-map/claims.md",
    "papers/07-program-map/RELEASE.md",
    "papers/08-nonexact-return/paper.md",
    "papers/08-nonexact-return/claims.md",
    "papers/08-nonexact-return/RELEASE.md",
    "papers/09-multifloor-worldweave/paper.md",
    "papers/09-multifloor-worldweave/claims.md",
    "papers/09-multifloor-worldweave/RELEASE.md",
    "papers/10-negative-gram-holonomy/paper.md",
    "papers/10-negative-gram-holonomy/claims.md",
    "papers/10-negative-gram-holonomy/RELEASE.md",
    "papers/11-mixed-state-exclusion/paper.md",
    "papers/11-mixed-state-exclusion/claims.md",
    "papers/11-mixed-state-exclusion/RELEASE.md",
    "papers/12-count-regions/paper.md",
    "papers/12-count-regions/claims.md",
    "papers/12-count-regions/RELEASE.md",
    "verification/evidence-manifest.md",
    "verification/scripts/run_all.py",
    "verification/scripts/exact_gap_certificate.py",
    "verification/scripts/nonexact_return_reconstruction.py",
    "verification/scripts/multifloor_worldweave.py",
    "verification/scripts/forcing_audit.py",
    "verification/scripts/wcd_actualization.py",
    "verification/scripts/negative_gram_holonomy.py",
    "verification/scripts/mixed_state_exclusion.py",
    "verification/scripts/count_regions.py",
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
    ("theory of everything", set()),
    ("proves the universal born rule", set()),
    ("derives all of physics", set()),
    ("derives einstein gravity", set()),
    ("unifies all forces", set()),
    ("gauge group of nature", set()),
    # Divergence-line guards: the negative-Gram prediction is CONDITIONAL and
    # experiment-open. These settled-discovery phrasings must never appear.
    ("disproves quantum mechanics", set()),
    ("refutes quantum mechanics", set()),
    ("quantum mechanics is falsified", set()),
    ("experimentally confirmed violation", set()),
    ("we have discovered", set()),
    ("an experimental discovery", set()),
    ("nature violates hilbert", set()),
    ("observed a negative gram", set()),
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
        'title: "Finite Contact Theory v0.',
        'family-names: "Douglas"',
        'given-names: "Seth"',
        'orcid: "https://orcid.org/0009-0007-4708-3252"',
        'repository-code: "https://github.com/Apsiape/finite-contact-theory-public"',
    ]
    # Version may be a pre-release ("0.X.0-pre") or a DOI-stamped tag ("0.X.0").
    # This tolerates the planned bump so the mint step does not fail the gate.
    if not re.search(r'^version: "0\.\d+\.\d+(-pre)?"$', citation, flags=re.MULTILINE):
        raise AuditFailure('CITATION.cff version must be a "0.X.Y" or "0.X.Y-pre" string')
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


# Each released ceiling is checked verbatim in its advertised locations. The
# v0.1, v0.2, and v0.7 ceilings live on unchanged in their frozen chapters and
# notes; the live (v0.8) ceiling controls the README, the claim register, the
# chapter-8 paper, and the v0.8.0 release notes.
CANONICAL_CEILINGS = [
    (
        "v0.1",
        (
            "Finite Contact Theory is a finite reconstruction program with a scoped "
            "theorem stack — from one-use contact to counting, to one-receiver gluing, "
            "to rational Born weights, to the CHSH/Pell boundary, to a carrier grammar "
            "grown from one-use contact — under which the quantum boundary is a floor "
            "theorem at binary-Bell finite-carrier scope, with every unearned "
            "generalization left open by name."
        ),
        [
            "papers/finite-contact-theory-v0.1.md",
            "RELEASE-NOTES-v0.1.0.md",
        ],
    ),
    (
        "v0.2",
        (
            "Finite Contact Theory is a finite reconstruction program with a scoped "
            "theorem stack — from one-use contact to counting, to one-receiver gluing, "
            "to rational Born weights, to the CHSH/Pell boundary, to a carrier grammar "
            "grown from one-use contact, to a behavior-conditioned contextual capacity "
            "with an exact strict preparation gap — under which the quantum boundary is "
            "a floor theorem at binary-Bell finite-carrier scope, the preparation gap "
            "is an exact theorem at KCBS-pentagon scope, and every unearned "
            "generalization is left open by name."
        ),
        [
            "papers/02-behavior-conditioned-capacity/paper.md",
            "RELEASE-NOTES-v0.2.0.md",
        ],
    ),
    (
        "v0.7",
        (
            "Finite Contact Theory is a finite reconstruction program with a scoped "
            "theorem stack on two published axes — a quantum-facing axis, from one-use "
            "contact to counting, one-receiver gluing, rational Born weights, the "
            "CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a "
            "behavior-conditioned contextual capacity with an exact strict preparation "
            "gap; and a finite-epistemics axis, from the identifiability and debt "
            "calculus to the inquiry calculus and its second law of asking, four "
            "theorems separating the structure of time, and a measured generative "
            "floor — under which the quantum boundary is a floor theorem at "
            "binary-Bell finite-carrier scope, the preparation gap is an exact "
            "theorem at KCBS-pentagon scope, every epistemics and time result is a "
            "finite machine-checked theorem or a fenced measurement at its stated "
            "model scope, and every unearned generalization is left open by name."
        ),
        [
            "papers/07-program-map/paper.md",
            "RELEASE-NOTES-v0.7.0.md",
        ],
    ),
    (
        "v0.8",
        (
            "Finite Contact Theory is a finite reconstruction program with a scoped "
            "theorem stack on three published lines — a quantum-facing axis, from "
            "one-use contact to counting, one-receiver gluing, rational Born weights, "
            "the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and "
            "a behavior-conditioned contextual capacity with an exact strict "
            "preparation gap; a finite-epistemics axis, from the identifiability and "
            "debt calculus to the inquiry calculus and its second law of asking, four "
            "theorems separating the structure of time, and a measured generative "
            "floor; and a contact-interface reconstruction, in which a retained "
            "interface forces a quaternionic state/receiver cell whose self-dual "
            "closure is the 24-cell and the F_4 root system and whose finite "
            "measurement calculus forces the quadratic Born frame rule (a finite "
            "Gleason theorem) exactly where a global noncontextual assignment is "
            "impossible (a triality Kochen-Specker obstruction) — under which the "
            "quantum boundary is a floor theorem at binary-Bell finite-carrier scope, "
            "the preparation gap is an exact theorem at KCBS-pentagon scope, the "
            "interface reconstruction is a finite model-scope recovery on a "
            "real-quantum cell, and every unearned generalization — complex quantum "
            "mechanics, the actuality of one outcome, the universal Born rule, and "
            "every nature-facing prediction — is left open by name."
        ),
        [
            "papers/08-nonexact-return/paper.md",
            "RELEASE-NOTES-v0.8.0.md",
        ],
    ),
    (
        "v0.9",
        'Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named positive, integral, triality-covariant, self-dual, and delocalizing receiver laws while a forcing audit proves those laws are not selected by the floor over matched lawful alternatives — so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, and every nature-facing prediction — is left open by name.',
        [
            "papers/09-multifloor-worldweave/paper.md",
            "RELEASE-NOTES-v0.9.0.md",
        ],
    ),
    (
        "v0.10",
        'Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input — and a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the accessible-positivity theorem is unconditional while its physical realization is a conditional, bridge-premise-gated prediction awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, and whether nature contains the odd identity-holonomy sector — is left open by name; this chapter is an archival priority record of a mathematically closed conditional prediction, not an empirical discovery.',
        [
            "papers/10-negative-gram-holonomy/paper.md",
            "RELEASE-NOTES-v0.10.0.md",
        ],
    ),
    (
        "v0.11",
        'Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input — and a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the accessible-positivity and mixed-state exclusion theorems are unconditional while the physical realization is a conditional, bridge-premise-gated prediction awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, and whether the apparatus nuisances close the full exclusion — is left open by name; this chapter is an archival priority record of mathematically closed theorems and a conditional prediction, not an empirical discovery.',
        [
            "papers/11-mixed-state-exclusion/paper.md",
            "RELEASE-NOTES-v0.11.0.md",
        ],
    ),
    (
        "v0.12",
        'Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.',
        [
            "README.md",
            "docs/public-claim-register.md",
            "papers/12-count-regions/paper.md",
            "RELEASE-NOTES-v0.12.0.md",
        ],
    ),
]


def check_canonical_ceiling() -> None:
    """Every released ceiling must appear verbatim in its advertised locations."""
    def normalize(text: str) -> str:
        text = text.replace("**", "").replace("> ", " ")
        return re.sub(r"\s+", " ", text)

    total = 0
    for name, ceiling, files in CANONICAL_CEILINGS:
        target = normalize(ceiling)
        missing = [f for f in files if target not in normalize(read_text(ROOT / f))]
        if missing:
            raise AuditFailure(
                f"canonical ceiling ({name}) missing/altered in: " + ", ".join(missing)
            )
        total += len(files)
    print(f"[PASS] canonical ceilings verbatim in {total} files")


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
