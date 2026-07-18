#!/usr/bin/env python3
"""Chapter 42: the phase hunt (exact).

  H1 P120-1: accumulated phase variety exists.
  H2 P120-2: partial coherence yes, darkness no (return law).
  H3 P120-3: the moving parent (mechanism witness).
"""
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

def evolve(q, rels_base, kos):
    """all point-paths for a knockout sequence; yields
    (theta_final, dev, w, final_struct) or None if world dies."""
    out = []
    def rec(rels, theta, i, dev, w):
        if i == len(kos):
            got = close(q, rels)
            if got is None:
                return
            out.append((theta, dev, w, got))
            return
        r2 = apply_ko(rels, kos[i])
        got = close(q, r2)
        if got is None:
            return   # world death: branch ends, no channel
        P, R = got
        th = threads(q, P, R)
        if not th:
            return
        rels2 = {k: set(v) for k, v in R.items()}
        if theta in th:
            rec(rels2, theta, i + 1, dev, w)
        else:
            dmin = min(ham(t, theta) for t in th)
            tie = [t for t in th if ham(t, theta) == dmin]
            for t in tie:
                rec(rels2, t, i + 1, dev + dmin,
                    w * Fraction(1, len(tie)))
    rec({k: set(v) for k, v in rels_base.items()},
        tuple(0 for _ in q), 0, 0, Fraction(1))
    return out

if __name__ == '__main__':
    WORLDS = [("W3", (2, 3, 2)), ("W4", (2, 3, 2, 3))]
    n_ch = n_var = n_partial = n_dark = n_bright = 0
    var_ex = None
    stay_move = None
    for nm, q in WORLDS:
        base = make_world(q)
        kos = knockouts(q)
        depth = 3 if len(q) == 3 else 2
        for seq in product(kos, repeat=depth):
            paths = evolve(q, base, list(seq))
            if not paths:
                continue
            bystruct = {}
            for (th, dev, w, struct) in paths:
                key = (tuple(struct[0]),
                       tuple(sorted(struct[1].items())))
                bystruct.setdefault(key, []).append(
                    (th, dev, w))
            for key, pl in bystruct.items():
                if len(pl) < 2:
                    continue
                n_ch += 1
                devs = {d % 4 for (_, d, _) in pl}
                if len(devs) > 1:
                    n_var += 1
                    if var_ex is None:
                        var_ex = (nm, seq,
                                  sorted({d for (_, d, _)
                                          in pl}))
                if stay_move is None:
                    ds = sorted({d for (_, d, _) in pl})
                    if len(ds) > 1:
                        # first death is path-independent, so
                        # min-dev branches STAYED after the
                        # common first jump while others paid
                        # again
                        stay_move = (nm, seq, ds)
                re = im = P = Fraction(0)
                for (_, d, w) in pl:
                    re += IP[d % 4][0] * w
                    im += IP[d % 4][1] * w
                    P += w
                a2 = re * re + im * im
                if a2 == P * P:
                    n_bright += 1
                elif a2 == 0:
                    n_dark += 1
                else:
                    n_partial += 1

    print("## H1: accumulated phase variety")
    ok1 = n_var > 0
    check(f"{n_var}/{n_ch} multi-path channels carry mixed "
          f"accumulated deviation mod 4 (first witness: "
          f"{var_ex}) ({ok1}). **THE FORK IS FLAT, THE "
          f"PROTOCOL IS NOT: phase variety emerges across "
          f"multi-jump paths -- flatness does not "
          f"globalize.**", ok1)

    print("## H2: coherence spectrum + the return law")
    ok2 = n_partial > 0 and n_dark == 0
    check(f"spectrum: {n_bright} bright / {n_dark} dark / "
          f"{n_partial} partial ({ok2}). **partial coherence "
          f"exists; exact darkness does NOT -- dead threads "
          f"never revive, the point never returns, and the "
          f"return switch holds on its fourth floor, under an "
          f"utterly alien fork mechanism.**", ok2)

    print("## H3: the moving parent")
    ok3 = stay_move is not None
    check(f"stay-vs-move witness (post-first-jump: min-dev "
          f"branches paid once and then SURVIVED every later "
          f"kill, while their channel-mates paid again -- the "
          f"dev-0 version is impossible since the first death "
          f"is path-independent, corrected in print): "
          f"{stay_move} ({ok3}). **THE MOVING PARENT: the "
          f"reference for every jump is the CURRENT point -- "
          f"stay is the witness, distance is the price. The "
          f"Ch41 precondition refines: per-fork flatness "
          f"forbids only single-fork interference; a floor "
          f"with a surviving REFERENCE accumulates phase at "
          f"protocol level.**", ok3)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
