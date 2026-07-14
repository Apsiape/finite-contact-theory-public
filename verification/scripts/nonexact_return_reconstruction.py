#!/usr/bin/env python3
"""Chapter 8 — the non-exact-return reconstruction.

Dependency-free (Python standard library only), exact arithmetic
throughout (fractions.Fraction; exhaustive enumeration; no floating-point
value is load-bearing). Verifies, from a retained contact interface, the
finite state/receiver closure and its measurement calculus:

  1. the primitive receiver is the quaternions H (minimal real dimension
     four; forced 1+3 split; unique invariant positive form);
  2. its unit state orbit is the 24-cell, whose polar dual is again a
     24-cell (an exact self-hosting state<->receiver fixed point);
  3. the 48 combined vectors are the F_4 root system (Weyl order 1152);
  4. every nonzero state/receiver contact has |<p,r>|^2/(|p|^2 |r|^2) =
     1/2 (the first forced scale-free interface magnitude);
  5. FINITE GLEASON: the 24 rays carry exactly 24 orthonormal tetrad
     contexts; the context-incidence rank is 15, so every normalized
     frame valuation is uniquely tr(rho P) for a real symmetric
     trace-one rho -- the quadratic Born frame rule, with no continuum
     and no continuity assumption;
  6. TRIALITY CONTEXTUALITY: no global deterministic noncontextual
     assignment exists; there are exactly 16 minimal nine-context parity
     proofs, all lying in the state<->receiver ("mixed") interface, and
     the obstruction is irreducibly three-way (D_4 triality).

Named incumbents (recovered here in a derivational role, not posited):
the Hurwitz unit quaternions / 24-cell; the F_4 root system; Gleason's
theorem (real, finite form); the Peres 24-ray Kochen-Specker set and its
Kernaghan-type nine-basis parity proofs.

Scope: real symmetric operators on R^4 (a real-quantum cell). This does
not derive complex quantum mechanics, the actuality of one outcome, or
the universal Born rule; see the chapter for the exact fences.
"""
from fractions import Fraction as F
from itertools import combinations, product

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def dot(a, b): return sum(x * y for x, y in zip(a, b))

# ---- quaternions on the basis 1, i, j, k (exact) -------------------------
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1,
            a0*b3 + a1*b2 - a2*b1 + a3*b0)
def lmat(q):
    cols = [qmul(q, e) for e in ((F(1),F(0),F(0),F(0)), (F(0),F(1),F(0),F(0)),
                                 (F(0),F(0),F(1),F(0)), (F(0),F(0),F(0),F(1)))]
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))
def mmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4))
                 for i in range(4))
def mneg(A): return tuple(tuple(-x for x in r) for r in A)
I4 = tuple(tuple(F(1) if i == j else F(0) for j in range(4)) for i in range(4))
Li = lmat((F(0), F(1), F(0), F(0)))
Lj = lmat((F(0), F(0), F(1), F(0)))
Lk = lmat((F(0), F(0), F(0), F(1)))

def rank_exact(rows):
    mat = [list(r) for r in rows]
    rk, nr = 0, len(mat)
    nc = len(mat[0]) if mat else 0
    for c in range(nc):
        piv = next((r for r in range(rk, nr) if mat[r][c] != 0), None)
        if piv is None: continue
        mat[rk], mat[piv] = mat[piv], mat[rk]
        pv = mat[rk][c]
        mat[rk] = [x / pv for x in mat[rk]]
        for r in range(nr):
            if r != rk and mat[r][c] != 0:
                f = mat[r][c]
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[rk])]
        rk += 1
    return rk

print("## 1: the primitive receiver is the quaternions H")
sq_ok = (mmul(Li, Li) == mneg(I4) and mmul(Lj, Lj) == mneg(I4)
         and mmul(Lk, Lk) == mneg(I4))
mul_ok = (mmul(Li, Lj) == Lk and mmul(Li, Lj) == mneg(mmul(Lj, Li)))
# commutant of {I,J,K} inside 4x4 real matrices has dimension 4 (= H, a
# real division algebra), so the representation is irreducible.
rows = []
for M in (Li, Lj, Lk):
    for i in range(4):
        for j in range(4):
            row = [F(0)]*16
            for k in range(4):
                row[i*4+k] += M[k][j]
                row[k*4+j] -= M[i][k]
            rows.append(row)
commutant_dim = 16 - rank_exact(rows)
# unique invariant symmetric form: G with M^T G M = G for M in {I,J,K}
sym_idx = [(i, j) for i in range(4) for j in range(i, 4)]
grows = []
for M in (Li, Lj, Lk):
    for a in range(4):
        for b in range(4):
            row = [F(0)]*10
            for idx, (i, j) in enumerate(sym_idx):
                coef = M[i][a]*M[j][b] + (M[j][a]*M[i][b] if i != j else F(0))
                if (i, j) == (a, b): coef -= F(1)
                elif (j, i) == (a, b) and i != j: coef -= F(1)
                row[idx] += coef
            grows.append(row)
