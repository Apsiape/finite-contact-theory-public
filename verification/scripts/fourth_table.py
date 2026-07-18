#!/usr/bin/env python3
"""Chapter 42: the fourth-floor table (exact).

  T1 P121-1: the sign table on F1.
  T2 P121-2: reveal fragility/persistence on floor four.
"""
import math
from fractions import Fraction
from itertools import product
from fourth_column import (close, threads, make_world,
                           knockouts, apply_ko)

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

IP = [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
      (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))]

def ham(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)

def evolve_traced(q, rels_base, kos):
    out = []
    def rec(rels, theta, i, trace, dev, w):
        if i == len(kos):
            got = close(q, rels)
            if got is None:
                return
            out.append((trace, dev, w, got))
            return
        r2 = apply_ko(rels, kos[i])
        got = close(q, r2)
        if got is None:
            return
        P, R = got
        th = threads(q, P, R)
        if not th:
            return
        rels2 = {k: set(v) for k, v in R.items()}
        if theta in th:
            rec(rels2, theta, i + 1, trace, dev, w)
        else:
            dmin = min(ham(t, theta) for t in th)
            tie = [t for t in th if ham(t, theta) == dmin]
            for t in tie:
                rec(rels2, t, i + 1, trace + ((i, t),),
                    dev + dmin, w * Fraction(1, len(tie)))
    rec({k: set(v) for k, v in rels_base.items()},
        tuple(0 for _ in q), 0, (), 0, Fraction(1))
    return out

def amp(pl):
    re = im = P = Fraction(0)
    for (_, d, w) in pl:
        re += IP[d % 4][0] * w
        im += IP[d % 4][1] * w
        P += w
    return re, im, P

if __name__ == '__main__':
    WORLDS = [("W3", (2, 3, 2), 3), ("W4", (2, 3, 2, 3), 2)]
    cnt_ok = True
    lp = ln = sp = sn = 0
    n_bright = n_frag = n_pers = 0
    for nm, q, depth in WORLDS:
        base = make_world(q)
        kos = knockouts(q)
        for seq in product(kos, repeat=depth):
            paths = evolve_traced(q, base, list(seq))
            bystruct = {}
            for (tr, dev, w, struct) in paths:
                key = (tuple(struct[0]),
                       tuple(sorted(struct[1].items())))
                bystruct.setdefault(key, []).append(
                    (dict(tr), dev, w))
            for key, pl in bystruct.items():
                if len(pl) < 2:
                    continue
                allk = sorted({k for (t, _, _) in pl
                               for k in t})
                und = [k for k in allk
                       if len({t.get(k, 'A')
                               for (t, _, _) in pl}) > 1]
                if not und:
                    continue
                re, im, P = amp(pl)
                a2 = re * re + im * im
                bright = a2 == P * P
                frag = False
                for u in und:
                    br = {}
                    for p in pl:
                        br.setdefault(p[0].get(u, 'A'),
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
                    incL = sum(
                        math.sqrt(float(a[0] * a[0]
                                        + a[1] * a[1]))
                        for a in amps.values())
                    if aL > incL + 1e-12:
                        lp += 1
                    elif aL < incL - 1e-12:
                        ln += 1
                    if bright:
                        for v, b in br.items():
                            if len(b) < 2:
                                frag = True
                            else:
                                r2, i2, P2 = amps[v]
                                if r2 * r2 + i2 * i2 != P2 * P2:
                                    frag = True
                if bright:
                    n_bright += 1
                    if frag:
                        n_frag += 1
                    else:
                        n_pers += 1

    print("## T1: the sign table on F1")
    sig = ("zero" if cnt_ok else "VIOLATED",
           "never-positive" if lp == 0 and ln > 0 else "other",
           "both-signs" if sp and sn else "other")
    ok1 = sig == ("zero", "never-positive", "both-signs")
    check(f"F1 NSIT census: counting exact ({cnt_ok}); linear "
          f"{lp}+/{ln}-; squared {sp}+/{sn}- -> {sig} ({ok1}). "
          f"**THE FOUR-FLOOR INVARIANT: the actuality "
          f"discriminator holds on a floor whose individual "
          f"forks are phase-flat -- the registered package's "
          f"bridge target is any of four dynamics.**", ok1)

    print("## T2: persistence on floor four")
    ok2 = n_bright > 0
    check(f"F1 bright channels: {n_bright} revealable, "
          f"{n_frag} fragile, {n_pers} persist ({ok2}).", ok2)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
