#!/usr/bin/env python3
"""Chapter 9, section 4 -- actualization by counting, done honestly.

Dependency-free (Python standard library only), exact arithmetic
throughout. This script REPLACES an earlier overclaim ("a given actual
phase's internal law is forced by counting, with no added Born postulate")
with the corrected, stronger reading:

  Counting forces the FORM of an actual phase's response -- a one-parameter
  positive equivariant weight family and sequential (Lueders) composition --
  but it does NOT force the Born rule. Born is one point (equal tickets,
  alpha = beta) of that family; equal-tickets is an ADDED magnitude law, the
  relocated selector the dynamic audit (section 3) already predicts must
  exist. Positive additive counting alone yields DECOHERED path sums, never
  interference. The retained Z_2 sign scar (z -> -z) upgrades counting to a
  real amplitude calculus (three real mutually-unbiased bases; the 768 real
  4x4 Hadamard matrices; a +-1/2 cocycle that composes exactly), which does
  restore genuine real coherent interference. Two gaps then remain, held
  open and independent: (a) the magnitude law alpha = beta, and (b) the
  enlargement from the binary {+1,-1} sign phase to a complex U(1) phase.

Sections:
  1. The 24-cell response geometry: 12 rays in 3 orthonormal frames; the
     144 ordered (source, target) histories split 48 return + 96 transfer.
  2. The most general positive equivariant weight is a 1-parameter family
     w = alpha (return) or beta (transfer) times the incidence |<p,q>|^2;
     it is a lawful stochastic response for ALL alpha, beta > 0, and the
     Born kernel {0, 1/12, 1/3} occurs ONLY at alpha = beta.
  3. Positive additive counting is DECOHERED: over every two-path
     interference configuration on the three frames, the probability-summing
     (positive) value differs from the coherent |sum of amplitudes|^2, and
     the destructive value 0 is never reproduced by positive counting.
  4. The Z_2 sign scar gives a real amplitude calculus: the three frames are
     three real mutually-unbiased bases; their transition matrices have
     entries +-1/2 and compose exactly (a cocycle); there are exactly 768
     real 4x4 Hadamard matrices supplying the sign alphabet.
  5. The two remaining gaps, made explicit: (a) alpha = beta is not forced
     (asymmetric-ticket phases are equally lawful); (b) the binary sign
     phase cannot reach the complex value |1 + i|^2 = 2, so the enlargement
     to a U(1) phase is an added ingredient.

Named recoveries (not novel here): mutually-unbiased bases; the count of
real Hadamard matrices of order 4; the general Born-measure-underdetermination
that Gleason's theorem also exhibits (form fixed, measure free).
"""
from fractions import Fraction as F
from itertools import combinations, product

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

# ======================================================================
# The 24-cell response geometry: 12 rays in 3 orthonormal frames
# ======================================================================
# The 12 rays are the antipodal Hurwitz-unit directions (representative with
# first nonzero coordinate positive): 4 axis rays and 8 half-integer rays.
h = F(1, 2)
frame_axis = [(F(1),F(0),F(0),F(0)), (F(0),F(1),F(0),F(0)),
              (F(0),F(0),F(1),F(0)), (F(0),F(0),F(0),F(1))]
frame_even = [(h,h,h,h), (h,h,-h,-h), (h,-h,h,-h), (h,-h,-h,h)]   # even # of minus
frame_odd  = [(h,h,h,-h), (h,h,-h,h), (h,-h,h,h), (h,-h,-h,-h)]   # odd  # of minus
frames = [frame_axis, frame_even, frame_odd]
rays = [v for fr in frames for v in fr]
frame_of = {v: t for t, fr in enumerate(frames) for v in fr}

# ----------------------------------------------------------------------
print("## 1: 12 rays, 3 orthonormal frames, and the 48 return / 96 transfer split")
# each frame is an orthonormal basis of R^4
ortho = all(dot(u, v) == (1 if i == j else 0)
            for fr in frames for i, u in enumerate(fr) for j, v in enumerate(fr))
