# Expected Output — `inquiry_calculus.py`

Dependency-free (Python 3 standard library only). Deterministic (fixed seed
`20260714`). Run:

```
python inquiry_calculus.py
```

Expected output, verbatim:

```
[PASS] T-22 residual composition law u^-1(v^-1 S) = (vu)^-1 S (300 randomized series)
[PASS] T-22 noncommutativity witness: S = {ab: 1} separates the two asking orders ({'': 1} vs {})
[PASS] T-22 Boolean shadow: count-only <=> commuting residuals on the exhaustive length-2 family (81 series): commutativity is exactly order-blindness
[PASS] T-23 second law of asking: EC = H + KL + O exact to 1e-12 with O, KL >= 0 (300 random trees/sources); Kraft Z <= 1 in exact rationals; EC >= H always
[PASS] T-23 equality witness: dyadic source on a full tree attains EC = H (cost = pure entropy, no mismatch, no slack)
[PASS] T-24 adaptivity interest: optimal adaptive cost <= optimal fixed cost on every tested source (exhaustive strategy search over the threshold-question family, |X| = 4) and strictly less on a shipped witness (J > 0): p ~ (1, 1, 1, 1), adaptive 2.0 vs fixed 2.25
[PASS] T-25 paradox = type collapse: ungraded x = x has exactly two solutions ([0, 1]), ungraded x = 1 - x has none ([]), and the graded recursion x_(n+1) = 1 - x_n has exactly two lawful orbits (2) with no contradiction: self-reference is lawful when the asking grade is kept, paradoxical only when it is collapsed
======================================================================
RESULT: ALL CHAPTER-4 CHECKS PASS
```

Exit code `0` on success, `1` on any failure.
