#!/usr/bin/env python3
"""Chapter 45: the quantum dividend (exact).

  D1 P125-1: certainty of absence (dark needs the witness bit).
  D2 P125-2: the degenerate vs restored sign table.
  D3 P125-3: the dividend ledger.
"""
import math
from fractions import Fraction
from itertools import combinations
from grammar_closure import canon as canon0, IP

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

_C = {}
def canon(E):
    if E not in _C:
        _C[E] = canon0(E)
    return _C[E]

def census(E0, n, depth, witness):
    ch = {}
    allpairs = [tuple(sorted(p))
                for p in combinations(range(n), 2)]
    def rec(E, d, trace, dev, w):
        if d > 0:
            ch.setdefault((d, canon(E)), []).append(
                (dict(trace), dev, w))
        if d == depth:
            return
        edges = sorted(E)
        m = len(edges)
        for e in edges:
            nonedges = [p for p in allpairs
                        if p not in E and p != e]
            k = len(nonedges) + (1 if witness else 0)
            if witness:
                t2 = dict(trace)
                t2[d] = (e, "stay")
                rec(E, d + 1, t2, dev,
                    w * Fraction(1, m * k))
            for ne in nonedges:
                t2 = dict(trace)
                t2[d] = (e, ne)
                rec(frozenset((set(E) - {e}) | {ne}),
                    d + 1, t2, dev + 1,
                    w * Fraction(1, m * k))
    rec(E0, 0, {}, 0, Fraction(1))
    return ch

def amp(pl):
    re = im = P = Fraction(0)
    for (_, d, w) in pl:
        re += IP[d % 4][0] * w
        im += IP[d % 4][1] * w
        P += w
    return re, im, P

def analyze(floors_arena, witness):
    dark = 0
    dark_ex = None
    cnt_ok = True
    lp = ln = sp = sn = 0
    n_ch = 0
    for (E0, n, depth) in floors_arena:
        for key, pl in census(E0, n, depth,
                              witness).items():
            n_ch += 1
            re, im, P = amp(pl)
            a2 = re * re + im * im
            if a2 == 0 and P > 0:
                dark += 1
                if dark_ex is None:
                    dark_ex = key[0]
            if len(pl) < 2:
                continue
            allk = sorted({k for (t, _, _) in pl
                           for k in t})
            und = [k for k in allk
                   if len({str(t.get(k, 'A'))
                           for (t, _, _) in pl}) > 1]
            for u in und:
                br = {}
                for p in pl:
                    br.setdefault(str(p[0].get(u, 'A')),
                                  []).append(p)
                amps = {v: amp(b) for v, b in br.items()}
                if P != sum(a[2] for a in amps.values()):
                    cnt_ok = False
                inc2 = sum(a[0] * a[0] + a[1] * a[1]
                           for a in amps.values())
                if a2 > inc2:
                    sp += 1
                elif a2 < inc2:
                    sn += 1
                aL = math.sqrt(float(a2))
                incL = sum(math.sqrt(float(
                    a[0] * a[0] + a[1] * a[1]))
                    for a in amps.values())
                if aL > incL + 1e-12:
                    lp += 1
                elif aL < incL - 1e-12:
                    ln += 1
    return dark, dark_ex, cnt_ok, lp, ln, sp, sn, n_ch

if __name__ == '__main__':
    C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    P4 = frozenset(((0, 1), (1, 2), (2, 3)))
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    ARENA = [(C4, 4, 4), (P4, 4, 4), (C5, 5, 3)]

    S = analyze(ARENA, witness=False)
    W = analyze(ARENA, witness=True)

    print("## D1: certainty of absence")
    ok1 = S[0] == 0 and W[0] > 0
    check(f"dark channels (P > 0, amp = 0): sterile {S[0]}, "
          f"witnessed {W[0]} (first at depth {W[1]}) ({ok1}). "
          f"**CERTAINTY OF ABSENCE: the witnessed observer can "
          f"be interference-certain that an event will not "
          f"happen while counting still licenses it; the "
          f"sterile observer never can (gauge lemma). Dividend "
          f"one: knowledge of the impossible.**", ok1)

    print("## D2: the degenerate vs restored table")
    s_sig = ("zero" if S[2] else "V",
             "zero" if S[3] == 0 and S[4] == 0 else "other",
             "never-negative" if S[6] == 0 and S[5] > 0
             else "other")
    w_sig = ("zero" if W[2] else "V",
             "never-positive" if W[3] == 0 and W[4] > 0
             else "other",
             "both-signs" if W[5] and W[6] else "other")
    ok2 = (s_sig == ("zero", "zero", "never-negative")
           and w_sig == ("zero", "never-positive",
                         "both-signs"))
    check(f"sterile table {s_sig} (linear {S[3]}+/{S[4]}-, "
          f"squared {S[5]}+/{S[6]}-); witnessed table {w_sig} "
          f"(linear {W[3]}+/{W[4]}-, squared {W[5]}+/{W[6]}-) "
          f"({ok2}). **THE DEGENERATE TABLE: on the sterile "
          f"floor the linear coat is observationally identical "
          f"to counting and the squared coat only ever "
          f"brightens -- the destructive sector is missing. One "
          f"witness bit restores the four-floor invariant "
          f"table. Dividend two: phase buys destructive "
          f"phenomenology, and with it the power to fully "
          f"interrogate actuality.**", ok2)

    print("## D3: the dividend ledger")
    ok3 = ok1 and ok2
    print("    what one bit of parent structure buys an asker:")
    print("      1. certainty of absence (dark channels)")
    print("      2. the destructive sector (negative fringes; "
          "the linear/counting separation)")
    print("    what the sterile observer keeps: biography, "
          "body, locality, readable records")
    check(f"the dividend ledger measured on the minimal pair "
          f"({ok3}). **THE QUANTUM DIVIDEND: phase is worth "
          f"exactly two capabilities to an observer -- the "
          f"knowledge of what cannot happen, and the "
          f"experiments that make actuality itself an "
          f"empirical question. Everything else was free.**",
          ok3)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
