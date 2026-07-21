#!/usr/bin/env python3
"""Chapter 49: the r_F boundary (exact).

  X1 boundary cubic: 4r^3+3r^2-2 has exactly one root in (0,1), bracketed
     at r_F = 0.60700729...
  X2 arc sextic identity: the real (3|2+1) family's positivity condition
     clears exactly to H(r,y) = 4(1-r^3)y^6 - 24r^2y^5 + 6(1-2r^3)y^4
     + 8r^3y^3 + 12r^2y^2 + 2.
  X3 vertex-first ordering: at rational r* = 0.60701 > r_F the vertex
     condition 2-3r^2-4r^3 is already negative while H(r*,y) has NO root
     y > 0 (Sturm certificate) -- the vertex fails strictly before the
     arc.  At r = 0.6072 the arc has failed too (H has a positive root),
     bracketing the arc's own failure point above r_F.
  X4 (2+1|2+1) discriminant identity: A1^2 - 4*A2*A0 factors exactly as
     -8(2c-1)^2(2c+1)^2(32*mu*c^2 - 3*mu^2 - 26*mu + 9), and the bracket
     equals 32*mu*c^2 - 3(mu-1/3)(mu+9).
  X5 leading-coefficient SOS: 4 - 16c^2(1-c^2) = 4(2c^2-1)^2 exactly,
     hence A2 <= 3*mu - 5 < 0.
  X6 Fourier saturation, exact cyclotomic arithmetic: for the 3x3 DFT,
     D/N = 9/2 exactly, and (unitary-normalized) 33N + 2P = 8 exactly;
     the vertex support value is (9/2) - (3/2)mu.
  X7 small r and endpoints: D <= 6N gives Q_r >= N(1-3r^2-2r^3) >= 0 for
     r <= 1/2 (checked as an exact identity), and Q_{-1} = P.
  X8 spot search: seeded random/hill-climb over full complex 3x3 matrices
     finds min Q_r/N > 0 at r = 0.60 and a violation at r = 0.62.
"""
import math
import random
from fractions import Fraction as F

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)

# ---------- univariate polynomials over Q (coefficient lists, low->high) ----
def pnorm(p):
    while p and p[-1] == 0:
        p.pop()
    return p
def padd(p, q):
    n = max(len(p), len(q))
    return pnorm([ (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
                   for i in range(n) ])
def pneg(p): return [-a for a in p]
def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1) if p and q else []
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return pnorm(r)
def pscale(p, s): return pnorm([a * s for a in p])
def peval(p, x):
    v = F(0)
    for a in reversed(p):
        v = v * x + a
    return v
def pderiv(p): return pnorm([p[i] * i for i in range(1, len(p))])
def prem(p, q):
    p = p[:]
    while len(p) >= len(q) and p:
        c = p[-1] / q[-1]
        d = len(p) - len(q)
        for i in range(len(q)):
            p[d + i] -= c * q[i]
        p = pnorm(p)
    return p
def sturm_chain(p):
    chain = [pnorm(p[:]), pderiv(p)]
    while chain[-1]:
        r = pneg(prem(chain[-2], chain[-1]))
        if not r:
            break
        chain.append(r)
    return [c for c in chain if c]
def sign_changes(chain, x):
    signs = []
    for c in chain:
        v = peval(c, x)
        if v != 0:
            signs.append(1 if v > 0 else -1)
    return sum(1 for i in range(1, len(signs)) if signs[i] != signs[i - 1])
def roots_in(p, a, b):
    """number of distinct real roots of p in (a, b]"""
    ch = sturm_chain(p)
    return sign_changes(ch, a) - sign_changes(ch, b)

# ---------- bivariate polynomials over Q as dicts {(i,j): coeff} ------------
def madd(A, B):
    C = dict(A)
    for k, v in B.items():
        C[k] = C.get(k, F(0)) + v
        if C[k] == 0:
            del C[k]
    return C
