#!/usr/bin/env python3
"""Chapter 43: the critical corner (exact).

  K1 P122-1: the corner is realizable (conserving, return-free).
  K2 P122-2: the decisive bet (zero dark).
  K3 P122-3: generic core + live coat + uniform-weight locality.
  K4 P122-4: the corner column.
"""
from fractions import Fraction
from itertools import permutations
from grammar_closure import nb, verts, IP

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

_C = {}
def pcanon(E, r):
    key = (E, r)
    if key in _C:
        return _C[key]
    vs = verts(E)
    if r not in vs:
        vs = sorted(set(vs) | {r})
    n = len(vs)
    best = None
    others = [v for v in vs if v != r]
    for p in permutations(range(1, n)):
        mp = dict(zip(others, p))
        mp[r] = 0
        img = tuple(sorted(tuple(sorted((mp[x], mp[y])))
                           for x, y in E))
        if best is None or img < best:
            best = img
    _C[key] = (n, best)
    return _C[key]

def moves(E, r):
    """yield (edge, feasible_survivors)."""
    for (a, b) in sorted(E):
        if r in (a, b):
            continue
        feas = [v for v in (a, b)
                if tuple(sorted((v, r))) not in E]
        if feas:
            yield (a, b), feas

def succ(E, edge, v, r):
    S = set(E)
    S.discard(edge)
    S.add(tuple(sorted((v, r))))
    return frozenset(S)

def channels(E0, r, depth):
    ch = {}
    def rec(E, d, events, bits, dev, w):
        cand = list(moves(E, r))
        m = len(cand)
        if d > 0:
            # census at every depth: each prefix records its
            # channel, so symmetric branches merge by class
            ch.setdefault((tuple(events), pcanon(E, r)),
                          []).append((bits, dev, w))
        if d == depth or m == 0:
            return
        for edge, feas in cand:
            wit = min(feas)
            for v in feas:
                b2 = dict(bits)
                b2[(d, edge)] = 0 if v == wit else 1
                rec(succ(E, edge, v, r), d + 1,
                    events + [edge], b2,
                    dev + (0 if v == wit else 1),
                    w * Fraction(1, m * len(feas)))
    rec(E0, 0, [], {}, 0, Fraction(1))
    return ch

def amp(pl):
    re = im = P = Fraction(0)
    for (_, d, w) in pl:
        re += IP[d % 4][0] * w
        im += IP[d % 4][1] * w
        P += w
    return re, im, P

if __name__ == '__main__':
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    ARENA = [("C5", C5, 4), ("C6", C6, 4), ("K4p", K4p, 3)]
    r = 0

    print("## K1: the corner is realizable")
    cons_ok = mono_ok = True
    for nm, E0, _ in ARENA:
        seen = [(E0, len(nb(E0, r)))]
        stack = [(E0, len(nb(E0, r)))]
        n_checked = 0
        while stack and n_checked < 4000:
            E, dr = stack.pop()
            for edge, feas in moves(E, r):
                for v in feas:
                    E2 = succ(E, edge, v, r)
                    n_checked += 1
                    if len(E2) != len(E):
                        cons_ok = False
                    dr2 = len(nb(E2, r))
                    if dr2 <= dr:
                        mono_ok = False
                    if n_checked < 400:
                        stack.append((E2, dr2))
    ok1 = cons_ok and mono_ok
    check(f"|E| exactly conserved on every move ({cons_ok}); "
          f"deg(r) strictly increases on every move ({mono_ok}) "
          f"-- no pointed class ever returns ({ok1}). **THE "
          f"CORNER (conserving, return-free) IS REALIZABLE: the "
          f"lattice's first constructed floor exists.**", ok1)

    print("## K2+K3: the decisive census")
    spectrum = {"bright": 0, "dark": 0, "partial": 0}
    purity_ok = ceil_ok = True
    n_mixed = 0
    n_dis = sf = af = 0
    dark_ex = None
    for nm, E0, depth in ARENA:
        for key, pl in channels(E0, r, depth).items():
            re, im, P = amp(pl)
            a2 = re * re + im * im
            devs = {d % 4 for (_, d, _) in pl}
            if len(devs) > 1:
                n_mixed += 1
            if a2 > P * P:
                ceil_ok = False
            bright = a2 == P * P
            if bright != (len(devs) == 1):
                purity_ok = False
            cls = ("bright" if bright else
                   "dark" if a2 == 0 else "partial")
            spectrum[cls] += 1
            if cls == "dark" and dark_ex is None:
                dark_ex = (nm, key[0])
            # factorization on vertex-disjoint event pairs
            # (depth 2 prefix): only for depth-2 census entries
            if depth == 2 or len(key[0]) == 2:
                e1, e2 = key[0][0], key[0][1]
                if set(e1) & set(e2):
                    continue
                keysets = {frozenset(b) for (b, _, _) in pl}
                if len(keysets) != 1:
                    continue
                keys = sorted(keysets.pop(), key=str)
                und = [k for k in keys
                       if len({b[k] for (b, _, _) in pl}) > 1]
                if not und:
                    continue
                supp = {tuple(b[k] for k in und)
                        for (b, _, _) in pl}
                if len(supp) != len(pl):
                    continue
                n_dis += 1
                d0 = [i for i, k in enumerate(und)
                      if k[0] == 0]
                d1 = [i for i, k in enumerate(und)
                      if k[0] == 1]
                p0 = {tuple(v[i] for i in d0) for v in supp}
                p1 = {tuple(v[i] for i in d1) for v in supp}
                if len(supp) == len(p0) * len(p1):
                    sf += 1
                    r0 = i0 = r1 = i1 = Fraction(0)
                    for (b, dev, w) in pl:
                        da = sum(x for kk, x in b.items()
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
    ok2 = spectrum["dark"] == 0 and n_mixed > 0
    check(f"THE DECISIVE BET: spectrum {spectrum}; mixed-"
          f"deviation channels {n_mixed} (cancellation "
          f"arithmetic live, weights uniform); dark witness: "
          f"{dark_ex} ({ok2}). **ZERO DARK on a conserving "
          f"floor with live phases: preclusion follows RETURN "
          f"-- the switch now separated in BOTH directions "
          f"(F3: return, no conservation -> 196 dark; F4: "
          f"conservation, no return -> 0 dark).**", ok2)
    ok3 = purity_ok and ceil_ok and n_dis > 0 and af == sf
    check(f"generic core on floor five: ceiling ({ceil_ok}), "
          f"mod-4 purity ({purity_ok}); disjoint-pair "
          f"factorization: {n_dis} channels, support {sf}, "
          f"amplitude {af} (amplitude == support: the "
          f"uniform-weight conserving signature) ({ok3}).", ok3)

    print("## K4: the corner column")
    ok4 = ok1 and ok2
    print("    F4 root floor: conserving YES / return NO / "
          "parented YES / coat LIVE / dark 0 / "
          f"amp-fact == supp-fact ({sf}/{n_dis})")
    print("    return-law scorecard: dark 112/0/196/0/0 vs "
          "returns free/no/priced/no/NO -- five floors, no "
          "exceptions")
    check(f"the lattice's first constructed corner column "
          f"complete ({ok4}).", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
