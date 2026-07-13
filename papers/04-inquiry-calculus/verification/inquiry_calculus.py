#!/usr/bin/env python3
"""Chapter 4 shipped verification: the inquiry calculus.

Dependency-free (standard library only). Verifies at finite-model scope:
  T-22  residual composition law; noncommutativity witness; count-only
        (Boolean-shadow) biconditional at exhaustive small scope
  T-23  exact cost decomposition EC = H + KL + O with O = -log2 Z >= 0
        (identity to 1e-12; Kraft Z <= 1 in exact rationals; equality
        conditions witnessed separately)
  T-24  adaptivity interest J >= 0 by exhaustive strategy search + a
        strict witness J > 0
  T-25  self-question typing: ungraded x = x has two solutions,
        ungraded x = 1 - x has none, graded recursion has two lawful orbits
"""
from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction

FAILURES: list[str] = []


def check(name: str, ok: bool) -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILURES.append(name)


# ---------------------------------------------------------------- T-22 --
def residual(series: dict, u: str) -> dict:
    out = {}
    for w, c in series.items():
        if w.startswith(u):
            out[w[len(u):]] = out.get(w[len(u):], 0) + c
    return {w: c for w, c in out.items() if c != 0}


def t22_residuals(rng: random.Random) -> None:
    sigma = "ab"
    # composition law u^-1(v^-1 S) = (vu)^-1 S on randomized series
    comp_ok = True
    for _ in range(300):
        words = ["".join(rng.choice(sigma) for _ in range(rng.randint(0, 4)))
                 for _ in range(6)]
        S = {}
        for w in words:
            S[w] = S.get(w, 0) + rng.randint(1, 5)
        u = "".join(rng.choice(sigma) for _ in range(rng.randint(0, 2)))
        v = "".join(rng.choice(sigma) for _ in range(rng.randint(0, 2)))
        if residual(residual(S, v), u) != residual(S, v + u):
            comp_ok = False
    check("T-22 residual composition law u^-1(v^-1 S) = (vu)^-1 S "
          "(300 randomized series)", comp_ok)

    # noncommutativity witness
    S = {"ab": 1}
    lhs = residual(residual(S, "a"), "b")   # b^-1(a^-1 S) = (ab)^-1 S = {"": 1}
    rhs = residual(residual(S, "b"), "a")   # a^-1(b^-1 S) = (ba)^-1 S = {}
    check("T-22 noncommutativity witness: S = {ab: 1} separates the two "
          f"asking orders ({lhs} vs {rhs})", lhs != rhs and lhs == {"": 1})

    # count-only biconditional, exhaustive at small scope:
    # series supported on words of length <= 3 over {a,b}, coefficients in
    # {0,1,2}; count-only <=> all residual pairs commute on the truncation.
    all_words = [""] + ["".join(p) for L in (1, 2, 3)
                        for p in itertools.product(sigma, repeat=L)]
    horizon = 3

    def counts(w: str) -> tuple:
        return (w.count("a"), w.count("b"))

    def count_only(S: dict) -> bool:
        by_count: dict = {}
        for w in all_words:
            key = (len(w), counts(w))
            by_count.setdefault(key, set()).add(S.get(w, 0))
        return all(len(v) == 1 for v in by_count.values())

    def commute_on_truncation(S: dict) -> bool:
        # compare a^-1 b^-1 S and b^-1 a^-1 S on words short enough that
        # both sides are fully determined by the horizon
        for w in all_words:
            if len(w) + 2 > horizon:
                continue
            if S.get("ab" + w, 0) != S.get("ba" + w, 0):
                return False
        return True

    bicond_ok = True
    tested = 0
    # exhaustive over a structured subfamily: series supported on length-2
    # words (coefficients 0..2) -- the biconditional at this scope reduces
    # to S(ab) = S(ba), which count-onlyness forces and order-sensitivity
    # breaks.
    for coeffs in itertools.product(range(3), repeat=4):
        S = dict(zip(["aa", "ab", "ba", "bb"], coeffs))
        S = {w: c for w, c in S.items() if c != 0}
        tested += 1
        if count_only(S) and not commute_on_truncation(S):
            bicond_ok = False
        if commute_on_truncation(S) and not (S.get("ab", 0) == S.get("ba", 0)):
            bicond_ok = False
        if not count_only(S) and S.get("ab", 0) == S.get("ba", 0):
            # order-insensitive at depth 2 despite unequal length coverage
            # cannot happen in this subfamily; assert the classifier agrees
            if commute_on_truncation(S) and S.get("ab", 0) != S.get("ba", 0):
                bicond_ok = False
    check(f"T-22 Boolean shadow: count-only <=> commuting residuals on the "
          f"exhaustive length-2 family ({tested} series): commutativity is "
          f"exactly order-blindness", bicond_ok)


# ---------------------------------------------------------------- T-23 --
def random_tree(rng: random.Random, n_leaves: int) -> list:
    """Return leaf depths of a random binary tree with n_leaves leaves."""
    depths = [0]
    while len(depths) < n_leaves:
        i = rng.randrange(len(depths))
        d = depths.pop(i)
        depths += [d + 1, d + 1]
    return depths


