# Changelog

All notable public-release changes will be recorded here.

## 0.8.0

Eighth public release: **Chapter 8 — The Non-Exact-Return Reconstruction:
Finite Born Valuation and Contextuality from a Retained Contact
Interface**. Opens the program's third line (a contact-interface
reconstruction). Version DOI `10.5281/zenodo.21360609`; concept DOI
`10.5281/zenodo.21253591`.

Added:

- `papers/08-nonexact-return/` — chapter, claim snapshot, freeze record,
  and a frozen copy of the shipped script with expected output;
- claim rows FCT-45 through FCT-50 and theorem rows T-33 through T-36 (the
  quaternionic receiver; the 24-cell self-hosting fixed point; the `F_4`
  closure; the forced `1/2` interface magnitude; a finite Gleason theorem;
  and a triality Kochen-Specker obstruction — all `shipped`);
- `verification/scripts/nonexact_return_reconstruction.py`, wired into
  `run_all.py` (now eleven scripts);
- **the new live release ceiling** (three published lines), quoted in the
  README, the claim register, the chapter-8 paper, and the v0.8.0 notes.

Changed:

- README overhauled to the three-line stack; theorem bank extended;
  `scripts/release_audit.py` updated (required files, migrated canonical
  ceilings, additional overclaim bans);
- `.zenodo.json` refreshed to the v0.8 deposit metadata.

## 0.7.0

Seventh public release: **Chapter 7 — The Taxonomy of Inevitability: A
Program Map**, the capstone of the v0.3.0–v0.7.0 consolidation round.
Archived on Zenodo; version DOI
`10.5281/zenodo.21333922`, concept DOI `10.5281/zenodo.21253591`.

Added:

- `papers/07-program-map/` — the survey chapter (no new theorems), claim
  snapshot, and freeze record;
- claim rows FCT-42 through FCT-44 (`PROGRAM / SCHEMA`: the two-axis index
  claim; the forced/received schema; the no-selector recurrence — each
  naming its shipped instances and carrying cited parts as cited);
- **the new live release ceiling** (two published axes), quoted in the
  README, the claim register, the chapter-7 paper, and the v0.7.0 notes.

Changed:

- README rewritten to program scale (seven chapters, ten shipped scripts,
  updated reading order and status);
- claim-register Release Ceiling section carries the v0.7 ceiling; the
  v0.1/v0.2 ceilings remain verbatim in their frozen chapters and notes;
- release audit: v0.7 ceiling checked in its four advertised locations;
  the v0.2 ceiling's checked locations re-scoped to its frozen files;
- reader guide (`docs/how-to-read.md`) points at the program map first.

## 0.6.0

Sixth public release: **Chapter 6 — A Measured Generative Floor**. Archived
on Zenodo; version DOI
`10.5281/zenodo.21333868`, concept DOI `10.5281/zenodo.21253591`.

Added:

- `papers/06-measured-floor/` — the chapter paper, claim snapshot, frozen
  engine + suite copy with expected output, and freeze record;
- the repository's first shipped INSTRUMENT: a complete, dependency-free
  public floor engine (exactly specified driven one-use dynamics) with
  replay and maximally-coupled counterfactual modes;
- claim rows FCT-38 through FCT-41 (the engine/instrument; measured
  delayed individuation with cross-engine agreement at 0.927; the
  short-tailed wait law; the ballistic counterfactual defect);
- theorem rows T-30 through T-32 (`MEASURED / MODEL-SCOPE`) with
  dependency-graph and crosswalk updates;
- shipped verification: `verification/scripts/floor_engine_measurements.py`
  wired into `run_all.py`, with
  `verification/results/FCT-38-FCT-41-measured-floor-RESULTS.md`;
- evidence-manifest row; the redundancy-engine inversion carried as a
  cited negative-at-public-scale with its scale fence stated.

The live release ceiling is unchanged.

## 0.5.0

Fifth public release: **Chapter 5 — Becoming Webs: Lawful Time Without
Foundation**. Archived on Zenodo; version DOI
`10.5281/zenodo.21333710`, concept DOI `10.5281/zenodo.21253591`.

Added:

- `papers/05-becoming-webs/` — the chapter paper, claim snapshot, frozen
  verification copy with expected output, and freeze record;
- claim rows FCT-34 through FCT-37 (torsor time; the helix covering; the
  ledger arrow without thermodynamics; lawfulness without foundation with
  the Mobius-twist witness);
- theorem rows T-26 through T-29 with proof sketches, dependency-graph and
  crosswalk updates;
- shipped verification: `verification/scripts/becoming_webs.py`
  (stdlib-only, fully deterministic/exhaustive), wired into `run_all.py`,
  with `verification/results/FCT-34-FCT-37-becoming-webs-RESULTS.md`;
- evidence-manifest row for the chapter.

The live release ceiling is unchanged (chapter 5 continues the
finite-epistemics axis: chapters 3–5 now run identification cost -> asking
-> time-like structure).

## 0.4.0

Fourth public release: **Chapter 4 — Questions as Operators: the Inquiry
Calculus and a Second Law of Asking**. Archived on Zenodo; version DOI
`10.5281/zenodo.21333642`, concept DOI `10.5281/zenodo.21253591`.

Added:

- `papers/04-inquiry-calculus/` — the chapter paper, claim snapshot, frozen
  verification copy with expected output, and freeze record;
