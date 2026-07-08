#!/usr/bin/env python3
"""Verify small exact identities in the binary-Bell native carrier lift.

Claim IDs: FCT-17, FCT-18, T-06, T-07.

This dependency-free script ships a public subset of the private native-lift
corpus. It verifies:

  1. binary one-use fork projectors produce a local involution U^2 = 1;
  2. the witness-overlap readout is exactly t(k,n)=k/n;
  3. site-disjoint witness products factor exactly.

It does not ship the full Sliwa certificate stack or the positivity/temperature
measurement. Those remain cited or held as described in the evidence manifest.
"""

from __future__ import annotations

from fractions import Fraction


Vector = tuple[Fraction, ...]


def signed_test(values: list[int]) -> Vector:
    return tuple(Fraction(v, 1) for v in values)


def pointwise(a: Vector, b: Vector) -> Vector:
    return tuple(x * y for x, y in zip(a, b))


def mean(v: Vector) -> Fraction:
    return sum(v, Fraction(0, 1)) / len(v)


def tensor_values(a: Vector, b: Vector) -> Vector:
    return tuple(x * y for x in a for y in b)


def overlap_contributions(n: int, k: int) -> Vector:
    """Build witness contributions with k shared aligned witnesses.

    Shared witnesses contribute +1 to U0*U1. Unshared witnesses are paired as
    complementary at the readout and contribute 0. The counting readout is the
    mean contribution over the n witnesses.
    """
    if not (0 <= k <= n):
        raise ValueError("need 0 <= k <= n")
    return tuple([Fraction(1)] * k + [Fraction(0)] * (n - k))


def run() -> None:
    print("native_lift_binary_bell")

    # N1: binary fork idempotents -> signed involution.
    e_plus = (Fraction(1), Fraction(0))
    e_minus = (Fraction(0), Fraction(1))
    u = tuple(a - b for a, b in zip(e_plus, e_minus))
    assert pointwise(e_plus, e_plus) == e_plus
    assert pointwise(e_minus, e_minus) == e_minus
    assert pointwise(e_plus, e_minus) == (Fraction(0), Fraction(0))
    assert tuple(a + b for a, b in zip(e_plus, e_minus)) == (Fraction(1), Fraction(1))
    assert pointwise(u, u) == (Fraction(1), Fraction(1))
    print("involution_check=PASS")

    # N3: t(k,n)=k/n exactly for finite witness-overlap carriers.
    for n in (4, 6):
        vals = []
        for k in range(n + 1):
            t = mean(overlap_contributions(n, k))
            vals.append(str(t))
            assert t == Fraction(k, n)
        print(f"t_values_n{n}={vals}")

    # N5: site-disjoint product factorizes exactly.
    a = overlap_contributions(4, 1)
    b = overlap_contributions(6, 2)
    omega_a = mean(a)
    omega_b = mean(b)
    omega_ab = mean(tensor_values(a, b))
    print(f"omega_a={omega_a} omega_b={omega_b} omega_ab={omega_ab}")
    assert omega_ab == omega_a * omega_b

    print("RESULT: PASS")


if __name__ == "__main__":
    run()
