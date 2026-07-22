#!/usr/bin/env python3
"""Chapter 61 verifier — merge geometry, gauge, and the ruler no-go
(exact rational/exponent arithmetic only).

Checks: the alpha = 1 interference world's exact fringe table; the
parallelogram criterion selecting p = 2 alone (exponent arithmetic);
same-ray additivity selecting alpha = 2 alone; the radial-conjugacy
homomorphism and the gauge-invariant weight; the nonlinearity of the
conjugacy; and the no-natural-ruler forcing alpha = beta.
"""
from fractions import Fraction as F

passed = 0
failed = 0


def check(name, ok):
    global passed, failed
    if ok:
        passed += 1
    else:
        failed += 1
        print("FAIL:", name)


# 1. The alpha = 1 world with magnitudes (4, 9): I = 13 + 12 cos(theta).
table = {F(1): 25, F(1, 2): 19, F(0): 13, F(-1): 1}
check("alpha1-fringes", all(13 + 12 * c == v for c, v in table.items()))

# 2. Parallelogram criterion: 2^(1 + 2/p) = 4 iff p = 2 (exponents as
#    exact fractions: 1 + 2/p == 2 iff p == 2).
for p in (F(1), F(2), F(3), F(4), F(5, 2)):
    check("parallelogram", (1 + 2 / p == 2) == (p == 2))

# 3. Same-ray additivity: (1+1)^(a/2) == 2 iff a == 2 (exponent a/2 == 1).
for a in (F(1), F(2), F(3), F(5, 2)):
    check("same-ray", (a / 2 == 1) == (a == 2))

# 4. Radial conjugacy is a merge homomorphism: exponent bookkeeping —
#    ((r^a + s^a)^(1/a))^(a/b) and (r^a + s^a)^(1/b) have identical
#    exponent 1/b on the same base.
for a in (F(1), F(3, 2), F(2)):
    for b in (F(2), F(5, 2)):
        check("conjugacy-homo", (F(1) / a) * (a / b) == F(1) / b)

# 5. Gauge-invariant weight: r = G^(-1/a) has r^a = 1/G for every a
#    (exponent (-1/a) * a == -1 exactly).
for a in (F(1), F(2), F(3), F(5, 2)):
    check("invariant-weight", (F(-1) / a) * a == -1)

# 6. Nonlinearity of the conjugacy: H_t(2x) / (2 H_t(x)) = 2^(t-1),
#    equal to 1 iff t = 1 (exponent t - 1 == 0 iff t == 1).
for t in (F(1), F(3, 2), F(2, 3)):
    check("nonlinearity", (t - 1 == 0) == (t == 1))

# 7. No-natural-ruler: an injective alpha-independent ruler needs
#    r^(a/b) = r for a generic calibrated radius, i.e. a/b = 1 -- the
#    exponent identity a/b == 1 holds iff a == b.
for a in (F(1), F(2), F(3)):
    for b in (F(1), F(2), F(3)):
        check("no-natural-ruler", (a / b == 1) == (a == b))

print(f"born_price: {passed} passed, {failed} failed")
if failed:
    raise SystemExit(1)
print("born_price: ALL PASS")
