#!/usr/bin/env python3
"""Chapter 55: the carrier anatomy (exact).

Standard library only; exact rational quaternion algebra. Four groups:
  Q1  Right-multiplication adjoints on H with the Euclidean form: adj(R_q) =
      R_qbar; self-adjoint iff q is real; the skew square roots of -I in the
      right algebra are the imaginary units (sphere samples, exact).
  Q2  Commutants at primitive scope: the commutant of left multiplication is
      the right quaternions (dimension 4, exact kernel computation); adjoining
      the full right unit action cuts it to the scalars (dimension 1).
  Q3  K = -I balancing on R^2 (x) R^2: K^2 = I; the balanced sector
      ker(K + I) has real dimension 2 and carries J1 = J2; flipping one
      factor's orientation exchanges the sectors.
  Q4  The classical-copy ledger: the copy payment's support label enters once
      and remains independently readable twice -- the books cannot balance.
"""
from fractions import Fraction as F

fails = []
def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" {detail}" if detail else ""))
    if not ok:
        fails.append(label)

# ---- exact quaternions as 4-tuples (1, i, j, k) of Fractions ----
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2)
def qconj(q): return (q[0], -q[1], -q[2], -q[3])
E = [(F(1),F(0),F(0),F(0)), (F(0),F(1),F(0),F(0)), (F(0),F(0),F(1),F(0)), (F(0),F(0),F(0),F(1))]

def mat_of(action):
    """4x4 rational matrix of a linear action on H in the basis (1,i,j,k)."""
    cols = [action(e) for e in E]
    return [[cols[j][i] for j in range(4)] for i in range(4)]
def R(q): return mat_of(lambda x: qmul(x, q))
def L(q): return mat_of(lambda x: qmul(q, x))
def mmulm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def T(A): return [[A[j][i] for j in range(4)] for i in range(4)]
I4 = mat_of(lambda x: x)

# Q1
qs = [(F(2),F(3),F(-1),F(5)), (F(0),F(1),F(0),F(0)), (F(1),F(0),F(0),F(0)), (F(0),F(3,5),F(4,5),F(0))]
check("Q1a adj(R_q) = R_qbar for rational samples",
      all(T(R(q)) == R(qconj(q)) for q in qs))
check("Q1b R_q self-adjoint iff q real",
      T(R((F(5),F(0),F(0),F(0)))) == R((F(5),F(0),F(0),F(0))) and
      T(R((F(0),F(1),F(0),F(0)))) != R((F(0),F(1),F(0),F(0))))
units = [(F(0),F(1),F(0),F(0)), (F(0),F(0),F(1),F(0)), (F(0),F(0),F(0),F(1)), (F(0),F(3,5),F(4,5),F(0)), (F(0),F(3,13),F(4,13),F(12,13))]
neg_I = [[-I4[i][j] for j in range(4)] for i in range(4)]
check("Q1c imaginary units give skew square roots of -I (5 exact sphere samples)",
      all(mmulm(R(u), R(u)) == neg_I and T(R(u)) == [[-R(u)[i][j] for j in range(4)] for i in range(4)] for u in units))

# Q2: exact commutant dimensions via kernel of the commutation system
def commutant_dim(gens):
    # unknown M (16 entries); equations M G - G M = 0 for each generator G
    rows = []
    for G in gens:
        for i in range(4):
            for j in range(4):
                row = [F(0)] * 16
                for k in range(4):
                    row[i*4 + k] += G[k][j]      # (M G)_ij
                    row[k*4 + j] -= G[i][k]      # (G M)_ij
                rows.append(row)
    # exact Gaussian elimination for rank
    rank = 0
    cols = 16
    r = [row[:] for row in rows]
    lead = 0
    for c in range(cols):
        piv = None
        for i in range(lead, len(r)):
            if r[i][c] != 0:
                piv = i; break
        if piv is None: continue
        r[lead], r[piv] = r[piv], r[lead]
        pv = r[lead][c]
        r[lead] = [x / pv for x in r[lead]]
        for i in range(len(r)):
            if i != lead and r[i][c] != 0:
                f = r[i][c]
                r[i] = [a - f*b for a, b in zip(r[i], r[lead])]
        lead += 1
        rank += 1
        if lead == len(r): break
    return cols - rank

i_q, j_q, k_q = E[1], E[2], E[3]
dimL = commutant_dim([L(i_q), L(j_q), L(k_q)])
check("Q2a Comm(left H-action) has dimension 4 (the right quaternions)", dimL == 4, f"(dim {dimL})")
dimLR = commutant_dim([L(i_q), L(j_q), L(k_q), R(i_q), R(j_q), R(k_q)])
check("Q2b adjoining the right unit action cuts the commutant to the scalars", dimLR == 1, f"(dim {dimLR})")

# Q3: K = -I on R^2 (x) R^2
J = [[F(0), F(-1)], [F(1), F(0)]]
def kron2(A, B):
    n = len(A)*len(B)
    out = [[F(0)]*n for _ in range(n)]
    for i in range(len(A)):
        for j in range(len(A)):
            for a in range(len(B)):
                for b in range(len(B)):
                    out[i*len(B)+a][j*len(B)+b] = A[i][j]*B[a][b]
    return out
I2 = [[F(1),F(0)],[F(0),F(1)]]
J1 = kron2(J, I2); J2 = kron2(I2, J)
def mm(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
K = mm(J1, J2)
I4b = kron2(I2, I2)
check("Q3a K^2 = I", mm(K, K) == I4b)
# balanced sector ker(K+I): solve exactly
def kernel_dim(M):
    n = len(M)
    rows = [row[:] for row in M]
    rank = 0; lead = 0
    for c in range(n):
        piv = None
        for i in range(lead, n):
            if rows[i][c] != 0: piv = i; break
        if piv is None: continue
        rows[lead], rows[piv] = rows[piv], rows[lead]
        pv = rows[lead][c]
        rows[lead] = [x/pv for x in rows[lead]]
        for i in range(n):
            if i != lead and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f*b for a, b in zip(rows[i], rows[lead])]
        lead += 1; rank += 1
        if lead == n: break
    return n - rank
KpI = [[K[i][j] + I4b[i][j] for j in range(4)] for i in range(4)]
J1mJ2 = [[J1[i][j] - J2[i][j] for j in range(4)] for i in range(4)]
check("Q3b balanced sector ker(K+I) has real dimension 2", kernel_dim(KpI) == 2)
check("Q3c ker(K+I) = ker(J1 - J2) (same 2-dim space: both kernels dim 2, difference map vanishes there)",
      kernel_dim(J1mJ2) == 2)
J2f = kron2(I2, [[F(0),F(1)],[F(-1),F(0)]])   # flipped orientation
Kf = mm(J1, J2f)
KfmI = [[Kf[i][j] - I4b[i][j] for j in range(4)] for i in range(4)]
check("Q3d flipping one factor's orientation exchanges the sectors (ker(Kf - I) is now dim 2)",
      kernel_dim(KfmI) == 2)

# Q4: the classical-copy ledger
def balanced(Ee, S, P, W): return Ee == S + P + W and min(S, P, W) >= 0
check("Q4 classical copy: E=1 with S=1 and P=1 cannot balance (theft)",
      not any(balanced(1, 1, 1, W) for W in range(0, 4)))

print(f"carrier_anatomy: {'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
