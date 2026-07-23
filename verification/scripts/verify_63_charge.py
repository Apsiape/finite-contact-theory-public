"""
Chapter 63 -- The Closure Charge and Its Witnesses. Exact verification.

STDLIB ONLY (fractions, itertools). No numpy. Self-contained.

Re-derives the chapter's core exact results and prints [PASS]/[FAIL] lines:

  PART A -- the fusion algebra (6 model-theorems), chi = sign(g12 g23 g31),
            the Z2 odd-cycle holonomy class on a unit-diagonal 3x3 Gram:
    A1  chi is gauge-invariant under all 8 local rephasings (a holonomy class)
    A2  visibility boundary det G_odd(v) = -(2v-1)(v+1)^2 exact (visible iff v>1/2)
    A3  odd # odd -> chi=+1, det=(1-v)^2(1+2v)>0 (EXACT charge cancellation)
    A4  multiplicativity chi(A#B)=chi(A)chi(B) over random sign patterns
    A5  odd # even screening below v=1/2 (chi=-1 but det>0: charged, invisible)
    A6  odd # strong-even survival (chi=-1 and det<0: charge survives fusion)
        + tensor-fusion sign law det(A(x)B)=det(A)^3 det(B)^3

  PART B -- the tritter amalgamability boundary theta_max(v):
            det G(v,theta) = 1 - 3v^2 + 2v^3 cos(theta); PSD iff
            cos(theta) >= (3v^2-1)/(2v^3). Landmarks exact:
    B1  cos(theta_max) = -1 at v=1/2   (all triad phases glue: theta_max=180 deg)
    B2  cos(theta_max) =  0 at v^2=1/3  (theta_max = 90 deg exact)

  PART C -- the commutator spoof-closure demo (exact 2x2 complex arithmetic):
    C1  a scalar route-phase (global phase) cancels identically in the group
        commutator U V U^-1 V^-1 = I  -- the witness is BLIND to it
    C2  a genuine anticommuting transport pair has commutator = -I  -- a
        signature no scalar route-phase can forge

Exits nonzero on any FAIL.
"""
from fractions import Fraction as F
import itertools, random, sys

PASS = []; FAIL = []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# ---------------------------------------------------------------------------
# PART A -- the fusion algebra
# ---------------------------------------------------------------------------

def det3(G):
    return (G[0][0]*(G[1][1]*G[2][2]-G[1][2]*G[2][1])
           -G[0][1]*(G[1][0]*G[2][2]-G[1][2]*G[2][0])
           +G[0][2]*(G[1][0]*G[2][1]-G[1][1]*G[2][0]))

def G_odd(r):  return [[F(1), r,  r], [ r, F(1), -r], [ r, -r, F(1)]]
def G_even(r): return [[F(1), r,  r], [ r, F(1),  r], [ r,  r, F(1)]]

def chi(G):
    sgn = lambda x: 1 if x > 0 else -1
    return sgn(G[0][1]) * sgn(G[1][2]) * sgn(G[0][2])

def hadamard(A, B):
    return [[A[i][j]*B[i][j] for j in range(3)] for i in range(3)]

print("PART A -- the fusion algebra (model-theorems):")

# A1: gauge invariance under psi_i -> -psi_i (edge (i,j) picks up f_i f_j)
r = F(3, 5); G = G_odd(r)
okA1 = all(
    chi([[f[i]*f[j]*G[i][j] if i != j else G[i][j] for j in range(3)]
         for i in range(3)]) == chi(G)
    for f in itertools.product((1, -1), repeat=3))
check("A1 chi gauge-invariant under all 8 local rephasings (holonomy class)", okA1)

# A2: visibility boundary, exact factorization at several rationals
okA2 = all(det3(G_odd(v)) == -(2*v-1)*(v+1)**2
           for v in [F(1,4), F(2,5), F(1,2), F(3,5), F(3,4), F(9,10)])
# and the visibility side: det<0 iff v>1/2
okA2 &= all((det3(G_odd(v)) < 0) == (v > F(1,2))
            for v in [F(1,4), F(2,5), F(1,2), F(3,5), F(3,4), F(9,10)])
