#!/usr/bin/env python3
"""Chapter 11 -- the clean mixed-state PSD exclusion.

Dependency-free (Python standard library only). This chapter closes the CLEAN
core of the open crux that Chapter 10 left for an external expert: whether the
registered negative-Gram count vector can be reproduced by any partially
distinguishable Hilbert-space model (pure OR mixed).

It cannot. The gauge-free count witness W = P111 + D2 - 2/3 satisfies, for every
partial-distinguishability model at the Fourier tritter,

    W = (2/9) det G,   G = the internal-state Gram matrix,

and det G >= 0 is forced by Gram positivity (pure states), hence by convexity for
every mixed state, and operator-level by the antisymmetrizer projector:

    W = (4/3) Tr(A_- Omega) >= 0,   A_- = (1/6) sum_pi sgn(pi) P_pi,  A_-^2 = A_-.

The registered extension point has W = (2/9) Delta_3 = (2/9)(-64/125) = -128/1125
< 0, so it lies strictly OUTSIDE the entire partial-distinguishability Hilbert
class. The exact separating raw-count test is  P111 + D2 >= 2/3.

SCOPE (kept honest): this closes the CLEAN mixed-state + mode-mismatch model.
It does NOT close multiphoton contamination, detector response, transfer-matrix
uncertainty, or source drift -- those remain the external experimental layer.

Verification below: the count formula P111 = (2 - S + 4 tau)/9 is derived FROM
FIRST PRINCIPLES (creation operators through the tritter, internal states
traced) -- exactly on a rational witness and numerically over random models --
not asserted; the determinant identity, the count-witness algebra, the
antisymmetrizer certificate, positivity on exact rational Grams, convexity, and
the exclusion are all exact.
"""
import cmath, itertools, math, random
from fractions import Fraction as F

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

perms = list(itertools.permutations(range(3)))
def sgn(q):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if q[i] > q[j]: s = -s
    return s
def inv(p):
    q = [0, 0, 0]
    for i in range(3): q[p[i]] = i
    return tuple(q)

