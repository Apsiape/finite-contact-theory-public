#!/usr/bin/env python3
"""Chapter 59 verifier — the three fork shapes (exact/integer only).

Checks: the split-extension splitting torsor and the automorphism that
exchanges its two points; the nonsplit companion; the chirality fiber
(conjugation swap, stacking escape); the outcome-fork torsor facts
(q = 2 free and transitive, q >= 3 transitive but not free); and the
splitting-calibration bit's invisibility to the extension class.
"""
from itertools import product, permutations

passed = 0
failed = 0


def check(name, ok):
    global passed, failed
    if ok:
        passed += 1
    else:
        failed += 1
        print("FAIL:", name)


# 1. V4 = Z2 x Z2 over Z2: exactly two homomorphic sections; the
#    exact-sequence automorphism tau exchanges them.
G = (0, 1)
E = list(product(G, G))
def addE(x, y):
    return ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)
splits = [e for e in E if e[1] == 1 and addE(e, e) == (0, 0)]
check("two-splittings", sorted(splits) == [(0, 1), (1, 1)])
tau = lambda x: ((x[0] + x[1]) % 2, x[1])
check("tau-kernel-fixed", all(tau((a, 0)) == (a, 0) for a in G))
check("tau-quotient-id", all(tau(x)[1] == x[1] for x in E))
check("tau-swaps", sorted(tau(s) for s in splits) == sorted(splits)
      and [tau(s) for s in splits] != splits)

# 2. Z4 over Z2: nonsplit (both odd elements have order four).
check("z4-nonsplit", [k for k in range(4) if k % 2 == 1 and (k + k) % 4 == 0] == [])

# 3. Chirality fiber: roots of -1 among Gaussian units; conjugation
#    swaps them; their products leave the fiber (stacking escape).
mul = lambda z, w: (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])
units = [(1, 0), (-1, 0), (0, 1), (0, -1)]
roots = [z for z in units if mul(z, z) == (-1, 0)]
check("fiber", sorted(roots) == [(0, -1), (0, 1)])
check("conjugation-swaps", sorted((z[0], -z[1]) for z in roots) == sorted(roots)
      and [(z[0], -z[1]) for z in roots] != roots)
check("stacking-escape",
      all(mul(z, w) not in roots for z in roots for w in roots))

# 4. Outcome forks: for q = 2 the symmetric action is free and
#    transitive (a torsor under branch-swap); for q >= 3 transitive
#    but NOT free (nontrivial stabilizers).
for q in (2, 3, 4):
    perms = list(permutations(range(q)))
    transitive = all(any(pm[0] == j for pm in perms) for j in range(q))
    # free iff no nonidentity permutation fixes a point
    free = all(pm == tuple(range(q)) or all(pm[i] != i for i in range(q))
               for pm in perms)
    if q == 2:
        check("q2-free-transitive", transitive and free)
    else:
        check(f"q{q}-not-free", transitive and not free)

# 5. The splitting-calibration bit is invisible to the extension class:
#    both splittings inhabit the same (zero) class -- the 2-cocycle of
#    the split extension is trivial regardless of the chosen section.
def cocycle(section):
    s = {0: (0, 0), 1: section}
    out = {}
    for g in G:
        for h in G:
            prod = addE(s[g], s[h])
            base = s[(g + h) % 2]
            out[(g, h)] = (prod[0] - base[0]) % 2
    return out
c0 = cocycle((0, 1))
c1 = cocycle((1, 1))
check("both-classes-zero", all(v == 0 for v in c0.values())
      and all(v == 0 for v in c1.values()))

print(f"spine_forks: {passed} passed, {failed} failed")
if failed:
    raise SystemExit(1)
print("spine_forks: ALL PASS")