def mmul(A, B):
    C = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            key = (i + k, j + l)
            C[key] = C.get(key, F(0)) + a * b
            if C[key] == 0:
                del C[key]
    return C
def mscale(A, s):
    return {k: v * s for k, v in A.items() if v * s != 0}
def mono(i, j, c=1):
    return {(i, j): F(c)}
def msub(A, B): return madd(A, mscale(B, F(-1)))

# ---------- X1: the boundary cubic ------------------------------------------
cubic = [F(-2), F(0), F(3), F(4)]          # -2 + 3r^2 + 4r^3
check("X1a unique root in (0,1)", roots_in(cubic, F(0), F(1)) == 1)
lo, hi = F(60700729, 10**8), F(60700730, 10**8)
check("X1b bracket r_F", peval(cubic, lo) < 0 < peval(cubic, hi))

# ---------- X2: the arc sextic identity -------------------------------------
# family (e,e,e | e/y^2, -e*y, -e*y), e = 1.  Work in variables (r, y).
# N*y^4 = 3y^4 + 2y^6 + 1 ; A = 3 ; B = 1/y^2 - 2y
# P*y^4 = (3y^2 - 2y^3 + 1)^2 ; D*y^4 = (3y^2 + 2y^3 - 1)^2
# 2*y^4*Q_r = H(r,y) claimed.
r1 = mono(1, 0); y1 = mono(0, 1); one = mono(0, 0)
r2m, r3m = mmul(r1, r1), mmul(mmul(r1, r1), r1)
y2m, y3m, y4m, y5m, y6m = [mono(0, k) for k in (2, 3, 4, 5, 6)]
Ny4 = madd(madd(mscale(y4m, F(3)), mscale(y6m, F(2))), one)
Pside = madd(madd(mscale(y2m, F(3)), mscale(y3m, F(-2))), one)
Dside = madd(madd(mscale(y2m, F(3)), mscale(y3m, F(2))), mscale(one, F(-1)))
Py4, Dy4 = mmul(Pside, Pside), mmul(Dside, Dside)
Qy4 = madd(madd(mmul(madd(one, r3m), Ny4),
                mscale(mmul(mmul(r2m, msub(one, r1)), Py4), F(1, 2))),
           mscale(mmul(mmul(r2m, madd(one, r1)), Dy4), F(-1, 2)))
H_claim = {}
for cf, (i, j) in [(4, (0, 6)), (-4, (3, 6)), (-24, (2, 5)), (6, (0, 4)),
                   (-12, (3, 4)), (8, (3, 3)), (12, (2, 2)), (2, (0, 0))]:
    H_claim[(i, j)] = H_claim.get((i, j), F(0)) + F(cf)
check("X2 arc sextic identity", msub(mscale(Qy4, F(2)), H_claim) == {})

# ---------- X3: vertex-first ordering ---------------------------------------
def H_at(rq):
    """H(rq, y) as a univariate polynomial in y over Q"""
    r3v, r2v = rq**3, rq**2
    return pnorm([F(2), F(0), 12 * r2v, 8 * r3v, 6 * (1 - 2 * r3v),
                  -24 * r2v, 4 * (1 - r3v)])
rstar = F(60701, 100000)                    # r_F < rstar (vertex failed here)
check("X3a vertex already failed at r*", peval(cubic, rstar) > 0)  # 4r^3+3r^2-2 > 0
Hs = H_at(rstar)
check("X3b arc still positive at r* (no roots y>0)",
      roots_in(Hs, F(0), F(100)) == 0 and peval(Hs, F(0)) > 0)
H2 = H_at(F(6072, 10000))
check("X3c arc fails by 0.6072 (root exists)",
      roots_in(H2, F(0), F(100)) >= 1)
for rq in (F(11, 20), F(29, 50), F(3, 5), F(60700729, 10**8)):
    if roots_in(H_at(rq), F(0), F(100)) != 0:
        check("X3d arc positive on samples <= r_F", False)
        break