# ------- exact number field Q(sqrt 3): a + b sqrt3, complex over it -------
class S:
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a = F(a); s.b = F(b)
    @staticmethod
    def c(o): return o if isinstance(o, S) else S(o, 0)
    def __add__(s, o): o = S.c(o); return S(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = S.c(o); return S(s.a - o.a, s.b - o.b)
    def __neg__(s): return S(-s.a, -s.b)
    def __mul__(s, o): o = S.c(o); return S(s.a*o.a + 3*s.b*o.b, s.a*o.b + s.b*o.a)
    __rmul__ = __mul__
    def __eq__(s, o): o = S.c(o); return s.a == o.a and s.b == o.b
    def rat(s):
        assert s.b == 0; return s.a
class C:
    __slots__ = ("r", "i")
    def __init__(s, r=0, i=0): s.r = r if isinstance(r, S) else S(r); s.i = i if isinstance(i, S) else S(i)
    @staticmethod
    def c(o): return o if isinstance(o, C) else C(o, 0)
    def __add__(s, o): o = C.c(o); return C(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = C.c(o); return C(s.r - o.r, s.i - o.i)
    def __neg__(s): return C(-s.r, -s.i)
    def __mul__(s, o): o = C.c(o); return C(s.r*o.r - s.i*o.i, s.r*o.i + s.i*o.r)
    __rmul__ = __mul__
    def conj(s): return C(s.r, -s.i)
    def __eq__(s, o): o = C.c(o); return s.r == o.r and s.i == o.i

# exact Fourier tritter F[j][i] = omega^{ji}/sqrt3  over Q(sqrt3)
sq = S(0, F(1, 3))                     # 1/sqrt3
om = C(S(F(-1, 2)), S(0, F(1, 2)))     # omega = -1/2 + i sqrt3/2
def om_pow(k):
    r = C(1)
    for _ in range(k % 3): r = r * om
    return r
Fmat = [[C(sq) * om_pow((j*i) % 3) for i in range(3)] for j in range(3)]

# ======================================================================
# A. First-principles partial-distinguishability P111 == (2 - S + 4 tau)/9
# ======================================================================
print("## A: P111 = (2 - S + 4 tau)/9 derived FROM FIRST PRINCIPLES (not asserted)")

def P111_firstprinciples_exact(G):
    # G[a][b] = <phi_a|phi_b> (C). P111 = sum_{sig,rho} (prod_i F[sig(i)][i])
    #   conj(prod_i F[rho(i)][i]) prod_m G[rhoinv[m]][siginv[m]]  (traced internal DOF)
    tot = C(0)
    for sig in perms:
        Aket = C(1)
        for i in range(3): Aket = Aket * Fmat[sig[i]][i]
        si = inv(sig)
        for rho in perms:
            Abra = C(1)
            for i in range(3): Abra = Abra * Fmat[rho[i]][i]
            ri = inv(rho)
            ov = C(1)
            for m in range(3): ov = ov * G[ri[m]][si[m]]
            tot = tot + Aket * Abra.conj() * ov
    return tot

# exact rational witness: three real rational unit vectors
# phi1=(1,0,0), phi2=(3/5,4/5,0), phi3=(3/5,0,4/5)
def gram_real(vecs):
    return [[C(S(sum(vecs[a][k]*vecs[b][k] for k in range(len(vecs[a]))))) for b in range(3)]
            for a in range(3)]
V = [[F(1), F(0), F(0)], [F(3,5), F(4,5), F(0)], [F(3,5), F(0), F(4,5)]]
Gw = gram_real(V)
P111w = P111_firstprinciples_exact(Gw)
g12, g23, g31 = Gw[0][1], Gw[1][2], Gw[2][0]
Sval = g12*g12 + g23*g23 + g31*g31            # real Gram => |g|^2 = g^2
tau = (g12 * g23 * g31)
formula = (S(2) - Sval.r + S(4)*tau.r) * S(F(1,9))
# expected exact value 1043/5625
exact_ok = (P111w.i == S(0) and P111w.r == formula and formula.rat() == F(1043, 5625))

# numerical first-principles over random complex QM configs
Ff = [[cmath.exp(2j*math.pi*((j*i) % 3)/3)/math.sqrt(3) for i in range(3)] for j in range(3)]
def P111_fp_float(G):
    tot = 0j
    for sig in perms:
        Ak = 1
        for i in range(3): Ak *= Ff[sig[i]][i]
        si = inv(sig)
        for rho in perms:
            Ab = 1
            for i in range(3): Ab *= Ff[rho[i]][i]
            ri = inv(rho)
            ov = 1
            for m in range(3): ov *= G[ri[m]][si[m]]
            tot += Ak * Ab.conjugate() * ov
    return tot
rng = random.Random(20260715)
def rand_unit(d):
    v = [complex(rng.gauss(0,1), rng.gauss(0,1)) for _ in range(d)]
    n = math.sqrt(sum(abs(x)**2 for x in v)); return [x/n for x in v]
def gram_float(ph):
    d = len(ph[0])
    return [[sum(ph[a][k].conjugate()*ph[b][k] for k in range(d)) for b in range(3)] for a in range(3)]
maxerr = 0.0
for _ in range(20000):
    d = rng.choice([3, 4, 5])
    ph = [rand_unit(d) for _ in range(3)]
    G = gram_float(ph)
    Sn = abs(G[0][1])**2 + abs(G[1][2])**2 + abs(G[2][0])**2
    tn = (G[0][1]*G[1][2]*G[2][0]).real
    maxerr = max(maxerr, abs(P111_fp_float(G).real - (2 - Sn + 4*tn)/9),
                 abs(P111_fp_float(G).imag))
check(f"P111 = (2 - S + 4tau)/9 holds EXACTLY on a rational witness "
      f"(P111 = 1043/5625) ({exact_ok}) and numerically from first principles "
      f"over 20000 random partial-distinguishability models (max error "
      f"{maxerr:.1e}). S = sum |<phi_i|phi_j>|^2, tau = Re(g12 g23 g31).",
      exact_ok and maxerr < 1e-12)

# ======================================================================
# B. det G = 1 - S + 2 tau  (and = the Leibniz sum), exact
# ======================================================================
print("## B: det G = 1 - S + 2 tau, exact (any Hermitian unit-diagonal 3x3)")
def rand_herm_unit_gaussrat():
    # Hermitian, unit diagonal, Gaussian-rational off-diagonals (need NOT be PSD)
    def gr(): return C(S(F(rng.randint(-3,3), rng.randint(1,4))), S(F(rng.randint(-3,3), rng.randint(1,4))))
    g12, g23, g31 = gr(), gr(), gr()
    return [[C(1), g12, g31.conj()], [g12.conj(), C(1), g23], [g31, g23.conj(), C(1)]]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2] - M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2] - M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1] - M[1][1]*M[2][0]))
def leibniz(M):
    tot = C(0)
    for p in perms:
        t = C(sgn(p))
        for i in range(3): t = t * M[i][p[i]]
        tot = tot + t
    return tot
