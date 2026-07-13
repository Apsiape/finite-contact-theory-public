# Expected Output — `floor_engine_measurements.py`

Dependency-free (Python 3 standard library only). Deterministic (fixed
seeds). Runtime about 3 seconds. Run:

```
python floor_engine_measurements.py
```

Expected output, verbatim:

```
grew 18 worlds (n = 32 x10, n = 40 x8); the full one-use contact budget E = n(n-1)/2 consumed in every world
[PASS] T-30 delayed individuation: the drive manufactures twins (pooled births = 262) and they overwhelmingly separate before world end: s-hat = 0.927 (fence: > 0.75), censored = 19 (7.3%)
[PASS] T-31 short-tailed separation waits: geometric MLE (p = 0.111, mean wait 9.0 adds) beats the best discrete power law (a = 1.35) by Delta-LL = 67.8 over 243 uncensored waits (fence: Delta-LL > 10, decisive) -- separation is a short-tailed process, not a scale-free one
[PASS] T-32 ballistic counterfactual defect: one swapped fork choice (RNG stream preserved) yields a defect mass growing linearly with subsequent contacts -- mean |Delta| at k = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60] is [2.0, 7.3, 14.0, 21.0, 28.3, 35.8, 41.2, 47.2, 52.0, 58.5, 64.5, 71.2, 75.8], linear fit slope = 1.25 edges/add with R^2 = 0.998 (fences: slope > 0.3, R^2 > 0.90, monotone start-to-end)
======================================================================
RESULT: ALL CHAPTER-6 CHECKS PASS
```

Exit code `0` on success, `1` on any failure. The fences are meant to
survive seed changes; edit the seed lists and re-run.
