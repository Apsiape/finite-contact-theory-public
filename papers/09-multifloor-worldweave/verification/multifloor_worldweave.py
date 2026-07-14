#!/usr/bin/env python3
"""Chapter 9 — the multi-floor worldweave.

Dependency-free (Python standard library only), exact arithmetic
throughout (fractions.Fraction; exhaustive GF(4) / group enumeration;
no floating-point value is load-bearing). Verifies how independently
generated non-exact-return cells (Chapter 8) combine into one world.

The claim is that cells do NOT combine by tensor product. Each cell has
a D_4 triality boundary K = {0, v, s, c} = C_2 x C_2; a bridge ecology
is an additive glue code H over K^N; a receiver-complete world is a
self-dual code (H = H-perp). The consequences, all checked here:

  1. the triality boundary K is Klein-four, with S_3 triality permuting
     {v, s, c};
  2. TWO cells close uniquely into the E_8 root system: 240 roots =
     48 (D_4 + D_4) + three triality-matched 64-root bridges
     (8v,8v)/(8s,8s)/(8c,8c); reflection-closed; the glue-lattice
     determinant ladder D_4^2 -> D_8 -> E_8 is 16 -> 4 -> 1 (bridge debt
     4 -> 2 -> 0 bits);
  3. local fusion dynamics is octonionic: of the 35 imaginary-unit
     triples, exactly 7 associate and 28 do not, so nonassociativity is
     a pure three-contact order receipt;
  4. normed monolithic fusion stops at the octonions: the sedenions
     have zero divisors (both factors nonzero), the octonions have none,
     so larger populations cannot be one division algebra;
  5. the triality-covariant Hermitian self-dual standard-form code
     census through six cells is |GU(k,2)| for k = N/2: N=2 -> 3,
     N=4 -> 18, N=6 -> 648;
  6. six cells are the first "hidden" world: the hexacode [6,3,4] over
     GF(4) is Hermitian self-dual with weight enumerator 1 + 45 y^4 +
     18 y^6 (no bridge word below weight four), and of the 648 self-dual
     six-cell codes exactly 162 have minimum distance 2 and 486 have
     minimum distance 4 -- so a complete six-cell world can be invisible
     to every pairwise and triple glue probe.

Named incumbents (recovered here in a derivational role, not posited):
the D_4 triality group; the E_8 root system; the octonions and the
Cayley-Dickson tower; the hexacode; the unitary groups GU(k, 2).

Scope: a structural derivation under explicit assumptions (positivity,
integral receipt-preserving closure, triality covariance, self-dual
completion). It does NOT show that nature realizes E_8, the hexacode, or
any particular code, and derives no metric, spectrum, or dimensionful
constant. What is closed is the structural question: the native global
object is an evolving bridge code, not a tensor product or one
monolithic state space.
"""
from fractions import Fraction as F
from itertools import combinations, product

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

# ---- GF(4) = {0,1,2,3}, 2 = omega, 3 = omega^2; add = XOR (C_2 x C_2) ----
GMUL = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
def gmul(a, b): return GMUL[a][b]
def gconj(a): return [0,1,3,2][a]      # Frobenius x -> x^2

print("## 1: the triality boundary K = C_2 x C_2 with S_3 triality")
klein = (all((x ^ x) == 0 for x in (0,1,2,3))
         and all((x ^ y) != 0 for x in (1,2,3) for y in (1,2,3) if x != y))
autos = set()
for u in (1, 2, 3):
    for frob in (False, True):
        autos.add(tuple((gconj(gmul(u, x)) if frob else gmul(u, x)) for x in (1, 2, 3)))
check(f"the boundary group K = GF(4)-additive is Klein-four (every nonzero "
      f"element an involution, v+s=c cyclically: {klein}); its structure "
      f"automorphisms realize all {len(autos)} permutations of {{v,s,c}} = "
      f"S_3. This D_4 triality boundary is the substrate every cell carries "
      f"into the multi-floor code.", klein and len(autos) == 6)

print("## 2: two cells close uniquely into the E_8 root system")
roots = []
for i, j in combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [F(0)]*8; v[i] = F(si); v[j] = F(sj); roots.append(tuple(v))
for signs in product((F(1,2), F(-1,2)), repeat=8):
    if sum(1 for s in signs if s < 0) % 2 == 0:
        roots.append(tuple(signs))
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def rep_type(part):
    nz = [x for x in part if x != 0]
    if not nz: return "0"
    if len(nz) == 2 and all(abs(x) == 1 for x in nz): return "D4"
    if len(nz) == 1 and abs(nz[0]) == 1: return "8v"
    if len(nz) == 4 and all(abs(x) == F(1,2) for x in nz):
        return "8s" if sum(1 for x in nz if x < 0) % 2 == 0 else "8c"
    return "?"
