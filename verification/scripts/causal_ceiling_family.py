#!/usr/bin/env python3
"""Chapter 51: the causal ceiling family (exact).

Standard library only; exact arithmetic in Q and in the field Q(sqrt2).

Checks, in four groups:
  H1  The closed form (d+1)/(2d) at d = 2, 3, 4 and the exact causal bound:
      over ALL deterministic one-way strategies (either order, any message
      alphabet -- reduced without loss to message partitions), the d-ary
      order game's maximum is exactly (d+1)/(2d), attained; mixtures cannot
      exceed a maximum over deterministic points.
  H2  The process-matrix side at d = 2, exactly: the two-way process term
      K = IZZI + ZIXZ satisfies K^2 = 2I (so W = (1/4)(I + K/sqrt2) has
      eigenvalues 0 and 1/2 -- positive semidefinite), Tr W = 4, and W is
      a fixed point of the process-matrix validity projector, all in exact
      Q(sqrt2) arithmetic.
  H3  Exact attainment: the closed-form strategy -- Alice measures z and
      encodes her input in z; Bob, on the send branch, measures the x basis
      and encodes his input corrected by the outcome, and on the read
      branch measures z -- achieves the game value (2 + sqrt2)/4 EXACTLY as
      an element of Q(sqrt2) against W. Combined with H1, the d = 2 gap
      over the causal bound is exactly (sqrt2 - 2)/4 + 1/2 - 3/4 =
      (sqrt2 - 1)/4 > 0.
  H4  The margin arithmetic: (2+sqrt2)/4 - 3/4 = (sqrt2-1)/4 is certified
      in (0.1035, 0.1036); the reported d = 3 see-saw value 0.738466 gives
      margin 0.738466 - 2/3 < the d = 2 margin -- the violation shrinks
      with d (existence, not growth).
"""
from fractions import Fraction as F
from itertools import product, permutations

fails = []
def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" {detail}" if detail else ""))
    if not ok:
        fails.append(label)

