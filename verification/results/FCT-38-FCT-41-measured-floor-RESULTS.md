# Results — `floor_engine_measurements.py` (FCT-38..FCT-41 / T-30..T-32)

Status: shipped result ledger for the chapter-6 engine + measurement suite.

## What the script does

Dependency-free (Python 3 standard library only), deterministic (fixed
seeds). Runtime ≈ 3 seconds. One file contains both the public floor
engine (an independent implementation of the exact dynamics specified in
the chapter) and the measurements:

0. **Engine sanity**: 18 worlds grown (n = 32 ×10, n = 40 ×8); the one-use
   contact budget `E = n(n-1)/2` asserted consumed in every world.
1. **T-30 (FCT-39), delayed individuation**: 262 twin births pooled;
   separation fraction `s-hat = 0.927` (fence > 0.75); censoring 7.3%.
   Independent-implementation agreement with the private engine's
   0.927/0.911 (n = 60/90).
2. **T-31 (FCT-40), short-tailed waits**: geometric MLE (mean wait 9.0
   adds) beats the best discrete power law by ΔLL = 67.8 over 243
   uncensored waits (fence > 10).
3. **T-32 (FCT-41), ballistic defects**: maximally coupled counterfactual
   pairs; defect mass at k = 0..60 fits linear with slope 1.25 edges/add,
   R² = 0.998 (fences: slope > 0.3, R² > 0.90, monotone). Private
   instrument's law: ≈ 2 + 1.4k.

## Reproduction

```powershell
python verification\scripts\floor_engine_measurements.py
```

Expected output is frozen verbatim in
[`papers/06-measured-floor/verification/EXPECTED-OUTPUT.md`](../../papers/06-measured-floor/verification/EXPECTED-OUTPUT.md).
All checks print `[PASS]`; the script exits `0` and prints
`RESULT: ALL CHAPTER-6 CHECKS PASS`.

The fences are meant to survive seed changes; readers are encouraged to
edit the seed lists and re-run.

## What this does not show

Measured facts about the specified dynamics only — nothing about nature.
The redundancy-engine inversion is cited and explicitly NOT claimed at
public scope (the shipped probe at n ≤ 64 is null; the private effect
needs n ≈ 1600). No n-scaling laws, no defect-radius (cone-speed)
measurement, no parameter sweeps beyond the shipped (1, 6, 0.5, 1).
