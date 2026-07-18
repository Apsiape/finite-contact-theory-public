#!/usr/bin/env python3
"""Chapter 36: the alien grammar and the reveal law (exact).

  F1 P111-1: the phase-purity law (bright <=> dev constant mod 4)
     at depths 2 and 3, all starts.
  F2 P111-2: the cardinality grammar (supports = affine AND
     weight-union; "other" = 0), adjudicated.
  F3 P111-3: the reveal law (bright reveal-robust) + the NSIT
     sign table vs the genesis table (Sprint 109 frozen).
  F4 P111-4: the darkness question at depth 3.
"""
from itertools import permutations, product
from fractions import Fraction
import math

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

IP = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]

def nb(E, v):
    return {b if a == v else a for a, b in E if v in (a, b)}

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

def channels(E0, depth):
    """channel = (merge-event tuple, final class); paths carry
    (retention bits, deviation, counting weight)."""
    ch = {}
    def rec3(E, d, events, bits, dev, w):
        if d == depth:
            ch.setdefault((tuple(events), canon(E)), []).append(
                (bits, dev, w))
            return
        m = len(E)
        if m == 0:
            return
        for (a, b) in sorted(E):
            singles, cap = coag_singles(E, a, b)
            k = len(singles)
            for mask in range(1 << k):
                keep = [singles[i] for i in range(k)
                        if mask >> i & 1]
                b2 = dict(bits)
                for u in singles:
                    b2[(d, u)] = 0 if u in keep else 1
                rec3(coag_succ(E, a, b, keep), d + 1,
                     events + [(a, b)], b2,
                     dev + (k - len(keep)),
                     w * Fraction(1, m * (1 << k)))
    rec3(E0, 0, [], {}, 0, Fraction(1))
    return ch

def amp(plist):
    re = im = P = Fraction(0)
    for (_, dev, w) in plist:
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

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
    """(und_keys, supp) for uniform-keyset faithful channels,
    else None."""
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

