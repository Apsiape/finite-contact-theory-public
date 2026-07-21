#!/usr/bin/env python3
"""Chapter 52: the amalgamation boundary (exact).

Standard library only; exact rational arithmetic throughout.

Checks, in five groups:
  G1  The tritter identity W = P111 + D2 - 2/3 = (2/9) det G, as an exact
      identity over random rational Hermitian Grams, with det G verified
      against the explicit 3x3 determinant.
  G2  The chordal contrast: a path-graph (chordal) partial Gram always
      completes by the product rule (exact samples), while an explicit
      4-cycle specification is certifiably non-completable (every candidate
      completion has a negative principal minor -- exact certificate).
  G3  Elliptope frustration at odd holonomy: the identity
      1 - 3r^2 - 2r^3 = (1+r)^2 (1-2r), hence det G < 0 exactly when
      r > 1/2 on the odd-holonomy line, with the boundary at r = 1/2 exact.
  G4  The rung table, exact where classical and bracketed where algebraic:
      CHSH classical 2 (exhaustive), PR value 4 (direct), Tsirelson 2*sqrt2
      (certified bracket); order-rung causal 3/4 (exhaustive one-way
      strategies); pentagon classical 8 (exhaustive chained strategies),
      quantum 10*cos(pi/10) > 8 via its minimal polynomial 16x^4-20x^2+5
      (certified root bracket).
  G5  Fourier saturation cross-check: at the maximally frustrated real
      point g_ij = -1/2 (trine), det G = 0 exactly -- the amalgamation
      boundary passes through the trine.
"""
from fractions import Fraction as F
import random

random.seed(7)
fails = []

def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" {detail}" if detail else ""))
    if not ok:
        fails.append(label)

# ---------- exact complex rationals ----------
class C:
    __slots__ = ("re", "im")
    def __init__(self, re, im=0):
        self.re = F(re); self.im = F(im)
    def __add__(a, b): return C(a.re + b.re, a.im + b.im)
    def __sub__(a, b): return C(a.re - b.re, a.im - b.im)
    def __mul__(a, b): return C(a.re*b.re - a.im*b.im, a.re*b.im + a.im*b.re)
    def conj(a): return C(a.re, -a.im)
    def abs2(a): return a.re*a.re + a.im*a.im
    def __eq__(a, b): return a.re == b.re and a.im == b.im

def randc():
    return C(F(random.randint(-4, 4), random.randint(1, 5)),
             F(random.randint(-4, 4), random.randint(1, 5)))

def det3_hermitian(g12, g13, g23):
    """det of [[1,g12,g13],[g12*,1,g23],[g13*,g23*,1]] -- cofactor expansion.

    det = (1 - |g23|^2) - Re part of g12 (g12* - g23 g13*) + g13 (g12* g23* - g13*);
    the determinant of a Hermitian matrix is real, and the expansion below keeps
    exact rational real parts throughout.
    """
    a, b, c = g12, g13, g23
    return (F(1) - c.abs2()) - (a * (a.conj() - c * b.conj())).re \
           + (b * (a.conj() * c.conj() - b.conj())).re

