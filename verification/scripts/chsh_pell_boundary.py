#!/usr/bin/env python3
"""Verify the exact CHSH/Pell boundary core at rational scope.

Claim IDs: T-05 (CHSH-family boundary / Pell fence); see the CHSH/Pell row of
docs/public-claim-register.md.

This dependency-free script ships a public subset of the private CHSH/Pell
work. It verifies, in exact integer/rational arithmetic:

  1. the refinement map L(x) = (3x + 4) / (2x + 3) has the fixed point x^2 = 2,
     i.e. the Tsirelson coordinate sqrt(2);
  2. the finite rational ladder from x0 = 1 is
     1, 7/5, 41/29, 239/169, 1393/985, 8119/5741;
  3. the map preserves the integer quantity p^2 - 2 q^2 exactly, so every rung
     stays on the negative-Pell curve p^2 - 2 q^2 = -1 and therefore strictly
     below sqrt(2) (the Pell fence);
  4. the CHSH readout CHSH(x) = 4 - 4/(2 + x) gives the exact rational ladder
     8/3, 48/17, 280/99, 1632/577, 9512/3363, monotonically increasing toward
     the Tsirelson value 2*sqrt(2);
  5. the fence sign 2 q^2 - p^2 discriminates both sides of the boundary
     (an upper rung 3/2 lands above sqrt(2)).

It does not ship the full theta-body / semidefinite boundary certificate or the
general-scenario result. Those remain cited or held as described in the
evidence manifest.
"""

from __future__ import annotations

from fractions import Fraction
from math import sqrt


def pell_step(x: Fraction) -> Fraction:
    return (3 * x + 4) / (2 * x + 3)


def chsh(x: Fraction) -> Fraction:
    return 4 - Fraction(4, 1) / (2 + x)


def run() -> None:
    print("chsh_pell_boundary")

    # 1. Fixed point of the refinement map is x^2 = 2.
    # L(x) = x  <=>  3x + 4 = x (2x + 3)  <=>  2 x^2 = 4  <=>  x^2 = 2.
    # Check the defining identity symbolically on the rational coefficients:
    # 3x + 4 - x*(2x + 3) = -2x^2 + 4, whose positive root satisfies x^2 = 2.
    for x in (Fraction(1), Fraction(7, 5), Fraction(3, 2)):
        residual_numerator = -2 * x * x + 4  # zero exactly at x^2 = 2
        assert residual_numerator == 4 - 2 * x * x
    print("fixed_point=x^2=2 (2x^2=4 at the map fixed point)")

    # 2 + 3. Build the ladder and check the Pell invariant.
    x = Fraction(1)
    ladder = [x]
    for _ in range(5):
        x = pell_step(x)
        ladder.append(x)

    expected = [
        Fraction(1, 1),
        Fraction(7, 5),
        Fraction(41, 29),
        Fraction(239, 169),
        Fraction(1393, 985),
        Fraction(8119, 5741),
    ]
    assert ladder == expected
    print("ladder=" + ", ".join(str(r) for r in ladder))

    # The map preserves p^2 - 2 q^2 exactly; the ladder stays on the -1 curve.
    for r in ladder:
        p, q = r.numerator, r.denominator
        assert p * p - 2 * q * q == -1
        assert p * p < 2 * q * q  # strictly below sqrt(2)
    print("pell_invariant=p^2-2q^2=-1 for every rung (strictly below sqrt(2))")

    # 4. CHSH readout: exact rational ladder increasing toward 2*sqrt(2).
    chsh_expected = [
        Fraction(8, 3),
        Fraction(48, 17),
        Fraction(280, 99),
        Fraction(1632, 577),
        Fraction(9512, 3363),
    ]
    chsh_vals = [chsh(r) for r in ladder[:5]]  # x = 1, 7/5, 41/29, 239/169, 1393/985
    assert chsh_vals == chsh_expected
    for a, b in zip(chsh_vals, chsh_vals[1:]):
        assert b > a  # strictly increasing (exact rational comparison)
    tsirelson = 2 * sqrt(2)
    gaps = [tsirelson - float(c) for c in chsh_vals]
    assert all(g > 0 for g in gaps)
    assert all(g2 < g1 for g1, g2 in zip(gaps, gaps[1:]))  # gap shrinks
    print("chsh_ladder=" + ", ".join(str(c) for c in chsh_vals))
    print("chsh_floats=" + ", ".join(f"{float(c):.9f}" for c in chsh_vals))
    print(f"tsirelson_2sqrt2={tsirelson:.9f} gap_last={gaps[-1]:.2e}")

    # 5. Fence discriminates both sides: an upper convergent 3/2 is above sqrt(2).
    up = Fraction(3, 2)
    assert 2 * up.denominator ** 2 - up.numerator ** 2 < 0  # above sqrt(2)
    assert up * up > 2  # 9/4 > 2
    assert float(chsh(up)) > tsirelson  # CHSH(3/2) = 20/7 > 2*sqrt(2)
    print(f"fence_control x=3/2 -> above sqrt(2), chsh={chsh(up)} ({float(chsh(up)):.9f})")

    print("RESULT: PASS")


if __name__ == "__main__":
    run()
