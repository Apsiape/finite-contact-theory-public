# Results — `identifiability_debt_calculus.py` (FCT-26..FCT-29 / T-18..T-21)

Status: shipped result ledger for the chapter-3 verification script.

## What the script verifies

Dependency-free (Python 3 standard library only), deterministic (fixed seed
`20260713`). Five checks:

1. **T-18 (FCT-26), the waist**: on 400 randomized finite
   description/purpose models, a purpose-respecting factorization exists iff
   the description kernel is contained in the purpose equivalence — both
   directions, exhaustive counterexample search per model.
2. **T-18 part b**: the biextensional core of a finite pairing is
   independent of reduction order — exhaustive over *all* binary pairings
   through size 3x3, four reduction orders each.
3. **T-19 (FCT-27), selector debt**: `ceil(log2 m)` receipt bits are both
   attained and un-improvable for `m = 2..8`; and on the minimal symmetric
   two-element fiber, both candidate selections break equivariance while
   the alternative set itself is invariant — the no-equivariant-selector
   theorem in its smallest witness.
4. **T-20 (FCT-28), continuation sufficiency**: on 400 randomized
   completion models, a present boundary is future-complete iff its fiber
   of completions is future-equivalent — both directions, every fiber.
5. **T-21 (FCT-29), no universal tomography depth**: explicit completion
   pairs whose first separation depth equals `d`, for `d = 1..8`.

## Reproduction

```powershell
python verification\scripts\identifiability_debt_calculus.py
```

Expected output is frozen verbatim in
[`papers/03-identifiability-and-debt/verification/EXPECTED-OUTPUT.md`](../../papers/03-identifiability-and-debt/verification/EXPECTED-OUTPUT.md).
All five checks print `[PASS]`; the script exits `0` and prints
`RESULT: ALL CHAPTER-3 CHECKS PASS`.

## What this does not show

The script verifies finite mathematics at its stated scope. It does not show
that any physical system realizes a particular alternative set, which
purposes nature runs, or that selection cannot occur — only that a derived,
symmetry-respecting selection rule does not exist and that identification
carries an exact receipt cost.
