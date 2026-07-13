# Expected Output — `identifiability_debt_calculus.py`

Dependency-free (Python 3 standard library only). Deterministic (fixed seed
`20260713`). Run:

```
python identifiability_debt_calculus.py
```

Expected output, verbatim:

```
[PASS] T-18 waist: factorization exists iff ker(pi) within ~T (400 random finite models, both directions)
[PASS] T-18 (part b) biextensional core order-independent (exhaustive, every binary pairing through 3x3, 4 orders)
[PASS] T-19 selector debt: ceil(log2 m) attained and un-improvable (m = 2..8) + no equivariant selector on the symmetric fiber (both candidates move; the set is invariant: True)
[PASS] T-20 continuation sufficiency biconditional (400 random completion models)
[PASS] T-21 explicit completion pairs separating first at depth d (certificates d = 1..8): no universal tomography depth
======================================================================
RESULT: ALL CHAPTER-3 CHECKS PASS
```

Exit code `0` on success, `1` on any failure.
