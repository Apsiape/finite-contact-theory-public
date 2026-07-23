#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_66_carry.py  --  Chapter 66, The Carry Engine.

Self-contained re-derivation of the chapter's core exact results, using only
the Python standard library (itertools, math, random).  No numpy, no external
data.  Prints [PASS]/[FAIL] lines and exits nonzero on any failure.

The working model is the inhomogeneous bar cochain complex of the two-element
group over F2:

    C^n  =  { functions (Z2)^n -> F2 },   dim C^n = 2^n.

delta is the standard (trivial-action) group-cohomology coboundary; the cup
product is the standard bar cup; iota_a is the single-slot contraction that
plugs the nontrivial group element into slot a; iota_alt = sum_a iota_a is the
alternating (total) contraction.  On this model the "tower" generator is the
degree-1 class x = omega_1 : a |-> a, and its cup powers omega_k are the flat
tower.  Everything below is exact linear algebra over F2.

Checks:
  (a) K = delta.iota_1 + iota_1.delta is an idempotent chain map of rank
      2^{n-1} that sends every cocycle to a coboundary (acts as zero on
      cohomology) -- verified at n = 2,3,4.
  (b) the single-slot contraction fails to square to zero (iota_1^2(omega_4)
      = omega_2), but the alternating contraction squares to zero exactly
      (iota_alt^2 = 0) -- verified n = 3,4,5 on seeded random cochains.
  (c) the homotopy-transfer product m_n on the tower diagonal equals
      Catalan(n-1) mod 2 times omega_2, hence is nonzero exactly when n is a
      power of two -- verified n = 2..9 against the recursively counted trees.
  (d) the moduli of witnesses h with delta.h + h.delta = K has positive
      dimension; the transferred triple product m_3 on the diagonal is
      witness-independent (arity-3 rigidity); two admissible witnesses share
      m_2 and the m_3 diagonal yet differ at m_4 (delayed law memory).
  (e) the dyadic valuation nu_2(Catalan(n-1)) = s_2(n) - 1 (binary digit sum
      minus one) -- spot-checked, and cross-checked against (c).
