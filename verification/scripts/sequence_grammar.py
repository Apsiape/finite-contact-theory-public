#!/usr/bin/env python3
"""Chapter 38: the sequence grammar (exact).

  S1 P114-1: sequence completeness (non-repeat stays in grammar).
  S2 P114-2: absolute factorization on disjoint neighborhoods.
  S3 P114-3: the orbit grammar needs survival.
  S4 P114-4: the interaction taxonomy.
"""
from fractions import Fraction
from grammar_closure import (nb, verts, canon as canon0,
                             coag_singles, coag_succ, gen_succ,
                             grammar, IP)

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

_C = {}
def canon(E):
    if E not in _C:
        _C[E] = canon0(E)
    return _C[E]

def depth2(E0, floor):
    ch = {}
    m0 = len(E0)
    for (a, b) in sorted(E0):
        if floor == "f2":
            singles, _ = coag_singles(E0, a, b)
        else:
            Na = nb(E0, a) - {b}
            Nb = nb(E0, b) - {a}
            singles = sorted(Na ^ Nb)
        k1 = len(singles)
        for mask in range(1 << k1):
            keep = [singles[i] for i in range(k1)
                    if mask >> i & 1]
            if floor == "f2":
                E1 = coag_succ(E0, a, b, keep)
            else:
                Na = nb(E0, a) - {b}
                parent = {u: (a if u in Na else b)
                          for u in singles}
                assign = {u: (parent[u] if u in keep else
                              (b if parent[u] == a else a))
                          for u in singles}
                E1 = gen_succ(E0, a, b, assign, singles)
            bits1 = {(0, u): (0 if u in keep else 1)
                     for u in singles}
            d1 = k1 - len(keep)
            m1 = len(E1)
            if m1 == 0:
                continue
            for (a2, b2) in sorted(E1):
                if floor == "f2":
                    singles2, _ = coag_singles(E1, a2, b2)
                else:
                    Na2 = nb(E1, a2) - {b2}
                    Nb2 = nb(E1, b2) - {a2}
                    singles2 = sorted(Na2 ^ Nb2)
                k2 = len(singles2)
                for mask2 in range(1 << k2):
                    keep2 = [singles2[i] for i in range(k2)
                             if mask2 >> i & 1]
                    if floor == "f2":
                        E2 = coag_succ(E1, a2, b2, keep2)
                    else:
                        Na2 = nb(E1, a2) - {b2}
                        par2 = {u: (a2 if u in Na2 else b2)
                                for u in singles2}
                        asg2 = {u: (par2[u] if u in keep2 else
                                    (b2 if par2[u] == a2
                                     else a2))
                                for u in singles2}
                        E2 = gen_succ(E1, a2, b2, asg2,
                                      singles2)
                    d2 = k2 - len(keep2)
                    bits = dict(bits1)
                    for u in singles2:
                        bits[(1, u)] = 0 if u in keep2 else 1
                    w = Fraction(1, m0 * (1 << k1)
                                 * m1 * (1 << k2))
                    ch.setdefault(
                        (((a, b), (a2, b2)), canon(E2)),
                        []).append((bits, d1 + d2, w))
    return ch

def faithful(plist):
    keysets = {frozenset(b) for (b, _, _) in plist}
    if len(keysets) != 1:
        return None
    keys = sorted(keysets.pop(), key=str)
    und = [k for k in keys
           if len({b[k] for (b, _, _) in plist}) > 1]
    if not und:
        return None
    supp = {tuple(b[k] for k in und) for (b, _, _) in plist}
    if len(supp) != len(plist):
        return None
    return und, supp

def amp(plist):
    re = im = P = Fraction(0)
    for (_, dev, w) in plist:
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

def itype(E0, e1, e2):
    if e1 == e2:
        return "repeat"
    if set(e1) & set(e2):
        return "vertex-sharing"
    N1 = set(e1) | nb(E0, e1[0]) | nb(E0, e1[1])
    N2 = set(e2) | nb(E0, e2[0]) | nb(E0, e2[1])
    return "disjoint-nbhd" if not (N1 & N2) else "vd-sharing"

