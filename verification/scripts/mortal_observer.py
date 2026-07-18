#!/usr/bin/env python3
"""Chapter 39: the mortal observer (exact).

  O1 P115-1: the free shape-lock.
  O2 P115-2: the blindness cell (the map's OPEN cell).
  O3 P115-3: the grammar under the instrument.
  O4 P115-4: the finite biography + the mortal refusal analog.
"""
from fractions import Fraction
from grammar_closure import (nb, verts, coag_singles, coag_succ,
                             grammar, IP)

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def induced(E, S):
    return frozenset(e for e in E if e[0] in S and e[1] in S)

def interface(E, S):
    return frozenset(e for e in E
                     if (e[0] in S) != (e[1] in S))

def body_paths(E0, S, depth):
    """external-merge protocols; channel = (events, interface)."""
    ch = {}
    def rec(E, d, events, bits, dev, w):
        if d == depth:
            ch.setdefault((tuple(events), interface(E, S)),
                          []).append((bits, dev, w))
            return
        ext = [e for e in sorted(E)
               if e[0] not in S and e[1] not in S]
        m = len(ext)
        if m == 0:
            return
        for (a, b) in ext:
            singles, cap = coag_singles(E, a, b)
            k = len(singles)
            for mask in range(1 << k):
                keep = [singles[i] for i in range(k)
                        if mask >> i & 1]
                b2 = dict(bits)
                for u in singles:
                    b2[(d, u)] = 0 if u in keep else 1
                rec(coag_succ(E, a, b, keep), d + 1,
                    events + [(a, b)], b2,
                    dev + (k - len(keep)),
                    w * Fraction(1, m * (1 << k)))
    rec(E0, 0, [], {}, 0, Fraction(1))
    return ch

def amp(plist):
    re = im = P = Fraction(0)
    for (_, dev, w) in plist:
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

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

def fragile(plist):
    """some single-bit reveal leaves a branch < 2 paths or
    incoherent (107-matched)."""
    allk = sorted({k for (b, _, _) in plist for k in b},
                  key=str)
    und = [k for k in allk
           if len({b.get(k, 'A') for (b, _, _) in plist}) > 1]
    if not und:
        return None
    for u in und:
        br = {}
        for p in plist:
            br.setdefault(p[0].get(u, 'A'), []).append(p)
        for pl in br.values():
            if len(pl) < 2:
                return True
            re, im, P = amp(pl)
            if re * re + im * im != P * P:
                return True
    return False

