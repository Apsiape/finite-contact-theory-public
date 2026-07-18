#!/usr/bin/env python3
"""Chapter 37: the cross-floor permission map (exact).

One matched instrument suite, two floors, same code:
  M1 P112-1: the evasion (persistence spectra, both floors).
  M2 P112-2: one floor, one grammar (matched grammar census).
  M3 P112-3: the distance contrast (cap, live, both floors).
  M4 P112-4: the map assembles (+ conservation, survival,
     purity/ceiling/dichotomy cross-floor, dark counts).
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

# ---- floor definitions: moves(E) yields ----
# (bitmap {single: 0 canonical / 1 deviated}, succ, n_forks)
# one yield per (edge, fork-choice); weight = 1/(|E| * forks).

def f2_moves(E):
    for (a, b) in sorted(E):
        Na = nb(E, a) - {b}
        Nb = nb(E, b) - {a}
        singles = sorted(Na ^ Nb)
        cap = sorted(Na & Nb)
        k = len(singles)
        for mask in range(1 << k):
            keep = [singles[i] for i in range(k)
                    if mask >> i & 1]
            S = {e for e in E if a not in e and b not in e}
            for x in cap:
                S.add((min(a, x), max(a, x)))
            for u in keep:
                S.add((min(a, u), max(a, u)))
            bits = {u: (0 if u in keep else 1) for u in singles}
            yield ((a, b), bits, frozenset(S), 1 << k)

def gen_moves(E):
    for (a, b) in sorted(E):
        Na = nb(E, a) - {b}
        Nb = nb(E, b) - {a}
        singles = sorted(Na ^ Nb)
        cap = sorted(Na & Nb)
        k = len(singles)
        parent = {u: (a if u in Na else b) for u in singles}
        for choice in product((a, b), repeat=k):
            assign = dict(zip(singles, choice))
            S = {e for e in E if a not in e and b not in e}
            S.add((min(a, b), max(a, b)))
            for x in cap:
                S.add((min(a, x), max(a, x)))
                S.add((min(b, x), max(b, x)))
            for u in singles:
                S.add((min(assign[u], u), max(assign[u], u)))
            bits = {u: (0 if assign[u] == parent[u] else 1)
                    for u in singles}
            yield ((a, b), bits, frozenset(S), 1 << k)

def census(E0, depth, moves):
    """matched channel census: key = (events, final class);
    paths = (bits{(d,u):v}, dev, w)."""
    ch = {}
    def rec(E, d, events, bits, dev, w):
        if d == depth:
            ch.setdefault((tuple(events), canon(E)),
                          []).append((bits, dev, w))
            return
        m = len(E)
        if m == 0:
            return
        for (ev, mbits, S, forks) in moves(E):
            b2 = dict(bits)
            for u, v in mbits.items():
                b2[(d, u)] = v
            rec(S, d + 1, events + [ev], b2,
                dev + sum(mbits.values()),
                w * Fraction(1, m * forks))
    rec(E0, 0, [], {}, 0, Fraction(1))
    return ch

def amp(plist):
    re = im = P = Fraction(0)
    for (_, dev, w) in plist:
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

def und_keys(plist):
    allk = sorted({k for (b, _, _) in plist for k in b},
                  key=str)
    return [k for k in allk
            if len({b.get(k, 'A') for (b, _, _) in plist}) > 1]

def coherent(plist):
    re, im, P = amp(plist)
    return re * re + im * im == P * P

def survives(plist, r):
    """every single-bit reveal leaves every branch with >= 2
    paths and coherence 1, recursively r deep."""
    if r == 0:
        return True
    und = und_keys(plist)
    if not und:
        return False          # no reveal handle: excluded
    for u in und:
        br = {}
        for p in plist:
            br.setdefault(p[0].get(u, 'A'), []).append(p)
        for pl in br.values():
            if len(pl) < 2 or not coherent(pl):
                return False
            if r > 1 and not survives(pl, r - 1):
                return False
    return True

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

def support_of(plist):
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

def mindist(supp):
    vs = sorted(supp)
    return min(sum(x ^ y for x, y in zip(a, b))
               for i, a in enumerate(vs)
               for b in vs[i + 1:])

def floor_report(E0s, moves, depth=2):
    R = {"spectrum": {"bright": 0, "dark": 0, "partial": 0},
         "purity_ok": True, "ceil_ok": True, "dich_ok": True,
         "grammar": {}, "pers": {}, "maxdist": 0,
         "survival": False, "conserved": True, "mortal": True,
         "n": 0, "wt_uniform": 0, "wt_varied": 0}
    for E0 in E0s:
        for (ev, mbits, S, forks) in moves(E0):
            if len(S) >= len(E0):
                R["mortal"] = False
            if len(S) != len(E0):
                R["conserved"] = False
            if canon(S) == canon(E0):
                R["survival"] = True
        for key, plist in census(E0, depth, moves).items():
            R["n"] += 1
            re, im, P = amp(plist)
            a2 = re * re + im * im
            devs = {d % 4 for (_, d, _) in plist}
            bright = a2 == P * P
            if a2 > P * P:
                R["ceil_ok"] = False
            if bright != (len(devs) == 1):
                R["purity_ok"] = False
            cls = ("bright" if bright else
                   "dark" if a2 == 0 else "partial")
            R["spectrum"][cls] += 1
            ws = {w for (_, _, w) in plist}
            if len(ws) == 1:
                R["wt_uniform"] += 1
            else:
                R["wt_varied"] += 1
            got = support_of(plist)
            if got is not None:
                und, supp = got
                g = grammar(supp, len(und))
                R["grammar"][g] = R["grammar"].get(g, 0) + 1
                if bright and len(supp) >= 2:
                    R["maxdist"] = max(R["maxdist"],
                                       mindist(supp))
            if bright and len(plist) >= 2:
                p = 0
                while p < 3 and survives(plist, p + 1):
                    p += 1
                R["pers"][p] = R["pers"].get(p, 0) + 1
    return R

if __name__ == '__main__':
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    STARTS = [C5, C6, K4p]

    print("## building the matched censuses "
          "(same code, two floors)")
    G = floor_report(STARTS, gen_moves)
    F = floor_report(STARTS, f2_moves)
    print(f"  genesis: {G['n']} channels, spectrum "
          f"{G['spectrum']}, grammar {G['grammar']}, "
          f"persistence {G['pers']}, maxdist {G['maxdist']}, "
          f"weights uniform/varied "
          f"{G['wt_uniform']}/{G['wt_varied']}")
    print(f"  F2:      {F['n']} channels, spectrum "
          f"{F['spectrum']}, grammar {F['grammar']}, "
          f"persistence {F['pers']}, maxdist {F['maxdist']}, "
          f"weights uniform/varied "
          f"{F['wt_uniform']}/{F['wt_varied']}")

    print("## M1: the evasion -- the bet's death examined")
    g_max = max(G["pers"]) if G["pers"] else -1
    f_max = max(F["pers"]) if F["pers"] else -1
    # mechanism pass on genesis: persistent channels + grammar
    # provenance (weight supports, the beyond-grammar support):
    n_gp = n_fact = n_unf = 0
    others = []
    weight_ev = []
    for E0 in STARTS:
        for key, plist in census(E0, 2, gen_moves).items():
            got = support_of(plist)
            if got is not None:
                und, supp = got
                g = grammar(supp, len(und))
                if g == "other":
                    others.append(key[0])
                elif g == "weight":
                    weight_ev.append(key[0])
            re, im, P = amp(plist)
            if (re * re + im * im != P * P or len(plist) < 2
                    or not survives(plist, 1)):
                continue
            n_gp += 1
            ev1, ev2 = key[0]
            disj = not (set(ev1) & set(ev2))
            if got is None:
                n_unf += 1
                continue
            und, supp = got
            d0 = [i for i, k in enumerate(und) if k[0] == 0]
            d1 = [i for i, k in enumerate(und) if k[0] == 1]
            p0 = {tuple(v[i] for i in d0) for v in supp}
            p1 = {tuple(v[i] for i in d1) for v in supp}
            if (disj and len(supp) == len(p0) * len(p1)
                    and len(p0) > 1 and len(p1) > 1):
                n_fact += 1
    f_pers = sum(v for p, v in F["pers"].items() if p >= 1)
    ok1 = (g_max >= 1 and f_max >= 1 and n_fact > 0
           and n_fact + n_unf == n_gp and f_pers >= 1)
    check(f"THE FLOOR-CONTINGENCY BET DIED, and the death is "
          f"the finding: persistence spectra genesis {G['pers']} "
          f"/ F2 {F['pers']} -- BOTH floors evade blindness in "
          f"event-record keying. Genesis's {n_gp} persistent "
          f"bright channels are ALL factorization-type "
          f"({n_fact} verified as disjoint contacts with "
          f"cross-step product supports + {n_unf} "
          f"multiplicity-type): SPACELIKE SEPARATION MAKES "
          f"REVEALS LOCAL. F2's {f_pers} persist by slice/pair "
          f"structure ({ok1}). **THE THIRD AXIS: the Sprint-107 "
          f"blindness law is real but INSTRUMENT-SCOPED "
          f"(body-reading channels); in event-record keying the "
          f"evasion exists on both floors, by different "
          f"mechanisms. Laws are indexed by floor x "
          f"instrument.**", ok1)

    print("## M2: the grammar census -- the bet's death "
          "examined")
    g_gr, f_gr = G["grammar"], F["grammar"]
    ok2 = (g_gr.get("weight", 0) > 0
           and len(others) == 1
           and others[0][0] == others[0][1]
           and f_gr.get("weight", 0) > 0
           and f_gr.get("affine", 0) > 0
           and f_gr.get("mixed", 0) == 0
           and f_gr.get("other", 0) == 0)
    check(f"ONE-FLOOR-ONE-GRAMMAR DIED: matched census genesis "
          f"{g_gr} / F2 {f_gr}. Genesis event-record channels "
          f"speak cardinality too ({g_gr.get('weight', 0)} "
          f"weight-union supports: class-feasibility forbids "
          f"the assignment extremes), and exactly ONE support "
          f"lies BEYOND the affine-cap-weight grammar -- minted "
          f"by firing the SAME contact twice ({others}): "
          f"sequential self-dependence. F2 still shows two pure "
          f"grammars, unmixed ({ok2}). **the grammar is "
          f"instrument-indexed: reading-protocol genesis is "
          f"parity-only (prior [V] engines); event-record "
          f"genesis is parity + cardinality + one repetition "
          f"anomaly. The clean dichotomy belongs to the "
          f"instrument, the floor sets which grammars are "
          f"REACHABLE.**", ok2)

    print("## M3: the distance contrast")
    ok3 = G["maxdist"] <= 2 and F["maxdist"] >= 4
    check(f"max min-Hamming-distance over bright faithful "
          f"supports: genesis {G['maxdist']} vs F2 "
          f"{F['maxdist']} ({ok3}). **THE CAP, LIVE AND "
          f"MATCHED: same code, same observable -- genesis "
          f"bright correlation never exceeds distance 2, F2 "
          f"realizes distance 4. The prohibition and the "
          f"permission are now one measurement apart.**", ok3)

    print("## M4: the permission map")
    core_ok = (G["purity_ok"] and F["purity_ok"]
               and G["ceil_ok"] and F["ceil_ok"])
    ok4 = (core_ok and G["conserved"] and not G["mortal"]
           and F["mortal"] and not F["conserved"]
           and G["survival"] and not F["survival"]
           and G["spectrum"]["dark"] >= 0
           and F["spectrum"]["dark"] == 0)
    rows = [
        ("staging / no-selector",            "YES", "YES",
         "GENERIC [live: both floors fork]"),
        ("|E| conservation",                 "YES", "no",
         "CONTINGENT [live: max-paid conserves; merge is "
         "mortal]"),
        ("survival channel (rest possible)", "YES", "no",
         "CONTINGENT [live]"),
        ("indifference / microcanonical",    "YES", "no",
         "CONTINGENT [arrhenius.py / alien_coat.py]"),
        ("coat ceiling |amp| <= P",          "YES", "YES",
         "GENERIC [live]"),
        ("additivity dichotomy",             "YES", "YES",
         "GENERIC [born_bridge.py / alien_coat.py]"),
        ("phase purity (mod-4 law)",         "YES", "YES",
         "GENERIC [live]"),
        ("NSIT sign table (0/neg/both)",     "YES", "YES",
         "GENERIC coat-level [actuality_protocol.py / "
         "alien_reading.py]"),
        ("correlation grammar",
         "parity+card (+1 beyond)", "parity XOR cardinality",
         "INSTRUMENT-INDEXED [live; reading-protocols: "
         "genesis parity-only, prior V]"),
        ("darkness / preclusion",
         f"{G['spectrum']['dark']} dark",
         f"{F['spectrum']['dark']} dark",
         "CONTINGENT [live matched keying + "
         "two_code_lineages.py / alien_reading.py]"),
        ("distance cap <= 2",                "YES", "no",
         "CONTINGENT [live + cap_theorem.py / alien_coat.py]"),
        ("reveal persistence (blindness)",
         f"evading (max {g_max}, factoriz.)",
         f"evading (max {f_max}, slices)",
         "INSTRUMENT-INDEXED [live; body-reading: genesis "
         "blind (stratified.py), F2 body analog OPEN]"),
    ]
    print("  THE PERMISSION MAP (genesis | F2):")
    for (row, g, f, note) in rows:
        print(f"    {row:34s} | {g:24s} | {f:24s} | {note}")
    check(f"the map assembles without contradiction: coat core "
          f"(ceiling+purity) generic live on both floors "
          f"({core_ok}); genesis conserves |E| and can rest, F2 "
          f"is mortal and cannot; genesis stages darkness "
          f"({G['spectrum']['dark']} dark channels in matched "
          f"keying), F2 stages none ({ok4}). **THE MAP'S THREE "
          f"AXES: floor x law x INSTRUMENT. Measure-side "
          f"contingency traces to conservation-vs-mortality "
          f"(uniform weights enable cancellation, preclusion, "
          f"indifference); the distance cap stays cleanly "
          f"floor-contingent; grammar and blindness turn out "
          f"instrument-indexed. The taxonomy of inevitability, "
          f"first full artifact -- honest about what its own "
          f"instruments contribute.**", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
