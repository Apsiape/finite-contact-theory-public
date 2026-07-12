# FCT-22 — Exact Strict Preparation Gap: Shipped Results

Script: [`../scripts/exact_gap_certificate.py`](../scripts/exact_gap_certificate.py)
(stdlib-only; every load-bearing check is exact rational arithmetic).
Claim rows: FCT-21 (support), FCT-22 (primary). Theorem rows: T-14, T-15.
Chapter: [`papers/02-behavior-conditioned-capacity/`](../../papers/02-behavior-conditioned-capacity/paper.md).

## What the script proves

For the pentagon (KCBS) behavior `p = (49/100, 25/81, 16/25, 36/121, 4/9)`
with `beta = 2137213/980100`:

1. **Realizability** — a rational Gram completion `H_feas` (diagonal 1,
   exclusivity edges 0) has `H_feas - v v^T` positive definite by exact LDL
   (all 5 pivots positive as fractions), so a sharp rank-one realization of
   `p` exists in `R^6`.
2. **Rigidity** — the real rigidity system is nonsingular (determinant
   exactly `112/495`), so any feasible Gram matrix with `lambda_max <= beta`
   has the unique real part `H*` with `H* v = beta v` (verified exactly).
3. **Obstruction** — the rational witness `y` gives
   `y^T H* y = -17658032557963925693/179590693860103680000 < 0` exactly,
   which kills every Hermitian completion with real part `H*` (for real `y`,
   the imaginary part cancels in the quadratic form).

Together: `kappa(p) > beta`, i.e. `Delta_prep(p) > 0` strictly, for **every**
sharp realization in **every** finite dimension (compression theorem T-14c
reduces the general sharp case to the rank-one pure case).

## Result

```text
5 exact checks: PASS
CERTIFIED: Delta_prep(p) > 0
```

Verbatim expected output is frozen in the chapter copy:
[`papers/02-behavior-conditioned-capacity/verification/EXPECTED-OUTPUT.md`](../../papers/02-behavior-conditioned-capacity/verification/EXPECTED-OUTPUT.md).

## Controls and provenance

- The numerical SDP magnitude (`Delta_prep ~ 0.0096474`) is context only; the
  script proves strictness, not magnitude.
- The first search candidate for a flagship behavior failed realizability and
  was discarded — realizability is part of the shipped proof, not an
  assumption.
- The naive "unique Hermitian completion" claim was corrected *by this
  certificate* (the imaginary rigidity subsystem is singular for every
  behavior vector); the shipped proof route is the corrected one. See the
  chapter's correction section.
