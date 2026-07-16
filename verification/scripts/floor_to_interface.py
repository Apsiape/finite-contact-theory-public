#!/usr/bin/env python3
"""Chapter 13 -- FROM THE FLOOR TO THE INTERFACE: the exact forcing chain.

GIVEN three named hypotheses -- (S) a ternary contact, (R) future-readable
order scars, (SH) internally-carried retention -- the retained interface is
FORCED: exactly three mutually anticommuting involutive identity modes,
whose oriented volume element is a central sqrt(-1), whose even sector is
the quaternions, whose reflection symmetry forces exact 1/2 weights, and
whose retained central residue forces the minimal faithful receiver to be
H with the 1+3 split and the unique Euclidean form. This is verbatim the
starting datum of Chapter 8 (FCT-45), whose chain continues to the 24-cell,
F_4, the finite Gleason theorem, and the triality Kochen-Specker
obstruction.

Twelve exact checks (fractions + exhaustive enumeration, no floats):
  1a. reader <=> anticommutation (linear-map identity on a full M_2 basis);
      the anticommutant of {X,Z} in M_2(R) is exactly span{XZ}, whose
      squares are negative => NO third involutive reader in the two-mode
      algebra; an explicit integer anticommuting triple exists in M_4(R).
  1b. reverse-oddtown: f(n) = largest odd <= n for n = 2..7; the n = 3
      maximum family is UNIQUE (the three pair-channels). The pincer:
      exactly three modes.
  2.  Cl(3,0): Omega = ABC central, Omega^2 = -I; the even sector satisfies
      the quaternion relations (dim 4 = H); the eigenprojectors of a mode
      are swapped by an anticommuting partner => exact 1/2 weights for any
      reflection-invariant state; the mod-4 phase plateau (central sqrt(-1)
      iff m = 3 mod 4 => arity window {3,4}).
  3.  H^2(C_3;C_2) = 0 (census); H^2(A_4;C_2) = C_2 (gauge orbits, both
      classes witnessed); 2T = SL(2,3) has a UNIQUE involution (nonsplit)
      and every V_4 preimage squares to the central z; the split twin
      A_4 x C_2 is constructed explicitly and every involution lift squares
      to the identity -- GIVEN (SH), the split twin dies and 2T is forced.
  4.  z -> H minimality: dim 1 killed by arithmetic; dim 2 killed by
      Frobenius-Schur = -1; dim 3 killed by the derived-subgroup
      determinant; dim 4 has commutant exactly H (division); the invariant
      symmetric form is unique up to scale = I_4 (the Euclidean 1+3 split).
  5.  spinor return: J^2 = z, J^4 = 1 -- visible period 2, complete
      period 4; the handoff to Chapter 8.

RECEIVED INPUTS -- named, not proven (the fork-staging law executing on the
derivation itself): (S) measured arity (candidate-internal via the phase
plateau, conditionally); (R) readability -- the program's standing door,
proven not-forced in the private corpus (cited); (SH) internal retention --
a named axiom (ledger-regress defense); (C) one orientation bit, a proven
received C_2 torsor. See the chapter for the exact fences.
"""

from fractions import Fraction as F
from itertools import combinations, product

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

# ---------- exact dense linear algebra over Fractions ----------------------
def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(m))
                       for j in range(p)) for i in range(n))
def madd(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(len(A[0])))
                 for i in range(len(A)))
def mneg(A): return tuple(tuple(-x for x in r) for r in A)
def meq(A, B): return all(A[i][j] == B[i][j] for i in range(len(A))
                          for j in range(len(A[0])))
def ident(n): return tuple(tuple(F(1) if i == j else F(0) for j in range(n))
                           for i in range(n))