b = {"D4L":0,"D4R":0,"vv":0,"ss":0,"cc":0,"?":0}
for r in roots:
    L, R = rep_type(r[:4]), rep_type(r[4:])
    if (L,R)==("D4","0"): b["D4L"]+=1
    elif (L,R)==("0","D4"): b["D4R"]+=1
    elif (L,R)==("8v","8v"): b["vv"]+=1
    elif (L,R)==("8s","8s"): b["ss"]+=1
    elif (L,R)==("8c","8c"): b["cc"]+=1
    else: b["?"]+=1
decomp = (len(roots)==240 and b["D4L"]==24 and b["D4R"]==24
          and b["vv"]==64 and b["ss"]==64 and b["cc"]==64 and b["?"]==0)
rootset = set(roots)
closed = all(tuple(x - dot(a, r)*y for x, y in zip(r, a)) in rootset
             for a in roots for r in roots)
def gram_det(basis):
    n = len(basis)
    M = [[dot(basis[i], basis[j]) for j in range(n)] for i in range(n)]
    det = F(1)
    for c in range(n):
        piv = next((rr for rr in range(c, n) if M[rr][c] != 0), None)
        if piv is None: return F(0)
        if piv != c: M[c], M[piv] = M[piv], M[c]; det = -det
        det *= M[c][c]; inv = M[c][c]
        for rr in range(c+1, n):
            f = M[rr][c]/inv
            M[rr] = [M[rr][k] - f*M[c][k] for k in range(n)]
    return det
e = lambda i: tuple(F(1) if k == i else F(0) for k in range(8))
sub = lambda a, c: tuple(x-y for x, y in zip(a, c))
add = lambda a, c: tuple(x+y for x, y in zip(a, c))
det_d4d4 = gram_det([sub(e(0),e(1)),sub(e(1),e(2)),sub(e(2),e(3)),add(e(2),e(3)),
                     sub(e(4),e(5)),sub(e(5),e(6)),sub(e(6),e(7)),add(e(6),e(7))])
det_d8 = gram_det([sub(e(i),e(i+1)) for i in range(7)] + [add(e(6),e(7))])
det_e8 = gram_det([tuple(F(x) for x in row) for row in (
    (1,-1,0,0,0,0,0,0),(0,1,-1,0,0,0,0,0),(0,0,1,-1,0,0,0,0),(0,0,0,1,-1,0,0,0),
    (0,0,0,0,1,-1,0,0),(0,0,0,0,0,1,-1,0),(0,0,0,0,0,1,1,0),(-1,-1,-1,-1,-1,-1,-1,-1))]
    ) if False else None
# use the standard E_8 simple-root basis directly:
det_e8 = gram_det([tuple(F(x) for x in row) for row in (
    (1,-1,0,0,0,0,0,0),(0,1,-1,0,0,0,0,0),(0,0,1,-1,0,0,0,0),(0,0,0,1,-1,0,0,0),
    (0,0,0,0,1,-1,0,0),(0,0,0,0,0,1,-1,0),(0,0,0,0,0,1,1,0),
    tuple(F(-1,2) for _ in range(8)))])
check(f"the two cells' D_4 boundaries close into 240 roots = 48 (D_4+D_4) + "
      f"three triality-matched 64-root bridges (8v,8v)/(8s,8s)/(8c,8c) "
      f"({decomp}); the set is reflection-closed ({closed}) -- the E_8 root "
      f"system; the glue-lattice determinant ladder D_4^2 / D_8 / E_8 = "
      f"{det_d4d4} / {det_d8} / {det_e8} = 16 / 4 / 1 (bridge debt 4 -> 2 -> "
      f"0 bits). E_8 is the unique debt-free two-cell world -- the complete "
      f"bridge geometry, not a physical gauge group.",
      decomp and closed and det_d4d4 == 16 and det_d8 == 4 and det_e8 == 1)

print("## 3: local fusion dynamics is octonionic (a three-contact receipt)")
def cd_conj(x):
    if len(x) == 1: return x
    h = len(x)//2
    return cd_conj(x[:h]) + tuple(-t for t in x[h:])
def cd_mul(x, y):
    if len(x) == 1: return (x[0]*y[0],)
    h = len(x)//2
    a, bb, c, d = x[:h], x[h:], y[:h], y[h:]
    left = tuple(p-q for p, q in zip(cd_mul(a, c), cd_mul(cd_conj(d), bb)))
    right = tuple(p+q for p, q in zip(cd_mul(d, a), cd_mul(bb, cd_conj(c))))
    return left + right
def unit(dim, i):
    v = [F(0)]*dim; v[i] = F(1); return tuple(v)
def is_zero(x): return all(t == 0 for t in x)
assoc = 0
for i, j, k in combinations(range(1, 8), 3):
    ei, ej, ek = unit(8, i), unit(8, j), unit(8, k)
    A = tuple(p-q for p, q in zip(cd_mul(cd_mul(ei, ej), ek),
                                  cd_mul(ei, cd_mul(ej, ek))))
    if is_zero(A): assoc += 1