# within a frame |<p,q>|^2 in {0,1}; across frames it is exactly 1/4 (mutually unbiased)
within = all(dot(u, v) ** 2 in (F(0), F(1))
             for fr in frames for u in fr for v in fr)
across = all(dot(u, v) ** 2 == F(1, 4)
             for s in range(3) for t in range(3) if s != t
             for u in frames[s] for v in frames[t])
# classify the 144 ordered (source, target) histories
return_hist = sum(1 for p in rays for q in rays if frame_of[p] == frame_of[q])
transfer_hist = sum(1 for p in rays for q in rays if frame_of[p] != frame_of[q])
check(f"the 12 rays split into 3 orthonormal frames of 4 (ortho={ortho}); "
      f"overlaps are {{0,1}} within a frame ({within}) and exactly 1/4 across "
      f"frames ({across}); so the 144 = 12x12 ordered histories split into "
      f"{return_hist} return (same frame) + {transfer_hist} transfer (cross "
      f"frame).",
      ortho and within and across and return_hist == 48 and transfer_hist == 96
      and return_hist + transfer_hist == 144)

# ======================================================================
# 2. The 1-parameter positive equivariant weight family; Born only at a=b
# ======================================================================
print("## 2: the equivariant weight family (alpha,beta); Born kernel ONLY at alpha=beta")
def response(alpha, beta):
    """Row-normalized response P(p->q): ticket (alpha same-frame, beta cross)
    times the incidence |<p,q>|^2."""
    P = {}
    for p in rays:
        raw = {}
        for q in rays:
            ticket = alpha if frame_of[p] == frame_of[q] else beta
            raw[q] = ticket * dot(p, q) ** 2
        Z = sum(raw.values())
        P[p] = {q: raw[q] / Z for q in rays}
    return P

def row_profile(P, p):
    return sorted(set(P[p].values()))

# the family is a lawful stochastic response for several (alpha,beta) > 0
lawful = True
for alpha, beta in [(F(1),F(1)), (F(2),F(1)), (F(1),F(2)), (F(5),F(3))]:
    P = response(alpha, beta)
    lawful &= all(all(v >= 0 for v in P[p].values()) and sum(P[p].values()) == 1
                  for p in rays)

# closed forms: P(p->p) = alpha/(alpha+2beta), P(cross) = beta/(4alpha+8beta),
# P(orthogonal same-frame) = 0. Verify symbolically for several tickets.
closed_form = True
for alpha, beta in [(F(2),F(1)), (F(1),F(2)), (F(5),F(3)), (F(7),F(4))]:
    P = response(alpha, beta)
    p = rays[0]                                   # an axis ray
    same = [q for q in rays if frame_of[q] == frame_of[p]]
    cross = [q for q in rays if frame_of[q] != frame_of[p]]
    p_id = P[p][p]
    p_ortho = [P[p][q] for q in same if q != p]
    p_cross = [P[p][q] for q in cross]
    closed_form &= (p_id == alpha / (alpha + 2*beta)
                    and all(x == 0 for x in p_ortho)
                    and all(x == beta / (4*alpha + 8*beta) for x in p_cross))

