#!/usr/bin/env python3
"""Chapter 41: the controls, run (exact).

  C1 P118-1: the measure control (population-independent
     weights).
  C2 P118-2: the record control (local-record keying).
  C3 P118-3: the refined holism theorem.
"""
from fractions import Fraction
from grammar_closure import (nb, verts, canon as canon0,
                             coag_singles, coag_succ, gen_succ,
                             IP)

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

_C = {}
def canon(E):
    if E not in _C:
        _C[E] = canon0(E)
    return _C[E]

def paths2(E0, floor):
    """depth-2 paths: (e1, e2, bits, dev, w, w_uniform, E2)."""
    out = []
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
                    bits = dict(bits1)
                    for u in singles2:
                        bits[(1, u)] = 0 if u in keep2 else 1
                    d2 = k2 - len(keep2)
                    out.append(
                        ((a, b), (a2, b2), bits, d1 + d2,
                         Fraction(1, m0 * (1 << k1)
                                  * m1 * (1 << k2)),
                         Fraction(1, (1 << k1) * (1 << k2)),
                         E2))
    return out

def amp_of(plist, wi):
    re = im = P = Fraction(0)
    for p in plist:
        dev, w = p[3], p[wi]
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

def facts(plist, wi):
    """(supp_factorizes, amp_factorizes) for a channel."""
    keysets = {frozenset(p[2]) for p in plist}
    if len(keysets) != 1:
        return None
    keys = sorted(keysets.pop(), key=str)
    und = [k for k in keys
           if len({p[2][k] for p in plist}) > 1]
    if not und:
        return None
    supp = {tuple(p[2][k] for k in und) for p in plist}
    if len(supp) != len(plist):
        return None
    d0 = [i for i, k in enumerate(und) if k[0] == 0]
    d1 = [i for i, k in enumerate(und) if k[0] == 1]
    p0 = {tuple(v[i] for i in d0) for v in supp}
    p1 = {tuple(v[i] for i in d1) for v in supp}
    sf = len(supp) == len(p0) * len(p1)
    re, im, P = amp_of(plist, wi)
    r0 = i0 = r1 = i1 = Fraction(0)
    for p in plist:
        bits, dev, w = p[2], p[3], p[wi]
        da = sum(v for kk, v in bits.items() if kk[0] == 0)
        db = dev - da
        r0 += IP[da % 4][0] * w
        i0 += IP[da % 4][1] * w
        r1 += IP[db % 4][0] * w
        i1 += IP[db % 4][1] * w
    rr = r0 * r1 - i0 * i1
    ri = r0 * i1 + i0 * r1
    af = (re * P == rr and im * P == ri)
    return sf, af

if __name__ == '__main__':
    P6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5)))
    P7 = frozenset(P6 | {(5, 6)})
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    ARENA = [("P6", P6), ("P7", P7), ("C6", C6), ("K4p", K4p)]

    stats = {}
    couple_ex = None
    for floor in ("gen", "f2"):
        n = sf_g = af_g = af_u = lf = 0
        for nm, E0 in ARENA:
            allp = paths2(E0, floor)
            byev = {}
            for p in allp:
                e1, e2 = p[0], p[1]
                N1 = set(e1) | nb(E0, e1[0]) | nb(E0, e1[1])
                N2 = set(e2) | nb(E0, e2[0]) | nb(E0, e2[1])
                if N1 & N2:
                    continue
                byev.setdefault((e1, e2, frozenset(N1),
                                 frozenset(N2)), []).append(p)
            for (e1, e2, N1, N2), plist in byev.items():
                # global-record channels:
                glob = {}
                for p in plist:
                    glob.setdefault(canon(p[6]), []).append(p)
                for cls, pl in glob.items():
                    got = facts(pl, 4)
                    if got is None:
                        continue
                    n += 1
                    sf, af = got
                    sf_g += 1 if sf else 0
                    af_g += 1 if af else 0
                    _, afu = facts(pl, 5)
                    af_u += 1 if afu else 0
                # local-record channels:
                loc = {}
                for p in plist:
                    E2 = p[6]
                    R1 = canon(frozenset(
                        e for e in E2
                        if e[0] in N1 and e[1] in N1))
                    R2 = canon(frozenset(
                        e for e in E2
                        if e[0] in N2 and e[1] in N2))
                    loc.setdefault((R1, R2), []).append(p)
                for cls, pl in loc.items():
                    got = facts(pl, 5)
                    if got is None:
                        continue
                    lf += 1 if got[0] else 0
                # collider witness: distinct (R1,R2) pairs
                # sharing one global class
                if floor == "f2" and couple_ex is None:
                    seen = {}
                    for (R1, R2), pl in loc.items():
                        for p in pl:
                            g = canon(p[6])
                            seen.setdefault(g, set()).add(
                                (R1, R2))
                    for g, prs in seen.items():
                        r1s = {x[0] for x in prs}
                        r2s = {x[1] for x in prs}
                        if len(prs) < len(r1s) * len(r2s):
                            couple_ex = (nm, e1, e2,
                                         len(prs), len(r1s),
                                         len(r2s))
                            break
        stats[floor] = (n, sf_g, af_g, af_u, lf)

    g = stats["gen"]
    f = stats["f2"]
    print("## C1: the measure control")
    ok1 = f[3] == f[1] and g[3] >= g[2]
    check(f"population-independent weights: F2 amp "
          f"factorization {f[2]}/{f[0]} (drive) -> {f[3]}/{f[0]} "
          f"(uniform) = support factorization {f[1]}/{f[0]} "
          f"exactly; genesis {g[2]} -> {g[3]} of {g[0]} ({ok1}). "
          f"**THE MEASURE CONTROL CLOSES: the population clock "
          f"was the only measure-side coupling -- every residual "
          f"amplitude failure is record-level.**", ok1)

    print("## C2: the record control")
    ok2 = f[1] < f[0] and f[4] > 0 and couple_ex is not None
    check(f"local-record keying: F2 support factorization "
          f"restores on {f[4]} local channels (global keying: "
          f"{f[1]}/{f[0]}); collider witness (one global class "
          f"fusing distinct local-record pairs): {couple_ex} "
          f"({ok2}). **THE RECORD CONTROL CLOSES: the coupling "
          f"lives in the GLOBAL class -- a genuine collider, "
          f"exhibited -- and local records restore locality.**",
          ok2)

    print("## C3: the refined holism theorem")
    ok3 = g[1] == g[0] and f[1] < f[0]
    check(f"the contrast in final form: the GLOBAL-record fiber "
          f"factorizes over disjoint-neighborhood events on the "
          f"conserving floor ({g[1]}/{g[0]}) and fails on the "
          f"mortal floor ({f[1]}/{f[0]}) ({ok3}). **MORTAL "
          f"HOLISM, refined and control-hardened: on a mortal "
          f"floor the global class is a genuine collider whose "
          f"conditioning couples spacelike events; on a "
          f"conserving floor the global class DECOMPOSES into "
          f"local classes. Both referee confounds are closed: "
          f"the measure coupling is the population clock "
          f"(removable), the record coupling is the collider "
          f"(exhibited), and the conserving/mortal contrast "
          f"survives both.**", ok3)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