if __name__ == '__main__':
    P6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5)))
    P7 = frozenset(P6 | {(5, 6)})
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    C8 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (5, 6), (6, 7), (0, 7)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    ARENAS = {"gen": [("P6", P6), ("P7", P7), ("C6", C6),
                      ("K4p", K4p)],
              "f2": [("P6", P6), ("P7", P7), ("C6", C6),
                     ("K4p", K4p), ("C8", C8)]}

    tax = {}
    nonrep_other = {}
    rep_other = {}
    fact = {}
    for floor, arena in ARENAS.items():
        for nm, E0 in arena:
            for key, plist in depth2(E0, floor).items():
                (e1, e2), _ = key
                it = itype(E0, e1, e2)
                got = faithful(plist)
                if got is not None:
                    und, supp = got
                    g = grammar(supp, len(und))
                    tax.setdefault((floor, it), {}).setdefault(
                        g, 0)
                    tax[(floor, it)][g] += 1
                    if g == "other":
                        (rep_other if it == "repeat"
                         else nonrep_other).setdefault(
                            floor, []).append((nm, e1, e2))
                if it == "disjoint-nbhd" and got is not None:
                    und, supp = got
                    d0 = [i for i, k in enumerate(und)
                          if k[0] == 0]
                    d1_ = [i for i, k in enumerate(und)
                           if k[0] == 1]
                    p0 = {tuple(v[i] for i in d0)
                          for v in supp}
                    p1 = {tuple(v[i] for i in d1_)
                          for v in supp}
                    sf = len(supp) == len(p0) * len(p1)
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
                    af = (re * P == rr and im * P == ri)
                    k = (floor,)
                    fact.setdefault(k, [0, 0, 0])
                    fact[k][0] += 1
                    fact[k][1] += 1 if sf else 0
                    fact[k][2] += 1 if af else 0

    print("## S1: sequence completeness (non-repeat)")
    f2w = nonrep_other.get("f2", [])
    ok1 = ("gen" not in nonrep_other and len(f2w) > 0
           and all(itype(dict(ARENAS["f2"])[nm], e1, e2)
                   == "vd-sharing" for (nm, e1, e2) in f2w))
    check(f"MY BET DIED INTO THE EXIT LAW: genesis non-repeat "
          f"supports NEVER exit the grammar (0 beyond-grammar); "
          f"F2 exits WITHOUT repetition -- {len(f2w)} "
          f"beyond-grammar witnesses, every one a NEIGHBOR-"
          f"SHARING pair, none at disjoint neighborhoods "
          f"({ok1}). **THE EXIT IS SEQUENTIAL DEPENDENCE, "
          f"per-floor: genesis via repetition only; the mortal "
          f"floor via shared neighbors (a released neighbor "
          f"reshapes the next fork).**", ok1)

    print("## S2: absolute factorization")
    g = fact.get(("gen",), [0, 0, 0])
    f = fact.get(("f2",), [0, 0, 0])
    ok2 = (g[0] > 0 and f[0] > 0 and g[1] == g[0]
           and g[2] == g[0] and f[1] == 0 and f[2] < f[0])
    check(f"disjoint-neighborhood pairs: genesis {g[0]} "
          f"channels, support {g[1]}, amp {g[2]} factorize; F2 "
          f"{f[0]} channels, support {f[1]}, amp {f[2]} "
          f"({ok2}). **MY BET HALF-DIED INTO MORTAL HOLISM: "
          f"genesis is ABSOLUTELY local at disjoint "
          f"neighborhoods (support AND amplitude 12/12 -- the "
          f"absolute factorization theorem); F2 support "
          f"factorization is ZERO even there -- the final-class "
          f"record of a shrinking world is a global quantity, "
          f"so even the RECORD couples spacelike events. "
          f"Mortality is holism; conservation buys separability "
          f"itself.**", ok2)

    print("## S3: the orbit grammar needs survival")
    f2_vs = tax.get(("f2", "vertex-sharing"), {})
    f2_rep = tax.get(("f2", "repeat"), {})
    gen_rep = tax.get(("gen", "repeat"), {})
    ok3 = (f2_vs.get("other", 0) == 0 and not f2_rep
           and gen_rep.get("other", 0) > 0)
    check(f"F2 vertex-sharing supports: {f2_vs} (0 beyond-"
          f"grammar); F2 repeat channels: {f2_rep} (none exist "
          f"-- both parents consumed); genesis repeat: "
          f"{gen_rep} (beyond-grammar present) ({ok3}). **refined by S1: on "
          f"GENESIS repetition is the only exit, and only a "
          f"conserving floor can re-fire a contact; the mortal "
          f"floor, unable to repeat, exits via neighbor-sharing "
          f"instead. Grammar depth is bought per-floor by "
          f"whichever dependence channel succession leaves "
          f"open.**", ok3)

    print("## S4: the interaction taxonomy")
    ok4 = len(tax) >= 5
    for k in sorted(tax, key=str):
        print(f"    {k}: {tax[k]}")
    check(f"the interaction taxonomy assembled "
          f"({len(tax)} floor x interaction cells) ({ok4}).",
          ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