- claim rows FCT-30 through FCT-33 (residual asking algebra + Boolean
  shadow; the exact `EC = H + KL + O` second law of asking; adaptivity
  interest with a strict threshold-family witness; paradox as type
  collapse);
- theorem rows T-22 through T-25 with proof sketches, dependency-graph and
  crosswalk updates;
- shipped verification: `verification/scripts/inquiry_calculus.py`
  (stdlib-only, deterministic), wired into `run_all.py`, with
  `verification/results/FCT-30-FCT-33-inquiry-calculus-RESULTS.md`;
- evidence-manifest row for the chapter.

The live release ceiling is unchanged (chapter 4 continues the
finite-epistemics axis opened by chapter 3).

## 0.3.0

Third public release: **Chapter 3 — The Identifiability and Debt Calculus**.
Archived on Zenodo; version DOI
`10.5281/zenodo.21333556`, concept DOI `10.5281/zenodo.21253591`.

Added:

- `papers/03-identifiability-and-debt/` — the chapter paper, claim snapshot,
  frozen verification copy with expected output, and freeze record;
- claim rows FCT-26 through FCT-29 (the waist biconditional + biextensional
  core; selector debt + the no-equivariant-selector theorem; continuation
  sufficiency; no universal tomography depth);
- theorem rows T-18 through T-21 with proof sketches, dependency-graph and
  crosswalk updates;
- shipped verification:
  `verification/scripts/identifiability_debt_calculus.py` (stdlib-only,
  deterministic, exhaustive where the scope is exhaustive), wired into
  `run_all.py`, with
  `verification/results/FCT-26-FCT-29-identifiability-debt-calculus-RESULTS.md`;
- evidence-manifest row for the chapter (shipped calculus + cited private
  arrival ledgers).

Changed:

- release-audit metadata gate generalized: the CITATION version check now
  accepts any `0.X.Y` / `0.X.Y-pre`, and the title check pins the stable
  prefix rather than one release's full title (required-file and ceiling
  checks unchanged; the live v0.2 ceiling still controls the README and
  register).

The live release ceiling is unchanged (see the v0.3.0 release notes for why:
chapter 3 opens the finite-epistemics axis rather than extending the
quantum-boundary stack).

## 0.2.0

Second public release: **Chapter 2 — Behavior-Conditioned Contextual Capacity
and an Exact Strict Preparation Gap**. Archived on Zenodo; version DOI
`10.5281/zenodo.21324301`, concept DOI `10.5281/zenodo.21253591`.

Added — chapter 2 content:

- `papers/02-behavior-conditioned-capacity/` — the chapter paper, the claim
  snapshot, the frozen certificate copy with expected output, and the freeze
  record (first chapter under the new directory convention);
- claim rows FCT-21 through FCT-25 (capacity + universal inequality; exact
  strict gap; headroom law; pentagon phase geometry; sharpness boundary and
  the graded INTERNAL-BLIND novelty posture);
- theorem rows T-14 through T-17 with proof sketches, dependency-graph and
  crosswalk updates;
- shipped verification: `verification/scripts/exact_gap_certificate.py`
  (stdlib-only, every load-bearing step exact rational arithmetic), wired
  into `run_all.py`, with
  `verification/results/FCT-22-exact-gap-certificate-RESULTS.md`;
- evidence-manifest row for the chapter (shipped certificate + cited private
  suites);
- release ceiling extended to name the preparation gap at KCBS-pentagon
  scope (v0.1 ceiling unchanged in the frozen v0.1 paper and notes).

Added — evolution/governance layer (no claim-content changes):

- `EVOLUTION.md` — the living-theory charter: one canonical repository
  released in chapters, append-only history, stable identifiers, the
  private-to-public export rules, and the citer's contract;
- `docs/release-checklist.md` — the reusable release gate (the v0.1-specific
  gate remains as `docs/release-roadmap.md`);
- `papers/README.md` — the chapter directory convention (`papers/<NN>-<slug>/`
  with paper, claims snapshot, frozen verification copies, and freeze record)
  and the chapter freeze/deposit rules;
- README section "How this repository evolves".

Not included (held or open, by name):

- general-graph phase geometry beyond the pentagon fence;
- the robust asymmetry bridge (C1, `OPEN`);
- external expert review of the novelty claim (evidence class is
  INTERNAL-BLIND and stated as such);
- everything held from v0.1 (general selector, `q >= 3`, cross-site
  interlocking, gravity sourcing, nature-facing predictions).

## 0.1.0

First public release. Archived on Zenodo; version DOI
`10.5281/zenodo.21253592`, concept DOI `10.5281/zenodo.21253591`.

Added:

- public theory scaffold;
- public claim register;
- status labels, including `MEASURED`;
- correction ledger;
- mathematical core;
- theorem bank with proof-sketch stubs;
- hold register;
- DOI release roadmap;
- evidence manifest;
- shipped public verification subset:
  - open fresh-mark no-jam core;
  - exchangeable frequency bridge core;
  - rational Born / gluing core;
  - CHSH/Pell boundary core;
  - native binary-Bell lift core;
- v0.1 technical-note draft.

Not included:

- general quantum selector theorem;
- q >= 3 or more-outcome native lift;
- cross-site interlocking / CHSH-weight dynamics;
- gravity sourcing;
- nature-facing prediction package;
- public copy of the full private research corpus.
