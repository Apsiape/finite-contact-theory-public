#!/usr/bin/env python3
"""Chapter 6 shipped verification: a measured generative floor.

Dependency-free (standard library only). This file contains BOTH the public
floor engine (an independent, self-contained implementation of the driven
one-use dynamics specified in the chapter) AND the measurement suite that
reproduces the chapter's three measured phenomena:

  T-30  delayed individuation: the drive manufactures adjacency twins and
        the overwhelming majority separate before world end (s-hat high)
  T-31  short-tailed separation waits: twin-separation waits are
        exponential-form (geometric decisively beats the power law)
  T-32  ballistic counterfactual defects: swapping one fork choice (RNG
        stream preserved) produces an edge-set defect whose mass grows
        linearly with subsequent contacts

All observables are COUNTING observables (occupancy, twin censuses, waits
in add-counts, symmetric differences) — nothing is clock-stamped. The engine here is NOT
the private laboratory engine; it is an independent implementation of the
same specified dynamics, which is the point: the phenomena are properties
of the dynamics, not of one codebase.

Dynamics spec (one world, n vertices, complete-graph event space):
  state: a simple graph, initially empty; a fill counter.
  channels, with weights (alpha, gamma, phi, rho) = (1, 6, 0.5, 1):
    add-missing  alpha * (#missing pairs)          — uniform missing pair
    add-fork     gamma * (sum of fork weights)     — missing pair chosen
                 proportionally to its fork weight = #common neighbors
    fill         phi * max(0, triangles - filled)  — increments `filled`
    remove       rho * (#removable edges)          — uniform removable
                 edge; (u, v) is removable iff u or v has a private
                 neighbor (a neighbor other than the partner that is not
                 a common neighbor)
  each step: draw one channel by total weight, apply it; stop after
  E = n(n-1)/2 total add events (the one-use contact budget; deleted pairs
  may be re-added and consume budget, so the final graph is generally NOT
  complete) or on the step cap.
"""
from __future__ import annotations

import itertools
import random

FAILURES: list[str] = []


def check(name: str, ok: bool) -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILURES.append(name)


# ------------------------------------------------------------ the engine --
def run_world(n: int, seed: int, alpha: float = 1.0, gamma: float = 6.0,
              phi: float = 0.5, rho: float = 1.0, max_steps: int = 200000,
              swap_at_fork: int | None = None):
    """Run one world; return (oplog, n_adds).

    oplog entries: ('add', u, v) / ('del', u, v) / ('fill', -1, -1).
    swap_at_fork = k: at the k-th fork event (0-based), after the weighted
    draw, redirect to the closest-fork-weight OTHER candidate (ties broken
    by pair order); every random draw is unchanged, so the two worlds are
    maximally coupled. Returns (oplog, n_adds, swap_add_idx) in this mode
    (swap_add_idx = the add index of the swapped event, or None).
    """
    rng = random.Random(seed)
    adj = [set() for _ in range(n)]
    all_pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    miss = set(all_pairs)
    forkw: dict = {}          # missing pair -> #common neighbors (> 0 only)
    rem: set = set()          # removable present pairs
    tri = 0
    filled = 0
    oplog = []
    fork_events = 0
    swapped = False
    swap_add_idx = None
    E = n * (n - 1) // 2
    adds = 0

    def cn(u: int, v: int) -> int:
        return len(adj[u] & adj[v])

    def removable(u: int, v: int) -> bool:
        common = adj[u] & adj[v]
        pu = adj[u] - common - {v}
        pv = adj[v] - common - {u}
        return bool(pu) or bool(pv)

    def refresh(z: int) -> None:
        for x in range(n):
            if x == z:
                continue
            p = (z, x) if z < x else (x, z)
            if p in miss:
                w = cn(*p)
                if w:
                    forkw[p] = w
                else:
                    forkw.pop(p, None)
            else:
                if removable(*p):
                    rem.add(p)
                else:
                    rem.discard(p)

    def do_add(u: int, v: int) -> None:
        nonlocal tri
        tri += cn(u, v)
        adj[u].add(v)
        adj[v].add(u)
        p = (u, v)
        miss.discard(p)
        forkw.pop(p, None)
        refresh(u)
        refresh(v)
        oplog.append(("add", u, v))

    def do_del(u: int, v: int) -> None:
        nonlocal tri
        adj[u].discard(v)
        adj[v].discard(u)
        tri -= cn(u, v)
        p = (u, v)
        miss.add(p)
        rem.discard(p)
        refresh(u)
        refresh(v)
        oplog.append(("del", u, v))

    steps = 0
    while adds < E and miss and steps < max_steps:
        steps += 1
        w_miss = alpha * len(miss)
        w_fork = gamma * sum(forkw.values())
        w_fill = phi * max(0, tri - filled)
        w_rem = rho * len(rem)
        tot = w_miss + w_fork + w_fill + w_rem
        if tot <= 0:
            break
        r = rng.random() * tot
        if r < w_miss:
            pair = sorted(miss)[rng.randrange(len(miss))]
            do_add(*pair)
            adds += 1
        elif r < w_miss + w_fork:
            items = sorted(forkw.items())
            total_w = sum(w for _, w in items)
            t = rng.random() * total_w
            acc = 0.0
            pair = items[-1][0]
            chosen_w = items[-1][1]
            for p, w in items:
                acc += w
                if t < acc:
                    pair, chosen_w = p, w
                    break
            if (swap_at_fork is not None and not swapped
                    and fork_events == swap_at_fork and len(items) > 1):
                others = [(abs(w - chosen_w), p, w) for p, w in items
                          if p != pair]
                others.sort()
                pair = others[0][1]
                swapped = True
                swap_add_idx = adds
            fork_events += 1
            do_add(*pair)
            adds += 1
        elif r < w_miss + w_fork + w_fill:
            filled += 1
            oplog.append(("fill", -1, -1))
        else:
            pair = sorted(rem)[rng.randrange(len(rem))]
            do_del(*pair)
    n_adds = sum(1 for op in oplog if op[0] == "add")
    if swap_at_fork is not None:
        return oplog, n_adds, swap_add_idx
    return oplog, n_adds