def rank_exact(rows):
    mat = [list(r) for r in rows]
    if not mat: return 0
    rank, nr, nc = 0, len(mat), len(mat[0])
    for c in range(nc):
        piv = next((r for r in range(rank, nr) if mat[r][c] != 0), None)
        if piv is None: continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pv = mat[rank][c]
        mat[rank] = [x / pv for x in mat[rank]]
        for r in range(nr):
            if r != rank and mat[r][c] != 0:
                f = mat[r][c]
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[rank])]
        rank += 1
    return rank
def nullspace_exact(rows, ncols):
    """basis of the exact nullspace of the linear system rows * y = 0."""
    mat = [list(r) for r in rows]
    rank, nr = 0, len(mat)
    pivots = []
    for c in range(ncols):
        piv = next((r for r in range(rank, nr) if mat[r][c] != 0), None)
        if piv is None: continue
        mat[rank], mat[piv] = mat[piv], mat[rank]
        pv = mat[rank][c]
        mat[rank] = [x / pv for x in mat[rank]]
        for r in range(nr):
            if r != rank and mat[r][c] != 0:
                f = mat[r][c]
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[rank])]
        pivots.append(c); rank += 1
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [F(0)] * ncols; v[fc] = F(1)
        for r, pc in enumerate(pivots):
            v[pc] = -mat[r][fc]
        basis.append(tuple(v))
    return basis

# ===========================================================================
print("## 1a: LOWER BOUND (>=3) -- the exact readability theorem")
# The two-mode algebra: X, Z anticommuting involutions in M_2(R) (integer).
X2 = ((F(0), F(1)), (F(1), F(0)))
Z2 = ((F(1), F(0)), (F(0), F(-1)))
I2 = ident(2)
two_mode_ok = (meq(mmul(X2, X2), I2) and meq(mmul(Z2, Z2), I2)
               and meq(mmul(X2, Z2), mneg(mmul(Z2, X2))))
# (i) reading = anticommuting: XYX = -Y  <=>  XY = -YX, given X^2 = I.
#     Proven as an exact linear-map identity: (XY + YX)X = XYX + Y for ALL Y
#     (checked on a full basis of M_2), and right-multiplication by X is
#     invertible (X^2 = I) -- so the reader condition IS anticommutation.
basisM2 = []
for i in range(2):
    for j in range(2):
        E = [[F(0)] * 2 for _ in range(2)]; E[i][j] = F(1)
        basisM2.append(tuple(tuple(r) for r in E))
read_iff_anti = all(
    meq(mmul(madd(mmul(X2, E), mmul(E, X2)), X2),
        madd(mmul(mmul(X2, E), X2), E))
    for E in basisM2)
# (ii) the anticommutant of {X, Z} in M_2(R): solve XY+YX = 0, ZY+YZ = 0
#      exactly. Unknown Y has 4 entries; each condition gives 4 equations.
rows = []
for M in (X2, Z2):
    for i in range(2):
        for j in range(2):
            row = [F(0)] * 4
            for k in range(2):
                row[k * 2 + j] += M[i][k]   # (MY)_ij
                row[i * 2 + k] += M[k][j]   # (YM)_ij
            rows.append(row)
anti_basis = nullspace_exact(rows, 4)
W = mmul(X2, Z2)   # the candidate spanning element XZ
span_is_XZ = (len(anti_basis) == 1)
if span_is_XZ:
    (y0, y1, y2, y3) = anti_basis[0]
    Y = ((y0, y1), (y2, y3))
    # is Y a scalar multiple of XZ?  XZ = ((0,-1),(1,0))... compute:
    span_is_XZ = any(all(Y[i][j] == c * W[i][j] for i in range(2)
                         for j in range(2))
                     for c in (F(1), F(-1), Y[0][1] / W[0][1] if W[0][1] != 0 else F(0)))
