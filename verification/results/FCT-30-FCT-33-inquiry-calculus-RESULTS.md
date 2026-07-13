# Results — `inquiry_calculus.py` (FCT-30..FCT-33 / T-22..T-25)

Status: shipped result ledger for the chapter-4 verification script.

## What the script verifies

Dependency-free (Python 3 standard library only), deterministic (fixed seed
`20260714`). Seven checks:

1. **T-22 (FCT-30), composition law**: residual operators compose
   contravariantly (`u^-1(v^-1 S) = (vu)^-1 S`) on 300 randomized series.
2. **T-22, noncommutativity**: the explicit witness `S = {ab: 1}` separates
   the two asking orders.
3. **T-22, Boolean shadow**: count-only ⟺ commuting residuals, exhaustive
   over the 81-member length-2 coefficient family.
4. **T-23 (FCT-31), second law of asking**: `EC = H + KL + O` exact to
   `1e-12` on 300 random tree/source pairs, with the Kraft inequality
   (`Z <= 1`) verified in exact rational arithmetic and `EC >= H` always.
5. **T-23, equality witness**: a dyadic source on a full tree attains
   `EC = H` (no mismatch, no slack).
6. **T-24 (FCT-32), adaptivity interest**: adaptive optimum ≤ fixed optimum
   on every tested source, by exhaustive strategy search over the
   threshold-question family at `|X| = 4`; strict on the uniform source
   (adaptive `2.0` vs best fixed `2.25`).
7. **T-25 (FCT-33), typing witnesses**: ungraded `x = 1 - x` has no
   solution; the graded recursion has exactly two lawful orbits.

## Reproduction

```powershell
python verification\scripts\inquiry_calculus.py
```

Expected output is frozen verbatim in
[`papers/04-inquiry-calculus/verification/EXPECTED-OUTPUT.md`](../../papers/04-inquiry-calculus/verification/EXPECTED-OUTPUT.md).
All seven checks print `[PASS]`; the script exits `0` and prints
`RESULT: ALL CHAPTER-4 CHECKS PASS`.

## What this does not show

The script verifies finite mathematics at its stated scope. It does not
identify quantum measurement with the residual calculus, does not cover
non-binary answer alphabets or noisy/adversarial interrogation, and claims
no asymptotic adaptivity rates.