# ------------------------------------------------------- replay utilities --
def replay(n: int, oplog, upto_adds: int | None = None):
    """Graph (list of sets) after the first `upto_adds` add events."""
    adj = [set() for _ in range(n)]
    adds = 0
    for op, u, v in oplog:
        if upto_adds is not None and adds >= upto_adds and op == "add":
            break
        if op == "add":
            adj[u].add(v)
            adj[v].add(u)
            adds += 1
        elif op == "del":
            adj[u].discard(v)
            adj[v].discard(u)
    return adj


def edge_set(adj) -> frozenset:
    return frozenset((u, v) for u in range(len(adj)) for v in adj[u] if u < v)


def distinct_rows(adj) -> int:
    return len({frozenset(adj[i]) for i in range(len(adj))})


def twins(adj) -> set:
    """All raw twin pairs: N(u) == N(v) (necessarily non-adjacent)."""
    n = len(adj)
    out = set()
    for u in range(n):
        for v in range(u + 1, n):
            if adj[u] == adj[v]:
                out.add((u, v))
    return out


# ---------------------------------------------------------------- T-30 --
def twin_census(worlds):
    """One pass over all worlds: twin births, separations, waits (in adds),
    censored count. Raw twins with content: N(u) == N(v), both rows equal,
    nonempty."""
    born_total, separated, censored = 0, 0, 0
    waits = []
    for n, oplog in worlds:
        adj = [set() for _ in range(n)]
        open_tw: dict = {}
        add_idx = 0
        is_twin = lambda a, b: adj[a] == adj[b] and bool(adj[a])
        for op, u, v in oplog:
            if op == "fill":
                continue
            if op == "add":
                adj[u].add(v)
                adj[v].add(u)
                add_idx += 1
            else:
                adj[u].discard(v)
                adj[v].discard(u)
            touched = {u, v}
            for pair in [p for p in open_tw
                         if p[0] in touched or p[1] in touched]:
                if not is_twin(*pair):
                    separated += 1
                    waits.append(max(1, add_idx - open_tw[pair]))
                    del open_tw[pair]
            for z in (u, v):
                for x in range(n):
                    if x == z:
                        continue
                    p2 = (z, x) if z < x else (x, z)
                    if p2 not in open_tw and is_twin(*p2):
                        open_tw[p2] = add_idx
                        born_total += 1
        censored += len(open_tw)
    return born_total, separated, censored, waits


def t30_delayed_individuation(census) -> None:
    born_total, separated, censored, _ = census
    s_hat = separated / born_total if born_total else 0.0
    check("T-30 delayed individuation: the drive manufactures twins "
          f"(pooled births = {born_total}) and they overwhelmingly "
          f"separate before world end: s-hat = {s_hat:.3f} (fence: "
          f"> 0.75), censored = {censored} "
          f"({100 * censored / max(1, born_total):.1f}%)",
          born_total > 0 and s_hat > 0.75)