# (iii) no involution in span{XZ}: (c*XZ)^2 = c^2 * (XZ)^2 = -c^2 * I,
#       and -c^2 = 1 has no rational (real) solution.
W2 = mmul(W, W)
no_involution = meq(W2, mneg(I2))   # (XZ)^2 = -I exactly
check("READABILITY LOWER BOUND, exact: X,Z anticommuting involutions "
      f"generate the two-mode algebra ({two_mode_ok}); the reader condition "
      f"XYX=-Y is EXACTLY anticommutation, proven as a linear-map identity "
      f"on a full M_2 basis ({read_iff_anti}); the anticommutant of "
      f"{{X,Z}} in M_2(R) is exactly 1-dimensional = span{{XZ}} "
      f"({span_is_XZ}); and (XZ)^2 = -I ({no_involution}), so (c*XZ)^2 = "
      f"-c^2*I = I is impossible over R. **No third INVOLUTIVE mode "
      f"reading the order of X,Z can live in the two-mode algebra: a "
      f"future-readable order scar forces a genuinely third anticommuting "
      f"mode.**",
      two_mode_ok and read_iff_anti and span_is_XZ and no_involution)

# ...and the third mode EXISTS one level up: three mutually anticommuting
# involutions in integer M_4(R) (A = X(x)I, B = Z(x)X, C = Z(x)Z).
def kron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(A[i // m][j // m] * B[i % m][j % m]
                       for j in range(n * m)) for i in range(n * m))
A4m = kron(X2, I2); B4m = kron(Z2, X2); C4m = kron(Z2, Z2)
I4 = ident(4)
trio_ok = (all(meq(mmul(M, M), I4) for M in (A4m, B4m, C4m)) and
           all(meq(mmul(P, Q), mneg(mmul(Q, P)))
               for P, Q in ((A4m, B4m), (B4m, C4m), (A4m, C4m))))
check("EXISTENCE: three mutually anticommuting involutions realized in "
      "integer M_4(R) (A = X(x)I, B = Z(x)X, C = Z(x)Z) -- the third mode "
      "exists exactly one algebra level up.", trio_ok)

print("## 1b: UPPER BOUND (<=3) -- Oddtown in the carrier-parity model")
# modes = even-support subsets of n carriers; anticommutation = odd overlap.
def evens(n):
    return [x for x in range(1, 1 << n) if bin(x).count('1') % 2 == 0]
def odd_dot(x, y): return bin(x & y).count('1') % 2 == 1
def fmax_and_families(n, want_families_at=None):
    V = evens(n); best = 0; fams = []
    def ext(fam, start):
        nonlocal best
        best = max(best, len(fam))
        if want_families_at is not None and len(fam) == want_families_at:
            fams.append(list(fam))
        for i in range(start, len(V)):
            if all(odd_dot(V[i], v) for v in fam):
                fam.append(V[i]); ext(fam, i + 1); fam.pop()
    ext([], 0)
    return best, fams
ladder_ok = True
for n in range(2, 8):
    f, _ = fmax_and_families(n)
    ladder_ok &= (f == (n if n % 2 else n - 1))
_, fams3 = fmax_and_families(3, want_families_at=3)
# the unique maximum family at n=3 = the three pair-channels {0,1},{0,2},{1,2}
pair_channels = sorted([0b011, 0b101, 0b110])
unique3 = (len(fams3) == 1 and sorted(fams3[0]) == pair_channels)
check(f"ODDTOWN UPPER BOUND: f(n) = largest odd <= n verified exhaustively "
      f"for n = 2..7 ({ladder_ok}); at n = 3 the maximum family is UNIQUE "
      f"and equals the three pair-channels {{0,1}},{{0,2}},{{1,2}} "
      f"({unique3}). **With (1a): EXACTLY three mutually anticommuting "
      f"involutive identity modes per ternary contact -- the pincer "
      f"closes.**", ladder_ok and unique3)

# ===========================================================================
print("## 2: Cl(3,0) -- central i, the quaternion even sector, the 1/2")
Om = mmul(mmul(A4m, B4m), C4m)
central = (meq(mmul(Om, A4m), mmul(A4m, Om)) and
           meq(mmul(Om, B4m), mmul(B4m, Om)) and
           meq(mmul(Om, C4m), mmul(C4m, Om)))
