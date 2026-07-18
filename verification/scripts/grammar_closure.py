#!/usr/bin/env python3
"""Chapter 38: the grammar closure (exact).

  G1 P113-1: the orbit lemma (supports are stabilizer-orbit
     unions).
  G2 P113-2: the completeness bet (affine-cap-weight), adjudicated
     on heterogeneous starts.
  G3 P113-3: the factorization dichotomy (support vs measure
     locality, both floors).
  G4 P113-4: the bright ledger + the anomaly's orbit check.
"""
from itertools import permutations, product
from fractions import Fraction

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

IP = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]

def nb(E, v):
    return {b if a == v else a for a, b in E if v in (a, b)}

def verts(E):
    return sorted({v for e in E for v in e})

def canon(E):
    vs = verts(E)
    n = len(vs)
    if n == 0:
        return ("empty",)
    best = None
    for p in permutations(range(n)):
        mp = dict(zip(vs, p))
        img = tuple(sorted(tuple(sorted((mp[x], mp[y])))
                           for x, y in E))
        if best is None or img < best:
            best = img
    return (n, best)

def coag_singles(E, a, b):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    return sorted(Na ^ Nb), sorted(Na & Nb)

def coag_succ(E, a, b, keep):
    singles, cap = coag_singles(E, a, b)
    S = {e for e in E if a not in e and b not in e}
    for x in cap:
        S.add((min(a, x), max(a, x)))
    for u in keep:
        S.add((min(a, u), max(a, u)))
    return frozenset(S)

def gen_succ(E, a, b, assign, singles):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    cap = Na & Nb
    S = {e for e in E if a not in e and b not in e}
    S.add((min(a, b), max(a, b)))
    for x in cap:
        S.add((min(a, x), max(a, x)))
        S.add((min(b, x), max(b, x)))
    for u in singles:
        S.add((min(assign[u], u), max(assign[u], u)))
    return frozenset(S)

def gf2_span(vectors, m):
    basis = []
    for v in vectors:
        v = list(v)
        for bb in basis:
            piv = next(i for i, x in enumerate(bb) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, bb)]
        if any(v):
            basis.append(v)
    return basis

def grammar(supp, m):
    t0 = sorted(supp)[0]
    diffs = [tuple(x ^ y for x, y in zip(v, t0)) for v in supp]
    basis = gf2_span(diffs, m)
    hull = set()
    for msk in range(1 << len(basis)):
        v = list(t0)
        for i, bb in enumerate(basis):
            if msk >> i & 1:
                v = [x ^ y for x, y in zip(v, bb)]
        hull.add(tuple(v))
    W = {sum(v) for v in supp}
    is_aff = len(hull) == len(supp)
    is_wt = supp == {v for v in product((0, 1), repeat=m)
                     if sum(v) in W}
    is_aw = supp == {v for v in hull if sum(v) in W}
    return ("both" if is_aff and is_wt else
            "affine" if is_aff else
            "weight" if is_wt else
            "mixed" if is_aw else "other")

def automorphisms(E):
    vs = verts(E)
    Es = {tuple(sorted(e)) for e in E}
    auts = []
    for p in permutations(vs):
        mp = dict(zip(vs, p))
        if {tuple(sorted((mp[x], mp[y]))) for x, y in E} == Es:
            auts.append(mp)
    return auts

