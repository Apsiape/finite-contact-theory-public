#!/usr/bin/env python3
"""Chapter 48: the opposition criterion (exact).

  H1 P128-1: T2 x Z6 parity-protected (no opposition, ever).
  H2 P128-2: T3 x Z4 opposes first at depth 6 (second
     harmonic).
  H3 P128-3: the full 2x2 verifies gcd(c, n) | n/2.
"""
from fractions import Fraction
from math import gcd

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def channels(c, depth):
    """loop floor T_c: state in Z_c; stay/advance uniform."""
    ch = {}
    def rec(s, d, dev, w):
        if d > 0:
            ch.setdefault((d, s), []).append((dev, w))
        if d == depth:
            return
        rec(s, d + 1, dev, w * Fraction(1, 2))
        rec((s + 1) % c, d + 1, dev + 1, w * Fraction(1, 2))
    rec(0, 0, 0, Fraction(1))
    return ch

def opposition(c, n, depth):
    """first depth at which some channel contains both phase 0
    and phase n/2 (mod n) deviations; also parity check."""
    ch = channels(c, depth)
    first = None
    parity_uniform = True
    for (d, s), pl in sorted(ch.items()):
        devs = {dev % n for (dev, _) in pl}
        pars = {dev % 2 for (dev, _) in pl}
        if len(pars) > 1:
            parity_uniform = False
        half = n // 2
        for a in devs:
            if (a + half) % n in devs:
                if first is None:
                    first = d
                break
        if first is not None:
            break
    return first, parity_uniform

if __name__ == '__main__':
    DEPTH = 8

    print("## H1: T2 x Z6 parity protection")
    f26, par26 = opposition(2, 6, DEPTH)
    ok1 = f26 is None and par26
    check(f"T2 x Z6: first opposition = {f26} (none through "
          f"depth {DEPTH}); every channel is parity-uniform "
          f"({par26}) ({ok1}). **PARITY PROTECTED: on a "
          f"cost-2 floor every accumulated deviation shares "
          f"the state's parity, and Z6's mirror is odd — a "
          f"world that can NEVER say no, for a divisibility "
          f"reason. gcd(2,6) = 2 does not divide 3.**", ok1)

    print("## H2: T3 x Z4 second harmonic")
    f34, _ = opposition(3, 4, DEPTH)
    ok2 = f34 == 6
    check(f"T3 x Z4: first opposition at depth {f34} "
          f"(predicted 6: the double loop, devs {{0,6}}, "
          f"i^6 = -1) ({ok2}). **THE SECOND HARMONIC, called "
          f"in advance: gcd(3,4) = 1 divides 2, harmonic "
          f"k = 2, first opposition at c*k = 6 exactly.**",
          ok2)

    print("## H3: the full 2x2 and the law")
    results = {}
    for c in (2, 3):
        for n in (4, 6):
            f, _ = opposition(c, n, DEPTH)
            g = gcd(c, n)
            reach_law = (n // 2) % g == 0
            k = (n // 2) // g if reach_law else None
            pred = c * ((n // 2) * pow(c // g,-1,n // g) % (n // g)) if reach_law else None
            results[(c, n)] = (f, reach_law)
    ok3 = all((f is not None) == law
              for (f, law) in results.values())
    ok3 = ok3 and results[(2, 4)][0] == 2 \
        and results[(3, 6)][0] == 3
    check(f"the 2x2 (cost, order) -> first opposition: "
          f"{{(c,n): results[(c,n)][0] for c in (2,3) "
          f"for n in (4,6)}} = { {k: v[0] for k, v in results.items()} } "
          f"({ok3}). **THE HARMONIC LAW verified on all four "
          f"cells: the mirror is reachable iff gcd(cost, "
          f"order) divides order/2 — first harmonics at depths "
          f"2 and 3, the second harmonic at 6, and one cell "
          f"parity-protected forever. WHICH WORLDS CAN SAY NO "
          f"IS EXACT NUMBER THEORY: a gcd condition between "
          f"how a world returns and how its coat turns.**",
          ok3)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