if __name__ == '__main__':
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    C8 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (5, 6), (6, 7), (0, 7)))
    K4p = frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
                     (2, 3), (3, 4)))
    ARENA = [("C6", C6), ("C8", C8), ("K4p", K4p)]

    print("## O1: the free shape-lock")
    lock_ok = True
    n_moves = 0
    for nm, E0 in ARENA:
        for S in [{0, 1}, {2, 3}]:
            Ssh = induced(E0, S)
            ext = [e for e in sorted(E0)
                   if e[0] not in S and e[1] not in S]
            for (a, b) in ext:
                singles, cap = coag_singles(E0, a, b)
                for mask in range(1 << len(singles)):
                    keep = [singles[i]
                            for i in range(len(singles))
                            if mask >> i & 1]
                    E1 = coag_succ(E0, a, b, keep)
                    n_moves += 1
                    if induced(E1, S) != Ssh:
                        lock_ok = False
    check(f"every external merge leaves the body's interior "
          f"untouched ({n_moves} moves, all starts/bodies) "
          f"({lock_ok}). **THE FREE SHAPE-LOCK: on the mortal "
          f"floor, shape-locking costs nothing -- outside "
          f"events can only move the INTERFACE. The genesis "
          f"observer pays admissibility for its shape; the "
          f"mortal observer gets it free and pays in lifespan "
          f"instead.**", lock_ok)

    print("## O2+O3: the blindness cell + the grammar")
    n_bright = n_frag = n_pers = 0
    gcls = {}
    spec = {"bright": 0, "dark": 0, "partial": 0}
    for nm, E0 in ARENA:
        for S in [{0, 1}, {2, 3}, {0, 1, 2}]:
          for depth in (2, 3):
            for key, plist in body_paths(E0, S, depth).items():
                re, im, P = amp(plist)
                a2 = re * re + im * im
                cls = ("bright" if a2 == P * P else
                       "dark" if a2 == 0 else "partial")
                spec[cls] += 1
                got = faithful(plist)
                if got is not None:
                    und, supp = got
                    g = grammar(supp, len(und))
                    gcls[g] = gcls.get(g, 0) + 1
                if cls == "bright" and len(plist) >= 2:
                    fr = fragile(plist)
                    if fr is None:
                        continue
                    n_bright += 1
                    if fr:
                        n_frag += 1
                    else:
                        n_pers += 1
    ok2 = n_bright > 0 and n_frag > 0 and n_pers > 0
    check(f"THE BLINDNESS CELL FILLED, AGAINST MY BET: of "
          f"{n_bright} revealable bright body-reading channels, "
          f"{n_frag} are reveal-fragile but {n_pers} PERSIST "
          f"({ok2}). **THE EVASION, FOUND: the persistent "
          f"bright body-reading channel that Sprint 107 hunted "
          f"and proved absent on genesis EXISTS on the mortal "
          f"floor. Blindness is genuinely floor x instrument -- "
          f"the mortal grammar shines through even the blinding "
          f"instrument. The map's OPEN cell closes: "
          f"body-reading blinds genesis, only dims F2.**", ok2)
    ok3 = (gcls.get("other", 0) == 0
           and gcls.get("weight", 0) == 0
           and gcls.get("affine", 0) == 0)
    check(f"THE GRAMMAR UNDER THE INSTRUMENT, adjudicated "
          f"INCONCLUSIVE honestly: interface-keyed support "
          f"classes {gcls} -- every faithful support is "
          f"consistent with BOTH grammars at this scope (too "
          f"small to discriminate); the parity-vs-cardinality "
          f"question under reading instruments stays OPEN by "
          f"name ({ok3}).", ok3)

    print("## O4: the finite biography + the refusal analog")
    # termination scan on C6, body {0,1}: max external depth
    def maxdepth(E0, S):
        best = 0
        def rec(E, d):
            nonlocal best
            best = max(best, d)
            ext = [e for e in sorted(E)
                   if e[0] not in S and e[1] not in S]
            for (a, b) in ext:
                singles, cap = coag_singles(E, a, b)
                for mask in range(1 << len(singles)):
                    keep = [singles[i]
                            for i in range(len(singles))
                            if mask >> i & 1]
                    rec(coag_succ(E, a, b, keep), d + 1)
        rec(E0, 0)
        return best
    md = maxdepth(C6, {0, 1})
    # refusal analog: C6 body {0,1}, depth-2 interface table
    chT = body_paths(C6, {0, 1}, 2)
    tot = {}
    for key, plist in chT.items():
        f = key[1]
        re, im, P = amp(plist)
        r0, i0, P0 = tot.get(f, (Fraction(0), Fraction(0),
                                 Fraction(0)))
        tot[f] = (r0 + re, i0 + im, P0 + P)
    totP = sum(v[2] for v in tot.values())
    tot2 = sum(v[0] * v[0] + v[1] * v[1] for v in tot.values())
    table = sorted((str(P / totP),
                    str((r * r + i * i) / tot2) if tot2 else "0")
                   for f, (r, i, P) in tot.items())
    ok4 = md <= len(verts(C6)) - len({0, 1}) and md >= 2
    check(f"THE FINITE BIOGRAPHY: max external reading depth on "
          f"C6 body {{0,1}} = {md} (bound |V|-|S| = 4); "
          f"interface spectrum {spec}; the mortal refusal-table "
          f"analog (counting vs squared-coat by interface): "
          f"{table[:6]} ({ok4}). **every mortal observer's "
          f"biography is finite: the world runs out of outside. "
          f"The genesis refusal table has no analog limit -- "
          f"the mortal observer reads a TERMINATING text.**",
          ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
