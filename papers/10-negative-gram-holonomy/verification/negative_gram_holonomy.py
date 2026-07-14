#!/usr/bin/env python3
"""Chapter 10 -- negative-Gram identity holonomy (the program's FIRST divergence).

Dependency-free (Python standard library only). Two separable things are
verified, and they must not be conflated:

  (A) THE THEOREM -- unconditionally true, no bridge premises. A three-contact
      class function with a NEGATIVE sign-sector eigenvalue nonetheless keeps
      EVERY passive-linear-optical probability nonnegative ("universal
      accessible positivity"), so it is a lawful probabilistic sector that
      lies OUTSIDE the positive-semidefinite Hilbert Gram cone. This is a
      mathematical fact and is stated with confidence.

  (B) THE PREDICTION -- conditional, preregistered, experiment-OPEN. On a
      received apparatus anchor r = 3/5 and the odd identity-holonomy sector
      (Phi = pi), the Gram discriminant is Delta_3 = -64/125 < 0, while
      ordinary complex-Hilbert QM forces Delta_3 >= 0. The registered joint
      count vector (Delta_3, W, Q_3) both excludes the PSD Gram class and
      rejects the pairwise-only null (Q_3 != 0). This is a registered BET and
      protocol, NOT a result; the physical bridge premises (that a particle
      class carries Z_2 identity holonomy, that photons receive it, that
      passive linear optics is the complete grammar) are held open, and the
      mixed-state / full-nuisance PSD-exclusion is an OPEN crux awaiting an
      external quantum-optics expert.

Sections:
  A. Core exact numbers (the prediction B): Delta_3 and its factorization;
     the r > 1/2 threshold; the tritter probabilities and their exact
     normalization; the pairwise statistic D_2; the gauge-free count
     witnesses W, Q_3; the pairwise-only null (Q_3 = 0).
  B. Incumbent PSD exclusion: Delta_3 = det G, and the positive-Hilbert cone
     forces cos(Phi) >= (3r^2 - 1)/(2r^3); at r = 3/5 that caps Phi at
     arccos(5/27) ~ 79.3 deg, while the extension reaches Phi = pi.
  C. The toric identity prod_{even} z = prod_{odd} z (exact and structural).
  D. Universal accessible positivity (the theorem A): the exact reduced
     proof-lemmas (collinear negative discriminant; noncollinear endpoint
     signs on the compact domain 0 <= p < 1/6), and a numerical margin check
     over random complex and targeted real interferometer submatrices,
     asserting 152||z||^2 + 9|per|^2 - 36|det|^2 >= (7/2)||z||^2.

Named recoveries (not novel here): the three-state Gram-determinant identity;
the S_3 character algebra; the permanent/determinant of a 3x3 matrix; Heron's
identity. The DIVERGENCE is the accessible-positivity-without-global-PSD
sector itself, and it is a conditional physical prediction, not a discovery.
"""
import cmath
import itertools
import random
from fractions import Fraction as F

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

# ======================================================================
# A. Core exact numbers -- the (conditional, preregistered) prediction B
# ======================================================================
print("## A: core exact numbers on the received anchor r = 3/5, odd sector Phi = pi")
r = F(3, 5)
a = r * r                 # J(transposition) = r^2
b = -(r ** 3)             # J(3-cycle) = r^3 * chi, chi = -1 (odd holonomy)

# Delta_3 (symmetric odd sector) = 1 - 3r^2 - 2r^3, and its factorization.
Delta3 = 1 - 3 * a - 2 * (r ** 3)
factor = (1 - 2 * r) * (1 + r) ** 2
# threshold: Delta_3(r) < 0 iff r > 1/2 (exhaustive sign scan on a fine grid)
threshold = (all((1 - 2*F(k, 20)) * (1 + F(k, 20))**2 > 0 for k in range(0, 10))
             and (1 - 2*F(1, 2)) * (1 + F(1, 2))**2 == 0
             and all((1 - 2*F(k, 20)) * (1 + F(k, 20))**2 < 0 for k in range(11, 20)))
check(f"Delta_3 = 1 - 3r^2 - 2r^3 = {Delta3} = -64/125 ({Delta3 == F(-64,125)}); it "
      f"factors as (1-2r)(1+r)^2 = {factor} ({Delta3 == factor}); and it is "
      f"negative exactly for r > 1/2 ({threshold}). The apparatus magnitude "
      f"r = 3/5 is received; the negative sign is an exact consequence of the "
      f"odd Z_2 identity-holonomy class.",
      Delta3 == F(-64, 125) and Delta3 == factor and threshold)