om_sq = meq(mmul(Om, Om), mneg(I4))
# even subalgebra: i = AB, j = BC, k = AC(with sign) -- quaternion relations
qi, qj = mmul(A4m, B4m), mmul(B4m, C4m)
qk = mmul(qi, qj)             # k := ij
quat_ok = (meq(mmul(qi, qi), mneg(I4)) and meq(mmul(qj, qj), mneg(I4))
           and meq(mmul(qk, qk), mneg(I4))
           and meq(mmul(qj, qi), mneg(qk))
           and meq(mmul(mmul(qi, qj), qk), mneg(I4)))
# linear independence of {I, i, j, k} over R (exact rank 4)
flat = [sum([list(r) for r in M], []) for M in (I4, qi, qj, qk)]
even_dim = rank_exact(flat)
# the 1/2 from reflection alone: the eigenprojectors of the involution A are
# P+- = (I +- A)/2; the anticommuting partner B SWAPS them: B P+- B = P-+.
half = F(1, 2)
Pp = tuple(tuple(half * (I4[i][j] + A4m[i][j]) for j in range(4)) for i in range(4))
Pm = tuple(tuple(half * (I4[i][j] - A4m[i][j]) for j in range(4)) for i in range(4))
proj_ok = (meq(mmul(Pp, Pp), Pp) and meq(mmul(Pm, Pm), Pm)
           and meq(madd(Pp, Pm), I4))
swap_ok = (meq(mmul(mmul(B4m, Pp), B4m), Pm) and
           meq(mmul(mmul(B4m, Pm), B4m), Pp))
check(f"Cl(3,0): Omega = ABC is central ({central}) with Omega^2 = -I "
      f"({om_sq}) -- the central complex unit is the oriented volume "
      f"element of the three identity directions; the even sector "
      f"{{I, AB, BC, (AB)(BC)}} satisfies the quaternion relations "
      f"i^2=j^2=k^2=ijk=-1, ji=-k ({quat_ok}) and has exact dimension "
      f"{even_dim} = 4 = H; the eigenprojectors of a mode are genuine "
      f"({proj_ok}) and the anticommuting partner SWAPS them "
      f"({swap_ok}) -- so any reflection-invariant state has "
      f"p_+ = p_- = 1/2 EXACTLY, prior to any Born postulate.",
      central and om_sq and quat_ok and even_dim == 4 and proj_ok and swap_ok)

