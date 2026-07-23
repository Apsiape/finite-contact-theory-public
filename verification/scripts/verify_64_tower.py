#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_64_tower.py  --  Chapter 64, "The Law Tower".

Dependency-free (stdlib only: fractions, itertools, math) re-derivation of the
chapter's exact results.  Every load-bearing computation is exact integer or
mod-m arithmetic; no floating point, no numpy.

Blocks:
  (a) top-cell lemma  -- the half-eraser: mod 2 never hits a top cell (no rung
      erased); mod 4 erases exactly the even rungs (lambda = 1 supplies the
      half), never the odd rungs.  Rungs 2..5.
  (b) the char-2 Weyl calculus on F2[x]: DU + UD = 1 through degree 12;
      ker D = im D = even degrees = im Frobenius (the law sector); and the
      p = 2 uniqueness (ker D != im D already at p = 3).
  (c) vertical exactness: x^4 = D(x^5).
  (d) the Bockstein carry theorem: the carry of the signed differential over
      the mod-2 differential, computed exactly on group cochains of Z2, equals
      the Bockstein; beta(omega_n) = omega_{n+1} for odd n, 0 for even n
      (n = 1..6).
  (e) the mirror = the Z/4 extension class = the first Witt carry: Witt
      addition (a0,a1)+(b0,b1) = (a0+b0, a1+b1+a0 b0) reproduces Z/4 on all 16
      pairs, and the factor set a*b is a genuine noncoboundary.
  (f) the carry-depth filtration: nu_2(Catalan(n-1)) = s_2(n) - 1, n = 2..40.

