#!/usr/bin/env python3
"""Chapter 32 -- The Coat and the Count (public verifier).

Exact, exhaustive, dependency-free. The amplitude calculus of the
quarter-turn coat (Chapters 30-31) at depth 2 and 3: the exact
double-slit (fringes, which-path, delayed-choice eraser), the
forced path integral with its exact onset, and the coupling
trichotomy relating coat statistics to counting statistics.
Classical frames cited in-line per the blind sweeps: the
delayed-choice eraser (Scully-Druhl; Kim et al.), decoherent-
histories genericity (Dowker-Kent), no-joint-distribution
structure (Fine; Feynman's negative-probability discussion),
quasiprobability calculi (Kirkwood-Dirac lineage), and Sorkin's
quantum measure. Frozen bets that died in the private campaign
are scored in print. The floor's founding postulate -- no
selector among staged paths -- is shown to be exactly the premise
that coat-following frequencies require.
"""
from itertools import combinations, product
from fractions import Fraction

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

IP = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]

def nb(E, v):
    return {b if a == v else a for a, b in E if v in (a, b)}

def contact_singles(E, a, b):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    return sorted((Na | Nb) - (Na & Nb))

def succ_max(E, a, b, assign, singles):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    cap = Na & Nb
    S = {e for e in E if a not in e and b not in e}
    S.add((min(a, b), max(a, b)))
    for x in cap:
        S.add((min(a, x), max(a, x)))
        S.add((min(b, x), max(b, x)))
    for s in singles:
        S.add((min(assign[s], s), max(assign[s], s)))
    return frozenset(S)

def induced(E, S):
    return frozenset(e for e in E if e[0] in S and e[1] in S)

def interface(E, S):
    return frozenset(e for e in E if (e[0] in S) != (e[1] in S))

WORLDS = {
    "C6": frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                     (0, 5))),
    "octahedron": frozenset(e for e in combinations(range(6), 2)
                            if e not in ((0, 3), (1, 4), (2, 5))),
    "K6-e": frozenset(e for e in combinations(range(6), 2)
                      if e != (0, 1)),
    "prism": frozenset(((0, 1), (1, 2), (0, 2), (3, 4), (4, 5),
                        (3, 5), (0, 3), (1, 4), (2, 5))),
}

def bodies(E, sizes=(2, 3), n=6):
    out = []
    for k in sizes:
        for S in combinations(range(n), k):
            Sset = set(S)
            Ein = induced(E, Sset)
            if not Ein and k > 1:
                continue
            seen = {S[0]}
            stack = [S[0]]
            while stack:
                v = stack.pop()
                for x, y in Ein:
                    w = y if x == v else (x if y == v else None)
                    if w is not None and w not in seen:
                        seen.add(w)
                        stack.append(w)
            if seen == Sset:
                out.append(Sset)
    return out

def admissible(E, S, c):
    a, b = c
    singles = contact_singles(E, a, b)
    parent = {u: (a if u in nb(E, a) else b) for u in singles}
    out = []
    shape = induced(E, S)
    for choice in product((a, b), repeat=len(singles)):
        assign = dict(zip(singles, choice))
        E2 = succ_max(E, a, b, assign, singles)
        if induced(E2, S) == shape:
            dev = sum(1 for u in singles if assign[u] != parent[u])
            out.append((assign, E2, dev))
    return out