def t31_wait_law(census) -> None:
    """Separation waits: geometric (exponential-form) vs discrete power law,
    both by maximum likelihood on the uncensored waits."""
    import math
    _, _, _, waits = census
    n_w = len(waits)
    mean_w = sum(waits) / n_w
    p_hat = 1.0 / mean_w
    ll_geom = sum((w - 1) * math.log(1 - p_hat) + math.log(p_hat)
                  for w in waits) if p_hat < 1 else         sum(math.log(p_hat) for w in waits)
    # discrete power law P(w) ~ w^-a on 1..W_cap, MLE by grid search
    w_cap = max(waits) * 10
    best_ll, best_a = -float("inf"), None
    a = 1.05
    while a <= 6.0:
        z = sum(k ** (-a) for k in range(1, w_cap + 1))
        ll = sum(-a * math.log(w) - math.log(z) for w in waits)
        if ll > best_ll:
            best_ll, best_a = ll, a
        a += 0.05
    delta = ll_geom - best_ll
    check("T-31 short-tailed separation waits: geometric MLE (p = "
          f"{p_hat:.3f}, mean wait {mean_w:.1f} adds) beats the best "
          f"discrete power law (a = {best_a:.2f}) by Delta-LL = "
          f"{delta:.1f} over {n_w} uncensored waits (fence: Delta-LL > "
          "10, decisive) -- separation is a short-tailed process, not a "
          "scale-free one", delta > 10)


# ---------------------------------------------------------------- T-32 --
def t32_ballistic_defect(n: int, seeds, swap_at: int, horizon: int) -> None:
    ks, means = [], []
    per_seed = {}
    for seed in seeds:
        base_log, base_adds = run_world(n, seed)
        pert_log, pert_adds, swap_idx = run_world(n, seed,
                                                  swap_at_fork=swap_at)
        assert swap_idx is not None, "no fork event reached the swap index"
        upto = min(base_adds, pert_adds)
        series = []
        for k in range(0, horizon + 1, 5):
            m = min(upto, swap_idx + 1 + k)
            e1 = edge_set(replay(n, base_log, upto_adds=m))
            e2 = edge_set(replay(n, pert_log, upto_adds=m))
            series.append(len(e1 ^ e2))
        per_seed[seed] = series
    npts = len(range(0, horizon + 1, 5))
    ks = list(range(0, horizon + 1, 5))
    means = [sum(per_seed[s][i] for s in seeds) / len(seeds)
             for i in range(npts)]
    # least-squares linear fit + R^2
    xb = sum(ks) / npts
    yb = sum(means) / npts
    sxx = sum((x - xb) ** 2 for x in ks)
    sxy = sum((x - xb) * (y - yb) for x, y in zip(ks, means))
    slope = sxy / sxx
    ss_res = sum((y - (yb + slope * (x - xb))) ** 2
                 for x, y in zip(ks, means))
    ss_tot = sum((y - yb) ** 2 for y in means)
    r2 = 1 - ss_res / ss_tot if ss_tot else 0.0
    check("T-32 ballistic counterfactual defect: one swapped fork choice "
          "(RNG stream preserved) yields a defect mass growing linearly "
          f"with subsequent contacts -- mean |Delta| at k = {ks} is "
          f"{[round(m, 1) for m in means]}, linear fit slope = "
          f"{slope:.2f} edges/add with R^2 = {r2:.3f} "
          "(fences: slope > 0.3, R^2 > 0.90, monotone start-to-end)",
          slope > 0.3 and r2 > 0.90 and means[-1] > means[0])


def main() -> int:
    # grow the world set (two sizes, fixed seeds)
    worlds = []
    for n, seeds in ((32, range(10)), (40, range(8))):
        for seed in seeds:
            oplog, n_adds = run_world(n, seed)
            assert n_adds == n * (n - 1) // 2, "one-use budget not consumed"
            worlds.append((n, oplog))
    print(f"grew {len(worlds)} worlds (n = 32 x10, n = 40 x8); the full "
          "one-use contact budget E = n(n-1)/2 consumed in every world")
    census = twin_census(worlds)
    t30_delayed_individuation(census)
    t31_wait_law(census)
    t32_ballistic_defect(32, range(6), swap_at=40, horizon=60)
    print("=" * 70)
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILURE(S)")
        return 1
    print("RESULT: ALL CHAPTER-6 CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