Prints [PASS]/[FAIL] per check.  Exits nonzero on any FAIL.
"""

import sys
import math
from itertools import product

FAILURES = []


def report(name, ok, detail=""):
    tag = "[PASS]" if ok else "[FAIL]"
    line = "%s %s" % (tag, name)
    if detail:
        line += "  --  " + detail
    print(line)
    if not ok:
        FAILURES.append(name)


# ---------------------------------------------------------------------------
# Group cohomology of Z2 = {0,1}, inhomogeneous (bar) resolution.
# An n-cochain is a dict from (Z2)^n -> ring value.  "Normalized" = vanishes
# whenever any argument is the identity 0.  Coboundary (coefficients in Z, or
# reduced mod m):
#   (d f)(g_1..g_{n+1}) =  f(g_2..g_{n+1})
#                        + sum_{i=1}^{n} (-1)^i f(..,g_i+g_{i+1},..)
#                        + (-1)^{n+1} f(g_1..g_n)
# with group operation g_i + g_{i+1} taken mod 2.
# ---------------------------------------------------------------------------

def coboundary(f, n, mod=None):
    """f: dict (Z2)^n->int  ->  (df): dict (Z2)^{n+1}->int, over Z (or mod)."""
    out = {}
    for g in product((0, 1), repeat=n + 1):
        # term 1: drop first argument
        val = f[g[1:]]
        # middle terms: merge adjacent pair i, i+1  (i = 1..n)
        for i in range(1, n + 1):
            merged = g[:i - 1] + ((g[i - 1] + g[i]) % 2,) + g[i + 1:]
            val += ((-1) ** i) * f[merged]
        # last term
        val += ((-1) ** (n + 1)) * f[g[:n]]
        if mod is not None:
            val %= mod
        out[g] = val
    return out


def omega_cochain(n, top_value, mod):
    """The class omega_n: value `top_value` at (1,...,1), 0 elsewhere, mod m."""
    f = {}
    for g in product((0, 1), repeat=n):
        f[g] = (top_value % mod) if all(x == 1 for x in g) else 0
    return f


def normalized_top_cochains(deg, mod):
    """All normalized deg-cochains on Z2: one free value lambda at the top
    cell (1,...,1); every other value forced to 0.  Yields (lambda, cochain)."""
    for lam in range(mod):
        f = {}
        for g in product((0, 1), repeat=deg):
            f[g] = lam if all(x == 1 for x in g) else 0
        yield lam, f


def is_coboundary_of_normalized_top(target, n, mod):
    """Is the degree-n cochain `target` = d(L) for some normalized (n-1)-
    cochain L (mod m)?  The normalized (n-1)-cochains are 1-dimensional."""
    for lam, L in normalized_top_cochains(n - 1, mod):
        dl = coboundary(L, n - 1, mod=mod)
        if all(dl[g] == (target[g] % mod) for g in target):
            return True, lam
    return False, None


def check_a_top_cell_lemma():
    # Represent omega_n as the 2-torsion class: value (mod/2) at the top cell.
    # mod 2 -> top value 1; mod 4 -> top value 2 (the order-2 element).
    ok_all = True
    detail = []
    for mod in (2, 4):
        top_value = mod // 2
        for n in (2, 3, 4, 5):
            target = omega_cochain(n, top_value, mod)
            erased, lam = is_coboundary_of_normalized_top(target, n, mod)
            # Predicted pattern:
            #   mod 2: never erased (top cell unreachable), any n.
            #   mod 4: erased iff n even (lambda = 1 supplies the half).
            if mod == 2:
                predicted = False
            else:
                predicted = (n % 2 == 0)
            match = (erased == predicted)
            ok_all &= match
            if mod == 4 and erased:
                # confirm the half is supplied by lambda = 1
                match &= (lam == 1)
                ok_all &= (lam == 1)
            detail.append("mod%d n=%d erased=%s(pred %s)"
                          % (mod, n, erased, predicted))
    report("(a) top-cell half-eraser (rungs 2-5, mod 2 & 4)",
           ok_all, "; ".join(detail))


# ---------------------------------------------------------------------------
# (b),(c)  The char-p Weyl calculus on the polynomial ring F_p[x].
#   U = multiply by x ;  D = formal derivative.
# Represent a polynomial as a dict {degree: coeff mod p}.
# ---------------------------------------------------------------------------

def poly_U(poly, p):
    return {d + 1: c % p for d, c in poly.items() if c % p}


def poly_D(poly, p):
    out = {}
    for d, c in poly.items():
        if d == 0:
            continue
        nc = (d * c) % p
        if nc:
            out[d - 1] = nc
    return out


def poly_add(a, b, p):
    out = dict(a)
    for d, c in b.items():
        out[d] = (out.get(d, 0) + c) % p
    return {d: c for d, c in out.items() if c % p}


def check_b_weyl_calculus():
    p = 2
    ok = True
    for k in range(0, 13):
        xk = {k: 1}
        du = poly_D(poly_U(xk, p), p)
        ud = poly_U(poly_D(xk, p), p)
        s = poly_add(du, ud, p)
        ok &= (s == {k: 1})
    report("(b1) DU + UD = 1 on F2[x], deg 0..12", ok)

    # ker D, im D, im Frobenius through degree 12.
    kerD = set()
    imD = set()
    for k in range(0, 13):
        xk = {k: 1}
        if poly_D(xk, p) == {}:
            kerD.add(k)
        d = poly_D({k + 1: 1}, p)   # D(x^{k+1}) lands in degree k
        if d == {k: 1}:
            imD.add(k)
    even = set(range(0, 13, 2))
    frob = set(range(0, 13, 2))    # im Frobenius = span of x^{2j}
    ok2 = (kerD == even) and (imD == even) and (frob == even)
    report("(b2) ker D = im D = im Frobenius = even degrees (p=2)",
           ok2, "ker=%s im=%s" % (sorted(kerD), sorted(imD)))

    # p = 2 uniqueness: at p = 3, ker D != im D.
    p3 = 3
    kerD3, imD3 = set(), set()
    for k in range(0, 13):
        if poly_D({k: 1}, p3) == {}:
            kerD3.add(k)
        d = poly_D({k + 1: 1}, p3)
        if d and list(d.values())[0] and list(d.keys())[0] == k:
            imD3.add(k)
    ok3 = (kerD3 != imD3)
    report("(b3) p-uniqueness: ker D != im D at p=3", ok3,
           "ker3=%s im3=%s" % (sorted(kerD3), sorted(imD3)))


def check_c_vertical_exact():
    ok = (poly_D({5: 1}, 2) == {4: 1})
    report("(c) vertical exactness: x^4 = D(x^5)", ok)


# ---------------------------------------------------------------------------
# (d)  The Bockstein as the carry of the differential.
#   kappa_delta(f) = ( delta_Z(lift f) - lift(delta_2 f) ) / 2   (mod 2)
# On a mod-2 cocycle omega_n this reduces to delta_Z(lift)/2 mod 2 = Bockstein.
# ---------------------------------------------------------------------------

def mod2_cochain(f):
    return {g: v % 2 for g, v in f.items()}


def carry_bockstein(f_mod2, n):
    """f_mod2: normalized mod-2 n-cochain.  Returns beta(f): mod-2
    (n+1)-cochain, computed as the exact carry of the signed differential."""
    lift = {g: (v % 2) for g, v in f_mod2.items()}          # {0,1} in Z
    d_lift = coboundary(lift, n, mod=None)                    # signed, over Z
    d2 = coboundary(f_mod2, n, mod=2)                         # mod-2 differential
    lift_d2 = {g: (v % 2) for g, v in d2.items()}            # {0,1} in Z
    beta = {}
    for g in d_lift:
        diff = d_lift[g] - lift_d2[g]
        if diff % 2 != 0:
            raise AssertionError("carry not divisible by 2 at %s" % (g,))
        beta[g] = (diff // 2) % 2
    return beta


def check_d_bockstein():
    ok_all = True
    detail = []
    for n in range(1, 7):
        om_n = omega_cochain(n, 1, 2)          # value 1 at top, mod 2
        beta = carry_bockstein(mod2_cochain(om_n), n)
        if n % 2 == 1:
            expected = omega_cochain(n + 1, 1, 2)
            label = "omega_%d" % (n + 1)
        else:
            expected = {g: 0 for g in beta}
            label = "0"
        match = all(beta[g] == expected[g] for g in beta)
        ok_all &= match
        detail.append("beta(omega_%d)=%s" % (n, label if match else "MISMATCH"))
    report("(d) Bockstein carry: beta(omega_n) pattern, n=1..6",
           ok_all, "; ".join(detail))


# ---------------------------------------------------------------------------
# (e)  Mirror = Z/4 extension class = first Witt carry.
# ---------------------------------------------------------------------------

def witt_add(a, b):
    a0, a1 = a
    b0, b1 = b
    s0 = (a0 + b0) % 2
    s1 = (a1 + b1 + a0 * b0) % 2
    return (s0, s1)


def witt_to_z4(v):
    return (v[0] + 2 * v[1]) % 4


def check_e_witt():
    ok = True
    for a in product((0, 1), repeat=2):
        for b in product((0, 1), repeat=2):
            lhs = witt_to_z4(witt_add(a, b))
            rhs = (witt_to_z4(a) + witt_to_z4(b)) % 4
            ok &= (lhs == rhs)
    report("(e1) Witt addition on W2(F2) reproduces Z/4 (all 16 pairs)", ok)

    # factor set f(a,b) = a*b is a noncoboundary of a normalized 1-cochain.
    # normalized 1-cochains g: Z2->Z2, g(0)=0, g(1)=t.  (dg)(a,b)=g(b)-g(a+b)+g(a).
    factor_set = {(a, b): (a * b) % 2 for a in (0, 1) for b in (0, 1)}
    is_cob = False
    for t in (0, 1):
        g = {(0,): 0, (1,): t}
        dg = coboundary(g, 1, mod=2)
        if all(dg[(a, b)] == factor_set[(a, b)] for a in (0, 1) for b in (0, 1)):
            is_cob = True
    report("(e2) factor set a*b is a noncoboundary (the mirror is nontrivial)",
           not is_cob)


# ---------------------------------------------------------------------------
# (f)  Carry-depth filtration:  nu_2(Catalan(n-1)) = s_2(n) - 1.
# ---------------------------------------------------------------------------

def nu2(m):
    if m == 0:
        return None
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def s2(n):
    return bin(n).count("1")


def catalan(m):
    return math.comb(2 * m, m) // (m + 1)


def check_f_carry_depth():
    ok = True
    detail = []
    for n in range(2, 41):
        lhs = nu2(catalan(n - 1))
        rhs = s2(n) - 1
        ok &= (lhs == rhs)
        if n <= 16:
            detail.append("n=%d:%d" % (n, lhs))
    report("(f) nu2(Catalan(n-1)) = s2(n)-1, n=2..40", ok, " ".join(detail))


def main():
    print("=" * 70)
    print("Chapter 64  --  The Law Tower : exact re-derivation")
    print("=" * 70)
    check_a_top_cell_lemma()
    check_b_weyl_calculus()
    check_c_vertical_exact()
    check_d_bockstein()
    check_e_witt()
    check_f_carry_depth()
    print("-" * 70)
    if FAILURES:
        print("RESULT: FAIL  (%d) : %s" % (len(FAILURES), ", ".join(FAILURES)))
        sys.exit(1)
    print("RESULT: ALL PASS")
    sys.exit(0)


if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------
# FALSIFIABILITY.
# This script FAILS (nonzero exit) if any of the following stops being true:
#   * the half-eraser inverts -- if a mod-2 coboundary ever hits a top cell,
#     or if adjoining i (mod 4) erased an ODD rung or spared an EVEN one;
#   * DU + UD were not the identity on some monomial of degree <= 12, or the
#     three characterizations of the law sector (ker D, im D, im Frobenius)
#     ceased to coincide at p = 2, or coincided at p = 3 (the uniqueness);
#   * x^4 were not the derivative of x^5;
#   * the carry of the signed differential over the mod-2 differential were not
#     divisible by 2, or its half did not equal the Bockstein pattern
#     beta(omega_n) = omega_{n+1} (n odd) / 0 (n even) for any n in 1..6;
#   * Witt addition on W2(F2) failed to reproduce Z/4 on any of the 16 pairs,
#     or the factor set a*b turned out to be a coboundary;
#   * nu2(Catalan(n-1)) != s2(n)-1 for any n in 2..40.
# Any single arithmetic drift in the group-cohomology, formal-derivative,
# Witt, or 2-adic-valuation routines surfaces here as a FAIL.
# ---------------------------------------------------------------------------