def det4_hermitian(gij):
    """Full 4x4 Hermitian determinant by Leibniz expansion (24 terms), exact.
    gij(i, j) returns the (i, j) entry for 1-based i, j."""
    from itertools import permutations
    n = 4
    total = C(0)
    for perm in permutations(range(1, n + 1)):
        sign = 1
        p = list(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    sign = -sign
        term = C(sign)
        for i in range(1, n + 1):
            term = term * gij(i, perm[i - 1])
        total = total + term
    return total.re

# G1: the tritter identity
ok_det = True; ok_w = True
for _ in range(60):
    g12, g13, g23 = randc(), randc(), randc()
    S = g12.abs2() + g13.abs2() + g23.abs2()
    # tau = Re(g12 g23 g31) with g31 = conj(g13)
    tau = (g12 * g23 * g13.conj()).re
    lhs = F(1) - S + 2*tau
    rhs = det3_hermitian(g12, g13, g23)
    if lhs != rhs: ok_det = False
    P111 = (F(2) - S + 4*tau) / 9
    D2 = F(2, 3) - S / 9
    W = P111 + D2 - F(2, 3)
    if W != F(2, 9) * lhs: ok_w = False
check("G1a det G = 1 - S + 2 tau (explicit determinant, 60 exact samples)", ok_det)
check("G1b W = P111 + D2 - 2/3 = (2/9) det G (exact identity)", ok_w)

# G2a: chordal path P4 completes by the product rule (exact samples)
ok_path = True
for _ in range(40):
    # specify g12, g23, g34 with |g| <= 1 (scale down), complete g13=g12 g23,
    # g14=g12 g23 g34, g24=g23 g34; the completed G is a Gram of the rank-one
    # chain construction, PSD by construction -- verify all principal minors >= 0.
    def small():
        z = randc()
        s = z.abs2()
        if s > 1:  # scale into the disc
            k = F(1, 2)
            while (C(k)*z).abs2() > 1: k /= 2
            z = C(k) * z
        return z
    a, b, c = small(), small(), small()
    g = {(1,2): a, (2,3): b, (3,4): c, (1,3): a*b, (1,4): a*b*c, (2,4): b*c}
    def gij(i, j):
        if i == j: return C(1)
        if (i, j) in g: return g[(i, j)]
        return g[(j, i)].conj()
    # principal minors: all 1x1 = 1; 2x2: 1-|g|^2 >= 0; 3x3 and 4x4 via det3 and
    # a Schur step for 4x4
    m3 = []
    for tri in [(1,2,3),(1,2,4),(1,3,4),(2,3,4)]:
        i,j,k = tri
        m3.append(det3_hermitian(gij(i,j), gij(i,k), gij(j,k)))
    ok2 = all(F(1) - gij(i,j).abs2() >= 0 for i in range(1,5) for j in range(i+1,5))
    m4 = det4_hermitian(gij)
    if not (ok2 and all(m >= 0 for m in m3) and m4 >= 0): ok_path = False
check("G2a chordal path completes by the product rule (all principal minors >= 0, 40 samples)", ok_path)

# G2b: the 4-cycle certificate: g12=g23=g34=1, g14=-1 has NO PSD completion.
# Any completion (s = g13, t = g24) must satisfy:
#   minor{1,2,3}: -(|s-1|^2) >= 0  => s = 1
#   minor{1,2,4}: -(|t+1|^2) >= 0  => t = -1
#   then minor{1,3,4} with g13=1, g14=-1, g34=1 equals -4 < 0.
one, mone = C(1), C(-1)
m123_at = lambda s: det3_hermitian(one, s, one)          # g12=1, g13=s, g23=1
m124_at = lambda t: det3_hermitian(one, mone, t)          # g12=1, g14=-1, g24=t
ok_i = True
for _ in range(30):
    s = randc(); t = randc()
    e123 = m123_at(s); want123 = -((s - one).abs2())
    e124 = m124_at(t); want124 = -((t + one).abs2())
    if e123 != want123 or e124 != want124: ok_i = False
check("G2b(i) 4-cycle forcing identities m123 = -|s-1|^2, m124 = -|t+1|^2 (exact)", ok_i)
m134 = det3_hermitian(one, mone, one)                     # g13=1, g14=-1, g34=1
check("G2b(ii) forced completion s=1, t=-1 kills minor {1,3,4}", m134 == F(-4), f"(= {m134})")

# G3: elliptope frustration on the odd-holonomy line
ok_id = True
for num in range(-20, 21):
    r = F(num, 10)
    lhs = 1 - 3*r*r - 2*r*r*r
    rhs = (1 + r)*(1 + r)*(1 - 2*r)
    if lhs != rhs: ok_id = False
check("G3a identity 1 - 3r^2 - 2r^3 = (1+r)^2 (1-2r) (41 exact points)", ok_id)
def detG_odd(r):  # all moduli r, odd holonomy: tau = -r^3
    return 1 - 3*r*r + 2*(-(r*r*r))
check("G3b det G(odd) = 0 exactly at r = 1/2", detG_odd(F(1,2)) == 0)
check("G3c det G(odd) > 0 for r < 1/2, < 0 for r > 1/2 (exact samples)",
      all(detG_odd(F(k,100)) > 0 for k in (10, 30, 49)) and
      all(detG_odd(F(k,100)) < 0 for k in (51, 70, 90)))

# G4: the rung table
# CHSH classical bound: exhaustive deterministic strategies
best = F(-10)
for a0 in (1,-1):
    for a1 in (1,-1):
        for b0 in (1,-1):
            for b1 in (1,-1):
                v = a0*b0 + a0*b1 + a1*b0 - a1*b1
                best = max(best, F(v))
check("G4a CHSH classical maximum = 2 (exhaustive 16 strategies)", best == 2)
# PR box: E(xy) = (-1)^{xy}, so S = E00 + E01 + E10 - E11 = 1 + 1 + 1 - (-1)
S_pr = F(1) + F(1) + F(1) - F(-1)
check("G4b PR box value = 4 (direct)", S_pr == 4)
# Tsirelson bracket: 2 sqrt2 in (2.8284271, 2.8284272): check via squares
lo, hi = F(28284271, 10**7), F(28284272, 10**7)
check("G4c Tsirelson 2*sqrt2 certified bracket", lo*lo < 8 < hi*hi)
# order rung causal bound 3/4: exhaustive one-way deterministic strategies (both orders)
def causal_max(d):
    best = F(0)
    msgs = [tuple(m) for m in _tuples(d, d)]
    guesses_E = [tuple(g) for g in _tuples(d, d)]
    for gE in guesses_E:
        pE = F(sum(1 for e in range(d) for l in range(d) if gE[e] == l), d*d)
        for m in msgs:
            # later party decodes optimally per (l, message-class)
            hit = 0
            for l in range(d):
                for c in set(m):
                    es = [e for e in range(d) if m[e] == c]
                    hit += max(sum(1 for e in es if e == e2) for e2 in range(d))
            pL = F(hit, d*d)
            best = max(best, (pE + pL) / 2)
    return best
def _tuples(n, d):
    if n == 0:
        yield ()
        return
    for rest in _tuples(n-1, d):
        for v in range(d):
            yield rest + (v,)
check("G4d order-rung causal maximum = 3/4 at d=2 (exhaustive)", causal_max(2) == F(3,4))
check("G4e order-rung causal maximum = 2/3 at d=3 (exhaustive over partitions)", causal_max(3) == F(2,3))
# pentagon: chained Bell N=5 classical bound 8 (exhaustive over 2^10 sign strategies)
bestP = F(-100)
for A in range(32):
    for B in range(32):
        a = [1 if (A >> i) & 1 else -1 for i in range(5)]
        b = [1 if (B >> i) & 1 else -1 for i in range(5)]
        v = sum(a[i]*b[i] for i in range(5)) + sum(a[(i+1) % 5]*b[i] for i in range(4)) - a[0]*b[4]
        bestP = max(bestP, F(v))
check("G4f pentagon (chained N=5) classical maximum = 8 (exhaustive 1024)", bestP == 8)
# quantum 10 cos(pi/10): cos(pi/10) is the root of 16x^4 - 20x^2 + 5 in (0.951056, 0.951057)
p = lambda x: 16*x**4 - 20*x**2 + 5
a, b = F(951056, 10**6), F(951057, 10**6)
check("G4g cos(pi/10) certified bracket for 16x^4-20x^2+5", p(a) * p(b) < 0)
check("G4h pentagon quantum 10*cos(pi/10) > classical 8", 10*a > 8)

# G5: the trine point
trine = det3_hermitian(C(F(-1,2)), C(F(-1,2)), C(F(-1,2)))
check("G5 trine g_ij = -1/2 sits exactly on the boundary (det G = 0)", trine == 0)

print(f"amalgamation_boundary: {'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