# Balanced Fourier-tritter probabilities and exact normalization.
P111 = (2 + 4*b - 3*a) / 9
P300 = (1 + 3*a + 2*b) / 27          # per bunched output
P210 = (1 - b) / 9                   # per collision output
norm = P111 + 3*P300 + 6*P210
check(f"the balanced tritter probabilities are P111 = {P111} (7/1125), "
      f"P300 = {P300} (206/3375, per bunched output), P210 = {P210} "
      f"(152/1125, per collision output), all nonnegative, and they normalize "
      f"exactly: P111 + 3*P300 + 6*P210 = {norm} ({norm == 1}).",
      P111 == F(7,1125) and P300 == F(206,3375) and P210 == F(152,1125)
      and norm == 1 and P111 >= 0 and P300 >= 0 and P210 >= 0)

# Pairwise statistic and the gauge-free count witnesses.
D2 = (2 - a) / 3
W = P111 + D2 - F(2, 3)
Q3 = P111 - D2 + F(4, 9)
check(f"the pairwise distinct-output statistic is D_2 = (2-a)/3 = {D2} (41/75); "
      f"the count witness W = P111 + D_2 - 2/3 = {W} (-128/1125) equals "
      f"(2/9)Delta_3 = {F(2,9)*Delta3} ({W == F(2,9)*Delta3}); and the cyclic "
      f"residual Q_3 = P111 - D_2 + 4/9 = {Q3} (-12/125) equals (4/9)b = "
      f"{F(4,9)*b} ({Q3 == F(4,9)*b}). All are dimensionless and count-based.",
      D2 == F(41,75) and W == F(-128,1125) and W == F(2,9)*Delta3
      and Q3 == F(-12,125) and Q3 == F(4,9)*b)

# The matched pairwise-only null deletes the cyclic class b -> 0.
b_null = F(0)
W_null = F(2, 9) * (1 - 3*a + 2*b_null)
Q3_null = F(4, 9) * b_null
check(f"the matched pairwise-only null keeps a = r^2 but deletes the cyclic "
      f"class (b -> 0): it predicts W_null = {W_null} (-4/225) but "
      f"Q_3_null = {Q3_null} (= 0). So the joint vector (Delta_3, W, Q_3) with "
      f"Q_3 = -12/125 != 0 both excludes the PSD Gram class AND rejects the "
      f"cyclic-erased null -- the discrimination the earlier capstone lacked.",
      W_null == F(-4,225) and Q3_null == 0 and Q3 != 0)

# ======================================================================
# B. Incumbent PSD exclusion: Delta_3 = det G, and the Hilbert cone bound
# ======================================================================
print("## B: the incumbent positive-Hilbert cone forces Delta_3 >= 0 (excluded here)")
# For three normalized states with equal overlap magnitude r and cyclic phase
# Phi, det G = 1 - 3r^2 + 2r^3 cos(Phi). PSD (a real Hilbert realization)
# requires det G >= 0, i.e. cos(Phi) >= (3r^2 - 1)/(2r^3).
detG_odd = 1 - 3*a + 2*(r**3)*(-1)        # cos(pi) = -1
cos_bound = (3*a - 1) / (2 * r**3)         # PSD threshold on cos(Phi)
# at r = 3/5 the bound is 5/27; the incumbent is confined to Phi <= arccos(5/27)
import math
phi_max_deg = math.degrees(math.acos(float(cos_bound)))
excluded = (detG_odd == Delta3 and detG_odd < 0            # odd sector is outside
            and cos_bound == F(5, 27)                       # exact PSD threshold
            and 79.0 < phi_max_deg < 79.6)                  # ~79.3 deg cap
check(f"Delta_3 is the Gram determinant det G = 1 - 3r^2 + 2r^3 cos(Phi) "
      f"({detG_odd == Delta3}); the positive-Hilbert (PSD) cone forces "
      f"cos(Phi) >= (3r^2-1)/(2r^3) = {cos_bound} (5/27), i.e. at r = 3/5 the "
      f"incumbent is capped at Phi <= arccos(5/27) = {phi_max_deg:.1f} deg, "
      f"while the odd-holonomy extension reaches Phi = pi (180 deg). So "
      f"Delta_3 = -64/125 < 0 lies strictly OUTSIDE the PSD Hilbert Gram cone "
      f"({excluded}). This is the registered divergence: dimensionless, "
      f"gauge-invariant, count-reconstructible.", excluded)