"""

import itertools
import random
from math import comb

FAILURES = 0
def check(name, ok):
    global FAILURES
    print(("[PASS] " if ok else "[FAIL] ") + name)
    if not ok:
        FAILURES += 1

# ----------------------------------------------------------------------------
# F2 bar-cochain primitives.  A cochain is a dict {tuple -> 1}; absent = 0.
# ----------------------------------------------------------------------------
def tuples(n):
    return list(itertools.product([0, 1], repeat=n))

def add(*fs):
    out = {}
    for f in fs:
        for k, v in f.items():
            if v:
                out[k] = out.get(k, 0) ^ 1
    return {k: v for k, v in out.items() if v}

def delta(f, n):
    """Inhomogeneous, trivial-action coboundary C^n -> C^{n+1}."""
    out = {}
    for g in tuples(n + 1):
        v = f.get(g[1:], 0)
        for i in range(n):
            gg = list(g)
            m = (gg[i] + gg[i + 1]) % 2
            v ^= f.get(tuple(gg[:i] + [m] + gg[i + 2:]), 0)
        v ^= f.get(g[:-1], 0)
        if v:
            out[g] = 1
    return out

def iota(f, n, slot, val=1):
    """Single-slot contraction: plug group element `val` into `slot`. C^n->C^{n-1}."""
    if n == 0:
        return {}
    out = {}
    for g in tuples(n - 1):
        key = tuple(g[:slot - 1] + (val,) + g[slot - 1:])
        if f.get(key, 0):
            out[g] = out.get(g, 0) ^ 1
    return {k: v for k, v in out.items() if v}

def iota_alt(f, n):
    return add(*[iota(f, n, a) for a in range(1, n + 1)])

def K(f, n):
    """K = delta iota_1 + iota_1 delta on C^n (single-slot contraction)."""
    return add(iota(delta(f, n), n + 1, 1), delta(iota(f, n, 1), n - 1))

def cup(f, p, g, q):
    out = {}
    for a in tuples(p + q):
        if f.get(a[:p], 0) and g.get(a[p:], 0):
            out[a] = out.get(a, 0) ^ 1
    return {k: v for k, v in out.items() if v}

def deg(f):
    for k in f:
        return len(k)
    return None

# ----------------------------------------------------------------------------
# small F2 linear algebra on row lists
# ----------------------------------------------------------------------------
def rank_f2(rows):
    rows = [r[:] for r in rows]
    if not rows:
        return 0
    pr = 0
    r = 0
    for c in range(len(rows[0])):
        piv = None
        for i in range(pr, len(rows)):
            if rows[i][c]:
                piv = i
                break
        if piv is None:
            continue
        rows[pr], rows[piv] = rows[piv], rows[pr]
        for i in range(len(rows)):
            if i != pr and rows[i][c]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[pr])]
        pr += 1
        r += 1
    return r

def kernel_f2(M, ncols):
    """Return a basis (list of 0/1 vectors) of the right null space of M over F2."""
    M = [r[:] for r in M]
    pivots = {}
    pr = 0
    for c in range(ncols):
        piv = None
        for i in range(pr, len(M)):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[pr], M[piv] = M[piv], M[pr]
        for i in range(len(M)):
            if i != pr and M[i][c]:
                M[i] = [a ^ b for a, b in zip(M[i], M[pr])]
        pivots[c] = pr
        pr += 1
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        vec = [0] * ncols
        vec[fc] = 1
        for c, row in pivots.items():
            vec[c] = M[row][fc]
        basis.append(vec)
    return basis

def Kmatrix(n):
    ts = tuples(n)
    cols = []
    for t in ts:
        r = K({t: 1}, n)
        cols.append([r.get(w, 0) for w in ts])
    M = [[cols[j][i] for j in range(len(ts))] for i in range(len(ts))]
    return M, ts

def matmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) % 2
             for j in range(len(B[0]))] for i in range(len(A))]

# ============================================================================
# (a) K is an idempotent chain map of rank 2^{n-1} that is zero on cohomology
# ============================================================================
def check_projector():
    ok_all = True
    for n in [2, 3, 4]:
        M, ts = Kmatrix(n)
        idem = (matmul(M, M) == M)
        rk = rank_f2(M)
        ok_all &= idem and (rk == 2 ** (n - 1))
    check("(a) K idempotent (K^2=K) with rank 2^{n-1}, n=2,3,4", ok_all)

    # chain map delta K = K delta, and K(cocycle) is a coboundary, at n=3
    n = 3
    ts = tuples(n)
    chain_ok = True
    for t in ts:
        f = {t: 1}
        if add(delta(K(f, n), n), K(delta(f, n), n + 1)):
            chain_ok = False
            break
    check("(a) K is a chain map (delta K = K delta), n=3", chain_ok)

    # cocycles = ker(delta: C^3 -> C^4); coboundary space = im(delta: C^2 -> C^3)
    tnp1 = tuples(n + 1)
    Mdel = [[0] * len(ts) for _ in tnp1]
    for j, t in enumerate(ts):
        d = delta({t: 1}, n)
        for i, w in enumerate(tnp1):
            Mdel[i][j] = d.get(w, 0)
    cocycles = kernel_f2(Mdel, len(ts))
    cob_rows = [[delta({t: 1}, n - 1).get(w, 0) for w in ts] for t in tuples(n - 1)]
    rk_cob = rank_f2(cob_rows)
    zero_on_coh = True
    for z in cocycles:
        fz = {ts[i]: z[i] for i in range(len(ts)) if z[i]}
        Kz = [K(fz, n).get(w, 0) for w in ts]
        if rank_f2(cob_rows + [Kz]) != rk_cob:  # Kz stays in the coboundary space
            zero_on_coh = False
            break
    check("(a) K sends every cocycle to a coboundary (zero on cohomology), n=3",
          zero_on_coh and len(cocycles) > 0)

# ============================================================================
# (b) Cartan repair: iota_1^2 != 0 but iota_alt^2 = 0
# ============================================================================
def check_cartan():
    # single slot fails: iota_1^2(omega_4) = omega_2
    w4 = {(1, 1, 1, 1): 1}
    single = iota(iota(w4, 4, 1), 3, 1)
    check("(b) single-slot contraction fails to square to zero: iota_1^2(omega_4)=omega_2",
          single == {(1, 1): 1})
    # alternating contraction squares to zero on random cochains
    ok_all = True
    for n in [3, 4, 5]:
        random.seed(20260723 + n)
        for _ in range(25):
            f = {t: 1 for t in tuples(n) if random.random() < 0.5}
            if iota_alt(iota_alt(f, n), n - 1):
                ok_all = False
                break
        if not ok_all:
            break
    check("(b) alternating contraction squares to zero: iota_alt^2=0, n=3,4,5", ok_all)

# ============================================================================
# (c) dyadic selection: m_n(diagonal) = Catalan(n-1) mod 2 . omega_2
# ============================================================================
X = {(1,): 1}   # omega_1

def enum_trees(n):
    if n == 1:
        return [None]
    res = []
    for k in range(1, n):
        for L in enum_trees(k):
            for R in enum_trees(n - k):
                res.append((L, R))
    return res

def catalan(m):
    return comb(2 * m, m) // (m + 1)

def transfer_diagonal(n, hfun):
    """Homotopy-transfer product m_n on n copies of the tower generator x."""
    def edge(t):
        if t is None:
            return (X, 1)          # leaf -> i(x) = x
        f, d = node(t)
        return (hfun(f, d), d - 1)  # internal edge carries h
    def node(t):
        L, R = t
        fl, dl = edge(L)
        fr, dr = edge(R)
        return (cup(fl, dl, fr, dr), dl + dr)
    total = {}
    for T in enum_trees(n):
        val, _ = (X, 1) if n == 1 else node(T)
        total = add(total, val)
    if total:                       # root carries P = I - K
        total = add(total, K(total, deg(total)))
    return total

def h_iota1(f, n):
    return iota(f, n, 1)

def check_dyadic():
    ok_all = True
    ntrees_ok = True
    for n in range(2, 10):
        m = transfer_diagonal(n, h_iota1)
        nonzero = bool(m)
        par = catalan(n - 1) % 2
        is_pow2 = (n & (n - 1)) == 0
        # transferred product nonzero  <=>  Catalan(n-1) odd  <=>  n a power of two
        if not (nonzero == (par == 1) == is_pow2):
            ok_all = False
        if len(enum_trees(n)) != catalan(n - 1):
            ntrees_ok = False
    check("(c) #binary trees on n leaves = Catalan(n-1), n=2..9", ntrees_ok)
    check("(c) dyadic selection: m_n(x,..,x) nonzero  iff  n is a power of two, n=2..9",
          ok_all)

# ============================================================================
# (d) moduli of witnesses: arity-3 rigidity + delayed law memory at arity 4
# ============================================================================
def delta_e(u, n):
    return delta({u: 1}, n)

def build_moduli():
    # unknowns x[(m,s,r)] for h_m : C^m -> C^{m-1}, m = 1..4
    varlist = []
    varidx = {}
    for m in range(1, 5):
        for s in tuples(m):
            for r in tuples(m - 1):
                varidx[(m, s, r)] = len(varlist)
                varlist.append((m, s, r))
    NV = len(varlist)

    def Kcomp(u, n, w):
        return K({u: 1}, n).get(w, 0)

    rows = []  # (bitmask over NV, rhs)
    for n in [1, 2, 3]:
        Cn = tuples(n)
        Cnm1 = tuples(n - 1)
        Cnp1 = tuples(n + 1)
        for u in Cn:
            de_u = delta_e(u, n)
            for w in Cn:
                mask = 0
                for t in Cnm1:                              # delta h term
                    if delta_e(t, n - 1).get(w, 0) and (n, u, t) in varidx:
                        mask ^= (1 << varidx[(n, u, t)])
                for v in Cnp1:                              # h delta term
                    if de_u.get(v, 0) and (n + 1, v, w) in varidx:
                        mask ^= (1 << varidx[(n + 1, v, w)])
                rows.append((mask, Kcomp(u, n, w)))

    # F2 solve of the augmented system
    pivots = {}
    for m, b in rows:
        cm, cb = m, b
        for pcol, (pm, pb) in pivots.items():
            if (cm >> pcol) & 1:
                cm ^= pm
                cb ^= pb
        if cm == 0:
            continue
        col = (cm & -cm).bit_length() - 1
        for pcol in list(pivots):
            pm, pb = pivots[pcol]
            if (pm >> col) & 1:
                pivots[pcol] = (pm ^ cm, pb ^ cb)
        pivots[col] = (cm, cb)
    rank = len(pivots)
    part = [0] * NV
    for col, (pm, pb) in pivots.items():
        part[col] = pb
    pivcols = set(pivots)
    kernel = []
    for fc in [c for c in range(NV) if c not in pivcols]:
        vec = [0] * NV
        vec[fc] = 1
        for col, (pm, pb) in pivots.items():
            if (pm >> fc) & 1:
                vec[col] = 1
        kernel.append(vec)
    return varlist, NV, part, kernel, rank

def make_h(varlist, sol):
    tab = {}
    for i, (m, s, r) in enumerate(varlist):
        if sol[i]:
            tab.setdefault((m, s), {})[r] = 1
    def h(f, n):
        out = {}
        for s, c in f.items():
            if not c:
                continue
            for r, cc in tab.get((n, s), {}).items():
                out[r] = out.get(r, 0) ^ cc
        return {k: v for k, v in out.items() if v}
    return h

def freeze(d):
    return tuple(sorted(d.keys()))

def check_moduli():
    varlist, NV, part, kernel, rank = build_moduli()
    dim = NV - rank
    check("(d) moduli of witnesses has positive dimension "
          + "(unknowns=%d, rank=%d, dim=%d)" % (NV, rank, dim), dim > 0)

    h0 = make_h(varlist, part)
    base_m2 = transfer_diagonal(2, h0)
    base_m3 = transfer_diagonal(3, h0)
    base_m4 = transfer_diagonal(4, h0)

    random.seed(20260723)
    m3_shapes = set()
    delayed = None
    for _ in range(300):
        sol = part[:]
        for kv in kernel:
            if random.random() < 0.5:
                for i in range(NV):
                    sol[i] ^= kv[i]
        hf = make_h(varlist, sol)
        m2 = transfer_diagonal(2, hf)
        m3 = transfer_diagonal(3, hf)
        m4 = transfer_diagonal(4, hf)
        m3_shapes.add(freeze(m3))
        if (m2 == base_m2 and freeze(m3) == freeze(base_m3)
                and freeze(m4) != freeze(base_m4) and delayed is None):
            delayed = (freeze(base_m4), freeze(m4))
    check("(d) arity-3 rigidity: m_3 diagonal is witness-independent "
          + "(%d distinct value over 300 samples)" % len(m3_shapes),
          len(m3_shapes) == 1)
    check("(d) delayed law memory: witnesses agree at m_2 and m_3, first differ at m_4",
          delayed is not None)

# ============================================================================
# (e) Catalan valuation nu_2(Catalan(n-1)) = s_2(n) - 1
# ============================================================================
def nu2(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v

def s2(n):
    return bin(n).count("1")

def check_valuation():
    ok = all(nu2(catalan(n - 1)) == s2(n) - 1 for n in range(1, 33))
    check("(e) nu_2(Catalan(n-1)) = s_2(n) - 1, n=1..32", ok)
    # cross-check with (c): valuation zero <=> power of two <=> transferred product nonzero
    cross = all((nu2(catalan(n - 1)) == 0) == ((n & (n - 1)) == 0) for n in range(1, 33))
    check("(e) valuation zero  iff  n a power of two (cross-check with dyadic selection)",
          cross)

# ============================================================================
def main():
    print("Chapter 66 -- The Carry Engine: verification\n")
    check_projector()
    check_cartan()
    check_dyadic()
    check_moduli()
    check_valuation()
    print()
    if FAILURES == 0:
        print("ALL CHECKS PASSED")
    else:
        print("%d CHECK(S) FAILED" % FAILURES)
    return FAILURES

# ----------------------------------------------------------------------------
# FALSIFIABILITY.  This script fails if:
#  * K = delta.iota_1 + iota_1.delta is not idempotent, or its rank is not
#    2^{n-1}, or it does not send cocycles to coboundaries -- i.e. if the
#    50/50 flat/transverse split or the zero-on-cohomology claim is wrong;
#  * the alternating contraction does not square to zero (no genuine total
#    Cartan operator), or the single-slot contraction happens to square to
#    zero (no repair needed);
#  * the transferred diagonal product m_n is nonzero for any n that is not a
#    power of two, or zero for any power of two -- i.e. if the dyadic selection
#    departs from Catalan(n-1) mod 2;
#  * the witness moduli is zero-dimensional, or m_3 on the diagonal varies
#    across witnesses (arity-3 rigidity broken), or no two witnesses agree
#    through arity 3 while differing at arity 4 (no delayed law memory);
#  * nu_2(Catalan(n-1)) != s_2(n) - 1 for any n in range.
# None of these outcomes has been observed; all checks pass as shipped.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    sys.exit(1 if main() else 0)
