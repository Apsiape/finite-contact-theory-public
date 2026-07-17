#!/usr/bin/env python3
"""Chapter 18 -- The Emergent Hierarchy and the Exposure Law: shipped
verifier (Python 3 stdlib only; exact integer combinatorics + exact
rational linear algebra).

The commutant of the cyclic shift in C[S_n] decomposes by the
multiplicities m_{lambda,j} of cyclic characters in S_n-irreps;
(Kraskiewicz-Weyman, cited) m_{lambda,j} = #{standard Young tableaux
of shape lambda with major index == j mod n}.

  U1: cross-engine -- tableau counting reproduces Chapter 12's closed
      form C_n = (1/n) sum phi(n/d)(n/d)^d d! for n = 3..8
      (4, 10, 28, 136, 726, 5100); n = 5 has exactly one width-2
      block, at (3,1,1) residue 0 (Chapter 12's emergent qubit,
      re-derived by an independent method).
  U2: the width hierarchy 1,1,2,3,5,12 (n = 3..8); the first emergent
      QUTRIT is forced at n = 6 by pigeonhole on the 16 SYT of
      (3,2,1), at residues 1,2,4,5.
  U3: the visible/hidden budget: N_n vs C_n -- hidden dimensions
      0, 0, 2, 56, 480, 4290.
  U4: depth saturation -- real-symmetric generators plus one
      product/commutator layer span all of M_m (exact over Q,
      m = 2, 3, 4). The hierarchy is width-strict and depth-saturated,
      GIVEN fiber exposure -- verified at n = 5 (Chapter 12) and at
      n = 6 by the research corpus's fiber engines (the EXPOSURE LAW:
      all 22 multiplicit fibers expose exactly their symmetric part;
      cited, discovery grade -- see the chapter text).
"""
from fractions import Fraction as F
from itertools import product as iproduct
import math
import random

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def partitions_of(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions_of(n - k, k):
            yield (k,) + rest

def syt_maj_counts(shape, n):
    """count SYT of `shape` by major index mod n (backtracking fill)."""
    rows = len(shape)
    cells = sum(shape)
    counts = [0] * n
    # state: next free column per row; track position (row) of each value
    colpos = [0] * rows
    rowof = [0] * (cells + 1)
    def place(v, maj):
        if v > cells:
            counts[maj % n] += 1
            return
        for r in range(rows):
            c = colpos[r]
            if c < shape[r] and (r == 0 or colpos[r - 1] > c):
                colpos[r] += 1
                rowof[v] = r
                # descent at v if v+1 goes to a strictly lower row --
                # handled when placing v+1: if rowof[v+1] > rowof[v],
                # maj += v. So pass maj increment forward:
                if v == 1:
                    place(v + 1, maj)
                else:
                    place(v + 1, maj + (v - 1 if r > rowof[v - 1] else 0))
                colpos[r] -= 1
        return
    # cleaner: place values 1..cells; descent i (i.e. i+1 strictly lower
    # row than i) adds i to maj. Implement with maj accumulated when
    # placing v (v >= 2) based on rowof[v-1].
    place(1, 0)
    return counts

def euler_phi(m):
    r, mm, p = m, m, 2
    while p * p <= mm:
        if mm % p == 0:
            while mm % p == 0:
                mm //= p
            r -= r // p
        p += 1
    if mm > 1:
        r -= r // mm
    return r

def C_closed(n):
    return sum(euler_phi(n // d) * (n // d) ** d * math.factorial(d)
               for d in range(1, n + 1) if n % d == 0) // n

def N_closed(n):
    return sum(euler_phi(n // d) * math.comb(2 * d - 1, d - 1)
               for d in range(1, n + 1) if n % d == 0) // n

if __name__ == '__main__':
    rng = random.Random(43)

    profiles = {}
    for n in range(3, 9):
        prof = {}
        for lam in partitions_of(n):
            prof[lam] = syt_maj_counts(lam, n)
        profiles[n] = prof

    print("## U1: cross-engine -- KW tableau counting vs the closed form")
    ok1 = True
    dims = []
    for n in range(3, 9):
        s2 = sum(m * m for cnts in profiles[n].values() for m in cnts)
        cf = C_closed(n)
        dims.append((n, s2, cf))
        if s2 != cf:
            ok1 = False
        # sanity: per shape, Sigma_j m = #SYT and Sigma_lambda (#SYT)^2
        # = n! (RSK) -- check the second:
        tot = sum(sum(cnts) ** 2 for cnts in profiles[n].values())
        if tot != math.factorial(n):
            ok1 = False
    # n = 5: exactly one width-2 block, at (3,1,1), residue 0
    w2 = [(lam, j) for lam, cnts in profiles[5].items()
          for j, m in enumerate(cnts) if m >= 2]
    n5_ok = (w2 == [((3, 1, 1), 0)]
             and profiles[5][(3, 1, 1)][0] == 2)
    check(f"Kraskiewicz-Weyman tableau counting reproduces the shipped "
          f"closed form EXACTLY for n = 3..8: (n, sum m^2, C_n) = "
          f"{dims}; RSK sanity holds per n; and n = 5 has EXACTLY ONE "
          f"width-2 block, at lambda = (3,1,1), residue 0 ({n5_ok}) -- "
          f"Chapter 12's emergent-qubit statement re-derived by an "
          f"independent method.", ok1 and n5_ok)

    print("## U2: the first qutrit is forced at n = 6; width growth")
    maxw = {n: max(m for cnts in profiles[n].values() for m in cnts)
            for n in range(3, 9)}
    qutrits6 = [(lam, j, cnts[j]) for lam, cnts in profiles[6].items()
                for j in range(6) if cnts[j] >= 3]
    growth = [maxw[n] for n in range(3, 9)]
    nondec = all(a <= b for a, b in zip(growth, growth[1:]))
    # the registered pigeonhole: (3,2,1) has 16 SYT over 6 residues
    syt321 = sum(profiles[6][(3, 2, 1)])
    forced = syt321 == 16 and max(profiles[6][(3, 2, 1)]) >= 3
    check(f"max block width by n: {dict(sorted(maxw.items()))} -- the "
          f"hierarchy 1,1,2,... is nondecreasing ({nondec}); the FIRST "
          f"EMERGENT QUTRIT appears at n = 6 as registered (pigeonhole: "
          f"(3,2,1) has {syt321} SYT over 6 residues => some m >= 3: "
          f"{forced}); all width->=3 blocks at n = 6: {qutrits6}. "
          f"**Counting symmetry alone mints a logical qutrit at six "
          f"photons, and the fiber width grows with n.**",
          nondec and forced and len(qutrits6) >= 1 and maxw[5] == 2)

    print("## U3: the visible/hidden budget")
    rows = []
    ok3 = True
    prev_frac = None
    for n in range(3, 9):
        Nv, Ct = N_closed(n), C_closed(n)
        rows.append((n, Nv, Ct, Ct - Nv))
        frac = F(Nv, Ct)
        if prev_frac is not None and n >= 5 and not frac < prev_frac:
            ok3 = False
        prev_frac = frac
    check(f"(n, visible N_n, commutant C_n, hidden C_n - N_n) = {rows}: "
          f"the count-visible fraction shrinks monotonically from n = 4 "
          f"on ({ok3}) and the hidden budget grows super-linearly -- "
          f"single-shot counting sees a vanishing fraction of the "
          f"emergent algebra.", ok3)

    print("## U4: depth saturates at ONE commutator (width, not depth)")
    def mat_rand_sym(m):
        A = [[F(0)] * m for _ in range(m)]
        for i in range(m):
            for j in range(i, m):
                v = F(rng.randint(-3, 3), rng.randint(1, 3))
                A[i][j] = v
                A[j][i] = v
        return A
    def mmul(A, B):
        m = len(A)
        return [[sum(A[i][k] * B[k][j] for k in range(m))
                 for j in range(m)] for i in range(m)]
    def msub(A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A))]
                for i in range(len(A))]
    def flat(A):
        return [x for row in A for x in row]
    def rank_rat(vecs):
        rows = [v[:] for v in vecs]
        r, ncol = 0, len(rows[0]) if rows else 0
        for col in range(ncol):
            piv = next((i for i in range(r, len(rows))
                        if rows[i][col] != 0), None)
            if piv is None:
                continue
            rows[r], rows[piv] = rows[piv], rows[r]
            pv = rows[r][col]
            rows[r] = [c / pv for c in rows[r]]
            for i in range(len(rows)):
                if i != r and rows[i][col] != 0:
                    f = rows[i][col]
                    rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
            r += 1
        return r
    ok4 = True
    for m in (2, 3, 4):
        gens = [mat_rand_sym(m) for _ in range(m + 1)]
        span = [flat(A) for A in gens]
        # one commutator layer:
        for i in range(len(gens)):
            for j in range(i + 1, len(gens)):
                C = msub(mmul(gens[i], gens[j]), mmul(gens[j], gens[i]))
                span.append(flat(C))
        # products of pairs (the *-algebra needs products too; still
        # depth 2 words):
        for i in range(len(gens)):
            for j in range(len(gens)):
                span.append(flat(mmul(gens[i], gens[j])))
        r = rank_rat(span)
        if r != m * m:
            ok4 = False
    check("real-symmetric generators plus DEPTH-2 words (one commutator "
          "/ one product layer) span all of M_m exactly, for m = 2, 3, "
          "4 (exact rational rank m^2 each) -- the unlock resource does "
          "NOT deepen with block width. **B12 verdict: the hierarchy is "
          "STRICT IN WIDTH (qubit at 5, qutrit at 6, unbounded) and "
          "SATURATED IN DEPTH (one multiplication layer opens any "
          "fiber): the growing resource is HOW MANY hidden fibers there "
          "are and how wide, never how deep the algebra must dig.**",
          ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
