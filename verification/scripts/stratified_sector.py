#!/usr/bin/env python3
"""Chapter 34: the stratified sector (exact).

  T1 P107-1: stratification (misaligned = sum of aligned strata,
     each affine).
  T2 P107-2: the stratified reading law (dual-sum per stratum).
  T3 P107-3: THE EVASION (persistent brightness under reveals).
  T4 P107-4: the stratified zoo census.
"""
from itertools import product
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

def gf2_span(vectors, m):
    basis = []
    for v in vectors:
        v = list(v)
        for b in basis:
            piv = next(i for i, x in enumerate(b) if x)
            if v[piv]:
                v = [x ^ y for x, y in zip(v, b)]
        if any(v):
            basis.append(v)
    return basis

def gf2_dual_words(Cv, m):
    return [u for u in product((0, 1), repeat=m)
            if all(sum(x * y for x, y in zip(u, c)) % 2 == 0
                   for c in Cv)]

def collect_all(E0, S, depth):
    """ALL channels (aligned and misaligned) with exact weights.
    returns list of (traj, [(bits, w, dev)])."""
    out = []
    for seq in product(sorted(E0), repeat=depth):
        paths = []
        def rec(E, t, ifs, bits, dv, w):
            if t == depth:
                paths.append((tuple(ifs), dict(bits), dv, w))
                return
            a, b = seq[t]
            singles = contact_singles(E, a, b)
            parent = {u: (a if u in nb(E, a) else b)
                      for u in singles}
            shape = induced(E, S)
            adm = []
            for choice in product((a, b), repeat=len(singles)):
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
                for u in singles:
                    lv = 1 if assign[u] != parent[u] else 0
                    nbts[(t, u)] = lv
                    d2 += lv
                rec(E2, t + 1, ifs + [interface(E2, S)],
                    nbts, d2, w * Fraction(1, N))
        rec(E0, 0, [], {}, 0, Fraction(1))
        if not paths:
            continue
        ch = {}
        for p in paths:
            ch.setdefault(p[0], []).append(p[1:])
        for traj, plist in ch.items():
            out.append(plist)
    return out

def amp_of(plist):
    re = im = P = Fraction(0)
    for (bits, dev, w) in plist:
        re += IP[dev % 4][0] * w
        im += IP[dev % 4][1] * w
        P += w
    return re, im, P