# ---------- the field Q(sqrt2): a + b*sqrt2 ----------
class Q2:
    __slots__ = ("a", "b")
    def __init__(self, a, b=0):
        self.a = F(a); self.b = F(b)
    def __add__(s, o): return Q2(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return Q2(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return Q2(s.a*o.a + 2*s.b*o.b, s.a*o.b + s.b*o.a)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __repr__(s): return f"({s.a}+{s.b}*sqrt2)"
Z2_0, Z2_1 = Q2(0), Q2(1)
INV_SQRT2 = Q2(0, F(1, 2))    # 1/sqrt2 = sqrt2/2

# ---------- H1: causal bound over all deterministic one-way strategies ----------
def set_partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i] + [part[i] + [first]] + part[i+1:]
        yield part + [[first]]

def causal_max(d):
    """Max over deterministic one-way strategies. The earlier party's guess of
    the later party's input is independent of it, so its success is exactly 1/d
    for every guess function (uniform inputs). The later party's success depends
    on the message only through the partition it induces on the earlier inputs:
    per input value and per block, one guess is right for exactly one member,
    so the total is (number of blocks)/d, maximized by the discrete partition.
    Both reductions are exhaustively verified here rather than assumed."""
    # earlier party's success: verify = 1/d for every guess function
    for gE in product(range(d), repeat=d):
        pE = F(sum(1 for e in range(d) for l in range(d) if gE[e] == l), d*d)
        if pE != F(1, d):
            return None
    # later party's success: exhaust partitions of the earlier inputs
    best = F(0)
    for part in set_partitions(list(range(d))):
        hit = 0
        for l in range(d):
            for block in part:
                hit += max(sum(1 for e in block if e == e2) for e2 in range(d))
        best = max(best, F(hit, d*d))
    return (F(1, d) + best) / 2

check("H1a closed form (d+1)/(2d) = 3/4, 2/3, 5/8 at d = 2, 3, 4",
      [F(d+1, 2*d) for d in (2, 3, 4)] == [F(3, 4), F(2, 3), F(5, 8)])
ok_bound = True
for d in (2, 3, 4):
    if causal_max(d) != F(d+1, 2*d):
        ok_bound = False
check("H1b causal maximum = (d+1)/(2d) exactly, d = 2, 3, 4 (exhaustive)", ok_bound)

# ---------- H2: the OCB process matrix, exact ----------
I2 = [[Z2_1, Z2_0], [Z2_0, Z2_1]]
Zm = [[Z2_1, Z2_0], [Z2_0, Q2(-1)]]
Xm = [[Z2_0, Z2_1], [Z2_1, Z2_0]]

def kron(*ms):
    out = [[Z2_1]]
    for m in ms:
        r = len(out); c = len(out[0]); mr = len(m); mc = len(m[0])
        new = [[Z2_0]*(c*mc) for _ in range(r*mr)]
        for i in range(r):
            for j in range(c):
                for a in range(mr):
                    for b in range(mc):
                        new[i*mr+a][j*mc+b] = out[i][j] * m[a][b]
        out = new
    return out

def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(s, A): return [[s * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[Z2_0]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            aik = A[i][k]
            if aik == Z2_0: continue
            for j in range(p):
                out[i][j] = out[i][j] + aik * B[k][j]
    return out

T1 = kron(I2, Zm, Zm, I2)     # order A_I, A_O, B_I, B_O
T2 = kron(Zm, I2, Xm, Zm)
K = madd(T1, T2)
K2 = mmul(K, K)
twoI = mscale(Q2(2), kron(I2, I2, I2, I2))
check("H2a K = IZZI + ZIXZ satisfies K^2 = 2I (exact)", K2 == twoI)
W = mscale(Q2(F(1, 4)), madd(kron(I2, I2, I2, I2), mscale(INV_SQRT2, K)))
trW = Z2_0
for i in range(16): trW = trW + W[i][i]
check("H2b Tr W = 4 (exact)", trW == Q2(4))
# PSD certificate: W = (1/4)(I + K/sqrt2), (K/sqrt2)^2 = I and K symmetric,
# so eigenvalues of K/sqrt2 are +-1 and W's are 0 and 1/2. Symmetry check:
check("H2c K symmetric (so the K^2 = 2I certificate gives W >= 0)",
      all(K[i][j] == K[j][i] for i in range(16) for j in range(16)))

# validity projector, exact: trace out subsystems and replace by I/2
def trace_replace(M, subs):
    dims = [2, 2, 2, 2]
    def idx(t):  # tensor index (i0,i1,i2,i3) -> flat
        return ((t[0]*2 + t[1])*2 + t[2])*2 + t[3]
    out = [[Z2_0]*16 for _ in range(16)]
    kept = [s for s in range(4) if s not in subs]
    half = F(1, 2**len(subs))
    for row in product(range(2), repeat=4):
        for col in product(range(2), repeat=4):
            # entry of the projected matrix at (row, col)
            if any(row[s] != col[s] for s in subs):
                # replaced identity factors are diagonal
                continue
            acc = Z2_0
            for tr in product(range(2), repeat=len(subs)):
                r2 = list(row); c2 = list(col)
                for s, v in zip(subs, tr):
                    r2[s] = v; c2[s] = v
                acc = acc + M[idx(tuple(r2))][idx(tuple(c2))]
            out[idx(row)][idx(col)] = Q2(half) * acc
    return out

def P_proc(M):
    t = trace_replace
    def msub(A, B): return [[A[i][j] - B[i][j] for j in range(16)] for i in range(16)]
    R = t(M, [1])
    R = madd(R, t(M, [3]))
    R = msub(R, t(M, [1, 3]))
    R = msub(R, t(M, [0, 1]))
    R = msub(R, t(M, [2, 3]))
    R = madd(R, t(M, [1, 2, 3]))
    R = madd(R, t(M, [0, 1, 3]))
    return R

check("H2d W is a fixed point of the validity projector (exact)", P_proc(W) == W)

# ---------- H3: exact attainment of (2+sqrt2)/4 ----------
# Basis vectors and rank-one Chois as 4x4 exact matrices over Q (embedded in Q(sqrt2)).
def ket(i):
    v = [Z2_0, Z2_0]; v[i] = Z2_1
    return v
def outer(u, v):
    return [[u[i] * v[j] for j in range(len(v))] for i in range(len(u))]
def choi(vin, vout):
    phi = [vin[i] * vout[j] for i in range(2) for j in range(2)]
    return [[phi[i] * phi[j] for j in range(4)] for i in range(4)]
HALF = Q2(F(1, 2))
def xket(beta):  # (|0> + (-1)^beta |1>)/sqrt2 -- Choi entries stay rational (halves)
    s = Q2(1) if beta == 0 else Q2(-1)
    return [INV_SQRT2, INV_SQRT2 * s]

Ai = {}
for x in range(2):
    for a in range(2):
        Ai[(x, a)] = choi(ket(a), ket(x))
Bi = {}
for y in range(2):
    for b in range(2):
        Bi[(2*y + 0, b)] = choi(xket(b), ket(y ^ b))
        Bi[(2*y + 1, b)] = choi(ket(b), ket(0))

def pair_value(A, B):
    """Tr[W (A x B)] = sum W[(ar,br),(ac,bc)] A[ac][ar] B[bc][br]."""
    acc = Z2_0
    for ar in range(4):
        for br in range(4):
            for ac in range(4):
                w = W[ar*4 + br]
                for bc in range(4):
                    acc = acc + w[ac*4 + bc] * A[ac][ar] * B[bc][br]
    return acc

def msum(ms):
    out = [[Z2_0]*4 for _ in range(4)]
    for m in ms:
        out = [[out[i][j] + m[i][j] for j in range(4)] for i in range(4)]
    return out

p = Z2_0
for x in range(2):
    for y in range(2):
        p = p + pair_value(Ai[(x, y)], msum([Bi[(2*y + 0, b)] for b in range(2)]))
        p = p + pair_value(msum([Ai[(x, a)] for a in range(2)]), Bi[(2*y + 1, x)])
p = Q2(F(1, 8)) * p
target = Q2(F(1, 2), F(1, 4))    # (2 + sqrt2)/4
check("H3 exact attainment: game value = (2 + sqrt2)/4 in Q(sqrt2)", p == target, f"(= {p})")

# ---------- H4: margins ----------
gap = p - Q2(F(3, 4))            # should be (sqrt2 - 1)/4 = (-1/4) + (1/4) sqrt2
check("H4a d = 2 gap = (sqrt2 - 1)/4 exactly", gap == Q2(F(-1, 4), F(1, 4)))
# certified bracket for the numeric margin: sqrt2 in (1.4142135, 1.4142136)
lo, hi = F(14142135, 10**7), F(14142136, 10**7)
check("H4b sqrt2 bracket", lo*lo < 2 < hi*hi)
m2_lo = (lo - 1) / 4
m3 = F(738466, 10**6) - F(2, 3)  # reported see-saw value minus the d = 3 ceiling
check("H4c margin shrinks: d = 3 reported margin < d = 2 margin", m3 < m2_lo,
      f"({float(m3):.6f} < {float(m2_lo):.6f})")
check("H4d d = 3 reported value exceeds the ceiling 2/3", m3 > 0, f"(margin {float(m3):.6f})")

print(f"causal_ceiling_family: {'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