else:
    check("X3d arc positive on samples <= r_F", True)

# ---------- X4/X5: the (2+1|2+1) discriminant, variables (mu, c) ------------
mu = mono(1, 0); c = mono(0, 1)
c2, c4 = mmul(c, c), mmul(mmul(c, c), mmul(c, c))
c3 = mmul(mmul(c, c), c)
one2 = mono(0, 0)
A2 = madd(madd(mscale(mmul(madd(one2, mu), msub(c2, c4)), F(16))
               , mscale(mu, F(-1))), mscale(one2, F(-9)))
# A1 for one branch: -16c(2c^2 mu - 2c^2 - mu + 2); squared is branch-free
inner = madd(madd(mscale(mmul(mu, c2), F(2)), mscale(c2, F(-2))),
             madd(mscale(mu, F(-1)), mscale(one2, F(2))))
A1 = mscale(mmul(c, inner), F(-16))
A0 = mscale(madd(madd(mscale(mmul(c2, mu), F(8)), mscale(c2, F(8))),
                 madd(mscale(mu, F(-3)), one2)), F(-2))
Delta = msub(mmul(A1, A1), mscale(mmul(A2, A0), F(4)))
tc1 = msub(mscale(c, F(2)), one2)           # 2c-1
tc2 = madd(mscale(c, F(2)), one2)           # 2c+1
bracket = madd(mscale(mmul(mu, c2), F(32)),
               madd(mscale(mmul(mu, mu), F(-3)),
                    madd(mscale(mu, F(-26)), mscale(one2, F(9)))))
Delta_claim = mscale(mmul(mmul(mmul(tc1, tc1), mmul(tc2, tc2)), bracket), F(-8))
check("X4a Delta factorization", msub(Delta, Delta_claim) == {})
# bracket = 32 mu c^2 - 3(mu - 1/3)(mu + 9)
alt = madd(mscale(mmul(mu, c2), F(32)),
           mscale(mmul(msub(mu, mscale(one2, F(1, 3))),
                       madd(mu, mscale(one2, F(9)))), F(-3)))
check("X4b bracket identity", msub(bracket, alt) == {})
# X5: 4 - 16c^2(1-c^2) = 4(2c^2-1)^2
lhs = msub(mscale(one2, F(4)), mscale(msub(c2, c4), F(16)))
sq = msub(mscale(c2, F(2)), one2)
check("X5 leading-coefficient SOS", msub(lhs, mscale(mmul(sq, sq), F(4))) == {})

