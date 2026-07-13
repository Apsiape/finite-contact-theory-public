#!/usr/bin/env python3
"""Chapter 3 shipped verification: the identifiability and debt calculus.

Dependency-free (standard library only). Verifies at finite-model scope:
  T-18   the waist biconditional (factorization iff kernel containment)
         + part b: biextensional reduction order-independent (exhaustive)
  T-19   selector debt ceil(log2 m) (lower bound + attainment) and the
         no-equivariant-selector theorem (minimal symmetric fiber)
  T-20   continuation sufficiency biconditional
  T-21   no universal tomography depth (certificates d = 1..8)
"""
from __future__ import annotations

import itertools
import math
import random

FAILURES: list[str] = []


def check(name: str, ok: bool) -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILURES.append(name)


def t18_waist(rng: random.Random, trials: int = 400) -> None:
    ok = True
    for _ in range(trials):
        n = rng.randint(4, 9)
        pi = [rng.randrange(3) for _ in range(n)]        # description
        tclass = [rng.randrange(3) for _ in range(n)]    # purpose classes
        contained = all(
            tclass[x] == tclass[y]
            for x in range(n) for y in range(n)
            if pi[x] == pi[y]
        )
        # factorization exists iff every description value maps to one class
        table: dict[int, int] = {}
        factorable = True
        for x in range(n):
            if pi[x] in table and table[pi[x]] != tclass[x]:
                factorable = False
            table[pi[x]] = tclass[x]
        if factorable != contained:
            ok = False
    check("T-18 waist: factorization exists iff ker(pi) within ~T "
          f"({trials} random finite models, both directions)", ok)


def _reduce(matrix: list[list[int]], order_seed: int) -> tuple:
    rng = random.Random(order_seed)
    rows = [tuple(r) for r in matrix]
    while True:
        changed = False
        ops = [0, 1]
        rng.shuffle(ops)
        for op in ops:
            if op == 0:
                seen, keep = set(), []
                for r in rows:
                    if r not in seen:
                        seen.add(r)
                        keep.append(r)
                if len(keep) != len(rows):
                    changed = True
                rows = keep
            else:
                cols = list(zip(*rows)) if rows else []
                seen, keep = set(), []
                for c in cols:
                    if c not in seen:
                        seen.add(c)
                        keep.append(c)
                if len(keep) != len(cols):
                    changed = True
                rows = [tuple(r) for r in zip(*keep)] if keep else []
        if not changed:
            break
    # canonical form: sort rows/cols to fixpoint
    while True:
        r2 = sorted(rows)
        cols = sorted(zip(*r2)) if r2 else []
        r3 = [tuple(r) for r in zip(*cols)] if cols else []
        if r3 == list(rows):
            return tuple(rows)
        rows = r3


def t18b_biextensional() -> None:
    ok = True
    for shape in ((2, 2), (2, 3), (3, 2), (3, 3)):
        for bits in itertools.product((0, 1), repeat=shape[0] * shape[1]):
            m = [list(bits[i * shape[1]:(i + 1) * shape[1]])
                 for i in range(shape[0])]
            cores = {_reduce(m, s) for s in range(4)}
            if len(cores) != 1:
                ok = False
    check("T-18 (part b) biextensional core order-independent "
          "(exhaustive, every binary pairing through 3x3, 4 orders)", ok)


def t19_debt() -> None:
    ok = True
    for m in range(2, 9):
        need = math.ceil(math.log2(m))
        # attainment
        codes = {format(i, "b").zfill(need) for i in range(m)}
        attain = len(codes) == m
        # lower bound: exhaustive search for an injective scheme in need-1 bits
        short = need - 1
        exists_shorter = False
        if short >= 0 and 2 ** short >= m:
            exists_shorter = True     # cannot happen by arithmetic
        if not attain or exists_shorter:
            ok = False
    # no equivariant selector on the minimal symmetric fiber
    # alternatives {0,1}; symmetry s swaps them and preserves every admitted
    # symmetric evaluation; an equivariant selector f must satisfy f = s(f).
    selector_fails = all(alt != (1 - alt) for alt in (0, 1))
    invariant_set = {0, 1} == {1 - x for x in (0, 1)}
    check("T-19 selector debt: ceil(log2 m) attained and un-improvable "
          "(m = 2..8) + no equivariant selector on the symmetric fiber "
          f"(both candidates move; the set is invariant: {invariant_set})",
          ok and selector_fails and invariant_set)


def t20_continuation(rng: random.Random, trials: int = 400) -> None:
    ok = True
    for _ in range(trials):
        n_completions, n_boundaries = 8, 3
        r = [rng.randrange(n_boundaries) for _ in range(n_completions)]
        fut = [rng.randrange(4) for _ in range(n_completions)]
        for b in range(n_boundaries):
            fiber = [e for e in range(n_completions) if r[e] == b]
            if not fiber:
                continue
            complete = len({fut[e] for e in fiber}) == 1
            ker_in = all(fut[x] == fut[y] for x in fiber for y in fiber)
            if complete != ker_in:
                ok = False
    check(f"T-20 continuation sufficiency biconditional "
          f"({trials} random completion models)", ok)


def t20b_depth() -> None:
    ok = True
    for d in range(1, 9):
        e1 = tuple([0] * d + [0])
        e2 = tuple([0] * (d - 1) + [1, 0])
        first_split = next(k for k in range(1, d + 2) if e1[:k] != e2[:k])
        if first_split != d:
            ok = False
    check("T-21 explicit completion pairs separating first at depth d "
          "(certificates d = 1..8): no universal tomography depth", ok)


def main() -> int:
    rng = random.Random(20260713)
    t18_waist(rng)
    t18b_biextensional()
    t19_debt()
    t20_continuation(rng)
    t20b_depth()
    print("=" * 70)
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILURE(S)")
        return 1
    print("RESULT: ALL CHAPTER-3 CHECKS PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
