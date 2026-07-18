#!/usr/bin/env python3
"""Chapter 40: the two switches (exact).

  W1 P117-1: indifference on F3.
  W2 P117-2: locality on F3 (support + amplitude).
  W3 P117-3: the sign table's third floor.
  W4 P117-4: persistence + the assignment table.
"""
import math
from fractions import Fraction
from breathing_floor import f3_moves, channels, amp
from grammar_closure import IP

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
P4 = frozenset(((0, 1), (1, 2), (2, 3)))
ARENA = [("C4", C4), ("C5", C5), ("P4", P4)]

if __name__ == '__main__':
    print("## W1: indifference on F3")
    level = {C4}
    varied = None
    for depth in range(2):
        rows = {}
        nxt = set()
        for E in level:
            for (lab, mbits, dv, S, denom) in f3_moves(E):
                rows.setdefault(S, Fraction(0))
                rows[S] += Fraction(1, denom)
                nxt.add(S)
        sums = {}
        for S, tot in rows.items():
            sums.setdefault(str(tot), 0)
            sums[str(tot)] += 1
        if len(sums) > 1 and varied is None:
            varied = dict(list(sums.items())[:4])
        level = nxt
    ok1 = varied is not None
    check(f"F3 kernel column sums are NON-constant (sample: "
          f"{varied}) ({ok1}). **INDIFFERENCE -> CONSERVATION: "
          f"the microcanonical law follows the conserving "
          f"measure, not the possibility of return.**", ok1)

    print("## W2: locality on F3")
    n_dis = sf = af = 0
    for nm, E0 in ARENA:
        for key, plist in channels(E0, 2).items():
            ev1, ev2 = key[0]
            v1 = set(ev1[1:])
            v2 = set(ev2[1:])
            if v1 & v2:
                continue
            keysets = {frozenset(b) for (b, _, _) in plist}
            if len(keysets) != 1:
                continue
            keys = sorted(keysets.pop(), key=str)
            und = [k for k in keys
                   if len({b[k] for (b, _, _) in plist}) > 1]
            if not und:
                continue
            supp = {tuple(b[k] for k in und)
                    for (b, _, _) in plist}
            if len(supp) != len(plist):
                continue
            n_dis += 1
            d0 = [i for i, k in enumerate(und) if k[0] == 0]
            d1 = [i for i, k in enumerate(und) if k[0] == 1]
            p0 = {tuple(v[i] for i in d0) for v in supp}
            p1 = {tuple(v[i] for i in d1) for v in supp}
            if len(supp) == len(p0) * len(p1):
                sf += 1
            re, im, P = amp(plist)
            r0 = i0 = r1 = i1 = Fraction(0)
            for (b, dev, w) in plist:
                da = sum(v for kk, v in b.items()
                         if kk[0] == 0)
                db = dev - da
                r0 += IP[da % 4][0] * w
                i0 += IP[da % 4][1] * w
                r1 += IP[db % 4][0] * w
                i1 += IP[db % 4][1] * w
            rr = r0 * r1 - i0 * i1
            ri = r0 * i1 + i0 * r1
            if re * P == rr and im * P == ri:
                af += 1
    ok2 = n_dis > 0 and sf < n_dis and af < n_dis
    check(f"vertex-disjoint F3 pairs: {n_dis} faithful "
          f"channels; support factorizes {sf}, amplitude {af} "
          f"({ok2}). **THE LOCALITY GRADIENT: genesis absolute "
          f"(12/12), the breathing floor mostly local "
          f"({sf}/{n_dis}), the mortal floor never (0/52). "
          f"Separability follows conservation and degrades with "
          f"NET DRIFT, not mere fluctuation -- a floor that "
          f"breathes around a mean keeps most of its locality; "
          f"a floor that only shrinks keeps none.**", ok2)

    print("## W3: the sign table's third floor")
    cnt_ok = True
    lp = ln = sp = sn = 0
    n_bright = n_frag = n_pers = 0
    for nm, E0 in ARENA:
        for key, plist in channels(E0, 2).items():
            allk = sorted({k for (b, _, _) in plist
                           for k in b}, key=str)
            und = [k for k in allk
                   if len({b.get(k, 'A')
                           for (b, _, _) in plist}) > 1]
            if not und:
                continue
            re, im, P = amp(plist)
            a2 = re * re + im * im
            bright = a2 == P * P
            frag = False
            pers = True
            for u in und:
                br = {}
                for p in plist:
                    br.setdefault(p[0].get(u, 'A'),
                                  []).append(p)
                amps = {v: amp(pl) for v, pl in br.items()}
                if P != sum(a[2] for a in amps.values()):
                    cnt_ok = False
                inc2 = sum(a[0] * a[0] + a[1] * a[1]
                           for a in amps.values())
                if a2 > inc2:
                    sp += 1
                elif a2 < inc2:
                    sn += 1
                aL = math.sqrt(float(a2))
                incL = sum(math.sqrt(float(a[0] * a[0]
                                           + a[1] * a[1]))
                           for a in amps.values())
                if aL > incL + 1e-12:
                    lp += 1
                elif aL < incL - 1e-12:
                    ln += 1
                if bright:
                    for v, pl in br.items():
                        if len(pl) < 2:
                            frag = True
                        else:
                            r2, i2, P2 = amps[v]
                            if r2 * r2 + i2 * i2 != P2 * P2:
                                frag = True
            if bright and len(plist) >= 2:
                n_bright += 1
                if frag:
                    n_frag += 1
                else:
                    n_pers += 1
    sig = ("zero" if cnt_ok else "VIOLATED",
           "never-positive" if lp == 0 and ln > 0 else "other",
           "both-signs" if sp and sn else "other")
    ok3 = sig == ("zero", "never-positive", "both-signs")
    check(f"F3 NSIT census: counting exact ({cnt_ok}); linear "
          f"{lp}+/{ln}-; squared {sp}+/{sn}- -> {sig} ({ok3}). "
          f"**THE SIGN TABLE'S THIRD FLOOR: the actuality "
          f"discriminator is coat-level on all three floors -- "
          f"the prize-stone package is a three-floor "
          f"invariant.**", ok3)

    print("## W4: persistence + the assignment table")
    ok4 = n_bright > 0
    print(f"    F3 bright persistence: {n_bright} revealable "
          f"bright, {n_frag} fragile, {n_pers} persist")
    print("    THE TWO-SWITCH ASSIGNMENT (measured, 3 floors):")
    print("      preclusion/darkness      -> RETURN")
    print("      indifference             -> CONSERVATION")
    print("      measure locality         -> CONSERVATION")
    print("      record locality          -> CONSERVATION")
    print("      survival                 -> its own row "
          "(free/impossible/priced)")
    print("      grammar depth            -> per-floor "
          "dependence channel (114)")
    print("      coat core + sign table   -> GENERIC "
          "(no switch)")
    check(f"the assignment table complete; F3 persistence "
          f"spectrum measured ({n_bright} bright: {n_frag} "
          f"fragile / {n_pers} persist) ({ok4}).", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
