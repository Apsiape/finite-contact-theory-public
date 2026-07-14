# Expected Output — negative_gram_holonomy.py

Frozen at the v0.10.0 release. Dependency-free; the core numbers and the
proof-lemmas are exact (`fractions.Fraction`); the accessible-positivity
margin is verified exactly over small-rational and Gaussian-rational
matrices and by a large well-conditioned float sweep. Runs in a few seconds.
Run from this directory (or from `verification/scripts/` — the live copy is
identical):

```powershell
python negative_gram_holonomy.py
## A: core exact numbers on the received anchor r = 3/5, odd sector Phi = pi
  [PASS] Delta_3 = 1 - 3r^2 - 2r^3 = -64/125 = -64/125 (True); it factors as (1-2r)(1+r)^2 = -64/125 (True); and it is negative exactly for r > 1/2 (True). The apparatus magnitude r = 3/5 is received; the negative sign is an exact consequence of the odd Z_2 identity-holonomy class.
  [PASS] the balanced tritter probabilities are P111 = 7/1125 (7/1125), P300 = 206/3375 (206/3375, per bunched output), P210 = 152/1125 (152/1125, per collision output), all nonnegative, and they normalize exactly: P111 + 3*P300 + 6*P210 = 1 (True).
  [PASS] the pairwise distinct-output statistic is D_2 = (2-a)/3 = 41/75 (41/75); the count witness W = P111 + D_2 - 2/3 = -128/1125 (-128/1125) equals (2/9)Delta_3 = -128/1125 (True); and the cyclic residual Q_3 = P111 - D_2 + 4/9 = -12/125 (-12/125) equals (4/9)b = -12/125 (True). All are dimensionless and count-based.
  [PASS] the matched pairwise-only null keeps a = r^2 but deletes the cyclic class (b -> 0): it predicts W_null = -4/225 (-4/225) but Q_3_null = 0 (= 0). So the joint vector (Delta_3, W, Q_3) with Q_3 = -12/125 != 0 both excludes the PSD Gram class AND rejects the cyclic-erased null -- the discrimination the earlier capstone lacked.
## B: the incumbent positive-Hilbert cone forces Delta_3 >= 0 (excluded here)
  [PASS] Delta_3 is the Gram determinant det G = 1 - 3r^2 + 2r^3 cos(Phi) (True); the positive-Hilbert (PSD) cone forces cos(Phi) >= (3r^2-1)/(2r^3) = 5/27 (5/27), i.e. at r = 3/5 the incumbent is capped at Phi <= arccos(5/27) = 79.3 deg, while the odd-holonomy extension reaches Phi = pi (180 deg). So Delta_3 = -64/125 < 0 lies strictly OUTSIDE the PSD Hilbert Gram cone (True). This is the registered divergence: dimensionless, gauge-invariant, count-reconstructible.
## C: the passive-linear-optics toric identity prod_even z = prod_odd z
  [PASS] the accessible amplitudes are monomials z_sigma = prod_i A[i][sigma(i)] of one 3x3 matrix, and they obey prod_{even} z = prod_{odd} z: structurally each product covers every (row,col) once, so both equal the full entry product (True); on an exact integer witness prod_even = 223092870 = prod_odd = 223092870 = prod all = 223092870 (True). The accessible amplitudes lie on this toric variety, not the full permutation space.
## D: universal accessible positivity -- 152||z||^2 + 9|per|^2 - 36|det|^2 >= (7/2)||z||^2
  [PASS] the analytic proof's reduced inequalities hold exactly: the collinear boundary numerator 11h^3 + 30h^2 - 16h + 8 is strictly positive for h >= 0 (its quadratic part has discriminant -704 < 0) (True); and on the noncollinear domain 0 <= p <= 1/6 both convex-maximum endpoint factors are strictly negative -- 18p^2+203p-123 and 72p^3+380p^2-3p-23 (True) -- so G_p(4p) <= 0 (= 0 only at the degenerate p = 0) and G_p(1-2p-3p^2) < 0 (True).
  [PASS] the strict-margin inequality 152||z||^2 + 9|per|^2 - 36|det|^2 >= (7/2)||z||^2 holds: EXACTLY over 15000 small-rational real and 15000 Gaussian-rational complex submatrices (all margins >= 0 in exact Fraction arithmetic, True; smallest exact real margin 0.0486, complex 46.3130); and over 200000 random complex + 200000 random real well-conditioned float matrices (min margin/||z||^2: complex 6.4134, real 0.6643, both >= 0). So every admitted passive-linear-optical probability is nonnegative DESPITE the sector lying outside the global PSD Hilbert Gram cone.

# RESULT: 8 passed, 0 failed
# Reminder: (A) the accessible-positivity theorem is unconditional;
#           (B) the physical Delta_3 < 0 prediction is CONDITIONAL,
#               preregistered, and experiment-OPEN -- not a discovery.
```

Reminder on scope: **(A)** the accessible-positivity theorem is
unconditional; **(B)** the physical `Delta_3 < 0` prediction is conditional,
preregistered, and experiment-open — an archival/priority record, not a
discovery.