if __name__ == '__main__':
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    STARTS = [("C5", C5), ("C6", C6), ("K4p", K4p)]

    ALL = []
    spectrum = {}
    for nm, E0 in STARTS:
        for depth in (2, 3):
            for key, plist in channels(E0, depth).items():
                ALL.append((nm, depth, key, plist))

    print("## F1: the phase-purity law")
    purity_ok = True
    for (nm, depth, key, plist) in ALL:
        re, im, P = amp(plist)
        a2 = re * re + im * im
        devs = {d % 4 for (_, d, _) in plist}
        bright = a2 == P * P
        if bright != (len(devs) == 1):
            purity_ok = False
        cls = ("bright" if bright else
               "dark" if a2 == 0 else "partial")
        spectrum.setdefault((nm, depth), {}).setdefault(cls, 0)
        spectrum[(nm, depth)][cls] += 1
    check(f"across {len(ALL)} channels (3 starts x depths 2,3): "
          f"bright <=> deviation constant mod 4, exactly "
          f"({purity_ok}). **THE PHASE-PURITY LAW IS THE "
          f"TRAVELING MOD-4 LAW: brightness = mod-4 purity of "
          f"the deviation count on every floor; genesis realizes "
          f"it by dual-code conditions, F2 by cardinality "
          f"supports. The law is generic; its carriers are each "
          f"floor's own.**", purity_ok)

    print("## F2: the cardinality grammar")
    cls_cnt = {"affine": 0, "weight": 0, "both": 0, "mixed": 0,
               "other": 0}
    n_cl = n_skip = 0
    other_ex = []
    mixed_ex = None
    for (nm, depth, key, plist) in ALL:
        got = support_of(plist)
        if got is None:
            n_skip += 1
            continue
        und, supp = got
        n_cl += 1
        m = len(und)
        t0 = sorted(supp)[0]
        diffs = [tuple(x ^ y for x, y in zip(v, t0))
                 for v in supp]
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
        is_wt = supp == {v for v in
                         product((0, 1), repeat=m)
                         if sum(v) in W}
        is_aw = supp == {v for v in hull if sum(v) in W}
        if is_aff and is_wt:
            cls_cnt["both"] += 1
        elif is_aff:
            cls_cnt["affine"] += 1
        elif is_wt:
            cls_cnt["weight"] += 1
        elif is_aw:
            cls_cnt["mixed"] += 1
            if mixed_ex is None:
                mixed_ex = (nm, depth, m, sorted(W),
                            len(basis), sorted(supp)[:4])
        else:
            cls_cnt["other"] += 1
            if len(other_ex) < 3:
                other_ex.append((nm, depth, m, sorted(supp)))
    ok2 = (cls_cnt["other"] == 0
           and cls_cnt["weight"] + cls_cnt["mixed"] > 0)
    check(f"support classification over {n_cl} faithful aligned "
          f"channels ({n_skip} non-uniform/degenerate skipped): "
          f"{cls_cnt}; first mixed example: {mixed_ex}; "
          f"non-(affine-cap-weight) examples: {other_ex} "
          f"({ok2}). **adjudication in RESULTS.**", ok2)

    print("## F3: the reveal law and the sign table")
    cnt_ok = True
    lin_pos = lin_neg = sq_pos = sq_neg = 0
    reveal_ok = True
    n_rev = n_reads = 0
    n_bright_ch = n_partial_ch = 0
    for (nm, depth, key, plist) in ALL:
        if depth != 2:
            continue
        # FULL census: every key appearing anywhere in the
        # channel; absent = its own read outcome ('A'):
        allkeys = sorted({k for (b, _, _) in plist for k in b},
                         key=str)
        und = [k for k in allkeys
               if len({b.get(k, 'A')
                       for (b, _, _) in plist}) > 1]
        if not und:
            continue
        re, im, P = amp(plist)
        a2 = re * re + im * im
        bright = a2 == P * P
        if bright:
            n_bright_ch += 1
        else:
            n_partial_ch += 1
        for u in und:
            n_reads += 1
            br = {}
            for p in plist:
                br.setdefault(p[0].get(u, 'A'), []).append(p)
            amps = {v: amp(pl) for v, pl in br.items()}
            Psum = sum(a[2] for a in amps.values())
            if P != Psum:
                cnt_ok = False
            inc2 = sum(a[0] * a[0] + a[1] * a[1]
                       for a in amps.values())
            if a2 > inc2:
                sq_pos += 1
            elif a2 < inc2:
                sq_neg += 1
            aL = math.sqrt(float(a2))
            incL = sum(math.sqrt(float(a[0] * a[0]
                                       + a[1] * a[1]))
                       for a in amps.values())
            if aL > incL + 1e-12:
                lin_pos += 1
            elif aL < incL - 1e-12:
                lin_neg += 1
            if bright:
                n_rev += 1
                for v, a in amps.items():
                    if a[0] * a[0] + a[1] * a[1] != a[2] * a[2]:
                        reveal_ok = False
                if a2 < inc2:
                    reveal_ok = False
    ok3a = cnt_ok and reveal_ok and n_rev > 0
    check(f"THE REVEAL LAW on {n_reads} single-bit reveals "
          f"(depth 2; FULL census: {n_bright_ch} bright + "
          f"{n_partial_ch} partial channels, absent-bit reads "
          f"included): counting NSIT exact ({cnt_ok}); on all "
          f"{n_rev} bright-channel reveals both branches stay "
          f"BRIGHT and the squared violation is non-negative "
          f"({reveal_ok}) ({ok3a}). **cardinality correlation "
          f"stores phase in the COUNT: revealing WHICH single "
          f"was released cannot touch HOW MANY -- mod-4 purity "
          f"passes to every sub-split. Alien light is "
          f"reveal-robust.**", ok3a)
    gen = ("zero", "never-positive", "both-signs")
    f2_lin = ("never-positive" if lin_pos == 0 and lin_neg > 0
              else "both-signs" if lin_pos and lin_neg
              else "never-negative" if lin_neg == 0 and lin_pos
              else "zero")
    f2_sq = ("both-signs" if sq_pos and sq_neg
             else "never-negative" if sq_neg == 0 and sq_pos
             else "never-positive" if sq_pos == 0 and sq_neg
             else "zero")
    f2 = ("zero" if cnt_ok else "VIOLATED", f2_lin, f2_sq)
    ok3b = f2 == gen
    check(f"THE SIGN TABLE transported: genesis (Sprint 109) = "
          f"{gen}; F2 = {f2} (linear {lin_pos}+/{lin_neg}-, "
          f"squared {sq_pos}+/{sq_neg}-) ({ok3b}). "
          f"**adjudication in RESULTS.**", ok3b)

    print("## F4: the darkness question at depth 3")
    d3 = {k: v for k, v in spectrum.items() if k[1] == 3}
    dark3 = sum(v.get("dark", 0) for v in d3.values())
    dark2 = sum(v.get("dark", 0) for k, v in spectrum.items()
                if k[1] == 2)
    ok4 = dark3 == 0 and dark2 == 0
    check(f"coherence spectra by (start, depth): "
          f"{ {k: v for k, v in sorted(spectrum.items())} }; "
          f"dark at depth 2: {dark2}, at depth 3: {dark3} "
          f"({ok4}). **THE POSITIVE FLOOR: no preclusion on F2 "
          f"through depth 3 -- exact cancellation needs the "
          f"uniform path weights genesis provides; F2's "
          f"heterogeneous weights (population and fork count "
          f"vary along the path) never balance. On the "
          f"coagulation floor nothing staged is ever "
          f"forbidden.**", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