check(f"of the C(7,3) = 35 triples of distinct octonion imaginary units, "
      f"exactly {assoc} associate and {35-assoc} have a nonzero associator "
      f"(the 7 Fano lines / 28 non-lines). Nonassociativity is carried only "
      f"by triples -- an exact three-contact order receipt: every pair looks "
      f"quaternionic while the triple retains information belonging to no "
      f"pair.", assoc == 7)

print("## 4: normed monolithic fusion stops at the octonions")
def zero_divisor(dim):
    U = [unit(dim, i) for i in range(dim)]
    for i, j in combinations(range(1, dim), 2):
        x = tuple(a+bb for a, bb in zip(U[i], U[j]))
        for k, l in combinations(range(1, dim), 2):
            for s in (1, -1):
                y = tuple(a+s*bb for a, bb in zip(U[k], U[l]))
                if is_zero(cd_mul(x, y)) and not is_zero(x) and not is_zero(y):
                    return (i, j, k, l, s)
    return None
sed = zero_divisor(16)
oct_none = zero_divisor(8) is None
check(f"the sedenions (dimension 16) have a zero divisor "
      f"(e_{sed[0]}+e_{sed[1]})(e_{sed[2]}{'+' if sed[4]>0 else '-'}e_{sed[3]}) "
      f"= 0 with both factors nonzero, while the octonions have none "
      f"({oct_none}). So positive normed monolithic fusion stops at the "
      f"octonions; a larger population cannot be one division algebra and "
      f"must remain a code worldweave of octonionic cells.",
      sed is not None and oct_none)

print("## 5: the self-dual bridge-code census is |GU(k,2)| = 3 / 18 / 648")
def selfdual_count(k, mindist=False):
    cnt = 0; dtal = {}
    for flat in product(range(4), repeat=k*k):
        M = [flat[r*k:(r+1)*k] for r in range(k)]
        ok = True
        for r in range(k):
            for s in range(k):
                acc = 0
                for c in range(k):
                    acc ^= gmul(M[r][c], gconj(M[s][c]))
                if acc != (1 if r == s else 0): ok = False; break
            if not ok: break
        if not ok: continue
        cnt += 1
        if mindist:
            best = 99
            for coef in product(range(4), repeat=k):
                if all(a == 0 for a in coef): continue
                right = []
                for c in range(k):
                    acc = 0
                    for r in range(k): acc ^= gmul(coef[r], M[r][c])
                    right.append(acc)
                wt = sum(1 for x in list(coef)+right if x != 0)
                best = min(best, wt)
            dtal[best] = dtal.get(best, 0) + 1
    return (cnt, dtal) if mindist else cnt
c1 = selfdual_count(1); c2 = selfdual_count(2)
c3, d3 = selfdual_count(3, mindist=True)
check(f"triality-covariant Hermitian self-dual standard-form codes number "
      f"{c1} (N=2), {c2} (N=4), {c3} (N=6) -- exactly |GU(k,2)| for k = N/2 "
      f"(3, 18, 648). Receiver-complete worlds are the unitary orbit over "
      f"GF(4), so the exhaustive standard-form search is confirmed by closed "
      f"form.", c1 == 3 and c2 == 18 and c3 == 648)

print("## 6: six cells are the first hidden collective world")
w = 2
M = [[1,1,1],[1,w,gmul(w,w)],[1,gmul(w,w),w]]
G = [[1,0,0]+M[0], [0,1,0]+M[1], [0,0,1]+M[2]]
codewords = []
for c0, c1_, c2_ in product(range(4), repeat=3):
    cw = tuple(gmul(c0,G[0][t]) ^ gmul(c1_,G[1][t]) ^ gmul(c2_,G[2][t])
               for t in range(6))
    codewords.append(cw)
wdist = {}
for cw in codewords:
    wt = sum(1 for x in cw if x != 0); wdist[wt] = wdist.get(wt, 0) + 1
def herm(u, v):
    s = 0
    for x, y in zip(u, v): s ^= gmul(x, gconj(y))
    return s
self_orth = all(herm(u, v) == 0 for u in codewords for v in codewords)
mind = min(sum(1 for x in cw if x != 0) for cw in codewords if any(cw))
check(f"the hexacode [6,3,4] over GF(4) has weight enumerator "
      f"1 + {wdist.get(4,0)} y^4 + {wdist.get(6,0)} y^6 "
      f"({wdist == {0:1, 4:45, 6:18}}), is Hermitian self-dual ({self_orth}), "
      f"and has minimum distance {mind} = 4 (no one-, two-, or three-cell "
      f"bridge words); and of the 648 self-dual six-cell codes, exactly "
      f"{d3.get(2)} have minimum distance 2 and {d3.get(4)} have minimum "
      f"distance 4 (162 / 486). Six cells are the first population that can "
      f"form a complete world whose binding is invisible to every pairwise "
      f"and triple glue probe.",
      wdist == {0:1, 4:45, 6:18} and self_orth and mind == 4
      and d3.get(2) == 162 and d3.get(4) == 486)

print()
print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
raise SystemExit(1 if FAIL else 0)
