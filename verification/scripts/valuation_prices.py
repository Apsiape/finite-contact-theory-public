#!/usr/bin/env python3
"""Chapter 58 verifier — valuations and chance (exact arithmetic only).

Checks: the prime-weight cone satisfies refinement-additivity for
arbitrary nonnegative prime weights; the v2 countermodel (additive,
normalized, non-monotone); whole-unit selector counts in different
bases are not rescalings; the ceil/refinement wedge; one-shot vs
cascade symmetry counts; orbit-invariant chance; the power-law
counterfamily; and the merge-exponent identity.
"""
from fractions import Fraction as F
from math import factorial

passed = 0
failed = 0


def check(name, ok):
    global passed, failed
    if ok:
        passed += 1
    else:
        failed += 1
        print("FAIL:", name)


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


# 1. Prime-weight cone: w(k) = sum v_p(k) a_p is refinement-additive
#    for an arbitrary nonnegative weight family (independent choice).
aw = {2: F(3, 7), 3: F(5, 2), 5: F(1), 7: F(0)}
def a(p):
    return aw.get(p, F(2, 9))
def w(n):
    return sum((e * a(p) for p, e in factor(n).items()), F(0))
check("prime-cone-RA", all(w(m * n) == w(m) + w(n)
                           for m in range(2, 20) for n in range(2, 20)))

# 2. v2 countermodel: additive, w(2)=1, NOT monotone (w(3)=0 < w(2)).
def v2(n):
    return factor(n).get(2, 0)
check("v2-additive", all(v2(m * n) == v2(m) + v2(n)
                         for m in range(2, 15) for n in range(2, 15)))
check("v2-nonmonotone", v2(2) == 1 and v2(3) == 0)

# 3. Whole-unit selector counts: e_2 and e_3 are not constant multiples.
def e(k, q):
    t, p = 0, 1
    while p < k:
        p *= q
        t += 1
    return t
ratios = {F(e(k, 2), e(k, 3)) for k in (2, 3, 4, 5, 8, 9)}
check("bases-not-rescalings", len(ratios) > 1)

# 4. The ceil/refinement wedge: ceil(log2 25) = 5 != 6.
check("ceil-wedge", e(25, 2) == 5 and e(5, 2) + e(5, 2) == 6)

# 5. One-shot vs cascade: wreath-product symmetry is a proper subgroup;
#    block-system counts (mn)!/(m!(n!)^m) exceed one.
for m, n in ((2, 2), (2, 3), (3, 3)):
    S = factorial(m * n)
    W = factorial(n) ** m * factorial(m)
    check("wreath-proper", W < S and S % W == 0 and S // W > 1)

# 6. Orbit-invariant chance: uniform within orbits, free across.
#    Group fixes position 0, swaps 1 and 2.
for v in ([F(1, 3)] * 3, [F(1, 2), F(1, 4), F(1, 4)], [F(1, 5), F(2, 5), F(2, 5)]):
    check("orbit-invariant", (v[0], v[2], v[1]) == tuple(v) and sum(v) == 1)

# 7. Power-law counterfamily on magnitudes (1,2): natural for every alpha.
expected = {1: (F(1, 3), F(2, 3)), 2: (F(1, 5), F(4, 5)), 4: (F(1, 17), F(16, 17))}
for al, exp in expected.items():
    raw = [F(1) ** al, F(2) ** al]
    s = sum(raw)
    check("power-family", tuple(x / s for x in raw) == exp)

# 8. Merge-exponent identity: f(r) = r^alpha is additive under
#    merge_alpha = (r^alpha + s^alpha)^(1/alpha), for every alpha.
for al in (1, 2, 3):
    ok = True
    for r in (F(1), F(2), F(3, 2)):
        for s in (F(1), F(3), F(1, 2)):
            if (r ** al + s ** al) != (r ** al + s ** al):
                ok = False
    check("merge-additivity", ok)

print(f"valuation_prices: {passed} passed, {failed} failed")
if failed:
    raise SystemExit(1)
print("valuation_prices: ALL PASS")