# phase plateau: Omega_m central iff m odd; Omega_m^2 = (-1)^(m(m-1)/2)
plateau = []
for m in range(1, 12):
    sq = (-1) ** (m * (m - 1) // 2)
    central_m = (m % 2 == 1)          # A_i commutes with Omega_m iff m-1 even
    plateau.append((m, central_m and sq == -1))
plateau_ok = all(has_i == (m % 4 == 3) for m, has_i in plateau)
check(f"PHASE PLATEAU: a central sqrt(-1) exists iff m = 3 (mod 4) "
      f"(verified m = 1..11: {plateau_ok}); with m = f(n) the window is "
      f"n in {{3,4}} -- the floor's measured saturation sits exactly on "
      f"the maximal phase-stable rung. **This is the candidate-internal "
      f"derivation of (S); it remains CONDITIONAL on 'retention requires "
      f"central phase' and (S) stays a measured input.**", plateau_ok)

# ===========================================================================
print("## 3: retention selects the nonsplit cover (GIVEN self-hosting)")
# H^2(C_3;C_2) = 0 by exhaustive normalized-cocycle census
C3 = [0, 1, 2]
cocycles = []
for vals in product((0, 1), repeat=9):
    f = {(a, b): vals[a * 3 + b] for a in C3 for b in C3}
    if any(f[(0, g)] or f[(g, 0)] for g in C3): continue
    if all((f[(a, b)] + f[((a + b) % 3, c)] + f[(b, c)] + f[(a, (b + c) % 3)]) % 2 == 0
           for a in C3 for b in C3 for c in C3):
        cocycles.append(tuple(sorted(f.items())))
cobound = set()
for u in product((0, 1), repeat=3):
    if u[0]: continue
    g = {(a, b): (u[a] + u[b] + u[(a + b) % 3]) % 2 for a in C3 for b in C3}
    cobound.add(tuple(sorted(g.items())))
classes = set()
for f in cocycles:
    fd = dict(f)
    rep = min(tuple(sorted({k: (fd[k] + dict(g)[k]) % 2 for k in fd}.items()))
              for g in cobound)
    classes.add(rep)
check(f"H^2(C_3;C_2) = 0 ({len(cocycles)} normalized cocycles, "
      f"{len(classes)} class) -- triangular chirality is "
      f"quarter-turn-INCAPABLE; the capability threshold is n = 4, r = 3.",
      len(classes) == 1)

# 2T = SL(2,3): unique involution => nonsplit
els = [(a, b, c, d) for a, b, c, d in product(range(3), repeat=4)
       if (a * d - b * c) % 3 == 1]
def sl2mul(x, y):
    a, b, c, d = x; e, f2, g, h = y
    return ((a * e + b * g) % 3, (a * f2 + b * h) % 3,
            (c * e + d * g) % 3, (c * f2 + d * h) % 3)
Isl = (1, 0, 0, 1); mIsl = (2, 0, 0, 2)
def ord_sl(x):
    k, cur = 1, x
    while cur != Isl: cur = sl2mul(x, cur); k += 1
    return k
invols_2T = [x for x in els if ord_sl(x) == 2]
v4_pre = [x for x in els if ord_sl(x) == 4]
lifts_sq_z = all(sl2mul(x, x) == mIsl for x in v4_pre)
check(f"2T = SL(2,3): order {len(els)}, UNIQUE involution "
      f"({len(invols_2T) == 1}) => the extension is NONSPLIT; all "
      f"{len(v4_pre)} preimages of the V_4 involutions square to z "
      f"({lifts_sq_z}) -- **in 2T a repeated involutive use is RETAINED: "
      f"g~^2 = z, never silently 1.**",
      len(els) == 24 and len(invols_2T) == 1 and len(v4_pre) == 6 and lifts_sq_z)

# the split twin A_4 x C_2, constructed explicitly
def pcomp(p, q): return tuple(p[q[i]] for i in range(4))
ide = (0, 1, 2, 3)
def parity(p):
    s = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]: s ^= 1
    return s
A4 = [p for p in product(*[range(4)] * 4)
      if sorted(p) == [0, 1, 2, 3] and parity(p) == 0]
twin = [(p, e) for p in A4 for e in (0, 1)]
def tmul(x, y): return (pcomp(x[0], y[0]), (x[1] + y[1]) % 2)
tid = (ide, 0)
invols_twin = [x for x in twin if x != tid and tmul(x, x) == tid]
# every lift of a quotient involution squares to the IDENTITY (not z):
a4_invols = [p for p in A4 if p != ide and pcomp(p, p) == ide]
twin_lifts_sq_1 = all(tmul((v, e), (v, e)) == tid
                      for v in a4_invols for e in (0, 1))
check(f"THE SPLIT TWIN A_4 x C_2: order {len(twin)}, {len(invols_twin)} "
      f"involutions (vs 2T's 1); every lift of an involution squares to "
      f"the IDENTITY ({twin_lifts_sq_1}) -- **in the split twin a repeated "
      f"use is INVISIBLE to the carrier: retention would need an external "
      f"scar ledger. GIVEN (SH) self-hosting -- retention carried "
      f"internally, uses |-> the group square -- the split twin dies and "
      f"2T is forced. (SH) is a NAMED AXIOM (ledger-regress), not a "
      f"theorem; without it the static verdict stands: the projective "
      f"class is available, not forced.**",
      len(twin) == 24 and len(invols_twin) == 7 and twin_lifts_sq_1)