if __name__ == '__main__':
    print("## 1: the double-slit census")
    sum_ok = ceiling_ok = True
    n_con = n_des = n_cases = 0
    n_recover = n_compound = 0
    dich_ok = True
    for wname, E0 in WORLDS.items():
        for S in bodies(E0):
            for c1 in E0:
                adm1 = admissible(E0, S, c1)
                if not adm1:
                    continue
                singles1 = contact_singles(E0, *c1)
                slits = [u for u in singles1 if u not in S]
                if not slits:
                    continue
                for u in slits:
                    by_rest = {}
                    for (assign, E1, d1) in adm1:
                        key = (tuple(sorted((x, v) for x, v in
                                            assign.items()
                                            if x != u)),
                               interface(E1, S))
                        by_rest.setdefault(key, set()).add(
                            assign[u])
                    if not any(len(v) == 2
                               for v in by_rest.values()):
                        continue
                    for c2 in E0:
                        n_cases += 1
                        paths = []
                        N1 = len(adm1)
                        for (a1, E1, d1) in adm1:
                            adm2 = admissible(E1, S, c2)
                            if not adm2:
                                continue
                            N2 = len(adm2)
                            for (a2, E2, d2) in adm2:
                                paths.append(
                                    (a1[u], interface(E2, S),
                                     (d1 + d2) % 4,
                                     Fraction(1, N1 * N2)))
                        if not paths:
                            continue
                        chA = {}
                        chR = {}
                        for (wb, F, dm, wgt) in paths:
                            chA.setdefault(F, []).append(
                                (dm, wgt))
                            chR.setdefault((wb, F), []).append(
                                (dm, wgt))
                        def amp(pl):
                            re = im = P = Fraction(0)
                            devs = set()
                            for dm, wgt in pl:
                                re += IP[dm][0] * wgt
                                im += IP[dm][1] * wgt
                                P += wgt
                                devs.add(dm)
                            return re, im, P, devs
                        for F, pl in chA.items():
                            re, im, P, devs = amp(pl)
                            a2m = re * re + im * im
                            sre = sim = Fraction(0)
                            inc = Fraction(0)
                            wbits = set()
                            for (wb, FF), pl2 in chR.items():
                                if FF != F:
                                    continue
                                wbits.add(wb)
                                r2, i2, P2, _ = amp(pl2)
                                sre += r2
                                sim += i2
                                inc += r2 * r2 + i2 * i2
                            if (sre, sim) != (re, im):
                                sum_ok = False
                            if a2m > P * P:
                                ceiling_ok = False
                            if a2m > inc:
                                n_con += 1
                            elif a2m < inc:
                                n_des += 1
                            pure = len(devs) == 1
                            if pure != (a2m == P * P):
                                dich_ok = False
                            if len(wbits) == 1 and pure \
                                    and a2m == P * P:
                                n_recover += 1
                            if len(wbits) == 2 and not pure:
                                n_compound += 1
    ok = (sum_ok and ceiling_ok and n_con > 0 and n_des > 0
          and dich_ok and n_recover > 0 and n_compound > 0)
    check(f"across {n_cases} slit configurations: the detector-off "
          f"amplitude is the coherent branch sum on every channel "
          f"({sum_ok}); fringes of both signs exist "
          f"({n_con} constructive / {n_des} destructive) with the "
          f"|amp| <= P ceiling never violated ({ceiling_ok}); the "
          f"additivity dichotomy (exact iff phase-pure) holds "
          f"({dich_ok}); and the delayed-choice eraser is exact -- "
          f"{n_recover} channels where the final record determines "
          f"the earlier unread bit recover coherence EXACTLY 1, "
          f"{n_compound} compounding channels ({ok}). The eraser "
          f"phenomenology (Scully-Druhl; Kim et al., cited) here "
          f"is a rational-arithmetic theorem; the moral is exact: "
          f"what matters is not WHEN a deviation is read but "
          f"WHETHER the record ever determines it.", ok)

    print("## 2: the forced path integral")
    C6 = WORLDS["C6"]
    boo_ok = True
    n_closed = n_fail = n_mis = 0
    char_ok = True
    deep = 0
    for S in [{0, 1}, {1, 2}]:
        for depth in (2, 3):
            for seq in product(sorted(C6), repeat=depth):
                paths = []
                def rec(E, t, ifs, bits, dv):
                    if t == depth:
                        paths.append((tuple(ifs), dict(bits), dv))
                        return
                    a, b = seq[t]
                    singles = contact_singles(E, a, b)
                    parent = {u: (a if u in nb(E, a) else b)
                              for u in singles}
                    shape = induced(E, S)
                    adm = []
                    for choice in product((a, b),
                                          repeat=len(singles)):
                        assign = dict(zip(singles, choice))
                        E2 = succ_max(E, a, b, assign, singles)
                        if induced(E2, S) == shape:
                            adm.append((assign, E2))
                    if not adm:
                        return
                    N = len(adm)
                    for (assign, E2) in adm:
                        nbts = dict(bits)
                        d2 = dv
                        for uu in singles:
                            lv = (1 if assign[uu] != parent[uu]
                                  else 0)
                            nbts[(t, uu)] = lv
                            d2 += lv
                        rec(E2, t + 1,
                            ifs + [interface(E2, S)], nbts, d2)
                rec(C6, 0, [], {}, 0)
                if not paths:
                    continue
                ch = {}
                for p in paths:
                    ch.setdefault(p[0], []).append(p)
                for traj, plist in ch.items():
                    keysets = {frozenset(p[1]) for p in plist}
                    if len(keysets) > 1:
                        n_mis += 1
                        continue
                    keys = sorted(keysets.pop())
                    det = {}
                    und = []
                    for k in keys:
                        vals = {p[1][k] for p in plist}
                        if len(vals) == 1:
                            det[k] = vals.pop()
                        else:
                            und.append(k)
                    m = len(und)
                    if len({p[2] % 4 for p in plist}) == 1 \
                            and len(plist) > 1 and depth == 3:
                        deep += 1
                    if len({round(float(p[2]), 9)
                            for p in plist}) >= 1:
                        pass
                    w0 = plist[0]
                    if len({str(p[1]) for p in plist}) != \
                            len(plist):
                        continue
                    # equal weights within channel required:
                    d = sum(det.values())
                    re = im = P = Fraction(0)
                    wgt = Fraction(1, len(paths))
                    # recompute weights properly: uniform per
                    # step is path-dependent; use path count as
                    # proxy only when uniform -- skip otherwise:
                    supp = {tuple(p[1][k] for k in und)
                            for p in plist}
                    if len(supp) != len(plist):
                        continue
                    for p in plist:
                        re += IP[p[2] % 4][0]
                        im += IP[p[2] % 4][1]
                        P += 1
                    cre, cim = Fraction(1), Fraction(0)
                    for _ in range(m):
                        cre, cim = ((cre - cim) / 2,
                                    (cre + cim) / 2)
                    ir, ii = IP[d % 4]
                    wre = P * (cre * ir - cim * ii)
                    wim = P * (cre * ii + cim * ir)
                    if (re, im) == (wre, wim):
                        n_closed += 1
                    else:
                        n_fail += 1
                        undl = [k for k in keys if k in und] \
                            if False else und
                        sup = supp
                        t0 = sorted(sup)[0]
                        Cv = {tuple(x ^ y for x, y in
                                    zip(v, t0)) for v in sup}
                        if len(sup) == (1 << m):
                            char_ok = False
    ok = (n_fail > 0 and n_closed > 0 and char_ok and deep > 0)
    check(f"the determined-bits law (amp = P x ((1+i)/2)^m x i^d, "
          f"m = record-undetermined bits) holds on {n_closed} "
          f"aligned channels and fails on {n_fail} -- and every "
          f"failure has NON-free (correlated) hidden-bit support "
          f"({char_ok}); {n_mis} channels are branch-misaligned "
          f"(the general path-integral sector); {deep} depth-3 "
          f"multi-path channels are phase-pure at coherence 1 "
          f"(the deep eraser) ({ok}). Feynman summation is not an "
          f"axiom here: the closed form fails EXACTLY at path "
          f"entanglement -- the sum over histories is the price "
          f"of correlated ignorance (genericity of interference: "
          f"Dowker-Kent, cited).", ok)

    print("## 3: the coupling trichotomy")
    lin_ok = True
    darken = preclude = 0
    for E0 in (C6, WORLDS["prism"]):
        for S in bodies(E0):
            for c in E0:
                if not (c[0] in S or c[1] in S):
                    continue
                adm = admissible(E0, S, c)
                if not adm:
                    continue
                N = len(adm)
                ch = {}
                for (assign, E2, dev) in adm:
                    f = interface(E2, S)
                    re, im, P = ch.get(f, (Fraction(0),
                                           Fraction(0),
                                           Fraction(0)))
                    w = Fraction(1, N)
                    ch[f] = (re + IP[dev % 4][0] * w,
                             im + IP[dev % 4][1] * w, P + w)
                for f, (re, im, P) in ch.items():
                    if re * re + im * im != P * P:
                        lin_ok = False
    for E0 in (C6, WORLDS["prism"]):
        for S in bodies(E0, sizes=(2,)):
            for c1 in E0:
                if c1[0] in S or c1[1] in S:
                    continue
                adm1 = admissible(E0, S, c1)
                if not adm1:
                    continue
                sing1 = contact_singles(E0, *c1)
                slits = [u for u in sing1 if u not in S]
                if not slits:
                    continue
                for c2 in E0:
                    N1 = len(adm1)
                    chA = {}
                    chR = {}
                    for (a1, E1, d1) in adm1:
                        adm2 = admissible(E1, S, c2)
                        if not adm2:
                            continue
                        N2 = len(adm2)
                        for (a2, E2, d2) in adm2:
                            f = interface(E2, S)
                            w = Fraction(1, N1 * N2)
                            dm = (d1 + d2) % 4
                            re, im, P = chA.get(
                                f, (Fraction(0), Fraction(0),
                                    Fraction(0)))
                            chA[f] = (re + IP[dm][0] * w,
                                      im + IP[dm][1] * w, P + w)
                            wb = a1[slits[0]]
                            re, im, P = chR.get(
                                (wb, f), (Fraction(0),
                                          Fraction(0),
                                          Fraction(0)))
                            chR[(wb, f)] = (
                                re + IP[dm][0] * w,
                                im + IP[dm][1] * w, P + w)
                    for f, (re, im, P) in chA.items():
                        a2m = re * re + im * im
                        if a2m == 0 and P > 0:
                            preclude += 1
                        for (wb, ff), (r2, i2, P2) in chR.items():
                            if ff == f and a2m < r2 * r2 + i2 * i2:
                                darken += 1
                                break
    ok = lin_ok and darken > 0 and preclude > 0
    check(f"THE LINEAR DICTIONARY: |amp| = P exactly on every "
          f"fully-read channel ({lin_ok}) -- the coat is "
          f"empirically silent wherever reading is perfect, and "
          f"because floor amplitudes are P-scaled, the coat's "
          f"frequency analogue is |amp|-linear (a quasiprobability "
          f"reading; the Kirkwood-Dirac lineage is engaged in the "
          f"paper, per sweep); THE PATH-MEASURE NO-GO: {darken} "
          f"darkening witnesses (adding a path strictly darkens) "
          f"and {preclude} preclusion witnesses (amp = 0, P > 0) "
          f"-- no nonnegative path measure reproduces coat "
          f"statistics under any reweighting (aggregation "
          f"monotonicity; the no-joint-distribution structure of "
          f"Fine and Feynman's negative-probability discussion, "
          f"cited; Sorkin's quantum-measure hierarchy engaged in "
          f"the paper) ({ok}). Coat-following frequencies require "
          f"actuality at the RECORD level -- which is exactly the "
          f"floor's founding no-selector postulate. The choice of "
          f"actuality measure is a named received input with an "
          f"exact separation table in the paper.", ok)

    print("## 4: the Sorkin hierarchy position (grade-2 check)")
    # Per the blind sweep, the mandatory flank: does the squared
    # measure mu = |amp|^2 satisfy Sorkin's k=3 sum rule (I3 = 0)
    # exactly? Verified on the slit arena's channel triples; also
    # report the LINEAR measure's grade (the two candidate
    # actuality measures sit at different hierarchy positions).
    import math as _math
    i3_ok = True
    lin_i3_nonzero = 0
    n_triples = 0
    for S in bodies(C6, sizes=(2,)):
        for c1 in C6:
            adm1 = admissible(C6, S, c1)
            if not adm1:
                continue
            for c2 in C6:
                N1 = len(adm1)
                chA = {}
                for (a1, E1, d1) in adm1:
                    adm2 = admissible(E1, S, c2)
                    if not adm2:
                        continue
                    N2 = len(adm2)
                    for (a2, E2, d2) in adm2:
                        f = interface(E2, S)
                        w = Fraction(1, N1 * N2)
                        dm = (d1 + d2) % 4
                        re, im = chA.get(f, (Fraction(0),
                                             Fraction(0)))
                        chA[f] = (re + IP[dm][0] * w,
                                  im + IP[dm][1] * w)
                fs = sorted(chA, key=str)
                if len(fs) < 3:
                    continue
                def mu2(idx):
                    re = sum(chA[fs[i]][0] for i in idx)
                    im = sum(chA[fs[i]][1] for i in idx)
                    return re * re + im * im
                def muL(idx):
                    re = sum(chA[fs[i]][0] for i in idx)
                    im = sum(chA[fs[i]][1] for i in idx)
                    return _math.sqrt(float(re * re + im * im))
                for i in range(len(fs)):
                    for j in range(i + 1, len(fs)):
                        for k in range(j + 1, len(fs)):
                            n_triples += 1
                            I3 = (mu2([i, j, k]) - mu2([i, j])
                                  - mu2([i, k]) - mu2([j, k])
                                  + mu2([i]) + mu2([j])
                                  + mu2([k]))
                            if I3 != 0:
                                i3_ok = False
                            L3 = (muL([i, j, k]) - muL([i, j])
                                  - muL([i, k]) - muL([j, k])
                                  + muL([i]) + muL([j])
                                  + muL([k]))
                            if abs(L3) > 1e-9:
                                lin_i3_nonzero += 1
    ok = i3_ok and n_triples > 100
    check(f"Sorkin's k=3 sum rule I3 = 0 holds EXACTLY for the "
          f"squared measure |amp|^2 on all {n_triples} channel "
          f"triples tested ({i3_ok}) -- the coat's squared "
          f"measure sits at grade 2 of Sorkin's interference "
          f"hierarchy, exactly where quantum theory sits (Sorkin "
          f"1994, cited; triple-slit bounds, Sinha et al., "
          f"engaged in the paper); the LINEAR measure |amp| has "
          f"nonzero I3 on {lin_i3_nonzero} triples -- the two "
          f"candidate actuality measures occupy DIFFERENT "
          f"hierarchy grades, sharpening the named door ({ok}).",
          ok)

    print("## 5: the mirror-pair")
    ok_pair = True
    found_bad11 = False
    S = {0, 1}
    for c in C6:
        adm = admissible(C6, S, c)
        if not adm:
            continue
        ch = {}
        for (assign, E2, dev) in adm:
            ch.setdefault(interface(E2, S), []).append(dev)
        for f, devs in ch.items():
            re = sum(IP[d % 4][0] for d in devs)
            im = sum(IP[d % 4][1] for d in devs)
            dre = dim_ = Fraction(0)
            d11re = d11im = Fraction(0)
            for d1 in devs:
                for d2 in devs:
                    dre += IP[(d1 - d2) % 4][0]
                    dim_ += IP[(d1 - d2) % 4][1]
                    d11re += IP[(d1 + d2) % 4][0]
                    d11im += IP[(d1 + d2) % 4][1]
            if (dre, dim_) != (re * re + im * im, Fraction(0)):
                ok_pair = False
            if dre < 0 or dim_ != 0:
                ok_pair = False
            if d11im != 0 or d11re < 0:
                found_bad11 = True
    ok = ok_pair and found_bad11
    check(f"on pairs of runs sharing a record, the conjugate-"
          f"charge pairing equals |amp|^2 channelwise, real and "
          f"nonnegative ({ok_pair}), while the same-charge pairing "
          f"fails positivity somewhere ({found_bad11}) ({ok}). "
          f"Honest algebraic status: the identity is |Sum|^2 "
          f"expanded; the content is uniqueness of the positive "
          f"pairing and the reading -- verification wears the "
          f"conjugate coat.", ok)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