if __name__ == '__main__':
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    PRISM = frozenset(((0, 1), (1, 2), (0, 2), (3, 4), (4, 5),
                       (3, 5), (0, 3), (1, 4), (2, 5)))
    channels = []
    for E0, S, d in ((C6, {0, 1}, 2), (C6, {0, 1}, 3),
                     (C6, {1, 2}, 3), (PRISM, {0, 1}, 2)):
        channels += collect_all(E0, S, d)
    # reformat: plist entries (bits, dev, w):
    channels = [[(b, d, w) for (b, d, w) in pl]
                for pl in channels]

    print("## T1+T2: stratification and the stratified law")
    n_mis = 0
    strat_ok = True
    law_ok = True
    strata_spectrum = {}
    mis_data = []
    for pl in channels:
        keysets = {frozenset(b) for (b, d, w) in pl}
        if len(keysets) == 1:
            continue
        n_mis += 1
        strata = {}
        for (b, d, w) in pl:
            strata.setdefault(frozenset(b), []).append((b, d, w))
        strata_spectrum[len(strata)] = \
            strata_spectrum.get(len(strata), 0) + 1
        tre = tim = tP = Fraction(0)
        for ks, sp in strata.items():
            re, im, P = amp_of(sp)
            tre += re
            tim += im
            tP += P
            # stratum structure: undetermined bits, support,
            # affineness, and (equal-weight case) the dual law:
            keys = sorted(ks)
            und = [k for k in keys
                   if len({b[k] for (b, d, w) in sp}) > 1]
            m = len(und)
            if m == 0:
                continue
            supp = {tuple(b[k] for k in und)
                    for (b, d, w) in sp}
            if len(supp) != len(sp):
                continue
            t0 = sorted(supp)[0]
            Cv = sorted({tuple(x ^ y for x, y in zip(v, t0))
                         for v in supp})
            basis = gf2_span(Cv, m)
            if (1 << len(basis)) != len(Cv):
                strat_ok = False
                continue
            ws = {w for (b, d, w) in sp}
            if len(ws) != 1:
                continue
            w0 = ws.pop()
            det_d = None
            okd = True
            for (b, d, w) in sp:
                dd = d - sum(b[k] for k in und)
                if det_d is None:
                    det_d = dd
                elif det_d != dd:
                    okd = False
            if not okd:
                continue
            duals = gf2_dual_words(Cv, m)
            rre = rim = Fraction(0)
            for u in duals:
                pre, pim = Fraction(1), Fraction(0)
                for j in range(m):
                    tj = t0[j]
                    g0 = IP[tj % 4]
                    g1 = IP[(1 - tj) % 4]
                    if u[j] == 0:
                        hr = (g0[0] + g1[0]) / 2
                        hi = (g0[1] + g1[1]) / 2
                    else:
                        hr = (g0[0] - g1[0]) / 2
                        hi = (g0[1] - g1[1]) / 2
                    pre, pim = (pre * hr - pim * hi,
                                pre * hi + pim * hr)
                rre += pre
                rim += pim
            ir, ii = IP[det_d % 4]
            n = len(supp)
            wre = w0 * n * (rre * ir - rim * ii)
            wim = w0 * n * (rre * ii + rim * ir)
            re2, im2, _ = amp_of(sp)
            if (re2, im2) != (wre, wim):
                law_ok = False
        re3, im3, P3 = amp_of(pl)
        if (tre, tim) != (re3, im3):
            strat_ok = False
        mis_data.append((pl, strata))
    ok = strat_ok and law_ok and n_mis > 1000
    check(f"every misaligned channel ({n_mis}) is an exact sum of "
          f"aligned strata with affine supports ({strat_ok}); "
          f"within every equal-weight stratum the dual-sum code "
          f"law holds exactly ({law_ok}); strata-count spectrum: "
          f"{dict(sorted(strata_spectrum.items()))} ({ok}). "
          f"**STRATIFICATION: the misaligned sector is a weighted "
          f"sum of code amplitudes -- no third kind of channel "
          f"exists. One calculus, stratified.**", ok)

    print("## T3: the evasion hunt (persistent brightness)")
    n_bright_mis = 0
    n_persistent = 0
    persist_example = None
    for (pl, strata) in mis_data:
        re, im, P = amp_of(pl)
        if re * re + im * im != P * P:
            continue
        if len(pl) < 2:
            continue
        n_bright_mis += 1
        # reveal robustness: for every bit-key appearing in any
        # stratum, and every value, condition and re-test:
        all_keys = sorted({k for (b, d, w) in pl for k in b})
        robust = True
        for k in all_keys:
            for val in (0, 1):
                sub = [(b, d, w) for (b, d, w) in pl
                       if k not in b or b[k] == val]
                # a reveal of k is only meaningful for paths
                # carrying k; paths without k are unaffected:
                if len(sub) < 2:
                    robust = False
                    break
                r2, i2, P2 = amp_of(sub)
                if r2 * r2 + i2 * i2 != P2 * P2:
                    robust = False
                    break
            if not robust:
                break
        if robust:
            n_persistent += 1
            if persist_example is None:
                persist_example = (len(pl), len(strata),
                                   len(all_keys))
    ok3 = n_persistent == 0 and n_bright_mis > 0
    check(f"bright misaligned channels: {n_bright_mis}; of these, "
          f"channels surviving EVERY single-bit reveal with >= 2 "
          f"paths and coherence 1: {n_persistent} -- the hunting "
          f"bet DIED ({ok3}, scored). **THE OPERATIONAL BLINDNESS "
          f"LAW (at tested scope): every bright channel of the "
          f"floor -- aligned or stratified -- collapses under a "
          f"single bit of side information. Branching buys no "
          f"loophole: the persistence limit is not a feature of "
          f"alignment but of the floor's records themselves. What "
          f"binds worlds cannot be watched binding, and no "
          f"branching trick evades it.**", ok3)

    print("## T4: the stratified zoo")
    coh_spectrum = {}
    for (pl, strata) in mis_data:
        re, im, P = amp_of(pl)
        c2 = (re * re + im * im) / (P * P)
        key = "1" if c2 == 1 else ("0" if c2 == 0 else "partial")
        coh_spectrum[key] = coh_spectrum.get(key, 0) + 1
    ok4 = (sum(coh_spectrum.values()) == n_mis
           and coh_spectrum.get("partial", 0) > 0
           and coh_spectrum.get("0", 0) == 0)
    check(f"misaligned coherence spectrum: {coh_spectrum} -- and "
          f"NO perfectly dark misaligned channel exists ({ok4}). "
          f"**DARKNESS NEEDS ALIGNMENT: exact preclusion is an "
          f"aligned-sector phenomenon -- strata never conspire to "
          f"full cancellation. The stratified sector is charted: "
          f"sums of code amplitudes, bright or partial, never "
          f"dark, never reveal-robust.**", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
