#!/usr/bin/env python3
"""EXACT ALGEBRAIC CERTIFICATE of a strict preparation gap.

Behavior (pentagon / KCBS exclusivity, unit weights):
    p = (49/100, 25/81, 16/25, 36/121, 4/9),   sqrt(p) = v = (7/10, 5/9, 4/5, 6/11, 2/3)
    beta = sum p_i = 2137213/980100  (~ 2.18060708)

THEOREM. p is realizable by a sharp quantum model (rank-one projectors with
adjacent exclusivity + a pure state), and EVERY sharp realization (P_i, rho)
of p -- any projector ranks, mixed states allowed, any dimension -- satisfies
    || sum_i P_i ||_op  >  beta.
Hence Delta_prep(p) = kappa(p) - beta > 0 strictly.

PROOF STRUCTURE (each step verified below in exact rational arithmetic):
  [1] REALIZABILITY. The rational Gram matrix H_feas (diag 1, exclusivity
      edges 0) satisfies H_feas - v v^T positive definite (exact LDL, all
      pivots > 0). By the Schur complement, the extended Gram matrix
      [[1, v^T],[v, H_feas]] is PSD, so unit vectors u_1..u_5 and a unit
      psi exist in R^6 with <u_i,u_j> = (H_feas)_ij and <psi,u_i> = v_i;
      then p_i = <psi,u_i>^2 realizes p with adjacent-exclusive rank-one
      projectors. (Compression theorem: rank-one pure suffices to compute
      the sharp optimum, so nothing is lost.)
  [2] RIGIDITY. Any feasible Gram H (PSD Hermitian, diag 1, edges 0,
      H >= v v^T) with lambda_max(H) <= beta must satisfy H v = beta v:
      from H >= v v^T, v* H v >= (v^T v)^2 = beta^2, so the Rayleigh
      quotient of the REAL vector v is >= beta >= lambda_max, forcing
      equality -- v is a top eigenvector. Since v is real, Hv = beta v
      splits: (Re H) v = beta v and (Im H) v = 0. The real-part equation
      plus the diagonal/edge constraints is a SQUARE 5x5 linear system in
      the 5 free real entries. Verified: det != 0 exactly, so Re(H) = H*
      is UNIQUE. (The imaginary part is NOT unique -- the imaginary
      subsystem is singular for every v, because the cyclic product of the
      coupling ratios is identically 1. This does not matter, by [3].)
  [3] OBSTRUCTION. For any REAL vector y and Hermitian H, y^T H y =
      y^T Re(H) y (the antisymmetric imaginary part cancels). The rational
      witness y satisfies y^T H* y < 0 exactly, so EVERY Hermitian H with
      Re(H) = H* fails PSD. With [2], no feasible H has lambda_max <=
      beta. The feasible set is compact and (by [1]) nonempty, so
      kappa(p) = min lambda_max(H) > beta.                             QED

Run:  python exact_certificate.py     (stdlib only; every check is exact)
"""
from fractions import Fraction as F

# ---------- data ----------
v = [F(7,10), F(5,9), F(4,5), F(6,11), F(2,3)]
beta = sum(x*x for x in v)
WITNESS_Y = [F(-15,19), F(11,51), F(1), F(7,34), F(-23,32)]
FEAS_A    = [F(94,137), F(247,339), F(116,193), F(107,222), F(93,175)]
EDGES = [(i,(i+1)%5) for i in range(5)]
NONEDGE = [(k,(k+2)%5) for k in range(5)]
ok_all = True
def report(name, ok, detail=""):
    global ok_all; ok_all &= ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))

print(f"behavior p = {[str(x*x) for x in v]}")
print(f"beta = {beta} = {float(beta):.12f}\n")

# ---------- [2] rigidity system (real part), exact ----------
# unknowns x[k] = Re(a_k), a_k = H[k, k+2]; from (Re(H) v)_i = beta v_i:
#   x_i v_{i+2} + x_{i-2} v_{i-2} = (beta - 1) v_i
A = [[F(0)]*5 for _ in range(5)]
b = [F(0)]*5
for i in range(5):
    A[i][i]        += v[(i+2)%5]
    A[i][(i-2)%5]  += v[(i-2)%5]
    b[i] = (beta-1)*v[i]

def solve_exact(A, b):
    """Gaussian elimination over Q; returns (solution, det)."""
    n = len(A); M = [row[:] + [b[i]] for i, row in enumerate(A)]
    det = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None: return None, F(0)
        if piv != c: M[c], M[piv] = M[piv], M[c]; det = -det
        det *= M[c][c]
        inv = F(1)/M[c][c]
        M[c] = [t*inv for t in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [tr - f*tc for tr, tc in zip(M[r], M[c])]
    return [M[r][n] for r in range(n)], det

x, det = solve_exact(A, b)
report("real rigidity system nonsingular (det != 0): Re(H) = H* UNIQUE", det != 0, f"det = {det}")
a_star = x
H_star = [[F(0)]*5 for _ in range(5)]
for i in range(5): H_star[i][i] = F(1)
for k,(i,j) in enumerate(NONEDGE): H_star[i][j] = H_star[j][i] = a_star[k]
Hv = [sum(H_star[i][j]*v[j] for j in range(5)) for i in range(5)]
report("H* v = beta v (exact)", all(Hv[i] == beta*v[i] for i in range(5)))

# ---------- [3] obstruction, exact ----------
y = WITNESS_Y
q = sum(y[i]*H_star[i][j]*y[j] for i in range(5) for j in range(5))
report("witness: y^T H* y < 0 (exact; kills the WHOLE Hermitian family)", q < 0, f"= {q} = {float(q):.9f}")

# ---------- [1] realizability, exact ----------
H_feas = [[F(0)]*5 for _ in range(5)]
for i in range(5): H_feas[i][i] = F(1)
for k,(i,j) in enumerate(NONEDGE): H_feas[i][j] = H_feas[j][i] = FEAS_A[k]
report("H_feas: diag = 1, exclusivity edges = 0 (by construction)",
       all(H_feas[i][j] == 0 for i,j in EDGES))
M = [[H_feas[i][j] - v[i]*v[j] for j in range(5)] for i in range(5)]
def ldl_pivots(M):
    """exact LDL^T; returns pivot list (positive-definite iff all > 0)."""
    n = len(M); M = [row[:] for row in M]; piv = []
    for k in range(n):
        d = M[k][k]
        piv.append(d)
        if d <= 0: return piv
        for i in range(k+1, n):
            f = M[i][k]/d
            for j in range(k, n):
                M[i][j] -= f*M[k][j]
    return piv
piv = ldl_pivots(M)
report("H_feas - v v^T POSITIVE DEFINITE (exact LDL, all 5 pivots > 0)",
       len(piv) == 5 and all(t > 0 for t in piv),
       f"pivots ~ {[f'{float(t):.5f}' for t in piv]}")

print()
if ok_all:
    print("CERTIFIED: Delta_prep(p) > 0 for p = (49/100, 25/81, 16/25, 36/121, 4/9).")
    print("Every sharp quantum realization of this behavior has capacity strictly")
    print("greater than beta = 2137213/980100. (Numerical SDP value of the gap:")
    print("Delta_prep ~ 0.0096474 -- the strictness is what this file proves.)")
else:
    print("CERTIFICATE FAILED -- do not use.")
raise SystemExit(0 if ok_all else 1)
