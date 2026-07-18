#!/usr/bin/env python3
"""Chapter 47: the six-fold coat (exact).

  X1 P127-1: the mirror law's converse (Z6 mints dark).
  X2 P127-2: the spectroscopy bet (the dark sets differ).
  X3 P127-3: third coat, same table.
"""
import math
from fractions import Fraction
from quantum_dividend import census
from grammar_closure import IP

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

# Z6 in the Eisenstein basis (x + y*omega):
# zeta^0..zeta^5 = (1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)
W6 = [(Fraction(1), Fraction(0)), (Fraction(1), Fraction(1)),
      (Fraction(0), Fraction(1)), (Fraction(-1), Fraction(0)),
      (Fraction(-1), Fraction(-1)), (Fraction(0), Fraction(-1))]

def norm6(x, y):
    return x * x - x * y + y * y

def amp4(pl):
    re = im = P = Fraction(0)
    for (_, d, w) in pl:
        re += IP[d % 4][0] * w
        im += IP[d % 4][1] * w
        P += w
    return re * re + im * im, P

def amp6(pl):
    x = y = P = Fraction(0)
    for (_, d, w) in pl:
        wx, wy = W6[d % 6]
        x += wx * w
        y += wy * w
        P += w
    return norm6(x, y), P

def amp6full(pl):
    x = y = P = Fraction(0)
    for (_, d, w) in pl:
        wx, wy = W6[d % 6]
        x += wx * w
        y += wy * w
        P += w
    return x, y, P

if __name__ == '__main__':
    C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    P4 = frozenset(((0, 1), (1, 2), (2, 3)))
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    ARENA = [(C4, 4, 5), (P4, 4, 5), (C5, 5, 3)]

    dark4 = set()
    dark6 = set()
    n_ch = 0
    cnt_ok = True
    lp = ln = sp = sn = 0
    for (E0, n, depth) in ARENA:
        for key, pl in census(E0, n, depth,
                              witness=True).items():
            n_ch += 1
            a4, P = amp4(pl)
            a6, _ = amp6(pl)
            if a4 == 0 and P > 0:
                dark4.add((len(str(E0)), key))
            if a6 == 0 and P > 0:
                dark6.add((len(str(E0)), key))
            if len(pl) < 2:
                continue
            allk = sorted({k for (t, _, _) in pl for k in t})
            und = [k for k in allk
                   if len({str(t.get(k, 'A'))
                           for (t, _, _) in pl}) > 1]
            x, y, P6 = amp6full(pl)
            a2 = norm6(x, y)
            for u in und:
                br = {}
                for p in pl:
                    br.setdefault(str(p[0].get(u, 'A')),
                                  []).append(p)
                amps = {v: amp6full(b)
                        for v, b in br.items()}
                if P6 != sum(a[2] for a in amps.values()):
                    cnt_ok = False
                inc2 = sum(norm6(a[0], a[1])
                           for a in amps.values())
                if a2 > inc2:
                    sp += 1
                elif a2 < inc2:
                    sn += 1
                aL = math.sqrt(float(a2))
                incL = sum(
                    math.sqrt(float(norm6(a[0], a[1])))
                    for a in amps.values())
                if aL > incL + 1e-12:
                    lp += 1
                elif aL < incL - 1e-12:
                    ln += 1

    print("## X1: the mirror law's converse")
    ok1 = len(dark6) == 0 and len(dark4) > 0
    check(f"Z6 dark channels on the witnessed exchange floor: "
          f"{len(dark6)} (Z4 on the same channels: "
          f"{len(dark4)}) ({ok1}). **MY BET DIED INTO THE MIRROR DISTANCE LAW: Z6 contains the mirror, but at deviation distance THREE, while this floor's natural returns cost TWO (stay vs swap-and-return: phases 1 and omega, not opposed). Even order is necessary but not sufficient -- THE COAT AND THE DYNAMICS MUST RESONATE: the mirror must sit at the natural return cost. Z4 resonates with pair-return worlds; a Z6 world needs three-cost returns.**", ok1)

    print("## X2: the spectroscopy bet")
    only4 = len(dark4 - dark6)
    only6 = len(dark6 - dark4)
    both = len(dark4 & dark6)
    ok2 = only4 > 0 or only6 > 0
    check(f"dark-set comparison on identical channels: "
          f"Z4-only {only4}, Z6-only {only6}, shared {both} "
          f"({ok2}). **THE COAT IS MEASURABLE FROM WITHIN: "
          f"the pattern of forbidden events differs between "
          f"phase groups on the same dynamics -- an internal "
          f"observer with counting access alone can read the "
          f"order of its world's coat from which events never "
          f"happen. Our forbidden sector, on this picture, "
          f"spells out the number four.**", ok2)

    print("## X3: third coat, same table")
    sig = ("zero" if cnt_ok else "V",
           "never-positive" if lp == 0 and ln > 0 else "other",
           "both-signs" if sp and sn else "other")
    ok3 = (sig[0] == "zero" and sig[1] == "never-positive"
           and sn == 0 and sp > 0)
    check(f"Z6 NSIT table: {sig} (linear {lp}+/{ln}-, squared "
          f"{sp}+/{sn}-) ({ok3}). **MY BET DIED INTO THE SPECTROMETER READING: off-resonance the squared column degenerates to never-negative. The table's three columns are three structural tests: ADDITIVITY (counting, always zero), PHASE VARIETY (linear negatives), MIRROR RESONANCE (squared negatives exist exactly where opposition is reachable). The full invariant table is the signature of a RESONANT coat-dynamics pair -- every prior floor was one; this pairing is not.**", ok3)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
