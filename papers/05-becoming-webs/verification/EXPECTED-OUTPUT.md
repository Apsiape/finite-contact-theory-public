# Expected Output — `becoming_webs.py`

Dependency-free (Python 3 standard library only). Fully deterministic (no
randomness). Run:

```
python becoming_webs.py
```

Expected output, verbatim:

```
[PASS] T-26 torsor time: heap axioms exhaustive on Z_5, Z_6, Z_7; every choice of origin recovers a group; translations free + transitive (no invariant element -- no derivable now)
[PASS] T-27 the helix covers the visible cycle: unique lifting from every start; monodromy = q = 1 per visible cycle from every basepoint; deck translations commute with the dynamics and act freely and transitively on fibers
[PASS] T-28 arrow without thermodynamics: exhaustive over all 510 step words to length 8 -- the visible state returns 170 times, the joint (visible, ledger) state returns for the empty word only (0 nonempty joint returns); the ledger gap equals exactly the steps asked: an arrow from bookkeeping, no probabilities, no entropy
[PASS] T-29a guarded self-reference is productive: x = cons(a, x) has exactly ONE solution at every truncation depth 1..4, reached from every initial guess (no base case needed); unguarded x = tail(x) has 2 solutions at every depth: uniqueness is the guard's doing, not a foundation's
[PASS] T-29b the Mobius-twisted 3-patch cover: local sections perfect on every patch, global sections = 0 (none) while the untwisted control has 2: a consistent global now can fail topologically while every local time is flawless
======================================================================
RESULT: ALL CHAPTER-5 CHECKS PASS
```

Exit code `0` on success, `1` on any failure.
