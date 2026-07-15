# Expected Output — mixed_state_exclusion.py

Frozen at the v0.11.0 release. Dependency-free; exact where it can be
(`fractions.Fraction` over `Q(sqrt 3)`): the first-principles count formula
on a rational witness, the determinant identity, the count-witness algebra,
the antisymmetrizer certificate, positivity on rational Grams, convexity, and
the exclusion are exact; a numerical first-principles sweep and an adversarial
descent corroborate. Runs in about a second. Run from this directory (or from
`verification/scripts/` — the live copy is identical):

```powershell
python mixed_state_exclusion.py
## A: P111 = (2 - S + 4 tau)/9 derived FROM FIRST PRINCIPLES (not asserted)
  [PASS] P111 = (2 - S + 4tau)/9 holds EXACTLY on a rational witness (P111 = 1043/5625) (True) and numerically from first principles over 20000 random partial-distinguishability models (max error 4.2e-16). S = sum |<phi_i|phi_j>|^2, tau = Re(g12 g23 g31).
## B: det G = 1 - S + 2 tau, exact (any Hermitian unit-diagonal 3x3)
  [PASS] det G = 1 - S + 2 Re(g12 g23 g31) exactly (and equals the Leibniz permutation sum) on 3000 random Hermitian unit-diagonal Gaussian-rational matrices: True.
## C: W = P111 + D2 - 2/3 = (2/9)(1 - S + 2tau) = (2/9) det G, exact
  [PASS] with P111 = (2-S+4tau)/9 and D2 = 2/3 - S/9, the count witness W = P111 + D2 - 2/3 equals (2/9)(1 - S + 2tau) = (2/9) det G exactly, over 4000 rational (S, tau): True.
## D: antisymmetrizer certificate <A_-> = det G/6 (A_- a positive projector)
  [PASS] <A_-> = det G / 6 exactly on 2000 random Grams (True); and the antisymmetrizer e = (1/6) sum sgn(pi) pi is a projector (e*e = e in Q[S_3], True), so <A_-> = ||A_-(phi1 x phi2 x phi3)||^2 >= 0, forcing det G >= 0 and W = (4/3)<A_-> = (2/9) det G >= 0.
## E: W = (2/9) det G >= 0 for every partial-distinguishability model
  [PASS] W >= 0 exactly on all 56 rational PSD Grams built from rational unit vectors (True); and an adversarial descent over partial-distinguishability models finds no W below zero (min 0.000001). Gram positivity forbids W < 0.
## F: mixed states are convex combinations; W is affine, so W(mix) >= 0
  [PASS] for a mixture p*Omega1 + (1-p)*Omega2 (p = 3/7), W is the affine combination p*W1 + (1-p)*W2 = 124616/3189375 >= 0 with W1 = 512/5625 >= 0, W2 = 2/18225 >= 0 (True). No convex combination crosses W = 0.
## G: the registered extension point lies OUTSIDE the whole QM class
  [PASS] the registered extension has W = (2/9)Delta_3 = -128/1125 = -128/1125 < 0, so it is outside the QM class (which requires W >= 0). The exact separating raw-count test is P111 + D2 >= 2/3: the extension gives P111 + D2 = 622/1125 = 622/1125 < 750/1125 = 2/3 (violation 128/1125). No partial-distinguishability Hilbert model, pure or mixed, reproduces the registered count vector.

# RESULT: 7 passed, 0 failed
# CLOSED (proven): the clean mixed-state + mode-mismatch PSD-exclusion.
# STILL OPEN (experimental layer, external expert): multiphoton
# contamination, detector response, transfer-matrix uncertainty, drift.
```

Reminder on scope: this closes the **clean** mixed-state + mode-mismatch
PSD-exclusion. Multiphoton contamination, detector response, transfer-matrix
uncertainty, and source drift remain the external experimental layer; the
Chapter-10 bridge premises are unchanged. Not an empirical discovery.