check("A2 det G_odd(v) = -(2v-1)(v+1)^2 exact; visible (det<0) iff v>1/2", okA2)

# A3: odd # odd -> fully positive triad, exact charge cancellation
s = F(3, 5); AB = hadamard(G_odd(r), G_odd(s)); v = r*s
okA3 = (chi(AB) == 1) and (det3(AB) == (1-v)**2*(1+2*v)) and (det3(AB) > 0)
check("A3 odd # odd = chi +1, det=(1-v)^2(1+2v)>0 (EXACT charge cancellation)", okA3)

# A4: multiplicativity over random sign patterns
random.seed(1); okA4 = True
for _ in range(500):
    def rnd():
        sg = [random.choice((1, -1)) for _ in range(3)]
        w = F(random.randint(1, 9), 10)
        return [[F(1), sg[0]*w, sg[2]*w],
                [sg[0]*w, F(1), sg[1]*w],
                [sg[2]*w, sg[1]*w, F(1)]]
    A, B = rnd(), rnd()
    okA4 &= chi(hadamard(A, B)) == chi(A)*chi(B)
check("A4 chi(A#B)=chi(A)chi(B) (500 random sign patterns)", okA4)

# A5: screening below the wall
a = hadamard(G_odd(F(3,5)), G_even(F(4,5)))   # v_fused = 12/25 < 1/2 -> screened
check("A5 odd # even screening below v=1/2 (chi=-1, det>0: charged but invisible)",
      chi(a) == -1 and det3(a) > 0)

