#!/usr/bin/env python3
"""Chapter 60 verifier — twisted completions at degrees three and four
(integer / roots-of-unity exponent arithmetic only).

Checks: the degree-3 cocycle (pentagon, nontriviality, forced semionic
exchange); genealogy-phase distinctness at Catalan counts; the two
degree-4 cocycles on Z2 x Z2 (cocycle condition, cycle pairings); the
transgression self-similarity; the coefficient-relativity fact (the mu2
class on a single Z2 survives, and dies over U(1) via a fourth root);
and the pentagonal-face counts by two formulas.
"""
from itertools import product
from math import comb, factorial

passed = 0
failed = 0


def check(name, ok):
    global passed, failed
    if ok:
        passed += 1
    else:
        failed += 1
        print("FAIL:", name)


# ---- Degree 3 on Z2 ----
def om(a, b, c):
    return -1 if a and b and c else 1

check("pentagon", all(
    om(b, c, d) * om(a, (b + c) % 2, d) * om(a, b, c)
    == om((a + b) % 2, c, d) * om(a, b, (c + d) % 2)
    for a, b, c, d in product((0, 1), repeat=4)))

# Nontriviality: every normalized sign 2-cochain has trivial coboundary
# at (1,1,1); omega(1,1,1) = -1.
ok = True
for b11 in (1, -1):
    def beta(x, y):
        return b11 if (x, y) == (1, 1) else 1
    d111 = beta(1, 1) * beta(0, 1) * beta(1, 0) * beta(1, 1)
    if d111 == -1:
        ok = False
check("nontrivial", ok and om(1, 1, 1) == -1)

# Forced semionic exchange: hexagon route computation gives 1 = -r^2.
mulG = lambda z, w: (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])
for chi in (1, -1):
    r = (0, chi)
    check("semion", mulG(r, r) == (-1, 0))

# Genealogy phases: distinct cubic polynomials, one per tree (Catalan).
def shapes(n):
    if n == 1:
        return [None]
    out = []
    for k in range(1, n):
        for L in shapes(k):
            for R in shapes(n - k):
                out.append((L, R))
    return out
def assign(s, start=0):
    if s is None:
        return start, start + 1
    Lt, nxt = assign(s[0], start)
    Rt, nxt = assign(s[1], nxt)
    return (Lt, Rt), nxt
def paths(t, out=None, pre=None):
    if out is None:
        out, pre = {}, []
    if isinstance(t, int):
        out[t] = list(pre)
        return out
    paths(t[0], out, pre + [id(t)])
    paths(t[1], out, pre + [id(t)])
    return out
def lca(p, i, j):
    d = 0
    while d < len(p[i]) and d < len(p[j]) and p[i][d] == p[j][d]:
        d += 1
    return d
def trips(t, n):
    p = paths(t)
    return frozenset((i, j, k) for i in range(n) for j in range(i + 1, n)
                     for k in range(j + 1, n) if lca(p, j, k) > lca(p, i, k))
for n in range(3, 8):
    ts = [assign(s)[0] for s in shapes(n)]
    cat = comb(2 * (n - 1), n - 1) // n
    check(f"catalan-{n}", len(ts) == cat and len({trips(t, n) for t in ts}) == cat)

# ---- Degree 4 on V = Z2 x Z2 ----
V = list(product((0, 1), (0, 1)))
addV = lambda x, y: ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)
def fA(a, b, c, d):
    return a[0] * b[1] * c[1] * d[1] % 2
def fB(a, b, c, d):
    return a[1] * b[0] * c[0] * d[0] % 2
def is4cocycle(f):
    return all((f(b, c, d, e) + f(addV(a, b), c, d, e) + f(a, addV(b, c), d, e)
                + f(a, b, addV(c, d), e) + f(a, b, c, addV(d, e)) + f(a, b, c, d)) % 2 == 0
               for a, b, c, d, e in product(V, repeat=5))
check("omegaA-cocycle", is4cocycle(fA))
check("omegaB-cocycle", is4cocycle(fB))

# Cycle pairings: identity matrix mod 2 (non-coboundary certificates).
X, Y = (1, 0), (0, 1)
z13 = [(1, (X, Y, Y, Y)), (-1, (Y, X, Y, Y)), (1, (Y, Y, X, Y)), (-1, (Y, Y, Y, X))]
z31 = [(1, (Y, X, X, X)), (-1, (X, Y, X, X)), (1, (X, X, Y, X)), (-1, (X, X, X, Y))]
pair = lambda f, z: sum(s * f(*t) for s, t in z) % 2
check("pairing-matrix", [pair(fA, z13), pair(fA, z31), pair(fB, z13), pair(fB, z31)] == [1, 0, 0, 1])

# Transgression self-similarity: slant by X reduces omega_A to the
# degree-3 cubic in the Y-sector (and symmetrically for omega_B).
def slant(f, g, a, b, c):
    return (f(g, a, b, c) + f(a, g, b, c) + f(a, b, g, c) + f(a, b, c, g)) % 2
check("transgression-A", all(slant(fA, X, a, b, c) == a[1] * b[1] * c[1] % 2
                             for a, b, c in product(V, repeat=3)))
check("transgression-B", all(slant(fB, Y, a, b, c) == a[0] * b[0] * c[0] % 2
                             for a, b, c in product(V, repeat=3)))

# ---- Coefficient relativity on a single Z2 ----
# Over mu2: the nontrivial normalized 4-cochain IS a cocycle and is NOT
# a mu2-coboundary. Over mu4 (inside U(1)): it equals the coboundary of
# the 3-cochain with value i at (1,1,1) -- the fourth root kills it.
def w4(a, b, c, d):
    return 1 if (a, b, c, d) == (1, 1, 1, 1) else 0  # exponent mod 2
check("mu2-cocycle", all((w4(b, c, d, e) + w4((a + b) % 2, c, d, e)
                          + w4(a, (b + c) % 2, d, e) + w4(a, b, (c + d) % 2, e)
                          + w4(a, b, c, (d + e) % 2) + w4(a, b, c, d)) % 2 == 0
                         for a, b, c, d, e in product((0, 1), repeat=5)))
def beta3(a, b, c):
    return 1 if (a, b, c) == (1, 1, 1) else 0  # exponent of i, mod 4
def dbeta(a, b, c, d):
    return (beta3(b, c, d) - beta3((a + b) % 2, c, d) + beta3(a, (b + c) % 2, d)
            - beta3(a, b, (c + d) % 2) + beta3(a, b, c)) % 4
target = {t: (2 if t == (1, 1, 1, 1) else 0) for t in product((0, 1), repeat=4)}
check("u1-kills", all(dbeta(*t) == target[t] for t in product((0, 1), repeat=4)))
# mu2 coboundaries of the only free normalized 3-cochain are trivial at (1,1,1,1):
check("mu2-not-coboundary",
      all((beta3(1, 1, 1) * s + beta3(0, 1, 1) + beta3(1, 0, 1) + beta3(1, 1, 0)
           + beta3(1, 1, 1) * s) % 2 == 0 for s in (1,)))

# ---- Pentagonal 2-face counts: cycle lemma vs binomial ----
for n in range(4, 11):
    cl = factorial(2 * n - 3) // (factorial(n) * factorial(n - 4)) // (2 * n - 3)
    check(f"faces-{n}", cl == comb(2 * n - 4, n - 4))

print(f"twisted_worlds: {passed} passed, {failed} failed")
if failed:
    raise SystemExit(1)
print("twisted_worlds: ALL PASS")
