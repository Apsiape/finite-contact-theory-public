#!/usr/bin/env python3
"""Verify a finite exchangeable frequency bridge by exact counting.

Claim IDs: FCT-10, T-03.

This dependency-free script checks the finite core of the frequency bridge:
for a fixed staged fork with multiplicities m=(2,2,1), the share of
micro-presentations whose empirical type vector deviates from the counting
share p=(2/5,2/5,1/5) is exactly enumerable and bounded by the standard
finite type bound

  share <= (T+1)^k * exp(-T * eps^2 / 2).

The script uses integer counts and rational shares. Floating point appears
only when evaluating the displayed exponential upper bound.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, exp


M = (2, 2, 1)
TOTAL = sum(M)
P = tuple(Fraction(m, TOTAL) for m in M)


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for i in range(total + 1):
        for tail in compositions(total - i, parts - 1):
            yield (i,) + tail


def multinomial(counts: tuple[int, ...]) -> int:
    remaining = sum(counts)
    out = 1
    for c in counts:
        out *= comb(remaining, c)
        remaining -= c
    return out


def type_count(counts: tuple[int, ...]) -> int:
    out = multinomial(counts)
    for c, m in zip(counts, M):
        out *= m**c
    return out


def l1_deviation(counts: tuple[int, ...]) -> Fraction:
    T = sum(counts)
    return sum(abs(Fraction(c, T) - p) for c, p in zip(counts, P))


def deviant_share(T: int, eps: Fraction) -> Fraction:
    dev = 0
    total = TOTAL**T
    for counts in compositions(T, len(M)):
        c = type_count(counts)
        if l1_deviation(counts) >= eps:
            dev += c
    assert sum(type_count(counts) for counts in compositions(T, len(M))) == total
    return Fraction(dev, total)


def run() -> None:
    exact_targets = {
        (12, Fraction(1, 10)): Fraction(227109457, 244140625),
        (12, Fraction(1, 5)): Fraction(198724177, 244140625),
        (12, Fraction(2, 5)): Fraction(73203793, 244140625),
    }

    print("frequency_bridge_exchangeable")
    print(f"multiplicities={M}")
    print(f"shares={tuple(str(p) for p in P)}")

    for (T, eps), expected in exact_targets.items():
        share = deviant_share(T, eps)
        bound = (T + 1) ** len(M) * exp(-T * float(eps) ** 2 / 2)
        print(
            f"T={T} eps={eps} share={share} "
            f"share_float={float(share):.9f} bound={bound:.9f}"
        )
        assert share == expected
        assert float(share) <= bound

    for T in (6, 12, 24, 48):
        for eps in (Fraction(1, 10), Fraction(1, 5), Fraction(2, 5)):
            share = deviant_share(T, eps)
            bound = (T + 1) ** len(M) * exp(-T * float(eps) ** 2 / 2)
            assert float(share) <= bound

    print("RESULT: PASS")


if __name__ == "__main__":
    run()