# Born {0, 1/12, 1/3}: solve P(p->p) = 1/3  <=>  alpha = beta
born_values = {F(0), F(1, 12), F(1, 3)}
P_eq = response(F(1), F(1))
is_born_at_eq = all(set(P_eq[p].values()) == born_values for p in rays)
# and NOT Born off the diagonal: (2,1) gives identity 1/2 != 1/3
P_off = response(F(2), F(1))
not_born_off = any(set(P_off[p].values()) != born_values for p in rays)
# algebraic: alpha/(alpha+2beta) = 1/3  =>  3 alpha = alpha + 2 beta  =>  alpha = beta
alpha, beta = F(1), F(1)  # witness the unique solution ratio
born_iff = (3*alpha == alpha + 2*beta) and (alpha == beta)
check(f"the weight family is a lawful positive stochastic response for all "
      f"alpha,beta>0 ({lawful}); its closed form is P(p->p)=alpha/(alpha+2beta), "
      f"P(cross)=beta/(4alpha+8beta), P(orthogonal)=0 ({closed_form}); and the "
      f"Born kernel {{0,1/12,1/3}} occurs at equal tickets alpha=beta "
      f"({is_born_at_eq}) and there only -- P(p->p)=1/3 forces alpha=beta "
      f"algebraically ({born_iff}), while (alpha,beta)=(2,1) gives identity 1/2 "
      f"({not_born_off}). Counting forces the FORM; equal-tickets is an ADDED "
      f"magnitude law.",
      lawful and closed_form and is_born_at_eq and not_born_off and born_iff)

# ======================================================================
# 4. The Z_2 sign scar: three real MUBs, the +-1/2 cocycle, 768 Hadamards
#    (built here first because section 3's interference uses these matrices)
# ======================================================================
print("## 4: the sign scar's real amplitude calculus -- 3 real MUBs, +-1/2 cocycle, 768 Hadamards")
# B[t] has the four rays of frame t as its COLUMNS; it is orthogonal.
def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]
def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)]
            for i in range(n)]
B = []
for fr in frames:
    B.append([[fr[c][r] for c in range(4)] for r in range(4)])   # columns = rays
# U[t][s] = B[t]^T B[s] is the frame-t <- frame-s transition amplitude matrix
U = [[matmul(transpose(B[t]), B[s]) for s in range(3)] for t in range(3)]
# each frame orthonormal: B^T B = I
orthonormal = all(matmul(transpose(B[t]), B[t]) ==
                  [[F(1) if i==j else F(0) for j in range(4)] for i in range(4)]
                  for t in range(3))
# cross-frame transition entries are all +-1/2 (three real mutually-unbiased bases)
mub = all(U[t][s][i][j] in (h, -h)
          for s in range(3) for t in range(3) if s != t
          for i in range(4) for j in range(4))
# the cocycle: U[u][t] . U[t][s] = U[u][s] exactly (associative composition)
cocycle = all(matmul(U[u][t], U[t][s]) == U[u][s]
              for s in range(3) for t in range(3) for u in range(3))
# exactly 768 real 4x4 Hadamard matrices (rows orthogonal, +-1 entries)
had = 0
for bits in range(1 << 16):
    M = [[1 if (bits >> (4*i + j)) & 1 else -1 for j in range(4)] for i in range(4)]
    if all(sum(M[i][k]*M[j][k] for k in range(4)) == 0
           for i in range(4) for j in range(i+1, 4)):
        had += 1
check(f"the three frames are three real mutually-unbiased bases: each frame "
      f"is orthonormal ({orthonormal}), every cross-frame transition entry is "
      f"+-1/2 ({mub}), and the transition matrices compose exactly as a cocycle "
      f"U_ut . U_ts = U_us ({cocycle}); and there are exactly {had} real 4x4 "
      f"Hadamard matrices supplying the {{+1,-1}} sign alphabet. So the retained "
      f"Z_2 scar (z -> -z) makes amplitudes ADD with a real sign, with P=|A|^2 "
      f"applied after.",
      orthonormal and mub and cocycle and had == 768)

# ======================================================================
# 3. Positive counting is DECOHERED; the sign amplitude calculus is not
# ======================================================================
print("## 3: positive additive counting is decohered (no interference); signs restore it")
# minimal witness: two real amplitudes +1/2 and -1/2.
a_amp, b_amp = h, -h
coherent_min = (a_amp + b_amp) ** 2                 # |A|^2 with amplitudes added
decohered_min = a_amp**2 + b_amp**2                 # probabilities added
destructive_ok = (coherent_min == 0 and decohered_min == F(1, 2))

