# Changelog

All notable public-release changes will be recorded here.

## 0.4.0

Fourth public release: **Chapter 4 — Questions as Operators: the Inquiry
Calculus and a Second Law of Asking**. Archived on Zenodo; version DOI
recorded in the chapter freeze record and CITATION.cff once minted; concept
DOI `10.5281/zenodo.21253591`.

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
Archived on Zenodo; version DOI recorded in the chapter freeze record and
CITATION.cff once minted; concept DOI `10.5281/zenodo.21253591`.

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