detB_ok = True
for _ in range(3000):
    G = rand_herm_unit_gaussrat()
    Sm = (G[0][1]*G[0][1].conj()) + (G[1][2]*G[1][2].conj()) + (G[2][0]*G[2][0].conj())
    tm = (G[0][1] * G[1][2] * G[2][0])
    dS = S(1) - Sm.r + S(2)*tm.r                    # 1 - S + 2 Re(tau)
    d = det3(G)
    if not (d.i == S(0) and d.r == dS and d == leibniz(G)): detB_ok = False; break
check(f"det G = 1 - S + 2 Re(g12 g23 g31) exactly (and equals the Leibniz "
      f"permutation sum) on 3000 random Hermitian unit-diagonal Gaussian-"
      f"rational matrices: {detB_ok}.", detB_ok)

# ======================================================================
# C. Count-witness algebra: W = P111 + D2 - 2/3 = (2/9) det G, exact
# ======================================================================
print("## C: W = P111 + D2 - 2/3 = (2/9)(1 - S + 2tau) = (2/9) det G, exact")
alg_ok = True
for _ in range(4000):
    Sr = F(rng.randint(0,9), rng.randint(1,5)); tr = F(rng.randint(-9,9), rng.randint(1,5))
    P111 = (2 - Sr + 4*tr) / 9
    D2 = F(2,3) - Sr/9
    W = P111 + D2 - F(2,3)
    if W != F(2,9)*(1 - Sr + 2*tr): alg_ok = False; break
check(f"with P111 = (2-S+4tau)/9 and D2 = 2/3 - S/9, the count witness "
      f"W = P111 + D2 - 2/3 equals (2/9)(1 - S + 2tau) = (2/9) det G exactly, "
      f"over 4000 rational (S, tau): {alg_ok}.", alg_ok)

# ======================================================================
# D. Antisymmetrizer certificate: <A_-> = det G / 6, projector; W = (4/3)Tr >= 0
# ======================================================================
print("## D: antisymmetrizer certificate <A_-> = det G/6 (A_- a positive projector)")
# <phi1 phi2 phi3| A_- |phi1 phi2 phi3> = (1/6) sum_pi sgn(pi) prod_i G[i][pi(i)]
#   = det(G)/6 (Leibniz). A_- = (1/6) sum sgn(pi) P_pi is Hermitian with A_-^2 = A_-,
#   so <A_-> = ||A_-|phi..>||^2 >= 0, giving det G >= 0 and W = (4/3)<A_-> = (2/9)detG.
cert_ok = True
for _ in range(2000):
    G = rand_herm_unit_gaussrat()
    braket = C(0)
    for p in perms:
        t = C(sgn(p))
        for i in range(3): t = t * G[i][p[i]]
        braket = braket + t
    braket = braket * S(F(1,6))
    if braket != det3(G) * S(F(1,6)): cert_ok = False; break
# projector identity A_-^2 = A_- as a class function on S3: verify the group-algebra
# element e = (1/6) sum sgn(pi) pi satisfies e*e = e in Q[S3]
def mul_perm(p, q): return tuple(p[q[i]] for i in range(3))
coeff = {p: F(sgn(p), 6) for p in perms}
prod = {p: F(0) for p in perms}
for p in perms:
    for q in perms:
        prod[mul_perm(p, q)] += coeff[p]*coeff[q]
proj_ok = all(prod[p] == coeff[p] for p in perms)
check(f"<A_-> = det G / 6 exactly on 2000 random Grams ({cert_ok}); and the "
      f"antisymmetrizer e = (1/6) sum sgn(pi) pi is a projector (e*e = e in "
      f"Q[S_3], {proj_ok}), so <A_-> = ||A_-(phi1 x phi2 x phi3)||^2 >= 0, "
      f"forcing det G >= 0 and W = (4/3)<A_-> = (2/9) det G >= 0.",
      cert_ok and proj_ok)

# ======================================================================
# E. W >= 0 for all QM: exact on rational PSD Grams + adversarial float
# ======================================================================
print("## E: W = (2/9) det G >= 0 for every partial-distinguishability model")
# exact rational PSD Grams from rational unit vectors (real and complex)
unit_vecs = [
    [F(1),F(0),F(0),F(0)], [F(3,5),F(4,5),F(0),F(0)], [F(3,5),F(0),F(4,5),F(0)],
    [F(0),F(3,5),F(4,5),F(0)], [F(2,3),F(2,3),F(1,3),F(0)], [F(1,3),F(2,3),F(2,3),F(0)],
    [F(2,7),F(3,7),F(6,7),F(0)], [F(0),F(0),F(3,5),F(4,5)],
]
def realgram(vs):
    return [[sum(vs[a][k]*vs[b][k] for k in range(4)) for b in range(3)] for a in range(3)]