form_dim = 10 - rank_exact(grows)
check("the three retained quarter-turns satisfy I^2=J^2=K^2=-1 and IJ=K=-JI "
      f"(quaternion relations: {sq_ok and mul_ok}); their real commutant has "
      f"dimension {commutant_dim} = H (a division algebra, so the 4-real-"
      f"dimensional carrier is irreducible and minimal); the invariant "
      f"symmetric positive form is unique up to scale (dimension {form_dim}) "
      f"= c*I_4, forcing the isotropic quadratic evaluation N=c(x0^2+..+x3^2). "
      f"The receiver carries a forced 1+3 split: one return-even direction "
      f"plus three noncommuting quarter-turns.",
      sq_ok and mul_ok and commutant_dim == 4 and form_dim == 1)

print("## 2: the 24-cell state orbit and its self-dual receiver pole")
P24 = []
for s in (1, -1):
    for a in range(4):
        v = [F(0)]*4; v[a] = F(s); P24.append(tuple(v))
for signs in product((F(1,2), F(-1,2)), repeat=4):
    P24.append(tuple(signs))
R24 = []
for i in range(4):
    for j in range(i+1, 4):
        for si in (1, -1):
            for sj in (1, -1):
                v = [F(0)]*4; v[i] = F(si); v[j] = F(sj); R24.append(tuple(v))
def polar_vertices(constraints):
    verts = set()
    for quad in combinations(range(len(constraints)), 4):
        M = [list(constraints[q]) + [F(1)] for q in quad]
        n = 4
        singular = False
        for c in range(n):
            piv = next((r for r in range(c, n) if M[r][c] != 0), None)
            if piv is None: singular = True; break
            M[c], M[piv] = M[piv], M[c]
            pv = M[c][c]
            M[c] = [x / pv for x in M[c]]
            for r in range(n):
                if r != c and M[r][c] != 0:
                    f = M[r][c]
                    M[r] = [a - f*b for a, b in zip(M[r], M[c])]
        if singular: continue
        y = tuple(M[r][4] for r in range(4))
        if all(dot(p, y) <= 1 for p in constraints):
            verts.add(y)
    return verts
dualP = polar_vertices(P24)
dualR = polar_vertices(R24)
check(f"the 24 unit states are the Hurwitz units (the 24-cell); exhaustive "
      f"polar enumeration over all C(24,4)=10626 supporting quadruples gives "
      f"conv(states)^o = the 24 receiver vectors ({dualP == set(R24)}) and "
      f"conv(receivers)^o = the 24 states ({dualR == set(P24)}). States "
      f"generate receivers and receivers regenerate the states: an exact "
      f"self-hosting state<->receiver fixed point.",
      dualP == set(R24) and dualR == set(P24))

print("## 3: the 48 vectors are the F_4 root system")
roots = list(P24) + list(R24)
rootset = set(roots)
closed, integral = True, True
for a in roots:
    na = dot(a, a)
    for b in roots:
        cart = F(2) * dot(a, b) / na
        if cart.denominator != 1: integral = False
        refl = tuple(x - cart * y for x, y in zip(b, a))
        if refl not in rootset: closed = False
simples = [(F(0),F(1),F(-1),F(0)), (F(0),F(0),F(1),F(-1)),
           (F(0),F(0),F(0),F(1)), (F(1,2),F(-1,2),F(-1,2),F(-1,2))]
def refl_mat(a):
    na = dot(a, a)
    return tuple(tuple((F(1) if i == j else F(0)) - F(2)*a[i]*a[j]/na
                       for j in range(4)) for i in range(4))
gens = [refl_mat(a) for a in simples]
W = set(gens) | {I4}
frontier = list(gens)
while frontier:
    x = frontier.pop()
    for g in gens:
        y = mmul(g, x)
        if y not in W: W.add(y); frontier.append(y)
check(f"the 48 combined state+receiver vectors are reflection-closed "
      f"({closed}) with integer Cartan numbers ({integral}); the four simple "
      f"reflections generate a group of order {len(W)} = 1152 = |W(F_4)|. The "
      f"exceptional root system arises as the reflection closure of the "
      f"state/receiver polarity, not as an installed symmetry.",
      closed and integral and len(W) == 1152)

print("## 4: the first forced scale-free interface magnitude is 1/2")
vals = set()
for p in P24:
    for r in R24:
        v = dot(p, r)
        if v != 0: vals.add(abs(v))
check(f"every nonzero state/receiver overlap has |<p,r>| = 1 exactly "
      f"({vals == {F(1)}}); with |p|^2=1 and |r|^2=2 the dimensionless "
      f"contact ratio |<p,r>|^2/(|p|^2|r|^2) = 1/2 for every contact (a "
      f"pi/4 angle). This is a forced, scale-free, gauge-free interface "
      f"invariant -- the first nontrivial magnitude the closure generates. "
      f"Scope: this 24-cell closure, not nature.",
      vals == {F(1)})

# ---- the 24 rays (as lines) and their orthogonal contexts ----------------
# The Peres set: 24 rays = 12 state-pole lines + 12 receiver-pole lines
# (one representative per antipodal pair). These are the projective lines
# carried by the F_4 vectors above; the polytope sections use the 48
# signed vectors, the measurement sections use the 24 lines.
srays = []
for i in range(4):
    v = [F(0)]*4; v[i] = F(1); srays.append(tuple(v))