# ======================================================================
# C. The toric identity prod_{even} z = prod_{odd} z
# ======================================================================
print("## C: the passive-linear-optics toric identity prod_even z = prod_odd z")
perms = list(itertools.permutations(range(3)))
def sgn(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s
# structural proof: BOTH products equal the product of all nine entries, since
# the three even (resp. three odd) permutations cover each (row, col) once.
even_cells = [(i, p[i]) for p in perms if sgn(p) == 1 for i in range(3)]
odd_cells = [(i, p[i]) for p in perms if sgn(p) == -1 for i in range(3)]
all_cells = [(i, j) for i in range(3) for j in range(3)]
structural = (sorted(even_cells) == sorted(all_cells)
              and sorted(odd_cells) == sorted(all_cells))
# exact witness over an integer matrix
Aint = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
z_int = [Aint[0][p[0]] * Aint[1][p[1]] * Aint[2][p[2]] for p in perms]
pe = 1; po = 1
for p, zz in zip(perms, z_int):
    if sgn(p) == 1: pe *= zz
    else: po *= zz
full = 1
for i in range(3):
    for j in range(3): full *= Aint[i][j]
check(f"the accessible amplitudes are monomials z_sigma = prod_i A[i][sigma(i)] "
      f"of one 3x3 matrix, and they obey prod_{{even}} z = prod_{{odd}} z: "
      f"structurally each product covers every (row,col) once, so both equal "
      f"the full entry product ({structural}); on an exact integer witness "
      f"prod_even = {pe} = prod_odd = {po} = prod all = {full} "
      f"({pe == po == full}). The accessible amplitudes lie on this toric "
      f"variety, not the full permutation space.",
      structural and pe == po == full)

# ======================================================================
# D. Universal accessible positivity -- the theorem (A)
# ======================================================================
print("## D: universal accessible positivity -- 152||z||^2 + 9|per|^2 - 36|det|^2 >= (7/2)||z||^2")

# D.1 -- the exact reduced proof-lemmas (from the analytic closure).
# Collinear branch: the boundary numerator reduces to 11h^3 + 30h^2 - 16h + 8
# for h >= 0; the quadratic part 30h^2 - 16h + 8 has NEGATIVE discriminant, so
# it is strictly positive, and 11h^3 >= 0 for h >= 0 -- hence strictly positive.
disc_collinear = 16**2 - 4*30*8                      # discriminant of 30h^2-16h+8
collinear_ok = (disc_collinear < 0
                and all(11*hh**3 + 30*hh**2 - 16*hh + 8 > 0
                        for hh in [F(0), F(1,4), F(1), F(3), F(10)]))
# Noncollinear branch: on the compact domain 0 <= p < 1/6 the convex maximum is
# at an endpoint, and both endpoints satisfy G <= 0:
#   G_p(4p)          = p(p+1)(18p^2 + 203p - 123)     <= 0  (= 0 only at p = 0)
#   G_p(1-2p-3p^2)   = (p+1)(72p^3 + 380p^2 - 3p - 23) < 0
# The load-bearing fact is that both INNER factors are strictly negative on the
# whole interval (each is monotone with its positive root well beyond 1/6), so
# the endpoint values inherit the sign from the manifestly-positive outer
# factors p(p+1) and (p+1).
def inner_low(p):  return 18*p*p + 203*p - 123
def inner_high(p): return 72*p**3 + 380*p*p - 3*p - 23
def G_low(p):  return p*(p+1)*inner_low(p)
def G_high(p): return (p+1)*inner_high(p)
grid = [F(k, 600) for k in range(0, 101)]             # p in [0, 1/6] finely
inner_neg = all(inner_low(p) < 0 and inner_high(p) < 0 for p in grid)
endpoints_ok = all(G_low(p) <= 0 and G_high(p) < 0 for p in grid)
zero_only_at_0 = (G_low(F(0)) == 0
                  and all(G_low(p) < 0 for p in grid if p != 0))
noncollinear_ok = (inner_neg and endpoints_ok and zero_only_at_0
                   and F(100, 600) == F(1, 6))        # grid reaches the endpoint
check(f"the analytic proof's reduced inequalities hold exactly: the collinear "
      f"boundary numerator 11h^3 + 30h^2 - 16h + 8 is strictly positive for "
      f"h >= 0 (its quadratic part has discriminant {disc_collinear} < 0) "
      f"({collinear_ok}); and on the noncollinear domain 0 <= p <= 1/6 both "
      f"convex-maximum endpoint factors are strictly negative -- 18p^2+203p-123 "
      f"and 72p^3+380p^2-3p-23 ({inner_neg}) -- so G_p(4p) <= 0 (= 0 only at the "
      f"degenerate p = 0) and G_p(1-2p-3p^2) < 0 ({endpoints_ok and zero_only_at_0}).",
      collinear_ok and noncollinear_ok)

# D.2 -- margin over random submatrices. To avoid the floating-point
# cancellation that plagues det/per on ill-conditioned matrices, the
# load-bearing sweep is EXACT: small-rational real and Gaussian-rational
# complex matrices, with the margin computed as an exact Fraction and asserted
# >= 0 with no rounding. A well-conditioned float sweep then adds breadth.
rng = random.Random(20260714)

# exact real margin: 152||z||^2 + 9 per^2 - 36 det^2 - (7/2)||z||^2  (Fraction)
def margin_exact_real(A):
    z = [A[0][p[0]] * A[1][p[1]] * A[2][p[2]] for p in perms]
    zn = sum(zz * zz for zz in z)
    if zn == 0:
        return None
    per = sum(z)
    det = sum(sgn(p) * zz for p, zz in zip(perms, z))
    return 152*zn + 9*per*per - 36*det*det - F(7, 2)*zn

# exact complex margin: entries are (re, im) pairs of Fractions
def cmul(x, y):
    return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def cabs2(x):
    return x[0]*x[0] + x[1]*x[1]
def margin_exact_cplx(A):
    z = [cmul(cmul(A[0][p[0]], A[1][p[1]]), A[2][p[2]]) for p in perms]
    zn = sum(cabs2(zz) for zz in z)
    if zn == 0:
        return None
    per = (F(0), F(0)); det = (F(0), F(0))
    for p, zz in zip(perms, z):
        per = (per[0]+zz[0], per[1]+zz[1])
        s = sgn(p); det = (det[0]+s*zz[0], det[1]+s*zz[1])
    return 152*zn + 9*cabs2(per) - 36*cabs2(det) - F(7, 2)*zn

def rat():   # a small rational in [-6, 6]
    return F(rng.randint(-6, 6), rng.randint(1, 6))

EX = 15000
min_ex_real = min_ex_cplx = None
ex_ok = True
for _ in range(EX):
    A = [[rat() for _ in range(3)] for _ in range(3)]
    m = margin_exact_real(A)
    if m is not None:
        ex_ok &= (m >= 0)
        min_ex_real = m if min_ex_real is None else min(min_ex_real, m)
    Ac = [[(rat(), rat()) for _ in range(3)] for _ in range(3)]
    mc = margin_exact_cplx(Ac)
    if mc is not None:
        ex_ok &= (mc >= 0)
        min_ex_cplx = mc if min_ex_cplx is None else min(min_ex_cplx, mc)

# well-conditioned float sweep for breadth (standard scale; guard tiny ||z||^2)
def margin_ratio_float(A):
    z = [A[0][p[0]] * A[1][p[1]] * A[2][p[2]] for p in perms]
    zn = sum(abs(zz) ** 2 for zz in z)
    if zn < 1e-3:                                   # skip ill-conditioned
        return None
    per = sum(z); det = sum(sgn(p) * zz for p, zz in zip(perms, z))
    return (152*zn + 9*abs(per)**2 - 36*abs(det)**2 - 3.5*zn) / zn

FL = 200000
worst_c = worst_r = 1e9
for _ in range(FL):
    A = [[complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)] for _ in range(3)]
    m = margin_ratio_float(A)
    if m is not None:
        worst_c = min(worst_c, m)
    Ar = [[rng.gauss(0, 1) for _ in range(3)] for _ in range(3)]
    mr = margin_ratio_float(Ar)
    if mr is not None:
        worst_r = min(worst_r, mr)
float_ok = (worst_c > -1e-9 and worst_r > -1e-9)
check(f"the strict-margin inequality 152||z||^2 + 9|per|^2 - 36|det|^2 >= "
      f"(7/2)||z||^2 holds: EXACTLY over {EX} small-rational real and {EX} "
      f"Gaussian-rational complex submatrices (all margins >= 0 in exact "
      f"Fraction arithmetic, {ex_ok}; smallest exact real margin "
      f"{float(min_ex_real):.4f}, complex {float(min_ex_cplx):.4f}); and over "
      f"{FL} random complex + {FL} random real well-conditioned float matrices "
      f"(min margin/||z||^2: complex {worst_c:.4f}, real {worst_r:.4f}, both "
      f">= 0). So every admitted passive-linear-optical probability is "
      f"nonnegative DESPITE the sector lying outside the global PSD Hilbert "
      f"Gram cone.", ex_ok and float_ok)

print()
print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
print("# Reminder: (A) the accessible-positivity theorem is unconditional;")
print("#           (B) the physical Delta_3 < 0 prediction is CONDITIONAL,")
print("#               preregistered, and experiment-OPEN -- not a discovery.")
raise SystemExit(1 if FAIL else 0)
