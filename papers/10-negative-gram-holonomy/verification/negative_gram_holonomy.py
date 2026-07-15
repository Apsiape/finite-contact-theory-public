#!/usr/bin/env python3
"""Chapter 10 -- negative-Gram identity holonomy (the program's FIRST divergence).

Dependency-free (Python standard library only). Two separable things are
verified, and they must not be conflated:

  (A) THE THEOREM -- unconditionally true, PROVEN, no bridge premises.
      "Universal accessible positivity": for EVERY complex 3x3 interferometer
      matrix A, with z_sigma = prod_i A[i][sigma(i)],
          152 N + 9 |per A|^2 - 36 |det A|^2 >= 0,   N = sum_sigma |z_sigma|^2.
      The proof uses only the toric product relation prod_{even} z = prod_{odd}
      z -- no unitarity. Because the form is degree-6 homogeneous, positivity
      on all matrices is equivalent to positivity on all contractions, i.e. on
      EVERY passive-linear-optical transfer matrix, lossless OR lossy. So the
      negative-eigenvalue sector is a lawful probabilistic model on the complete
      admitted grammar that lies OUTSIDE the positive-semidefinite Hilbert Gram
      cone: global Hilbert PSD fails while operational block positivity survives.
      On the lossless unitary core U(3) the sharper strict margin
      152N+9|per|^2-36|det|^2 >= (7/2)N holds (saturated by the Fourier tritter);
      the (7/2) margin for ARBITRARY matrices is FALSE and stays killed
      (explicit -495 witness).

  (B) THE PREDICTION -- conditional, preregistered, experiment-OPEN. On a
      received apparatus anchor r = 3/5 and the odd identity-holonomy sector
      (Phi = pi), Delta_3 = -64/125 < 0 while ordinary complex-Hilbert QM forces
      Delta_3 >= 0. The registered joint count vector (Delta_3, W, Q_3) excludes
      the PSD Gram class and rejects the pairwise-only null. A registered BET
      with a protocol and kill conditions, NOT a discovery; the physical bridge
      premises are held open and the mixed-state / full-nuisance PSD-exclusion
      is the OPEN crux for an external quantum-optics expert.

Verification below: the theorem (A) is checked EXACTLY (the foundational
Fourier-coordinate identity; positivity on exact rational toric witnesses; the
-495 kill of the (7/2)-universal; the exact U(3) reduction identity and strict
margin on rational Cayley unitaries and the Fourier tritter; exact separable-
loss covariance) and by an INDEPENDENT adversarial descent over the full toric
set. The prediction (B) numbers are all exact.
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
EVEN = [q for q in perms if sgn(q) == 1]
ODD = [q for q in perms if sgn(q) == -1]

# ======================================================================
# Exact number field Q(sqrt 3): a + b*sqrt3 for the real/imag parts, and
# complex over it -- enough for rational matrices AND the Fourier tritter.
# ======================================================================
class S:
    __slots__ = ("a", "b")
    def __init__(s, a=0, b=0): s.a = F(a); s.b = F(b)
    @staticmethod
    def c(o): return o if isinstance(o, S) else S(o, 0)
    def __add__(s, o): o = S.c(o); return S(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = S.c(o); return S(s.a - o.a, s.b - o.b)
    def __neg__(s): return S(-s.a, -s.b)
    def __mul__(s, o):
        o = S.c(o); return S(s.a * o.a + 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def inv(s):
        d = s.a * s.a - 3 * s.b * s.b; return S(s.a / d, -s.b / d)
    def __truediv__(s, o): return s * S.c(o).inv()
    def __eq__(s, o): o = S.c(o); return s.a == o.a and s.b == o.b
    def __ge__(s, o):    # only used when b == 0 (rational)
        o = S.c(o); assert s.b == 0 and o.b == 0; return s.a >= o.a
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
    def __mul__(s, o):
        o = C.c(o); return C(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def conj(s): return C(s.r, -s.i)
    def ab2(s): return s.r * s.r + s.i * s.i          # -> S
    def inv(s): n = s.ab2(); c = s.conj(); return C(c.r / n, c.i / n)
    def __truediv__(s, o): return s * C.c(o).inv()
    def __eq__(s, o): o = C.c(o); return s.r == o.r and s.i == o.i

def emono(A): return {q: A[0][q[0]] * A[1][q[1]] * A[2][q[2]] for q in perms}
def edet(A):
    o = C(0)
    for q in perms:
        t = C(sgn(q))
        for i in range(3): t = t * A[i][q[i]]
        o = o + t
    return o
def eper(A):
    o = C(0)
    for q in perms:
        t = C(1)
        for i in range(3): t = t * A[i][q[i]]
        o = o + t
    return o
def eN(A):
    o = S(0)
    for z in emono(A).values(): o = o + z.ab2()
    return o

# ======================================================================
# A. Prediction (B) -- exact core numbers on r = 3/5, odd sector Phi = pi
# ======================================================================
print("## A: the (conditional, preregistered) prediction -- exact numbers")
r = F(3, 5); a = r * r; b = -(r ** 3)
Delta3 = 1 - 3 * a - 2 * (r ** 3)
factor = (1 - 2 * r) * (1 + r) ** 2
thresh = all((1 - 2 * F(k, 20)) * (1 + F(k, 20)) ** 2 > 0 for k in range(0, 10)) \
    and (1 - 2 * F(1, 2)) * (1 + F(1, 2)) ** 2 == 0 \
    and all((1 - 2 * F(k, 20)) * (1 + F(k, 20)) ** 2 < 0 for k in range(11, 20))
check(f"Delta_3 = 1-3r^2-2r^3 = {Delta3} = -64/125, factors as (1-2r)(1+r)^2 "
      f"({Delta3 == factor}), negative exactly for r > 1/2 ({thresh}); r = 3/5 "
      f"received, negative sign is the odd Z_2 holonomy consequence.",
      Delta3 == F(-64, 125) and Delta3 == factor and thresh)

P111 = (2 + 4 * b - 3 * a) / 9; P300 = (1 + 3 * a + 2 * b) / 27; P210 = (1 - b) / 9
norm = P111 + 3 * P300 + 6 * P210
check(f"tritter probs P111={P111}(7/1125), P300={P300}(206/3375), "
      f"P210={P210}(152/1125), nonnegative, normalized ({norm}=1).",
      P111 == F(7, 1125) and P300 == F(206, 3375) and P210 == F(152, 1125)
      and norm == 1 and min(P111, P300, P210) >= 0)

D2 = (2 - a) / 3; W = P111 + D2 - F(2, 3); Q3 = P111 - D2 + F(4, 9)
check(f"D_2={D2}(41/75); W = P111+D_2-2/3 = {W} = (2/9)Delta_3 "
      f"({W == F(2,9)*Delta3}); Q_3 = P111-D_2+4/9 = {Q3} = (4/9)b "
      f"({Q3 == F(4,9)*b}); pairwise-only null gives Q_3 = 0 (b->0).",
      D2 == F(41, 75) and W == F(-128, 1125) and W == F(2, 9) * Delta3
      and Q3 == F(-12, 125) and Q3 == F(4, 9) * b and F(4, 9) * 0 == 0)

# PSD exclusion: Delta_3 = det G; the positive-Hilbert cone forces
# cos Phi >= (3r^2-1)/(2r^3) = 5/27, capping Phi <= ~79.3 deg.
cos_bound = (3 * a - 1) / (2 * r ** 3)
phi_max = math.degrees(math.acos(float(cos_bound)))
check(f"Delta_3 = det G = 1-3r^2+2r^3 cosPhi; PSD forces cosPhi >= "
      f"(3r^2-1)/(2r^3) = {cos_bound}(5/27), i.e. Phi <= {phi_max:.1f} deg, "
      f"while the extension reaches Phi = pi. So Delta_3 = -64/125 < 0 is "
      f"OUTSIDE the PSD Hilbert Gram cone.",
      cos_bound == F(5, 27) and 79.0 < phi_max < 79.6)

# ======================================================================
# B. The toric product identity (exact + structural)
# ======================================================================
print("## B: the passive-linear-optics toric identity prod_even z = prod_odd z")
even_cells = sorted((i, q[i]) for q in EVEN for i in range(3))
odd_cells = sorted((i, q[i]) for q in ODD for i in range(3))
allc = sorted((i, j) for i in range(3) for j in range(3))
Aw = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
zt = {q: Aw[0][q[0]] * Aw[1][q[1]] * Aw[2][q[2]] for q in perms}
pe = 1; po = 1; full = 1
for q in EVEN: pe *= zt[q]
for q in ODD: po *= zt[q]
for i in range(3):
    for j in range(3): full *= Aw[i][j]
check(f"the even and odd permutation triples each cover every (row,col) once "
      f"({even_cells == allc and odd_cells == allc}); so prod_even z = "
      f"prod_odd z = prod(all entries): {pe} = {po} = {full} "
      f"({pe == po == full}).", even_cells == allc and odd_cells == allc and pe == po == full)

# ======================================================================
# C. THE THEOREM (A) -- universal accessible positivity, PROVEN
# ======================================================================
print("## C: universal accessible positivity -- 152N + 9|per|^2 - 36|det|^2 >= 0 for EVERY A")

# C1 -- the foundational identity, exact. With alpha = (sum x)/3, delta =
# (sum y)/3, M = |alpha|^2+|delta|^2:  Q = 152 N - 243 M + 810 Re(alpha conj(delta)).
def Q_of(x, y):
    N = sum((z.ab2() for z in x), S(0)) + sum((z.ab2() for z in y), S(0))
    sx = C(0); sy = C(0)
    for z in x: sx = sx + z
    for z in y: sy = sy + z
    return S(152) * N + S(9) * (sx + sy).ab2() - S(36) * (sx - sy).ab2(), N
def randCq(rng): return C(S(F(rng.randint(-4, 4), rng.randint(1, 4))),
                          S(F(rng.randint(-4, 4), rng.randint(1, 4))))
rng = random.Random(20260714)
id5_ok = True
for _ in range(4000):
    x = [randCq(rng) for _ in range(3)]; y = [randCq(rng) for _ in range(3)]
    Q, N = Q_of(x, y)
    sx = C(0); sy = C(0)
    for z in x: sx = sx + z
    for z in y: sy = sy + z
    al = sx * S(F(1, 3)); de = sy * S(F(1, 3))
    M = al.ab2() + de.ab2()
    reAD = (al * de.conj()).r
    rhs = S(152) * N - S(243) * M + S(810) * reAD
    id5_ok &= (Q == rhs)
check(f"the foundational identity Q = 152N - 243M + 810 Re(alpha conj delta) "
      f"holds exactly on 4000 Gaussian-rational (x,y) ({id5_ok}) -- the "
      f"C_3-Fourier reduction the proof rests on.", id5_ok)

# C2 -- EXACT positivity on rational toric witnesses  x0 x1 x2 = y0 y1 y2.
exact_toric_ok = True; wit = 0
for _ in range(6000):
    x = [randCq(rng) for _ in range(3)]
    y0 = randCq(rng); y1 = randCq(rng)
    if y0.ab2() == 0 or y1.ab2() == 0: continue
    y2 = (x[0] * x[1] * x[2]) / (y0 * y1)          # enforce the toric constraint
    y = [y0, y1, y2]
    if not (x[0] * x[1] * x[2] == y[0] * y[1] * y[2]): exact_toric_ok = False; break
    Q, N = Q_of(x, y)
    if N == 0: continue
    wit += 1
    if not (Q.rat() >= 0): exact_toric_ok = False; break
check(f"POSITIVITY is exact on {wit} nonzero rational toric witnesses "
      f"(x0x1x2 = y0y1y2 enforced exactly; Q >= 0 in exact Q(sqrt3) "
      f"arithmetic): {exact_toric_ok}.", exact_toric_ok and wit > 1000)

# C3 -- INDEPENDENT adversarial descent over the full toric set (float): the
# theorem is Q > 0 on every nonzero toric vector; hunt hard for a violation.
def Qf(x, y):
    N = sum(abs(v) ** 2 for v in x) + sum(abs(v) ** 2 for v in y)
    sx = sum(x); sy = sum(y)
    return 152 * N + 9 * abs(sx + sy) ** 2 - 36 * abs(sx - sy) ** 2, N
def toric(rng):
    x = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(3)]
    y0 = complex(rng.gauss(0, 1), rng.gauss(0, 1)); y1 = complex(rng.gauss(0, 1), rng.gauss(0, 1))
    if abs(y0 * y1) < 1e-9: y1 = 1 + 0j
    return x, [y0, y1, x[0] * x[1] * x[2] / (y0 * y1)]
def ratio(x, y):
    Q, N = Qf(x, y); return Q / N if N > 1e-14 else None
worst = 1e9
for _ in range(200000):
    x, y = toric(rng); rr = ratio(x, y)
    if rr is not None: worst = min(worst, rr)
best = 1e9
for _ in range(300):
    x, y = toric(rng); cur = ratio(x, y) or 1e9
    for eps in (0.4, 0.15, 0.06, 0.02, 0.008):
        for _ in range(60):
            xx = [v + complex(rng.gauss(0, 1), rng.gauss(0, 1)) * eps for v in x]
            y0 = y[0] + complex(rng.gauss(0, 1), rng.gauss(0, 1)) * eps
            y1 = y[1] + complex(rng.gauss(0, 1), rng.gauss(0, 1)) * eps
            if abs(y0 * y1) < 1e-9: continue
            yy = [y0, y1, xx[0] * xx[1] * xx[2] / (y0 * y1)]
            c2 = ratio(xx, yy)
            if c2 is not None and c2 < cur: x, y, cur = xx, yy, c2
    best = min(best, cur)
check(f"an INDEPENDENT adversarial descent over the full toric set (200k broad "
      f"+ 300 restarts) finds NO Q/N below zero: min broad {worst:.4f}, min "
      f"descent {best:.4f} (both > 0, strict). The proof's conclusion Q > 0 on "
      f"every nonzero toric vector is corroborated by a hostile numerical hunt.",
      worst > 1e-4 and best > 1e-4)

# C4 -- the (7/2)-margin UNIVERSAL statement is FALSE and stays killed.
Ak = [[C(-4), C(-1), C(1)], [C(-7), C(1), C(-3)], [C(6), C(-3), C(-5)]]
Nk = eN(Ak).rat(); perk = eper(Ak).r.rat(); detk = edet(Ak).r.rat()
strong = 152 * Nk + 9 * perk * perk - 36 * detk * detk - F(7, 2) * Nk
zeromargin = 152 * Nk + 9 * perk * perk - 36 * detk * detk
zk = emono(Ak); pek = C(1); pok = C(1)
for q in EVEN: pek = pek * zk[q]
for q in ODD: pok = pok * zk[q]
check(f"the (7/2)-margin ARBITRARY-matrix statement is FALSE (stays killed): "
      f"A=[[-4,-1,1],[-7,1,-3],[6,-3,-5]] has N={Nk}, per={perk}, det={detk}, "
      f"152N+9|per|^2-36|det|^2-(7/2)N = {strong} (-495 < 0); yet it obeys the "
      f"toric identity ({pek == pok}) and still satisfies the PROVEN zero-margin "
      f"152N+9|per|^2-36|det|^2 = {zeromargin} >= 0.",
      strong == -495 and pek == pok and zeromargin >= 0)

# ======================================================================
# D. The sharper U(3) strict margin (7/2)N -- exact corollary on the core
# ======================================================================
print("## D: on the lossless unitary core U(3), the strict margin 152N+9|per|^2-36|det|^2 >= (7/2)N")
def matmul_f(A, B): return [[sum((A[i][k] * B[k][j] for k in range(3)), F(0)) for j in range(3)] for i in range(3)]
def inv3_f(M):
    det = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    cof = [[(M[(i+1)%3][(j+1)%3]*M[(i+2)%3][(j+2)%3]-M[(i+1)%3][(j+2)%3]*M[(i+2)%3][(j+1)%3]) for j in range(3)] for i in range(3)]
    return [[cof[j][i] / det for j in range(3)] for i in range(3)]
def cayley(p, q, r_):
    Sk = [[F(0), -p, -q], [p, F(0), -r_], [q, r_, F(0)]]
    I = [[F(1 if i == j else 0) for j in range(3)] for i in range(3)]
    Ip = [[I[i][j] + Sk[i][j] for j in range(3)] for i in range(3)]
    Im = [[I[i][j] - Sk[i][j] for j in range(3)] for i in range(3)]
    Uf = matmul_f(Im, inv3_f(Ip))
    return [[C(S(Uf[i][j])) for j in range(3)] for i in range(3)]
def reduction_bundle(U):
    z = emono(U); det = edet(U); nrm = det.conj()
    E = [nrm * z[q] for q in EVEN]; O = [nrm * z[q] for q in ODD]
    y = E[0].i
    common = all(x.i == y for x in E + O)
    e = [x.r for x in E]; o = [x.r for x in O]
    m = (e[0] + e[1] + e[2] + o[0] + o[1] + o[2]) * S(F(1, 6))
    aa = [x - (m + S(F(1, 6))) for x in e]; bb = [x - (m - S(F(1, 6))) for x in o]
    A2 = aa[0]*aa[0]+aa[1]*aa[1]+aa[2]*aa[2]; B2 = bb[0]*bb[0]+bb[1]*bb[1]+bb[2]*bb[2]
    A3 = aa[0]*aa[1]*aa[2]; B3 = bb[0]*bb[1]*bb[2]
    s = A2 + B2; D = A3 - B3
    N = eN(U); per2 = eper(U).ab2()
    lhs = S(33) * N + S(2) * per2 - S(8)
    rhs = S(F(3, 2)) * (S(7) * s + S(180) * D)
    return common and (lhs == rhs) and (lhs.rat() >= 0) and ((33*N + 2*per2).rat() >= 8)
cvals = [F(-2), F(-1), F(-1, 2), F(1, 3), F(0), F(1, 2), F(1), F(2)]
cases = [(p, q, rr) for p in cvals for q in cvals for rr in cvals if (p, q, rr) != (0, 0, 0)][::3][:120]
u3_ok = all(reduction_bundle(cayley(*c)) for c in cases)
perm_ok = all(reduction_bundle([[C(1 if q[i] == j else 0) for j in range(3)] for i in range(3)]) for q in perms)
sq = S(0, F(1, 3)); om = C(S(F(-1, 2)), S(0, F(1, 2)))
Ff = [[C(sq), C(sq), C(sq)], [C(sq), C(sq)*om, C(sq)*om*om], [C(sq), C(sq)*om*om, C(sq)*om]]
NF = eN(Ff).rat(); perF2 = eper(Ff).ab2().rat(); detF2 = edet(Ff).ab2().rat()
fourier_ok = (NF == F(2, 9) and perF2 == F(1, 3) and detF2 == 1
              and 33 * NF + 2 * perF2 == 8
              and 152 * NF + 9 * perF2 - 36 * detF2 - F(7, 2) * NF == 0)
check(f"on the unitary core the exact reduction 33N+2|per|^2-8 = (3/2)(7s+180D) "
      f"and the strict margin hold on {len(cases)} rational Cayley unitaries "
      f"({u3_ok}) and all six permutation matrices ({perm_ok}); the Fourier "
      f"tritter (exact) has N=2/9, |per|^2=1/3 and SATURATES at 33N+2|per|^2=8 "
      f"({fourier_ok}).", u3_ok and perm_ok and fourier_ok)

# ======================================================================
# E. Separable-loss covariance -- exact
# ======================================================================
print("## E: separable input/output loss A = D_L U D_R is covered (exact covariance)")
U = cayley(F(1, 3), F(-1, 2), F(2, 5))
dl = [C(S(F(1, 2)), S(F(1, 4))), C(S(F(2, 3))), C(S(0), S(F(-1, 5)))]
dr = [C(S(F(3, 4))), C(S(F(-1, 6)), S(F(1, 7))), C(S(F(5, 8)))]
Al = [[dl[i] * U[i][j] * dr[j] for j in range(3)] for i in range(3)]
kap = C(1)
for x in dl + dr: kap = kap * x
zU = emono(U); zA = emono(Al); sc = kap.ab2()
cov = all(zA[q] == kap * zU[q] for q in perms)
Ncov = eN(Al) == sc * eN(U)
percov = eper(Al).ab2() == sc * eper(U).ab2()
detcov = edet(Al).ab2() == sc * edet(U).ab2()
check(f"every monomial of A = D_L U D_R picks up the same factor kappa "
      f"({cov}); hence N, |per|^2, |det|^2 all scale by |kappa|^2 "
      f"({Ncov and percov and detcov}); the degree-6 form scales by |kappa|^2, "
      f"so positivity transfers to every separably attenuated unitary -- and, "
      f"with the universal theorem, to every passive-linear-optical apparatus.",
      cov and Ncov and percov and detcov)

print()
print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
print("# (A) universal accessible positivity: PROVEN + verified (exact + adversarial).")
print("# (B) the physical Delta_3 < 0 prediction is CONDITIONAL, preregistered,")
print("#     experiment-OPEN -- an archival/priority record, not a discovery.")
raise SystemExit(1 if FAIL else 0)