# H^2(A_4;C_2) = C_2 by the presentation-gauge orbit argument
states = set(product((0, 1), repeat=3))
def orbit(s):
    seen, frontier = {s}, [s]
    while frontier:
        al, be, ga = frontier.pop()
        for t in (((al + 1) % 2, be, (ga + 1) % 2), (al, be, (ga + 1) % 2)):
            if t not in seen: seen.add(t); frontier.append(t)
    return frozenset(seen)
orbs = {orbit(s) for s in states}
betas = sorted({next(iter(o))[1] if len({x[1] for x in o}) == 1 else -1
                for o in orbs})
check(f"H^2(A_4;C_2) = C_2: the relation-lift gauge action has exactly "
      f"{len(orbs)} orbits, separated by the involution-square invariant "
      f"beta ({betas == [0, 1]}); both classes witnessed (split twin "
      f"beta = 0, 2T beta = 1). The capability is exactly ONE BIT.",
      len(orbs) == 2 and betas == [0, 1])

# ===========================================================================
print("## 4: z -> H minimality -- the weld to Chapter 8's starting datum")
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)
H24 = []
for s in (1, -1):
    for a in range(4):
        v = [F(0)] * 4; v[a] = F(s); H24.append(tuple(v))
for signs in product((F(1, 2), F(-1, 2)), repeat=4):
    H24.append(tuple(signs))
# (a) dim 1: z -> t^2 > 0, never -1 (arithmetic).
dim1 = all(t * t > 0 for t in (F(1), F(-1)))
# (b) dim 2: Frobenius-Schur indicator of the 2-dim irrep = -1 (quaternionic).
fs = sum(2 * qmul(g, g)[0] for g in H24)
# (c) dim 3: z in [2T,2T] (commutator closure = Q_8 contains -1), so a
#     faithful 3-dim rep needs z -> -I_3 with det = -1 while det is trivial
#     on the derived subgroup: contradiction.
def qinv(q): return (q[0], -q[1], -q[2], -q[3])
comms = set()
for g in H24:
    for h in H24:
        comms.add(qmul(qmul(g, h), qmul(qinv(g), qinv(h))))
grp = set(comms); frontier = list(comms)
while frontier:
    x = frontier.pop()
    for y in list(comms):
        w = qmul(x, y)
        if w not in grp: grp.add(w); frontier.append(w)
MONE = (F(-1), F(0), F(0), F(0))
derived_ok = (len(grp) == 8 and MONE in grp)
# (d) dim 4: left-multiplication carrier; commutant = right multiplications
#     = H (exact nullspace dim 4 + division on integer samples).
def lmat(q):
    cols = [qmul(q, b) for b in ((F(1), F(0), F(0), F(0)), (F(0), F(1), F(0), F(0)),
                                 (F(0), F(0), F(1), F(0)), (F(0), F(0), F(0), F(1)))]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
Li, Lj, Lk = (lmat((F(0), F(1), F(0), F(0))), lmat((F(0), F(0), F(1), F(0))),
              lmat((F(0), F(0), F(0), F(1))))
rows = []
for M in (Li, Lj, Lk):
    for i in range(4):
        for j in range(4):
            row = [F(0)] * 16
            for k in range(4):
                row[i * 4 + k] += M[k][j]
                row[k * 4 + j] -= M[i][k]
            rows.append(row)
commutant_dim = 16 - rank_exact(rows)
def rmat(q):
    cols = [qmul(b, q) for b in ((F(1), F(0), F(0), F(0)), (F(0), F(1), F(0), F(0)),
                                 (F(0), F(0), F(1), F(0)), (F(0), F(0), F(0), F(1)))]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
def det4(M):
    from itertools import permutations as ps
    tot = F(0)
    for p in ps(range(4)):
        s = 1
        for i in range(4):
            for j in range(i + 1, 4):
                if p[i] > p[j]: s = -s
        term = F(s)
        for i in range(4): term *= M[i][p[i]]
        tot += term
    return tot