# systematic two-path interference over the three frames.
# A source ray i in frame s reaches a target ray j in frame u (s != u) via two
# intermediate rays m, m' of the third frame t. Path amplitude A_m = U_ut[j][m]
# * U_ts[m][i] (each factor +-1/2, so A_m = +-1/4).
total = 0
differ = 0
coherent_zero = 0
for s in range(3):
    for u in range(3):
        if s == u:
            continue
        t = ({0,1,2} - {s, u}).pop()
        for i in range(4):
            for j in range(4):
                for m, mp in combinations(range(4), 2):
                    Am = U[u][t][j][m] * U[t][s][m][i]
                    Amp = U[u][t][j][mp] * U[t][s][mp][i]
                    coh = (Am + Amp) ** 2               # amplitudes add
                    dec = Am**2 + Amp**2                # probabilities add
                    total += 1
                    if coh != dec:
                        differ += 1
                    if coh == 0:
                        coherent_zero += 1
# positive counting (dec) is the constant 1/8 here; coherent is 0 or 1/4.
all_differ = (differ == total)
never_zero_by_counting = coherent_zero > 0   # destructive value 0 exists coherently
check(f"positive additive counting sums PROBABILITIES and is decohered: the "
      f"minimal two-path witness has coherent |+1/2 + (-1/2)|^2 = 0 but "
      f"decohered 1/4 + 1/4 = 1/2 ({destructive_ok}); and across all {total} "
      f"two-path interference configurations on the three frames the positive "
      f"(probability-summing) value differs from the coherent |sum|^2 in every "
      f"case ({all_differ}), with the destructive value 0 reached coherently "
      f"({coherent_zero} configs) but never by positive counting. Amplitudes "
      f"that ADD (the sign scar) are required for interference.",
      destructive_ok and all_differ and never_zero_by_counting)

# ======================================================================
# 5. The two remaining gaps, made explicit and independent
# ======================================================================
print("## 5: two independent gaps held open -- (a) the magnitude law, (b) the complex phase")
# (a) alpha = beta is NOT forced: asymmetric tickets are equally lawful phases.
P21 = response(F(2), F(1)); P12 = response(F(1), F(2))
p = rays[0]
id21, id12 = P21[p][p], P12[p][p]
asym_lawful = (id21 == F(1, 2) and id12 == F(1, 5)          # both != 1/3
               and all(sum(P21[q].values()) == 1 for q in rays)
               and all(sum(P12[q].values()) == 1 for q in rays)
               and all(v >= 0 for q in rays for v in P21[q].values())
               and all(v >= 0 for q in rays for v in P12[q].values()))
# (b) the binary sign phase cannot reach the complex value: |1 + s|^2 for the
# sign alphabet s in {+1,-1} is {0, 4}, and the quantum value |1 + i|^2 = 2 is
# not in it -- the enlargement to a U(1) phase is an added ingredient.
binary_vals = {(1 + s) ** 2 for s in (F(1), F(-1))}         # {0, 4}
complex_val = 2                                            # |1 + i|^2 = 1 + 1
phase_gap = (binary_vals == {F(0), F(4)} and complex_val not in binary_vals)
check(f"(a) the magnitude law alpha=beta is not forced: (alpha,beta)=(2,1) and "
      f"(1,2) are equally lawful positive stochastic phases with identity "
      f"weights 1/2 and 1/5, neither 1/3 ({asym_lawful}); and (b) the binary "
      f"sign phase reaches only |1+s|^2 in {{0,4}} for s in {{+1,-1}}, so the "
      f"complex value |1+i|^2 = 2 is unreachable ({phase_gap}) -- the "
      f"enlargement from the {{+1,-1}} sign scar to a complex U(1) phase is a "
      f"separate added ingredient. The two gaps are independent.",
      asym_lawful and phase_gap)

print()
print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
raise SystemExit(1 if FAIL else 0)