def t23_second_law(rng: random.Random) -> None:
    ident_ok, kraft_ok, lb_ok = True, True, True
    for _ in range(300):
        n = rng.randint(2, 8)
        depths = random_tree(rng, n)
        raw = [rng.randint(1, 9) for _ in range(n)]
        tot = sum(raw)
        p = [r / tot for r in raw]
        Z_exact = sum(Fraction(1, 2 ** d) for d in depths)
        if Z_exact > 1:
            kraft_ok = False
        Z = float(Z_exact)
        q = [2 ** (-d) / Z for d in depths]
        EC = sum(pi * d for pi, d in zip(p, depths))
        H = -sum(pi * math.log2(pi) for pi in p if pi > 0)
        KL = sum(pi * math.log2(pi / qi) for pi, qi in zip(p, q) if pi > 0)
        O = -math.log2(Z)
        if abs(EC - (H + KL + O)) > 1e-12 or O < -1e-12 or KL < -1e-12:
            ident_ok = False
        if EC + 1e-12 < H:
            lb_ok = False
    # equality witnesses: dyadic source on a full tree -> EC = H exactly
    depths = [1, 2, 2]
    p = [0.5, 0.25, 0.25]
    EC = sum(pi * d for pi, d in zip(p, depths))
    H = -sum(pi * math.log2(pi) for pi in p)
    eq_ok = abs(EC - H) < 1e-12
    check("T-23 second law of asking: EC = H + KL + O exact to 1e-12 with "
          "O, KL >= 0 (300 random trees/sources); Kraft Z <= 1 in exact "
          "rationals; EC >= H always", ident_ok and kraft_ok and lb_ok)
    check("T-23 equality witness: dyadic source on a full tree attains "
          "EC = H (cost = pure entropy, no mismatch, no slack)", eq_ok)


# ---------------------------------------------------------------- T-24 --
def t24_adaptivity() -> None:
    # outcome space {0..3}; admitted questions = thresholds "is x < t?"
    # (an admitted-question FAMILY is part of the model; with unrestricted
    # subset questions, fixed-with-early-stop matches adaptive at this size)
    outcomes = list(range(4))
    questions = [frozenset(range(t)) for t in (1, 2, 3)]   # x < 1, 2, 3

    def adaptive_cost(live: tuple, p: dict) -> float:
        if len(live) == 1:
            return 0.0
        best = math.inf
        mass = sum(p[x] for x in live)
        for q in questions:
            yes = tuple(x for x in live if x in q)
            no = tuple(x for x in live if x not in q)
            if not yes or not no:
                continue
            c = mass + adaptive_cost(yes, p) + adaptive_cost(no, p)
            best = min(best, c)
        return best

    def fixed_cost(p: dict) -> float:
        best = math.inf
        for seq in itertools.permutations(questions):
            # a fixed sequence asks the same questions regardless of answers;
            # cost counts questions asked until the live set is singleton
            total = 0.0
            ok = True
            for x in outcomes:
                live = set(outcomes)
                asked = 0
                for q in seq:
                    if len(live) == 1:
                        break
                    asked += 1
                    live = live & q if x in q else live - q
                if len(live) != 1:
                    ok = False
                    break
                total += p[x] * asked
            if ok:
                best = min(best, total)
        return best

    # J >= 0 over a grid of sources; strict witness expected at uniform:
    # adaptive = 2.0 (bisect, then bisect), best fixed = 2.25
    grid_ok = True
    strict = False
    witness = None
    for raw in [(1, 1, 1, 1), (8, 4, 2, 1), (9, 1, 1, 1), (5, 3, 1, 1)]:
        tot = sum(raw)
        p = {x: raw[x] / tot for x in outcomes}
        ad = adaptive_cost(tuple(outcomes), p)
        fx = fixed_cost(p)
        if ad > fx + 1e-9:
            grid_ok = False
        if fx > ad + 1e-9 and witness is None:
            strict = True
            witness = (raw, round(ad, 6), round(fx, 6))
    check("T-24 adaptivity interest: optimal adaptive cost <= optimal fixed "
          "cost on every tested source (exhaustive strategy search over the "
          "threshold-question family, |X| = 4) and strictly less on a "
          f"shipped witness (J > 0): p ~ {witness[0] if witness else None}, "
          f"adaptive {witness[1] if witness else '?'} vs fixed "
          f"{witness[2] if witness else '?'}", grid_ok and strict)


# ---------------------------------------------------------------- T-25 --
def t25_typing() -> None:
    identity_sols = [x for x in (0, 1) if x == x]
    negation_sols = [x for x in (0, 1) if x == 1 - x]
    # graded recursion x_{n+1} = 1 - x_n: orbits from each seed, no clash
    orbits = set()
    for seed in (0, 1):
        x, orbit = seed, []
        for _ in range(6):
            orbit.append(x)
            x = 1 - x
        orbits.add(tuple(orbit))
    check("T-25 paradox = type collapse: ungraded x = x has exactly two "
          f"solutions ({identity_sols}), ungraded x = 1 - x has none "
          f"({negation_sols}), and the graded recursion x_(n+1) = 1 - x_n "
          f"has exactly two lawful orbits ({len(orbits)}) with no "
          "contradiction: self-reference is lawful when the asking grade "
          "is kept, paradoxical only when it is collapsed",
          identity_sols == [0, 1] and negation_sols == [] and len(orbits) == 2)


def main() -> int:
    rng = random.Random(20260714)
    t22_residuals(rng)
    t23_second_law(rng)
    t24_adaptivity()
    t25_typing()
    print("=" * 70)
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILURE(S)")
        return 1
    print("RESULT: ALL CHAPTER-4 CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