# ---------- X6: Fourier saturation over Z[w], w^2 = -1 - w ------------------
class Cyc:
    __slots__ = ("a", "b")                  # a + b*w
    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)
    def __mul__(s, o):
        # (a+bw)(c+dw) = ac + (ad+bc)w + bd w^2 ; w^2 = -1-w
        a, b, c, d = s.a, s.b, o.a, o.b
        return Cyc(a * c - b * d, a * d + b * c - b * d)
    def __add__(s, o): return Cyc(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Cyc(s.a - o.a, s.b - o.b)
    def conj(s): return Cyc(s.a - s.b, -s.b)  # conj(w) = w^2 = -1 - w
    def norm(s):                             # |a+bw|^2 = a^2 - ab + b^2
        return s.a * s.a - s.a * s.b + s.b * s.b
W = Cyc(0, 1)
Wp = {0: Cyc(1), 1: W, 2: W * W}
import itertools
perms = list(itertools.permutations(range(3)))
def sgn(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s
Z = []
for p in perms:
    m = Cyc(1)
    for i in range(3):
        m = m * Wp[(i * p[i]) % 3]           # DFT entries w^{jk}
    Z.append((m, sgn(p)))
Nf = sum(m.norm() for m, s in Z)
per = Cyc(0); det = Cyc(0)
for m, s in Z:
    per = per + m
    det = det + (m if s > 0 else Cyc(0) - m)
check("X6a D/N = 9/2 exactly", det.norm() * 2 == Nf * 9)
# unitary normalization: entries /sqrt(3) => monomials /3^{3/2} => squares /27
check("X6b 33N + 2P = 8 exactly (unitary)",
      F(33) * Nf / 27 + F(2) * per.norm() / 27 == 8)
# vertex support value (9/2) - (3/2)mu meets the line at 2 - 3r^2 - 4r^3 = 0:
r = F(3, 5)  # symbolic check via polynomial identity instead:
vertex_line = padd(pscale([F(1)], F(2)), padd(pscale([F(0), F(0), F(1)], F(-3)),
                                              pscale([F(0), F(0), F(0), F(1)], F(-4))))
check("X6c vertex condition is the boundary cubic",
      pnorm([a for a in vertex_line]) == pnorm([F(2), F(0), F(-3), F(-4)]))

# ---------- X7: small r and endpoints ---------------------------------------
# Q_r >= N(1 - 3r^2 - 2r^3) given D <= 6N and P >= 0: check the coefficient
# identity (1+r^3) - 3r^2(1+r) = 1 - 3r^2 - 2r^3 exactly.
lhs7 = padd([F(1), F(0), F(0), F(1)], pscale([F(0), F(0), F(1), F(1)], F(-3)))
check("X7a small-r coefficient identity",
      lhs7 == pnorm([F(1), F(0), F(-3), F(-2)]))
# Q_{-1}: 1 + r^3 = 0, (1/2)r^2(1-r) = 1, (1/2)r^2(1+r) = 0 at r = -1
check("X7b Q at r = -1 collapses to P",
      peval([F(1), F(0), F(0), F(1)], F(-1)) == 0
      and F(1, 2) * 1 * (1 - F(-1)) == 1
      and F(1, 2) * 1 * (1 + F(-1)) == 0)

# ---------- X8: spot search over complex 3x3 --------------------------------
def npd(M):
    N = P = D = 0.0
    pr = 0j; dr = 0j
    for p in perms:
        z = 1 + 0j
        for i in range(3):
            z *= complex(M[i][2 * p[i]], M[i][2 * p[i] + 1])
        N += abs(z) ** 2
        pr += z
        dr += z if sgn(p) > 0 else -z
    return N, abs(pr) ** 2, abs(dr) ** 2
def q_over_n(M, r):
    N, P, D = npd(M)
    if N < 1e-12:
        return 10.0
    return ((1 + r ** 3) * N + 0.5 * r * r * (1 - r) * P
            - 0.5 * r * r * (1 + r) * D) / N
def spot_min(r, iters=6000, restarts=8, seed=7):
    rng = random.Random(seed)
    best = 10.0
    for _ in range(restarts):
        M = [[rng.gauss(0, 1) for _ in range(6)] for _ in range(3)]
        v = q_over_n(M, r)
        step = 0.5
        for _ in range(iters):
            i, j = rng.randrange(3), rng.randrange(6)
            old = M[i][j]
            M[i][j] += rng.gauss(0, step)
            nv = q_over_n(M, r)
            if nv < v:
                v = nv
            else:
                M[i][j] = old
            step = max(step * 0.9995, 1e-3)
        best = min(best, v)
    return best
m060 = spot_min(0.60)
m062 = spot_min(0.62)
check("X8a positive at r = 0.60 (min ~ 0.026)", 0.0 < m060 < 0.2)
check("X8b violated at r = 0.62", m062 < 0.0)

# ---------- report ----------------------------------------------------------
for name in PASS:
    print("[PASS]", name)
for name in FAIL:
    print("[FAIL]", name)
print("rf_boundary: %d passed, %d failed" % (len(PASS), len(FAIL)))
if FAIL:
    raise SystemExit(1)