for signs in product((F(1), F(-1)), repeat=3):
    srays.append((F(1), signs[0], signs[1], signs[2]))
rrays = []
for i in range(4):
    for j in range(i+1, 4):
        for s in (F(1), F(-1)):
            v = [F(0)]*4; v[i] = F(1); v[j] = s; rrays.append(tuple(v))
rays = srays + rrays
NS = len(srays)
contexts = [q for q in combinations(range(24), 4)
            if all(dot(rays[a], rays[b]) == 0 for a, b in combinations(q, 2))]

print("## 5: FINITE GLEASON -- the Born frame rule is forced")
B = [[F(1) if x in C else F(0) for x in range(24)] for C in contexts]
rankB = rank_exact(B)
projs = []
proj_rows = []
for q in rays:
    nq = dot(q, q)
    Pj = tuple(tuple(q[i]*q[j]/nq for j in range(4)) for i in range(4))
    projs.append(Pj)
    proj_rows.append([Pj[i][j] for (i, j) in sym_idx])
span = rank_exact(proj_rows)
res_ok = all(
    all(sum(projs[x][i][j] for x in C) == (F(1) if i == j else F(0))
        for i in range(4) for j in range(4))
    for C in contexts)
check(f"the 24 rays carry exactly {len(contexts)} orthonormal tetrad contexts; "
      f"the context-incidence rank is {rankB}, so normalized frame valuations "
      f"form a {24 - rankB}-dimensional affine family -- the dimension of "
      f"real symmetric trace-one 4x4 operators; the 24 ray projectors span "
      f"all of Sym(4) (rank {span}) and every context resolves the identity "
      f"({res_ok}). Therefore every normalized frame valuation is uniquely "
      f"f(x)=tr(rho P_x). The quadratic Born frame rule is forced by the "
      f"finite context family alone -- no continuum, no continuity.",
      len(contexts) == 24 and rankB == 15 and span == 10 and res_ok)

print("## 6: TRIALITY CONTEXTUALITY -- probability lives where pointing cannot")
ctx_sets = [set(C) for C in contexts]
def has_global_section(active):
    ordered = sorted(active, key=lambda ci: len(ctx_sets[ci]))
    val = {}
    def bt(k):
        if k == len(ordered): return True
        for pick in contexts[ordered[k]]:
            if val.get(pick) == 0: continue
            newly = []
            ok = True
            if val.get(pick) is None: val[pick] = 1; newly.append(pick)
            for other in contexts[ordered[k]]:
                if other == pick: continue
                if val.get(other) == 1: ok = False; break
                if val.get(other) is None: val[other] = 0; newly.append(other)
            if ok and bt(k + 1): return True
            for x in newly: del val[x]
        return False
    return bt(0)
no_global = not has_global_section(range(len(contexts)))
mixed_idx = [ci for ci, C in enumerate(contexts)
             if 0 < sum(1 for x in C if x < NS) < 4]
proofs = []
for combo in combinations(range(len(contexts)), 9):
    deg = [0]*24
    for ci in combo:
        for x in contexts[ci]: deg[x] += 1
    if all(d in (0, 2) for d in deg):
        proofs.append(combo)
all_in_mixed = all(set(pr) <= set(mixed_idx) for pr in proofs)
def sector(q):
    if sum(1 for x in q if x != 0) == 1: return "v"
    return "s" if sum(1 for x in q[1:] if x < 0) % 2 == 0 else "c"
def mixed_sector(ci):
    return sector(rays[[x for x in contexts[ci] if x < NS][0]])
proof_split_ok = all(
    sum(1 for ci in pr if mixed_sector(ci) == sct) == 3
    for pr in proofs for sct in ("v", "s", "c"))
def sector_ids(secs):
    ids = [ci for ci, C in enumerate(contexts) if ci not in mixed_idx]
    ids += [ci for ci in mixed_idx if mixed_sector(ci) in secs]
    return ids
one_ok = all(has_global_section(sector_ids([s])) for s in ("v", "s", "c"))
two_ok = all(has_global_section(sector_ids(list(p)))
             for p in (("v","s"), ("s","c"), ("v","c")))
three_no = not has_global_section(sector_ids(["v", "s", "c"]))
check(f"no global deterministic noncontextual assignment exists "
      f"({no_global}, exhaustive); there are exactly {len(proofs)} minimal "
      f"nine-context parity proofs, ALL inside the state<->receiver interface "
      f"({all_in_mixed}) and each using three contexts from every D_4 "
      f"triality sector ({proof_split_ok}); any one or two sectors admit a "
      f"global assignment ({one_ok and two_ok}) while all three together do "
      f"not ({three_no}). Neither pole is contextual alone -- contextuality "
      f"is an irreducibly three-way (triality) obstruction generated at the "
      f"interface. The valuation is uniquely lawful exactly where a global "
      f"pointing is impossible.",
      no_global and len(proofs) == 16 and all_in_mixed and proof_split_ok
      and one_ok and two_ok and three_no)

print()
print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
raise SystemExit(1 if FAIL else 0)