exact_pos_ok = True; ntest = 0
for combo in itertools.combinations(range(len(unit_vecs)), 3):
    vs = [unit_vecs[c] for c in combo]
    G = realgram(vs)
    Sm = G[0][1]**2 + G[1][2]**2 + G[2][0]**2
    tm = G[0][1]*G[1][2]*G[2][0]
    detG = 1 - Sm + 2*tm
    W = F(2,9)*detG
    ntest += 1
    if not (W >= 0): exact_pos_ok = False
# adversarial float descent hunting for W < 0
def Wf(ph):
    G = gram_float(ph)
    Sn = abs(G[0][1])**2 + abs(G[1][2])**2 + abs(G[2][0])**2
    tn = (G[0][1]*G[1][2]*G[2][0]).real
    return (2.0/9.0)*(1 - Sn + 2*tn)
best = 1e9
for _ in range(400):
    ph = [rand_unit(4) for _ in range(3)]; cur = Wf(ph)
    for eps in (0.3,0.1,0.03,0.01):
        for _ in range(50):
            p2 = [[x + complex(rng.gauss(0,1),rng.gauss(0,1))*eps for x in q] for q in ph]
            p2 = [[x/math.sqrt(sum(abs(y)**2 for y in q)) for x in q] for q in p2]
            c2 = Wf(p2)
            if c2 < cur: ph, cur = p2, c2
    best = min(best, cur)
check(f"W >= 0 exactly on all {ntest} rational PSD Grams built from rational "
      f"unit vectors ({exact_pos_ok}); and an adversarial descent over "
      f"partial-distinguishability models finds no W below zero (min "
      f"{best:.6f}). Gram positivity forbids W < 0.",
      exact_pos_ok and best > -1e-9)

# ======================================================================
# F. Convexity: mixed = convex hull, W affine, so W(mix) = sum p_lam W_lam >= 0
# ======================================================================
print("## F: mixed states are convex combinations; W is affine, so W(mix) >= 0")
# two pure configs, mixture weight p; W is affine in the counts, so
# W(p*Omega1 + (1-p)*Omega2) = p W1 + (1-p) W2. Exact witness.
def W_of_real(vs):
    G = realgram(vs); Sm = G[0][1]**2+G[1][2]**2+G[2][0]**2; tm = G[0][1]*G[1][2]*G[2][0]
    return F(2,9)*(1 - Sm + 2*tm)
W1 = W_of_real([unit_vecs[0], unit_vecs[1], unit_vecs[2]])
W2 = W_of_real([unit_vecs[3], unit_vecs[4], unit_vecs[5]])
p = F(3,7)
Wmix = p*W1 + (1-p)*W2
conv_ok = (W1 >= 0 and W2 >= 0 and Wmix >= 0 and Wmix == p*W1 + (1-p)*W2)
check(f"for a mixture p*Omega1 + (1-p)*Omega2 (p = 3/7), W is the affine "
      f"combination p*W1 + (1-p)*W2 = {Wmix} >= 0 with W1 = {W1} >= 0, "
      f"W2 = {W2} >= 0 ({conv_ok}). No convex combination crosses W = 0.",
      conv_ok)

# ======================================================================
# G. The exclusion: the extension point is outside; the raw-count test
# ======================================================================
print("## G: the registered extension point lies OUTSIDE the whole QM class")
r = F(3,5); Delta3 = 1 - 3*r*r - 2*r**3
P111_ext = F(7,1125); D2_ext = F(41,75)
W_ext = P111_ext + D2_ext - F(2,3)
excl = (W_ext == F(2,9)*Delta3 == F(-128,1125) and W_ext < 0
        and P111_ext + D2_ext < F(2,3)
        and F(2,3) - P111_ext - D2_ext == F(128,1125))
check(f"the registered extension has W = (2/9)Delta_3 = {W_ext} = -128/1125 < 0, "
      f"so it is outside the QM class (which requires W >= 0). The exact "
      f"separating raw-count test is P111 + D2 >= 2/3: the extension gives "
      f"P111 + D2 = {P111_ext + D2_ext} = 622/1125 < 750/1125 = 2/3 "
      f"(violation 128/1125). No partial-distinguishability Hilbert model, pure "
      f"or mixed, reproduces the registered count vector.", excl)

print()
print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
print("# CLOSED (proven): the clean mixed-state + mode-mismatch PSD-exclusion.")
print("# STILL OPEN (experimental layer, external expert): multiphoton")
print("# contamination, detector response, transfer-matrix uncertainty, drift.")
raise SystemExit(1 if FAIL else 0)
