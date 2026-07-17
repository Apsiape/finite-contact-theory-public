#!/usr/bin/env python3
"""Pre-release audit for the public Finite Contact Theory repository.

The audit is intentionally conservative. It catches common release hygiene
failures without trying to decide whether a theory claim is correct.
"""

from __future__ import annotations

import json
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
    "papers/20-observers-price/paper.md",
    "papers/20-observers-price/claims.md",
    "papers/20-observers-price/RELEASE.md",
    "papers/20-observers-price/verification/observers_price.py",
    "papers/21-genesis-of-space/paper.md",
    "papers/21-genesis-of-space/claims.md",
    "papers/21-genesis-of-space/RELEASE.md",
    "papers/21-genesis-of-space/verification/genesis_of_space.py",
    "papers/22-price-of-chance/paper.md",
    "papers/22-price-of-chance/claims.md",
    "papers/22-price-of-chance/RELEASE.md",
    "papers/22-price-of-chance/verification/price_of_chance.py",
    "verification/scripts/observers_price.py",
    "verification/scripts/genesis_of_space.py",
    "verification/scripts/price_of_chance.py",
    "RELEASE-NOTES-v0.19.0.md",
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
    "RELEASE-NOTES-v0.13.0.md",
    "RELEASE-NOTES-v0.14.0.md",
    "RELEASE-NOTES-v0.15.0.md",
    "RELEASE-NOTES-v0.16.0.md",
    "RELEASE-NOTES-v0.17.0.md",
    "RELEASE-NOTES-v0.18.0.md",
    "docs/mathematical-core.md",
    "docs/related-work-linear-optics.md",
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
    "papers/13-floor-to-interface/paper.md",
    "papers/13-floor-to-interface/claims.md",
    "papers/13-floor-to-interface/RELEASE.md",
    "papers/14-atlas-of-floors/paper.md",
    "papers/14-atlas-of-floors/claims.md",
    "papers/14-atlas-of-floors/RELEASE.md",
    "papers/15-ladder-of-scars/paper.md",
    "papers/15-ladder-of-scars/claims.md",
    "papers/15-ladder-of-scars/RELEASE.md",
    "papers/16-debt-ledger/paper.md",
    "papers/16-debt-ledger/claims.md",
    "papers/16-debt-ledger/RELEASE.md",
    "papers/17-mint-and-bill/paper.md",
    "papers/17-mint-and-bill/claims.md",
    "papers/17-mint-and-bill/RELEASE.md",
    "papers/18-emergent-hierarchy/paper.md",
    "papers/18-emergent-hierarchy/claims.md",
    "papers/18-emergent-hierarchy/RELEASE.md",
    "papers/19-seventh-attempt/paper.md",
    "papers/19-seventh-attempt/claims.md",
    "papers/19-seventh-attempt/RELEASE.md",
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
    "verification/scripts/floor_to_interface.py",
    "verification/scripts/atlas_of_floors.py",
    "verification/scripts/ladder_of_scars.py",
    "verification/scripts/debt_ledger.py",
    "verification/scripts/mint_and_bill.py",
    "verification/scripts/emergent_hierarchy.py",
    "verification/scripts/seventh_attempt.py",
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

    zen = json.loads(read_text(ROOT / ".zenodo.json"))
    m = re.search(r'^version: "([^"]+)"$', citation, flags=re.MULTILINE)
    cff_version = m.group(1).replace("-pre", "") if m else ""
    if zen.get("version") != cff_version:
        raise AuditFailure(
            f".zenodo.json version {zen.get('version')!r} does not match "
            f"CITATION.cff version {cff_version!r} -- Zenodo will mint the "
            f"deposit with stale metadata (the v0.3-v0.7 drift gotcha)"
        )
    if "v0." + cff_version.split(".")[1] not in zen.get("title", ""):
        raise AuditFailure(".zenodo.json title does not match the release version")

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
            "papers/12-count-regions/paper.md",
            "RELEASE-NOTES-v0.12.0.md",
        ],
    ),
    (
        "v0.14",
        'Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem now closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.',
        [
            "papers/13-floor-to-interface/paper.md",
            "RELEASE-NOTES-v0.14.0.md",
        ],
    ),
    (
        "v0.15",
        'Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit, and in which an atlas of generative floors now classifies what any floor can carry: order-writability and residue-retention are independent, presentation-relative capabilities whose four cells are exemplified and fenced by exact theorems — lattice floors are orderless in their settled states, reversible floors write order but can never scar, commutative creation scars without order, and the marks floor carries both — with the retained contact containing an exact one-mode fermionic kernel whose complex structure is the central square root of minus one, a retention tower computed through third order (a unique first-order scar class, four second-order classes read by a gauge-invariant bracket witness, and exactly one third-order class), and the measurement obstruction relocated: no equivariant selector from the law quotient to its history space exists, the retained bit is tomographically silent at law level yet certainty-grade to a scar reader, and promoting a registration into the law-state lifts prediction from exact chance to certainty — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the atlas capability theorems, the tower censuses, and the relocation model are exact, shipped, and presentation-relative by stated scope while the boundary-layer measurements are cited from the research corpus and nature is not claimed to realize any particular cell, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.',
        [
            "papers/14-atlas-of-floors/paper.md",
            "RELEASE-NOTES-v0.15.0.md",
        ],
    ),
    (
        "v0.16",
        "Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit, and in which an atlas of generative floors now classifies what any floor can carry: order-writability and residue-retention are independent, presentation-relative capabilities whose four cells are exemplified and fenced by exact theorems — lattice floors are orderless in their settled states, reversible floors write order but can never scar, commutative creation scars without order, and the marks floor carries both — with the retained contact containing an exact one-mode fermionic kernel whose complex structure is the central square root of minus one, a retention tower computed through third order (a unique first-order scar class, four second-order classes read by a gauge-invariant bracket witness, and exactly one third-order class), and the measurement obstruction relocated: no equivariant selector from the law quotient to its history space exists, the retained bit is tomographically silent at law level yet certainty-grade to a scar reader, and promoting a registration into the law-state lifts prediction from exact chance to certainty — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — a sixth line reading the obstruction tower itself: the retention tower of the four-mark contact group is one ladder of gauge-invariant witnesses, in which the unique fourth-order class is the retention class cup-squared and is read as value one by a quadruple involutive self-contact, the involution-silent third-order class is read by an explicit twenty-five-word cycle witness, the no-global-now of the time chapter and the no-outcome-selector of the interface chapters are adjacent instances of one torsor-obstruction pattern with the arrow of time strictly below the whole tower as act-monoid non-invertibility, the retention cover itself is first-order-scar-free yet carries exactly one coherence scar whose reading requires a four-word composite cycle, and a boundary-pinning theorem shows that every Hilbert carrier with two-dimensional twisted sectors pins the odd identity-holonomy class at the trine overlap one-half exactly — explaining the r = 1/2 saturation of current photonic experiments, placing the registered r = 3/5 bet exactly one contact beyond every such carrier, and making overlap rigidity and the fourth contact count-level witnesses of the carrier grade — and a seventh line, an exact combinatorial debt ledger built from counting alone: no fixed carrier reversibly absorbs a merging act, one fresh one-use register per step always does, the minimal register alphabet is exactly the largest merge multiplicity, distinction is never destroyed unpaid — existence bits equal surviving bits plus paid bits, with waste possible and theft impossible — the n-fork's collapse cost, question depth, and record alphabet are one number log2 n, and every completion that resolves a staged fork books exactly that price, so the no-selector law is a refused debt and lawlike evolution is exactly the debt-free sector — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the atlas capability theorems, the tower censuses, and the relocation model are exact, shipped, and presentation-relative by stated scope while the boundary-layer measurements are cited from the research corpus and nature is not claimed to realize any particular cell, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, the ladder witnesses and second-storey censuses are exact and shipped with their classical cohomology dimensions and the torsor pattern cited as known rather than claimed, the debt-ledger theorems are exact finite counting whose component results are classical and cited — with the contribution claimed only for the witness suite, the capability separation of the arrow, the pinning consequences, and the pre-probabilistic derivation route of the selection price — while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, whether any physical carrier realizes the pinned or the floppy grade, whether the combinatorial act-price is met by any measured dissipation rate, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.",
        [
            "papers/15-ladder-of-scars/paper.md",
            "papers/16-debt-ledger/paper.md",
            "RELEASE-NOTES-v0.16.0.md",
        ],
    ),
    (
        "v0.17",
        "Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit, and in which an atlas of generative floors now classifies what any floor can carry: order-writability and residue-retention are independent, presentation-relative capabilities whose four cells are exemplified and fenced by exact theorems — lattice floors are orderless in their settled states, reversible floors write order but can never scar, commutative creation scars without order, and the marks floor carries both — with the retained contact containing an exact one-mode fermionic kernel whose complex structure is the central square root of minus one, a retention tower computed through third order (a unique first-order scar class, four second-order classes read by a gauge-invariant bracket witness, and exactly one third-order class), and the measurement obstruction relocated: no equivariant selector from the law quotient to its history space exists, the retained bit is tomographically silent at law level yet certainty-grade to a scar reader, and promoting a registration into the law-state lifts prediction from exact chance to certainty — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — a sixth line reading the obstruction tower itself: the retention tower of the four-mark contact group is one ladder of gauge-invariant witnesses, in which the unique fourth-order class is the retention class cup-squared and is read as value one by a quadruple involutive self-contact, the involution-silent third-order class is read by an explicit twenty-five-word cycle witness, the no-global-now of the time chapter and the no-outcome-selector of the interface chapters are adjacent instances of one torsor-obstruction pattern with the arrow of time strictly below the whole tower as act-monoid non-invertibility, the retention cover itself is first-order-scar-free yet carries exactly one coherence scar whose reading requires a four-word composite cycle, and a boundary-pinning theorem shows that every Hilbert carrier with two-dimensional twisted sectors pins the odd identity-holonomy class at the trine overlap one-half exactly — explaining the r = 1/2 saturation of current photonic experiments, placing the registered r = 3/5 bet exactly one contact beyond every such carrier, and making overlap rigidity and the fourth contact count-level witnesses of the carrier grade — and a seventh line, an exact combinatorial debt ledger built from counting alone: no fixed carrier reversibly absorbs a merging act, one fresh one-use register per step always does, the minimal register alphabet is exactly the largest merge multiplicity, distinction is never destroyed unpaid — existence bits equal surviving bits plus paid bits, with waste possible and theft impossible — the n-fork's collapse cost, question depth, and record alphabet are one number log2 n, and every completion that resolves a staged fork books exactly that price, so the no-selector law is a refused debt and lawlike evolution is exactly the debt-free sector — an eighth line completing the ledger: ledger flow types the atlas cells — paid settlement (confluence is bought), flat reversibility, free creation, and the mixed marks cell where history is written free while the law quotient prices at exactly one bit, the retained central residue, so the registration promotion is a one-bit ledger transaction and the marks cell is the only floor whose ledger balances internally — deterministic multi-step one-use floors do not exist (the fork-staging half of the central law is a theorem at model scope while the no-selector half remains the named postulate), the admissible orderings of every content class equal the order-forgetting quotient fiber exactly, the law/present identification asymmetry is derived and flow-typed (the present is expensive because it is minted; paid cells erase their present at their terminals and reversible cells never grow one — the Cut is the signature of the mint), the identifiability and debt calculus instantiates on every rival floor with order bits future-inert (re-deriving the readability-of-order axiom as necessary) and its receipt bound equal to the ledger price of the floor evolution map, a constant acquires a structural definition as a fork-registration the law action inherits — underived, readable from every window at constant cost, paid once and replicated free — separating constants from laws and states in a three-column cut, and a driven floor steady-state dissipation is shown orthogonal to the ledger price, which floors the erasure bill only — and a ninth line extending the count-region hierarchy: the cyclic-multiplicity width grows 1, 1, 2, 3, 5, 12 for three through eight photons with the first emergent qutrit forced at six by pigeonhole, and the exposure law holds fiber-exhaustively at six photons — single-shot counting spans exactly the symmetric part of every emergent fiber, its orientation always and only one multiplication away — so the hidden resource of the counting grammar grows in width, never in depth — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the atlas capability theorems, the tower censuses, and the relocation model are exact, shipped, and presentation-relative by stated scope while the boundary-layer measurements are cited from the research corpus and nature is not claimed to realize any particular cell, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, the ladder witnesses and second-storey censuses are exact and shipped with their classical cohomology dimensions and the torsor pattern cited as known rather than claimed, the debt-ledger theorems are exact finite counting whose component results are classical and cited — with the contribution claimed only for the witness suite, the capability separation of the arrow, the pinning consequences, and the pre-probabilistic derivation route of the selection price — the ledger-completion results are exact at their stated finite model scopes with every classical component cited — the persistence/diamond lemma, trace linearization counting, sorting under partial information, and the housekeeping/excess decomposition — and the two-bills section labeled numeric discovery grade, the hierarchy extension ships its exact tableau-counting engine while the fiber-exhaustive exposure law is cited at discovery grade from the research corpus, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, whether any physical carrier realizes the pinned or the floppy grade, whether nature realizes constants as column-two registrations, whether any emergent qutrit fiber admits a practical encoding, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.",
        [
            "papers/17-mint-and-bill/paper.md",
            "papers/18-emergent-hierarchy/paper.md",
            "RELEASE-NOTES-v0.17.0.md",
        ],
    ),
    (
        "v0.18",
        "Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit, and in which an atlas of generative floors now classifies what any floor can carry: order-writability and residue-retention are independent, presentation-relative capabilities whose four cells are exemplified and fenced by exact theorems — lattice floors are orderless in their settled states, reversible floors write order but can never scar, commutative creation scars without order, and the marks floor carries both — with the retained contact containing an exact one-mode fermionic kernel whose complex structure is the central square root of minus one, a retention tower computed through third order (a unique first-order scar class, four second-order classes read by a gauge-invariant bracket witness, and exactly one third-order class), and the measurement obstruction relocated: no equivariant selector from the law quotient to its history space exists, the retained bit is tomographically silent at law level yet certainty-grade to a scar reader, and promoting a registration into the law-state lifts prediction from exact chance to certainty — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — a sixth line reading the obstruction tower itself: the retention tower of the four-mark contact group is one ladder of gauge-invariant witnesses, in which the unique fourth-order class is the retention class cup-squared and is read as value one by a quadruple involutive self-contact, the involution-silent third-order class is read by an explicit twenty-five-word cycle witness, the no-global-now of the time chapter and the no-outcome-selector of the interface chapters are adjacent instances of one torsor-obstruction pattern with the arrow of time strictly below the whole tower as act-monoid non-invertibility, the retention cover itself is first-order-scar-free yet carries exactly one coherence scar whose reading requires a four-word composite cycle, and a boundary-pinning theorem shows that every Hilbert carrier with two-dimensional twisted sectors pins the odd identity-holonomy class at the trine overlap one-half exactly — explaining the r = 1/2 saturation of current photonic experiments, placing the registered r = 3/5 bet exactly one contact beyond every such carrier, and making overlap rigidity and the fourth contact count-level witnesses of the carrier grade — and a seventh line, an exact combinatorial debt ledger built from counting alone: no fixed carrier reversibly absorbs a merging act, one fresh one-use register per step always does, the minimal register alphabet is exactly the largest merge multiplicity, distinction is never destroyed unpaid — existence bits equal surviving bits plus paid bits, with waste possible and theft impossible — the n-fork's collapse cost, question depth, and record alphabet are one number log2 n, and every completion that resolves a staged fork books exactly that price, so the no-selector law is a refused debt and lawlike evolution is exactly the debt-free sector — an eighth line completing the ledger: ledger flow types the atlas cells — paid settlement (confluence is bought), flat reversibility, free creation, and the mixed marks cell where history is written free while the law quotient prices at exactly one bit, the retained central residue, so the registration promotion is a one-bit ledger transaction and the marks cell is the only floor whose ledger balances internally — deterministic multi-step one-use floors do not exist (the fork-staging half of the central law is a theorem at model scope while the no-selector half remains the named postulate), the admissible orderings of every content class equal the order-forgetting quotient fiber exactly, the law/present identification asymmetry is derived and flow-typed (the present is expensive because it is minted; paid cells erase their present at their terminals and reversible cells never grow one — the Cut is the signature of the mint), the identifiability and debt calculus instantiates on every rival floor with order bits future-inert (re-deriving the readability-of-order axiom as necessary) and its receipt bound equal to the ledger price of the floor evolution map, a constant acquires a structural definition as a fork-registration the law action inherits — underived, readable from every window at constant cost, paid once and replicated free — separating constants from laws and states in a three-column cut, and a driven floor steady-state dissipation is shown orthogonal to the ledger price, which floors the erasure bill only — and a ninth line extending the count-region hierarchy: the cyclic-multiplicity width grows 1, 1, 2, 3, 5, 12 for three through eight photons with the first emergent qutrit forced at six by pigeonhole, and the exposure law holds fiber-exhaustively at six photons — single-shot counting spans exactly the symmetric part of every emergent fiber, its orientation always and only one multiplication away — so the hidden resource of the counting grammar grows in width, never in depth — and a tenth line, hosting the observer: an exact finite theory of hosted observers whose records are floor events, in which a causally decoupled register carries zero world-information without an interpretation key, the keyless deficit is a computable floor invariant that strictly grows with inert capacity, the key suffices exactly and is underived — a constant of the hosted world in the three-column sense — the complete interpretation map is unwritable by the entire floor with no equivariant convention at any level of a record-of-record tower, a matched registrar tracks the world fork-for-fork and the hosted present has width equal to the mint since the last banked record, coupling mints new joint distinction and information is key-free exactly where the observer co-minted it (null-result information recovering interaction-free measurement exactly), participation heals what inert capacity worsens, privacy requires an unobserved pair, every observer's biography and proper time are free while the unknown is always when-relative-to-others, co-witnessed order is forced to agree, and pooled experience determines everything except what neither observer touched — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the atlas capability theorems, the tower censuses, and the relocation model are exact, shipped, and presentation-relative by stated scope while the boundary-layer measurements are cited from the research corpus and nature is not claimed to realize any particular cell, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, the ladder witnesses and second-storey censuses are exact and shipped with their classical cohomology dimensions and the torsor pattern cited as known rather than claimed, the debt-ledger theorems are exact finite counting whose component results are classical and cited — with the contribution claimed only for the witness suite, the capability separation of the arrow, the pinning consequences, and the pre-probabilistic derivation route of the selection price — the ledger-completion results are exact at their stated finite model scopes with every classical component cited — the persistence/diamond lemma, trace linearization counting, sorting under partial information, and the housekeeping/excess decomposition — and the two-bills section labeled numeric discovery grade, the hierarchy extension ships its exact tableau-counting engine while the fiber-exhaustive exposure law is cited at discovery grade from the research corpus, the hosted-observer theorems are exact and exhaustive at their model scopes with the impossibility core and the intersubjectivity semantics cited as known (Breuer, Wolpert, Löfgren, Putnam, Everett, Lamport, Mazurkiewicz) and the claims confined to the price structure, the two participation theorems, the healing/worsening juxtaposition, and the new proof route to the received key, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, whether any physical carrier realizes the pinned or the floppy grade, whether nature realizes constants as column-two registrations, whether any emergent qutrit fiber admits a practical encoding, whether nature's observers are participation-bounded in the hosted sense, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.",
        [
            "papers/19-seventh-attempt/paper.md",
            "RELEASE-NOTES-v0.18.0.md",
        ],
    ),
    (
        "v0.19",
        """Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit, and in which an atlas of generative floors now classifies what any floor can carry: order-writability and residue-retention are independent, presentation-relative capabilities whose four cells are exemplified and fenced by exact theorems — lattice floors are orderless in their settled states, reversible floors write order but can never scar, commutative creation scars without order, and the marks floor carries both — with the retained contact containing an exact one-mode fermionic kernel whose complex structure is the central square root of minus one, a retention tower computed through third order (a unique first-order scar class, four second-order classes read by a gauge-invariant bracket witness, and exactly one third-order class), and the measurement obstruction relocated: no equivariant selector from the law quotient to its history space exists, the retained bit is tomographically silent at law level yet certainty-grade to a scar reader, and promoting a registration into the law-state lifts prediction from exact chance to certainty — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — a sixth line reading the obstruction tower itself: the retention tower of the four-mark contact group is one ladder of gauge-invariant witnesses, in which the unique fourth-order class is the retention class cup-squared and is read as value one by a quadruple involutive self-contact, the involution-silent third-order class is read by an explicit twenty-five-word cycle witness, the no-global-now of the time chapter and the no-outcome-selector of the interface chapters are adjacent instances of one torsor-obstruction pattern with the arrow of time strictly below the whole tower as act-monoid non-invertibility, the retention cover itself is first-order-scar-free yet carries exactly one coherence scar whose reading requires a four-word composite cycle, and a boundary-pinning theorem shows that every Hilbert carrier with two-dimensional twisted sectors pins the odd identity-holonomy class at the trine overlap one-half exactly — explaining the r = 1/2 saturation of current photonic experiments, placing the registered r = 3/5 bet exactly one contact beyond every such carrier, and making overlap rigidity and the fourth contact count-level witnesses of the carrier grade — and a seventh line, an exact combinatorial debt ledger built from counting alone: no fixed carrier reversibly absorbs a merging act, one fresh one-use register per step always does, the minimal register alphabet is exactly the largest merge multiplicity, distinction is never destroyed unpaid — existence bits equal surviving bits plus paid bits, with waste possible and theft impossible — the n-fork's collapse cost, question depth, and record alphabet are one number log2 n, and every completion that resolves a staged fork books exactly that price, so the no-selector law is a refused debt and lawlike evolution is exactly the debt-free sector — an eighth line completing the ledger: ledger flow types the atlas cells — paid settlement (confluence is bought), flat reversibility, free creation, and the mixed marks cell where history is written free while the law quotient prices at exactly one bit, the retained central residue, so the registration promotion is a one-bit ledger transaction and the marks cell is the only floor whose ledger balances internally — deterministic multi-step one-use floors do not exist (the fork-staging half of the central law is a theorem at model scope while the no-selector half remains the named postulate), the admissible orderings of every content class equal the order-forgetting quotient fiber exactly, the law/present identification asymmetry is derived and flow-typed (the present is expensive because it is minted; paid cells erase their present at their terminals and reversible cells never grow one — the Cut is the signature of the mint), the identifiability and debt calculus instantiates on every rival floor with order bits future-inert (re-deriving the readability-of-order axiom as necessary) and its receipt bound equal to the ledger price of the floor evolution map, a constant acquires a structural definition as a fork-registration the law action inherits — underived, readable from every window at constant cost, paid once and replicated free — separating constants from laws and states in a three-column cut, and a driven floor steady-state dissipation is shown orthogonal to the ledger price, which floors the erasure bill only — and a ninth line extending the count-region hierarchy: the cyclic-multiplicity width grows 1, 1, 2, 3, 5, 12 for three through eight photons with the first emergent qutrit forced at six by pigeonhole, and the exposure law holds fiber-exhaustively at six photons — single-shot counting spans exactly the symmetric part of every emergent fiber, its orientation always and only one multiplication away — so the hidden resource of the counting grammar grows in width, never in depth — and a tenth line, hosting the observer: an exact finite theory of hosted observers whose records are floor events, in which a causally decoupled register carries zero world-information without an interpretation key, the keyless deficit is a computable floor invariant that strictly grows with inert capacity, the key suffices exactly and is underived — a constant of the hosted world in the three-column sense — the complete interpretation map is unwritable by the entire floor with no equivariant convention at any level of a record-of-record tower, a matched registrar tracks the world fork-for-fork and the hosted present has width equal to the mint since the last banked record, coupling mints new joint distinction and information is key-free exactly where the observer co-minted it (null-result information recovering interaction-free measurement exactly), participation heals what inert capacity worsens, privacy requires an unobserved pair, every observer's biography and proper time are free while the unknown is always when-relative-to-others, co-witnessed order is forced to agree, and pooled experience determines everything except what neither observer touched — and an eleventh line, completing the hosted-observer constitution: for nested observers the sub-experience is exactly the restriction of the super's and knowledge across containment is exactly asymmetric with additively telescoping inter-level ignorance (the interpreted-systems and trace-theory laws recovered from one-use counting), teaching and measurement are one boundary co-minting operation differing only in which side is called the instrument, with capacity equal to the boundary fork width and a learner's budget equal to the boundary mint, a shared sense is an automatic consensus channel and overlap does not grow the common sector but redirects agreement from facts about the pair to facts about the world while pooled coverage pays, observer membership is opaque to all experience so mutual knowledge requires a received membership key, and the ways of knowing close into a two-currency price list: every knowing is participation paid in consumed marks or convention paid in received keys — and a twelfth line, the genesis of space: a measure-free anthropic filter in which three exact observer-capability predicates (faithful biography, non-vacuous participation, internal affordability) select the mixed cell as the only asker-compatible floor, locality is the affordability condition for bounded observers (frontier width is world-size-independent exactly on bounded degree), a priced inheritance dynamics on minting floors has an exact budget theorem (intersection inheritance is always paid; union inheritance is unpaid in every contact where the parents' neighborhoods differ), total tolerance is monotone non-increasing (the sparsification arrow: a paid floor can only get sparser), reproduction is classified by the twin theorem (a contact reproduces the world iff the parents are adjacent twins; every contact reproduces iff the world is a disjoint union of cliques; wounded cliques heal only by fission; triangle-free worlds decay to dust with the triangle the minimal witnessed durable structure), and a radius-one locality lemma yields a saturated discrete light cone that exists exactly when the world is sparse (a Lieb-Robinson-shaped recovery whose speed cap is the degree geometry itself) — and a thirteenth line, the price of chance: time factors into a clock arrow and a ledger arrow with all divergence dynamics on the spend sector (the frozen-wound theorem: equilibrium contacts hand differences on pointwise unchanged), symmetry forces the counting measure on bare floors while an observer's seat un-forces it (the invariant simplex is positive-dimensional with the participation calendar as exact coordinates and a closed form on cliques), received slot-exchangeability collapses the key to interaction-type propensities, no internal filter forces the value while cross-seat agreement forces exactly the counting measure and counting is provably nonlocal, giving the measure dilemma (a weighting can be shared or affordable, never both), the dilemma dissolves on structured worlds at the price of a received field (a three-dimensional strictly local transfer recurrence carrying the shared measure with all seats' joint predictions agreeing automatically; the transfer-matrix and belief-propagation machinery classical and cited), the field's ratios converge geometrically to forced algebraic constants (the Padovan-Perrin-plastic-number laws of the maximal-matching literature, cited as recovery) with a boundary layer of chance and a bulk identity in which a boundaryless world is pure bulk and cycle branch counts are the Perrin numbers whose prime divisibility is the free action of rotation on branches (spontaneous-symmetry-breaking structure with an arithmetic witness, classical components cited), and on self-reproducing worlds the measure key becomes earnable: world size is written in the observer's waiting times, one mortal life can identify world structure but provably never the measure (an exact total-variation floor), mortal and eternal worlds assign different chances to identical events, and measure-holding closes into a three-rung ladder priced in nothing, boundary data, or time — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the atlas capability theorems, the tower censuses, and the relocation model are exact, shipped, and presentation-relative by stated scope while the boundary-layer measurements are cited from the research corpus and nature is not claimed to realize any particular cell, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, the ladder witnesses and second-storey censuses are exact and shipped with their classical cohomology dimensions and the torsor pattern cited as known rather than claimed, the debt-ledger theorems are exact finite counting whose component results are classical and cited — with the contribution claimed only for the witness suite, the capability separation of the arrow, the pinning consequences, and the pre-probabilistic derivation route of the selection price — the ledger-completion results are exact at their stated finite model scopes with every classical component cited — the persistence/diamond lemma, trace linearization counting, sorting under partial information, and the housekeeping/excess decomposition — and the two-bills section labeled numeric discovery grade, the hierarchy extension ships its exact tableau-counting engine while the fiber-exhaustive exposure law is cited at discovery grade from the research corpus, the hosted-observer theorems are exact and exhaustive at their model scopes with the impossibility core and the intersubjectivity semantics cited as known (Breuer, Wolpert, Löfgren, Putnam, Everett, Lamport, Mazurkiewicz) and the claims confined to the price structure, the two participation theorems, the healing/worsening juxtaposition, and the new proof route to the received key, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, the observer-hierarchy, genesis-of-space, and price-of-chance theorems are exact and exhaustive at their stated finite model scopes with every classical component cited as recovery (interpreted systems and trace theory, quantum-Darwinism consensus, Gallai twin algebra and cluster graphs, Lieb-Robinson bounds, Choquet simplices, the Padovan-Perrin-plastic-number maximal-matching literature, belief propagation, Le Cam two-point bounds, the inspection paradox, and the frequentism critiques) and the claims confined to the redirection conservation, the teaching-measurement identity, the priced two-currency exhaustiveness, the inheritance budget dichotomy, the sparsification arrow, the fission-only healing, the participation-calendar coordinates, the shared-or-affordable dilemma, the mortal-eternal chance split, and the cost-structure ladder, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, whether any physical carrier realizes the pinned or the floppy grade, whether nature realizes constants as column-two registrations, whether any emergent qutrit fiber admits a practical encoding, whether nature's observers are participation-bounded in the hosted sense, and whether any experiment realizes the conjugation witness, whether nature's chance is field-carried or earned, and whether any physical observer's measure key is received in the column-two sense — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.""",
        [
            "README.md",
            "docs/public-claim-register.md",
            "papers/22-price-of-chance/paper.md",
            "RELEASE-NOTES-v0.19.0.md",
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


# Agent attribution must never appear in a public commit message. The file
# scans above cannot catch this: commit messages are not files. This is the
# gate that would have caught the co-author trailer that once reached this
# repository and left a stale entry on GitHub's contributor graph.
AGENT_ATTRIBUTION = re.compile(
    r"noreply@anthropic\.com"
    r"|co-authored-by:\s*[^\n]*(claude|fable)"
    r"|generated with[^\n]*claude"
    r"|\bclaude\b"
    r"|\bfable\b",
    re.IGNORECASE,
)


def check_commit_trailers() -> None:
    """No commit reachable from HEAD may carry agent attribution."""
    try:
        proc = subprocess.run(
            ["git", "log", "-z", "--format=%H%n%B", "HEAD"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        print("[SKIP] commit-trailer scan (git not available)")
        return
    if proc.returncode != 0:
        print("[SKIP] commit-trailer scan (no git history available)")
        return

    hits: list[str] = []
    for record in proc.stdout.split("\x00"):
        record = record.strip("\n")
        if not record:
            continue
        sha, _, body = record.partition("\n")
        match = AGENT_ATTRIBUTION.search(body)
        if match:
            hits.append(f"{sha[:9]}: {match.group(0)!r}")

    if hits:
        raise AuditFailure(
            "agent attribution in commit messages (public commits must carry "
            "none):\n  " + "\n  ".join(hits)
        )
    print(f"[PASS] commit messages carry no agent attribution ({proc.stdout.count(chr(0))} commits)")


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
        check_commit_trailers()
        run_command("shipped verification", [sys.executable, "verification/scripts/run_all.py"])
        run_command("git whitespace check", ["git", "diff", "--check"])
    except AuditFailure as exc:
        print(f"[FAIL] {exc}", file=sys.stderr)
        return 1

    print("\nPUBLIC RELEASE AUDIT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
