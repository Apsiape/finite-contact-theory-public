#!/usr/bin/env python3
"""Chapter 35: the actuality protocol (exact).

  A1 P109-1: counting satisfies NSIT everywhere.
  A2 P109-2: the sign separation (zero / one-signed / two-signed).
  A3 P109-3: the triple test (grades, protocol-usable).
  A4 P109-4: the registered package (frozen tables).
"""
from itertools import combinations, product
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
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                    (0, 5)))
    PRISM = frozenset(((0, 1), (1, 2), (0, 2), (3, 4), (4, 5),
                       (3, 5), (0, 3), (1, 4), (2, 5)))
    def bodies(E, n=6):
        out = []
        for S in combinations(range(n), 2):
            if induced(E, set(S)):
                out.append(set(S))
        return out

    print("## A1+A2: NSIT and the sign separation")
    count_ok = True
    lin_pos = 0
    lin_neg = 0
    sq_pos = 0
    sq_neg = 0
    n_ch = 0
    for E0 in (C6, PRISM):
        for S in bodies(E0):
            for c1 in E0:
                adm1 = admissible(E0, S, c1)
                if not adm1:
                    continue
                sing1 = contact_singles(E0, *c1)
                slits = [u for u in sing1 if u not in S]
                if not slits:
                    continue
                u = slits[0]
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
                            wb = a1[u]
                            re, im, P = chR.get(
                                (wb, f), (Fraction(0),
                                          Fraction(0),
                                          Fraction(0)))
                            chR[(wb, f)] = (
                                re + IP[dm][0] * w,
                                im + IP[dm][1] * w, P + w)
                    for f, (re, im, P) in chA.items():
                        n_ch += 1
                        Psum = Fraction(0)
                        inc2 = Fraction(0)
                        incL = 0.0
                        for (wb, ff), (r2, i2, P2) in chR.items():
                            if ff != f:
                                continue
                            Psum += P2
                            inc2 += r2 * r2 + i2 * i2
                            incL += math.sqrt(
                                float(r2 * r2 + i2 * i2))
                        # counting NSIT:
                        if P != Psum:
                            count_ok = False
                        # squared NSIT sign:
                        a2m = re * re + im * im
                        if a2m > inc2:
                            sq_pos += 1
                        elif a2m < inc2:
                            sq_neg += 1
                        # linear NSIT sign (|sum| vs sum| |):
                        aL = math.sqrt(float(a2m))
                        if aL > incL + 1e-12:
                            lin_pos += 1
                        elif aL < incL - 1e-12:
                            lin_neg += 1
    ok1 = count_ok
    check(f"COUNTING SATISFIES NSIT: the unread distribution "
          f"equals the read marginal exactly on all {n_ch} "
          f"channels ({ok1}). **classical statistics never notice "
          f"the reading -- counting-actuality is the macrorealist "
          f"candidate (Leggett-Garg NIM / Kofler-Brukner NSIT, "
          f"engaged).**", ok1)
    ok2 = (lin_pos == 0 and lin_neg > 0
           and sq_pos > 0 and sq_neg > 0)
    check(f"THE SIGN SEPARATION: linear-coat NSIT violations: "
          f"{lin_pos} positive / {lin_neg} negative (never "
          f"positive -- the triangle inequality: in the linear "
          f"reading, forgetting only darkens); squared-coat: "
          f"{sq_pos} positive / {sq_neg} negative (BOTH signs -- "
          f"constructive fringes) ({ok2}). **an exact three-way "
          f"discriminator: zero / one-signed / two-signed. Any "
          f"substrate showing a POSITIVE NSIT violation kills "
          f"both counting- and linear-actuality in one "
          f"measurement.**", ok2)

    print("## A3: the triple test")
    # squared I3 = 0 exact everywhere; search protocols for a
    # linear-I3 witness:
    ok_sq = True
    lin_wit = 0
    wit_protocol = None
    for E0 in (C6, PRISM):
        for S in bodies(E0):
            for c1 in E0:
                adm1 = admissible(E0, S, c1)
                if not adm1:
                    continue
                for c2 in E0:
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
                    def m2(idx):
                        re = sum(chA[fs[i]][0] for i in idx)
                        im = sum(chA[fs[i]][1] for i in idx)
                        return re * re + im * im
                    def mL(idx):
                        return math.sqrt(float(m2(idx)))
                    for i in range(len(fs)):
                        for j in range(i + 1, len(fs)):
                            for k in range(j + 1, len(fs)):
                                I3 = (m2([i, j, k])
                                      - m2([i, j]) - m2([i, k])
                                      - m2([j, k]) + m2([i])
                                      + m2([j]) + m2([k]))
                                if I3 != 0:
                                    ok_sq = False
                                L3 = (mL([i, j, k])
                                      - mL([i, j]) - mL([i, k])
                                      - mL([j, k]) + mL([i])
                                      + mL([j]) + mL([k]))
                                if abs(L3) > 1e-9:
                                    lin_wit += 1
                                    if wit_protocol is None:
                                        wit_protocol = (
                                            sorted(S), c1, c2,
                                            f"L3~{L3:.5f}")
    ok3 = ok_sq and lin_wit > 0
    check(f"THE TRIPLE TEST across all depth-2 protocols: "
          f"squared-coat I3 = 0 exactly on every channel triple "
          f"({ok_sq}; grade 2, quantum's grade); linear-coat "
          f"I3 != 0 on {lin_wit} triples (first witness: "
          f"{wit_protocol}); counting I3 = 0 (additive) ({ok3}). "
          f"**a triple-slit-type experiment separates linear "
          f"from squared: nonzero third-order interference is "
          f"linear-actuality's signature (Sinha-type bounds "
          f"engaged in the paper).**", ok3)

    print("## A4: the registered package (frozen)")
    # the refusal table on the maximal-divergence protocol:
    S = {0, 1}
    c = (0, 1)
    adm1 = admissible(C6, S, c)
    N1 = len(adm1)
    chT = {}
    for (a1, E1, d1) in adm1:
        adm2 = admissible(E1, S, c)
        if not adm2:
            continue
        N2 = len(adm2)
        for (a2, E2, d2) in adm2:
            f = interface(E2, S)
            w = Fraction(1, N1 * N2)
            dm = (d1 + d2) % 4
            re, im, P = chT.get(f, (Fraction(0), Fraction(0),
                                    Fraction(0)))
            chT[f] = (re + IP[dm][0] * w, im + IP[dm][1] * w,
                      P + w)
    totP = sum(v[2] for v in chT.values())
    tot2 = sum(v[0] * v[0] + v[1] * v[1] for v in chT.values())
    table = []
    for f, (re, im, P) in sorted(chT.items(), key=str):
        a2 = re * re + im * im
        table.append((str(P / totP), str(a2 / tot2)))
    counting_col = sorted(t[0] for t in table)
    coat_col = sorted(t[1] for t in table)
    ok4 = (counting_col == ['1/4'] * 4
           and coat_col == ['0', '0', '0', '1'])
    check(f"THE REFUSAL TABLE frozen (C6 body {{0,1}}, the "
          f"internal contact fired twice): counting = "
          f"{counting_col}, squared coat = {coat_col} ({ok4}). "
          f"**THE REGISTERED PACKAGE: three exact tables (P1 the "
          f"refusal 1/4x4 vs 0,1,0,0; P2 the NSIT sign table "
          f"zero/one-signed/two-signed; P3 the triple table "
          f"0/nonzero/0), with kill conditions per candidate and "
          f"the bridge premises named OPEN: no physical substrate "
          f"for the genesis dynamics is currently identified -- "
          f"this package is an exact target suite awaiting its "
          f"bridge, stated plainly, in the tradition of the "
          f"program's registered conditional protocols.**", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