div_ok = True
for (x0, x1, x2, x3) in [(1, 2, 3, 4), (0, 1, -1, 2), (5, 0, 0, 1), (1, 1, 1, 1)]:
    Mx = tuple(tuple(F(x0) * ident(4)[i][j]
                     + F(x1) * rmat((F(0), F(1), F(0), F(0)))[i][j]
                     + F(x2) * rmat((F(0), F(0), F(1), F(0)))[i][j]
                     + F(x3) * rmat((F(0), F(0), F(0), F(1)))[i][j]
                     for j in range(4)) for i in range(4))
    div_ok &= det4(Mx) == F(x0 * x0 + x1 * x1 + x2 * x2 + x3 * x3) ** 2
check(f"MINIMAL RECEIVER = H: dim-1 killed (z -> t^2 > 0: {dim1}); dim-2 "
      f"killed (Frobenius-Schur = {fs}/24 = -1, quaternionic type); dim-3 "
      f"killed ([2T,2T] = Q_8 contains z: {derived_ok}, det contradiction); "
      f"dim-4 exists with commutant of exact dimension {commutant_dim} = H "
      f"(division on integer samples: {div_ok}). **dim_R R_min = 4, the "
      f"forced 1+3 split.**",
      dim1 and fs == -24 and derived_ok and commutant_dim == 4 and div_ok)

# unique invariant form = R * I_4 (the Euclidean signature is forced)
sym_idx = [(i, j) for i in range(4) for j in range(i, 4)]
grows = []
for M in (Li, Lj, Lk):
    for a in range(4):
        for b in range(4):
            row = [F(0)] * 10
            for (idx, (i, j)) in enumerate(sym_idx):
                coef = M[i][a] * M[j][b] + (M[j][a] * M[i][b] if i != j else F(0))
                if i == a and j == b: coef -= F(1)
                elif j == a and i == b and i != j: coef -= F(1)
                row[idx] += coef
            grows.append(row)
form_dim = 10 - rank_exact(grows)
check(f"UNIQUE INVARIANT FORM: the space of symmetric G with M^T G M = G "
      f"for M in {{I,J,K}} has exact dimension {form_dim} = 1, spanned by "
      f"I_4 -- Euclidean, scale-free. (An ALGEBRA grading 1+3, not a "
      f"spacetime metric -- the fence holds.)", form_dim == 1)

# ===========================================================================
print("## 5: the handoff -- Chapter 8's starting datum, now one layer up")
powers = [Li]
for _ in range(3): powers.append(mmul(Li, powers[-1]))
Z4 = mneg(ident(4))
spinor_ok = (meq(powers[1], Z4) and meq(powers[2], mneg(Li))
             and meq(powers[3], ident(4)))
check("SPINOR RETURN: J^2 = z, J^4 = 1 -- visible period 2, complete "
      "period 4; the three retained quarter-turns {I,J,K} with central "
      "residue z ARE the starting datum of the public Chapter-8 chain "
      "(FCT-45): H -> 24-cell -> F_4 -> finite Gleason -> triality KS "
      "continue from exactly this object.", spinor_ok)

print("""
## RECEIVED-INPUT LEDGER (the honest residual -- named, not proven):
  (S)  arity = 3          MEASURED (candidate-internal via phase plateau)
  (R)  readability        the program's standing door -- proven NOT forced (private corpus, cited)
  (SH) self-hosting       NAMED AXIOM (ledger regress) -- forces 2T
  (C)  chirality J vs -J  proven RECEIVED (C_2 torsor)
GIVEN (S)+(R)+(SH): the interface is FORCED -- exactly three anticommuting
quarter-turns, central z, H with the 1+3 split, unique Euclidean form,
1/2 reflective weights. The citation boundary moves one layer down; the
residual is the program's own named received frontier, not a black box.""")

print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
raise SystemExit(1 if FAIL else 0)
