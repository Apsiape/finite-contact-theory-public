# Chapter 63 — freeze record

- Release tag: `v0.36.0`
- Concept DOI (the program, all versions): `10.5281/zenodo.21253591`
- Version DOI (v0.36.0): `10.5281/zenodo.21506169`
- Chapter deposit DOI: none (repository deposit only).
- Freeze date: 2026-07-23.

## Shipped verification

- `verify_63_charge.py` — stdlib only (`fractions`, `itertools`), no
  third-party dependencies. Runs from a clean clone in seconds. Ten exact
  checks, all `[PASS]`; exits nonzero on any `[FAIL]`.
  - PART A (A1–A6): the fusion algebra — gauge invariance of χ, the exact
    visibility factorization −(2v−1)(v+1)², odd–odd cancellation
    (1−v)²(1+2v), multiplicativity over randomized patterns, screening at
    v = 1/2, strong-even survival, and the tensor-fusion sign law
    det(A⊗B) = det(A)³det(B)³.
  - PART B (B1–B2): the tritter amalgamability landmarks —
    cos θ_max = −1 at v = 1/2 and cos θ_max = 0 at v² = 1/3, exact.
  - PART C (C1–C2): the commutator spoof-closure demo — a scalar route-phase
    commutator equals I; an anticommuting pair's commutator equals −I.

## Label posture (as printed in `paper.md`)

- Fusion algebra: `THEOREM (model)` — six exact checks.
- Tritter amalgamability boundary θ_max(v): `RECOVERY` — one-line corollary
  of Gram positive-semidefiniteness; presentational contribution; cites
  Menssen et al. 2017 and the Tichy / Brod indistinguishability-Gram
  literature.
- Charge in nature: `EXTENSION / REGISTERED`, zero observations; conditional
  wager; requires a non-photonic realization (photons always glue).
- Below-wall fusion protocol: `REGISTERED / RECOVERY-grade`, photonically
  testable now.
- Witness designs (commutator, sector-conditional K): `REGISTERED protocols`;
  route-phase spoof cites Oi 2003 and the Kristjánsson–Chiribella
  channel-superposition literature.
- Exclusivity-from-two-conservation-laws: strongest available novelty
  language with the no-cloning/monogamy-distinction check stated `OPEN`
  in print.
