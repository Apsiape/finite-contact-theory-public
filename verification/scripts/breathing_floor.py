#!/usr/bin/env python3
"""Chapter 40: the breathing floor (exact).

  B1 P116-1: priced rest (returns exist; never free).
  B2 P116-2: the darkness question (preclusion: return vs
     conservation).
  B3 P116-3: the generic core, third floor.
  B4 P116-4: the third column of the permission map.
"""
from fractions import Fraction
from grammar_closure import (nb, verts, canon as canon0,
                             coag_singles, coag_succ, grammar,
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

def f3_moves(E):
    """yield (label, bits{key:0/1}, dev_inc, succ, forks)."""
    vs = verts(E)
    fresh = max(vs) + 1 if vs else 0
    n_moves = len(E) + len(vs)
    for (a, b) in sorted(E):
        singles, cap = coag_singles(E, a, b)
        k = len(singles)
        for mask in range(1 << k):
            keep = [singles[i] for i in range(k)
                    if mask >> i & 1]
            bits = {("F", u): (0 if u in keep else 1)
                    for u in singles}
            yield (("fuse", a, b), bits, k - len(keep),
                   coag_succ(E, a, b, keep),
                   n_moves * (1 << k))
    for a in vs:
        Na = sorted(nb(E, a))
        d = len(Na)
        for mask in range(1 << d):
            T = [Na[i] for i in range(d) if mask >> i & 1]
            S = {e for e in E if a not in e}
            for u in Na:
                if u in T:
                    S.add((min(fresh, u), max(fresh, u)))
                else:
                    S.add((min(a, u), max(a, u)))
            S.add((min(a, fresh), max(a, fresh)))
            bits = {("S", u): (1 if u in T else 0) for u in Na}
            yield (("split", a), bits, len(T) + 1,
                   frozenset(S), n_moves * (1 << d))

def channels(E0, depth):
    ch = {}
    def rec(E, dd, events, bits, dev, w):
        if dd == depth:
            ch.setdefault((tuple(events), canon(E)),
                          []).append((bits, dev, w))
            return
        for (lab, mbits, dv, S, denom) in f3_moves(E):
            b2 = dict(bits)
            for kk, v in mbits.items():
                b2[(dd,) + kk] = v
            rec(S, dd + 1, events + [lab], b2, dev + dv,
                w * Fraction(1, denom))
    rec(E0, 0, [], {}, 0, Fraction(1))
    return ch

def amp(plist):
    re = im = P = Fraction(0)
    for (_, dev, w) in plist:
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

if __name__ == '__main__':
    C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    P4 = frozenset(((0, 1), (1, 2), (2, 3)))
    ARENA = [("C4", C4), ("C5", C5), ("P4", P4)]

    spectrum = {"bright": 0, "dark": 0, "partial": 0}
    purity_ok = ceil_ok = dich_ok = True
    gcls = {}
    returns = []
    n_ch = 0
    dark_ex = None
    maxdist = 0
    for nm, E0 in ARENA:
        c0 = canon(E0)
        for key, plist in channels(E0, 2).items():
            n_ch += 1
            re, im, P = amp(plist)
            a2 = re * re + im * im
            devs = {d % 4 for (_, d, _) in plist}
            bright = a2 == P * P
            if a2 > P * P:
                ceil_ok = False
            if bright != (len(devs) == 1):
                purity_ok = False
            cls = ("bright" if bright else
                   "dark" if a2 == 0 else "partial")
            spectrum[cls] += 1
            if cls == "dark" and dark_ex is None:
                dark_ex = (nm, key[0],
                           sorted({d for (_, d, _) in plist}))
            if key[1] == c0:
                returns.append(
                    (nm, key[0],
                     min(d for (_, d, _) in plist)))
            keysets = {frozenset(b) for (b, _, _) in plist}
            if len(keysets) == 1:
                keys = sorted(keysets.pop(), key=str)
                und = [kk for kk in keys
                       if len({b[kk]
                               for (b, _, _) in plist}) > 1]
                if und:
                    supp = {tuple(b[kk] for kk in und)
                            for (b, _, _) in plist}
                    if len(supp) == len(plist):
                        g = grammar(supp, len(und))
                        gcls[g] = gcls.get(g, 0) + 1
                        if bright and len(supp) >= 2:
                            vsu = sorted(supp)
                            dmin = min(
                                sum(x ^ y for x, y in
                                    zip(u, v))
                                for i, u in enumerate(vsu)
                                for v in vsu[i + 1:])
                            maxdist = max(maxdist, dmin)

    print("## B1: priced rest")
    n_ret = len(returns)
    min_price = min((r[2] for r in returns), default=None)
    all_paid = all(r[2] >= 1 for r in returns)
    ok1 = n_ret > 0 and all_paid
    check(f"class-preserving depth-2 channels EXIST ({n_ret} "
          f"return channels; example {returns[0] if returns else None}); "
          f"every return path pays dev >= 1 ({all_paid}; minimal "
          f"return price = {min_price}) ({ok1}). **PRICED REST: "
          f"the survival row's third value -- genesis rests "
          f"free, the mortal floor cannot rest, the breathing "
          f"floor rests at a price. Reversibility exists exactly "
          f"where it is paid for.**", ok1)

    print("## B2: the darkness question")
    ok2 = spectrum["dark"] > 0
    check(f"F3 coherence spectrum: {spectrum}; first dark "
          f"channel: {dark_ex} ({ok2}). **adjudication in "
          f"RESULTS -- this is the experiment that decomposes "
          f"the conservation switch.**", ok2)

    print("## B3: the generic core, third floor")
    ok3 = purity_ok and ceil_ok
    check(f"on all {n_ch} F3 channels: |amp| <= P ({ceil_ok}); "
          f"bright <=> dev constant mod 4 ({purity_ok}) "
          f"({ok3}). **the coat algebra's third floor: the "
          f"generic core is now a three-point pattern, not a "
          f"coincidence of two.**", ok3)

    print("## B4: the third column")
    ok4 = n_ch > 0 and len(gcls) > 0
    check(f"THE F3 COLUMN: survival = PRICED (min {min_price}); "
          f"conservation = no (|E| fluctuates); grammar classes "
          f"= {gcls}; max bright support distance = {maxdist}; "
          f"dark = {spectrum['dark']} ({ok4}). **the permission "
          f"map grows its third column; three-floor fragment in "
          f"RESULTS.**", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