# A6: survival against a strong even triad + tensor-fusion sign law
b = hadamard(G_odd(F(9,10)), G_even(F(9,10)))  # v_fused = 81/100 > 1/2 -> survives
okA6 = chi(b) == -1 and det3(b) < 0
# tensor-fusion sign law det(A (x) B) = det(A)^3 det(B)^3 for 3x3 Grams
def kron(A, B):
    out = [[F(0)]*9 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    out[3*i+k][3*j+l] = A[i][j]*B[k][l]
    return out
def det9(M):
    # exact fraction Gaussian elimination with row swaps (sign-tracked)
    M = [row[:] for row in M]; n = 9; det = F(1)
    for c in range(n):
        p = next((rr for rr in range(c, n) if M[rr][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]; det = -det
        det *= M[c][c]; inv = M[c][c]
        for rr in range(c+1, n):
            if M[rr][c] != 0:
                fac = M[rr][c]/inv
                M[rr] = [M[rr][k] - fac*M[c][k] for k in range(n)]
    return det
A6a, A6b = G_odd(F(3,5)), G_even(F(2,5))
okA6 &= det9(kron(A6a, A6b)) == det3(A6a)**3 * det3(A6b)**3
check("A6 odd # strong-even survival (chi=-1, det<0) + tensor sign law det(A(x)B)=det(A)^3det(B)^3", okA6)

# ---------------------------------------------------------------------------
# PART B -- the tritter amalgamability boundary
# ---------------------------------------------------------------------------
# det G(v,theta) = 1 - 3v^2 + 2v^3 cos(theta); PSD boundary cos(theta_max)=(3v^2-1)/(2v^3).
print("\nPART B -- the tritter amalgamability boundary theta_max(v):")

def cos_theta_max(v):
    return (3*v*v - 1) / (2*v**3)

# B1: v = 1/2 -> cos(theta_max) = -1  => theta_max = 180 deg (all phases glue)
okB1 = cos_theta_max(F(1,2)) == F(-1)
check("B1 cos(theta_max) = -1 at v=1/2 (all triad phases glue: theta_max = 180 deg)", okB1)

# B2: v^2 = 1/3 -> cos(theta_max) = 0 => theta_max = 90 deg exact.
# v = 1/sqrt(3) is irrational; verify symbolically via the numerator 3v^2-1 = 0
# using the exact relation v^2 = 1/3 (so 3v^2 - 1 = 0 exactly).
v2 = F(1, 3)                      # v^2 = 1/3 exactly
numerator = 3*v2 - 1             # = 3v^2 - 1
okB2 = (numerator == 0)          # cos(theta_max) = numerator/(2v^3) = 0
check("B2 cos(theta_max) = 0 at v^2=1/3 (theta_max = 90 deg exact)", okB2)

# ---------------------------------------------------------------------------
# PART C -- the commutator spoof-closure demo (exact 2x2 complex arithmetic)
# ---------------------------------------------------------------------------
# complex number = (re, im) as a pair of Fractions; matrix = 2x2 nested list.
print("\nPART C -- the commutator spoof-closure demo:")

def cadd(a, b): return (a[0]+b[0], a[1]+b[1])
def cmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cneg(a):    return (-a[0], -a[1])
C0 = (F(0), F(0)); C1 = (F(1), F(0)); Ci = (F(0), F(1))

def mmul(A, B):
    return [[cadd(cmul(A[i][0], B[0][j]), cmul(A[i][1], B[1][j]))
             for j in range(2)] for i in range(2)]
def scalar_mat(z):
    return [[z, C0], [C0, z]]
def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(2) for j in range(2))

I2   = scalar_mat(C1)
negI = scalar_mat(cneg(C1))
X = [[C0, C1], [C1, C0]]           # Pauli X (self-inverse, unitary)
Z = [[C1, C0], [C0, cneg(C1)]]     # Pauli Z (self-inverse, unitary)

def commutator(U, V, Uinv, Vinv):
    return mmul(mmul(mmul(U, V), Uinv), Vinv)

# C1: a scalar route-phase (global phase e^{i*phi}; here phi=90deg, z=i).
# U = i*I is scalar; its inverse is -i*I. Commutator with ANY V is identity:
U   = scalar_mat(Ci)
Uinv = scalar_mat(cneg(Ci))
okC1 = meq(commutator(U, X, Uinv, X), I2) and meq(commutator(U, Z, Uinv, Z), I2)
check("C1 scalar route-phase commutator U V U^-1 V^-1 = I (witness blind to it)", okC1)

# C2: genuine anticommuting transport pair -> commutator = -I (un-forgeable).
okC2 = meq(commutator(X, Z, X, Z), negI)   # X,Z self-inverse; (XZ)^2 = -I
check("C2 anticommuting pair commutator = -I (a signature no scalar phase forges)", okC2)

# ---------------------------------------------------------------------------
print(f"\n{len(PASS)} PASS, {len(FAIL)} FAIL")
if FAIL:
    print("FAILURES:", "; ".join(FAIL))
    sys.exit(1)

# FALSIFIABILITY NOTE:
# This script FAILS (nonzero exit) if any of the following stop holding exactly:
#  - the odd-cycle sign chi is NOT invariant under a local rephasing (A1) -- then
#    chi is a coordinate convention, not a gauge-invariant holonomy class, and
#    the whole "charge" reading collapses;
#  - the visibility factorization -(2v-1)(v+1)^2 is wrong, or det<0 does not
#    coincide with v>1/2 (A2) -- then the v=1/2 wall is not exact;
#  - odd#odd fails to cancel to a PSD triad with det=(1-v)^2(1+2v) (A3), or
#    multiplicativity/screening/survival/tensor-sign fail (A4-A6) -- then the
#    "fusion algebra" is not an algebra and the kill condition (3) is met;
#  - the tritter landmarks cos(theta_max) = -1 at v=1/2 or = 0 at v^2=1/3 are
#    off (B1,B2) -- then the amalgamability boundary is misstated;
#  - a scalar (global) route-phase leaves any residue in the group commutator
#    (C1), or the anticommuting pair does not yield -I (C2) -- then the
#    commutator witness is not actually blind to route-phase spoofs, i.e. the
#    spoof-closure design is broken.
# None of these successes assert the charge exists in nature: PART A/B are
# model-theorems and a photonic RECOVERY boundary; the nature-facing charge is
# a registered EXTENSION wager with zero observations.