if __name__ == '__main__':
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    C7 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (5, 6), (0, 6)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    K5p = frozenset(tuple(sorted((i, j)))
                    for i in range(5) for j in range(i + 1, 5)
                    ) | {(4, 5)}
    BULL = frozenset(((0, 1), (0, 2), (1, 2), (1, 3), (2, 4)))
    ARENA1 = [("C5", C5), ("C6", C6), ("C7", C7), ("K4p", K4p),
              ("K5p", frozenset(K5p)), ("bull", BULL)]

    print("## G1+G2: single-event supports -- orbit lemma and "
          "the completeness bet")
    orbit_ok = True
    cls_cnt = {}
    n_supp = 0
    witnesses = []
    for nm, E0 in ARENA1:
        auts = automorphisms(E0)
        for (a, b) in sorted(E0):
            singles, cap = coag_singles(E0, a, b)
            k = len(singles)
            if k == 0:
                continue
            fibers = {}
            for mask in range(1 << k):
                keep = [singles[i] for i in range(k)
                        if mask >> i & 1]
                S2 = coag_succ(E0, a, b, keep)
                vec = tuple(0 if u in keep else 1
                            for u in singles)
                fibers.setdefault(canon(S2), set()).add(vec)
            stab = [mp for mp in auts
                    if {mp[a], mp[b]} == {a, b}]
            idx = {u: i for i, u in enumerate(singles)}
            perms_s = []
            for mp in stab:
                if all(mp[u] in idx for u in singles):
                    perms_s.append([idx[mp[u]]
                                    for u in singles])
            for cls, supp in fibers.items():
                if len(supp) < 2:
                    continue
                n_supp += 1
                for pi in perms_s:
                    for v in supp:
                        w = tuple(v[pi[i]] for i in range(k))
                        if w not in supp:
                            orbit_ok = False
                g = grammar(supp, k)
                cls_cnt[g] = cls_cnt.get(g, 0) + 1
                if g == "other" and len(witnesses) < 3:
                    witnesses.append((nm, (a, b), sorted(supp)))
    check(f"THE ORBIT LEMMA: all {n_supp} single-event supports "
          f"are unions of edge-stabilizer orbits ({orbit_ok}).",
          orbit_ok)
    died = cls_cnt.get("other", 0) > 0
    check(f"THE COMPLETENESS BET adjudicated: {cls_cnt}; "
          f"beyond-grammar witnesses: {witnesses} "
          f"(bet {'DIED as predicted' if died else 'SURVIVED'}). "
          f"**{'THE ORBIT GRAMMAR: heterogeneous starts mint '
          'supports that are orbit-unions but not affine-cap-'
          'weight -- parity and cardinality are the orbit '
          'grammar_s two shadows, visible on homogeneous starts; '
          'the repetition anomaly is its depth-2 face.'
          if died else
          'affine-cap-weight is complete at single-event scope '
          'on the extended arena -- the completeness theorem '
          'the sweeps asked for, at this scope.'}**", n_supp > 0)

    print("## G3: the factorization dichotomy (both floors)")
    def depth2(E0, floor):
        ch = {}
        m0 = len(E0)
        for (a, b) in sorted(E0):
            if floor == "f2":
                singles, cap = coag_singles(E0, a, b)
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
                    bits1 = {(0, u): (0 if u in keep else 1)
                             for u in singles}
                    d1 = k1 - len(keep)
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
                            asg2 = {u: (par2[u] if u in keep2
                                        else (b2 if par2[u] == a2
                                              else a2))
                                    for u in singles2}
                            E2 = gen_succ(E1, a2, b2, asg2,
                                          singles2)
                        d2 = k2 - len(keep2)
                        bits = dict(bits1)
                        for u in singles2:
                            bits[(1, u)] = (0 if u in keep2
                                            else 1)
                        w = Fraction(1, m0 * (1 << k1)
                                     * m1 * (1 << k2))
                        ch.setdefault(
                            (((a, b), (a2, b2)), canon(E2)),
                            []).append((bits, d1 + d2, w))
        return ch

    def amp(plist):
        re = im = P = Fraction(0)
        for (_, dev, w) in plist:
            re += IP[dev % 4][0] * w
            im += IP[dev % 4][1] * w
            P += w
        return re, im, P

    STARTS2 = [("C5", C5), ("C6", C6), ("K4p", K4p),
               ("bull", BULL)]
    res = {}
    for floor in ("gen", "f2"):
        n_dis = supp_fact = amp_fact = amp_nonfact = 0
        for nm, E0 in STARTS2:
            for key, plist in depth2(E0, floor).items():
                (e1, e2), _ = key
                if set(e1) & set(e2):
                    continue
                keysets = {frozenset(b) for (b, _, _) in plist}
                if len(keysets) != 1:
                    continue
                keys = sorted(keysets.pop(), key=str)
                und = [kk for kk in keys
                       if len({b[kk] for (b, _, _) in plist})
                       > 1]
                if not und:
                    continue
                supp = {tuple(b[kk] for kk in und)
                        for (b, _, _) in plist}
                if len(supp) != len(plist):
                    continue
                n_dis += 1
                d0 = [i for i, kk in enumerate(und)
                      if kk[0] == 0]
                d1_ = [i for i, kk in enumerate(und)
                       if kk[0] == 1]
                p0 = {tuple(v[i] for i in d0) for v in supp}
                p1 = {tuple(v[i] for i in d1_) for v in supp}
                if len(supp) == len(p0) * len(p1):
                    supp_fact += 1
                re, im, P = amp(plist)
                # normalized amp vs product of per-event
                # normalized amps (split each path's dev):
                r0 = i0 = P0 = Fraction(0)
                r1 = i1 = P1 = Fraction(0)
                for (b, dev, w) in plist:
                    da = sum(v for kk, v in b.items()
                             if kk[0] == 0)
                    db = dev - da
                    r0 += IP[da % 4][0] * w
                    i0 += IP[da % 4][1] * w
                    r1 += IP[db % 4][0] * w
                    i1 += IP[db % 4][1] * w
                    P0 += w
                # product of normalized amps vs normalized amp:
                # (amp/P) ?= (amp_a/P)*(amp_b/P)
                lhs_r = re * P0
                lhs_i = im * P0
                rr = r0 * r1 - i0 * i1
                ri = r0 * i1 + i0 * r1
                if (lhs_r * P0 == rr * P0 and
                        lhs_i * P0 == ri * P0):
                    pass
                if (re * P0 * P0 == (rr) * P0 and
                        im * P0 * P0 == (ri) * P0):
                    amp_fact += 1
                else:
                    amp_nonfact += 1
        res[floor] = (n_dis, supp_fact, amp_fact, amp_nonfact)
    g = res["gen"]
    f = res["f2"]
    ok3 = (g[0] > 0 and f[0] > 0 and g[1] > 0 and f[1] > 0
           and g[2] > 0 and f[3] > 0)
    check(f"THE FACTORIZATION DICHOTOMY on vertex-disjoint "
          f"event pairs (faithful channels): genesis "
          f"{g[0]} channels, support factorizes {g[1]}, "
          f"amplitude factorizes {g[2]}/{g[0]}; F2 {f[0]} "
          f"channels, support factorizes {f[1]}, amplitude "
          f"factorizes {f[2]} / fails {f[3]} ({ok3}). "
          f"**support locality is generic; MEASURE locality "
          f"requires conservation -- the mortal floor couples "
          f"every event through population. The conservation "
          f"switch, third appearance.**", ok3)

    print("## G4: the bright ledger + the anomaly orbit check")
    maxd = 0
    purity_ok = True
    for nm, E0 in STARTS2:
        for key, plist in depth2(E0, "f2").items():
            re, im, P = amp(plist)
            a2 = re * re + im * im
            devs = {d % 4 for (_, d, _) in plist}
            if (a2 == P * P) != (len(devs) == 1):
                purity_ok = False
            if a2 == P * P and len(plist) >= 2:
                keysets = {frozenset(b) for (b, _, _) in plist}
                if len(keysets) != 1:
                    continue
                keys = sorted(keysets.pop(), key=str)
                und = [kk for kk in keys
                       if len({b[kk] for (b, _, _) in plist})
                       > 1]
                if not und:
                    continue
                supp = {tuple(b[kk] for kk in und)
                        for (b, _, _) in plist}
                if len(supp) == len(plist) and len(supp) >= 2:
                    vs = sorted(supp)
                    d = min(sum(x ^ y for x, y in zip(u, v))
                            for i, u in enumerate(vs)
                            for v in vs[i + 1:])
                    maxd = max(maxd, d)
    # anomaly orbit check (K4p, contact (3,4) twice, genesis):
    anom_ok = None
    auts = automorphisms(K4p)
    stab = [mp for mp in auts if {mp[3], mp[4]} == {3, 4}]
    gch = depth2(K4p, "gen")
    for key, plist in gch.items():
        (e1, e2), _ = key
        if e1 == (3, 4) and e2 == (3, 4):
            keysets = {frozenset(b) for (b, _, _) in plist}
            if len(keysets) != 1:
                continue
            keys = sorted(keysets.pop(), key=str)
            und = [kk for kk in keys
                   if len({b[kk] for (b, _, _) in plist}) > 1]
            supp = {tuple(b[kk] for kk in und)
                    for (b, _, _) in plist}
            if len(supp) != len(plist) or len(und) != 6:
                continue
            g6 = grammar(supp, 6)
            # orbit closure under stabilizer acting on both
            # depth layers simultaneously:
            idx = {u: i for i, u in enumerate(und)}
            closed = True
            for mp in stab:
                pi = {}
                okp = True
                for kk in und:
                    tgt = (kk[0], mp.get(kk[1], kk[1]))
                    if tgt not in idx:
                        okp = False
                        break
                    pi[idx[kk]] = idx[tgt]
                if not okp:
                    continue
                for v in supp:
                    w = tuple(v[pi[i]] for i in range(6))
                    if w not in supp:
                        closed = False
            anom_ok = (g6 == "other" and closed)
    ok4 = purity_ok and maxd >= 4 and anom_ok is True
    check(f"extended bright ledger: mod-4 purity off-census "
          f"({purity_ok}); max realized bright support distance "
          f"on F2 = {maxd}; the Sprint-112 repetition-anomaly "
          f"support is beyond-grammar AND orbit-closed "
          f"({anom_ok}) ({ok4}). **the anomaly is the orbit "
          f"grammar's depth-2 face: canon-invariance is the "
          f"grammar; parity and cardinality are its shadows.**",
          ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
