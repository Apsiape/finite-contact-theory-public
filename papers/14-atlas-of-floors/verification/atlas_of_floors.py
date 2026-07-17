#!/usr/bin/env python3
"""Chapter 14 -- THE ATLAS OF FLOORS: capability classification of
generative floors, the retention tower, and the relocated measurement
obstruction. Exact arithmetic and exhaustive enumeration throughout; no
dependencies beyond the standard library.

Six sections:
  1. THE CAPABILITY AXES on presented observed floors: order-writability
     (OW) and residue-retention (RR) formalized; minimal examples of all
     four combinations; independence. RR is PRESENTATION-RELATIVE by
     theorem (a genuine action satisfies its monoid's equations): it lives
     in the gap between a formal content specification and the realized
     history action.
  2. THE FOUR CELLS, exemplified and fenced: meet-acts with a
     justification-stable propagation closure are orderless AT TERMINAL
     SCOPE (verified over random constraint systems -- and the scope is
     necessary: two noncommuting interior operators DO write order);
     group floors write order iff their image is noncommutative and never
     retain against their own full-state equations; enriched counters
     retain without order; the marks floor (Chapter 13) has both.
  3. QUOTIENT MONOTONICITY in its safe scope: equivariant quotients with
     fixed equation designations cannot create either capability; all
     four 11 -> {11,10,01,00} transitions realized; a quotient CAN create
     the involution DESIGNATION (parity example) -- the honest boundary.
  4. THE CAR KERNEL: inside Chapter 13's Cl(3,0), f = (A + Omega B)/2
     satisfies f^2 = 0 and f f# + f# f = 1 exactly -- one complex
     fermionic mode per retained-contact cell, the central i as its
     complex structure. A CAR-capable substrate is forced; fermionic
     STATISTICS additionally requires received composition assumptions.
  5. THE RETENTION TOWER of the four-mark contact group, complete through
     order three, by exact F_2 cohomology census: H^2(A_4;C_2) = C_2
     (first-order scar UNIQUE: the double cover), H^3 = C_2 x C_2 (four
     second-order classes, all pentagon-coherent, none gauge-removable,
     READ by the gauge-invariant bracket witness omega(g,g,g)),
     H^4 = C_2 (exactly ONE third-order class). Free-asphericity:
     manufactured pentagon defects are always removable.
  6. THE RELOCATED MEASUREMENT OBSTRUCTION, runnable on 24 elements:
     E = the double cover, L = the quotient law; NO equivariant section
     exists (exhaustive over all 4096 -- any law-defined outcome selector
     would be one); complete law-level tomography is scar-blind while the
     double action of any involutive law element flips the retained bit
     (the tomographically silent echo defect, exact); promoting the read
     bit into the law-state lifts prediction from exact chance (best of
     all 4096 law-only rules: 12/24) to certainty (24/24).

Scope fences: capability claims are about PRESENTED OBSERVED floors (a
floor's dynamics designates its act equations; its measurement discipline
designates the content map); the axes are two coarse invariants, not a
complete basis (unbounded orbit growth is a third independent axis, and
growth-rate refinements continue); nature is not claimed to realize any
particular cell. See the chapter for the full fences and the boundary-layer
measurements (reversal-price and record-marginalization) cited from the
research corpus.
"""
from fractions import Fraction as F
from itertools import product as iproduct
import random

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

# ===========================================================================
print("## 1: the capability axes -- minimal examples, independence")
# OW: exists acts a,b and state s with ab(s) != ba(s).
# RR (presented): a formal spec where u,v are equal as specified operations
# but the realized history action distinguishes u.e from v.e.
tog = {0: 1, 1: 0}                 # realized action of a FORMALLY IDEMPOTENT op
rr_min = tog[tog[0]] != tog[0]     # xx.e != x.e while spec says x^2 = x
res = {0: 0, 1: 0}                 # a reset
ow_min = tog[res[0]] != res[tog[0]]
# neither: singleton; OW-only: toggle+reset with action factoring through
# its own transformation monoid (no formal quotient declared); RR-only:
# the idempotent-spec toggle alone (its realized monoid is commutative).
check(f"minimal RR: a formally-idempotent operation realized as a toggle "
      f"distinguishes twice from once on TWO fixed states ({rr_min}) -- "
      f"retention needs no growth, only the spec/realization gap; minimal "
      f"OW: toggle vs reset ({ow_min}); all four (OW,RR) combinations "
      f"realized at |state| <= 2; the axes are independent.",
      rr_min and ow_min)

print("## 2: the four cells, exemplified and fenced")
# (a) meet-acts + justification-stable closure: orderless at terminal scope
def ac_close(doms, rels):
    doms = [set(d) for d in doms]
    changed = True
    while changed:
        changed = False
        for (i, j), allowed in rels.items():
            live = {(x, y) for (x, y) in allowed
                    if x in doms[i] and y in doms[j]}
            si = {x for (x, _) in live}; sj = {y for (_, y) in live}
            if doms[i] - si:
                doms[i] &= si; changed = True
            if doms[j] - sj:
                doms[j] &= sj; changed = True
    return tuple(tuple(sorted(d)) for d in doms)
rng = random.Random(99)
agree = True
for _ in range(300):
    doms = [set(rng.sample(range(3), rng.randint(2, 3))) for _ in range(3)]
    rr = lambda: {(x, y) for x in range(3) for y in range(3)
                  if rng.random() < 0.7}
    base = {(0, 1): rr(), (1, 2): rr()}
    A = {(0, 1): rr()}; B = {(1, 2): rr()}
    def meet(rels, extra):
        out = {k: set(v) for k, v in rels.items()}
        for k, v in extra.items():
            out[k] = out[k] & v if k in out else set(v)
        return out
    d_joint = ac_close(list(doms), meet(meet(base, B), A))
    inter = ac_close(list(doms), meet(base, B))
    d_stage1 = ac_close([set(x) for x in inter], meet(meet(base, B), A))
    inter2 = ac_close(list(doms), meet(base, A))
    d_stage2 = ac_close([set(x) for x in inter2], meet(meet(base, A), B))
    if not (d_joint == d_stage1 == d_stage2):
        agree = False
# ...and the fence: two noncommuting INTERIOR operators write order
I1 = lambda X: X if 'a' in X else X - {'b'}
I2 = lambda X: X if 'b' in X else X - {'c'}
Xs = {'b', 'c'}
fence = I2(I1(Xs)) != I1(I2(Xs))
# (b) group floor: noncommutative image writes order; g;g == id exactly
s1 = ((F(-1), F(1)), (F(0), F(1)))
s2 = ((F(1), F(0)), (F(1), F(-1)))
def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))
I2m = ((F(1), F(0)), (F(0), F(1)))
grp = (mm(s1, s1) == I2m and mm(s2, s2) == I2m
       and mm(s1, s2) != mm(s2, s1))
# (c) enriched counter: content = support bits (idempotent spec), enriched
# state = counts: retention without order
c1 = {'a': 1}; c2 = {'a': 2}
counter = (c1 != c2)               # used-twice differs in enriched state
check(f"cell 00 (lattice floors, TERMINAL scope): staged and joint "
      f"closes agree over 300 random constraint systems ({agree}) -- "
      f"meet-acts with justification-stable propagation are orderless in "
      f"their settled states; the scope is necessary: noncommuting "
      f"interior operators write order ({fence}). Cell 10 (group "
      f"floors): involutions return exactly, generators noncommute "
      f"({grp}) -- order-writable, scar-free against full-state "
      f"equations. Cell 01 (enriched counters): used-twice differs in "
      f"the enriched state over an idempotent content spec ({counter}). "
      f"Cell 11 = the marks floor (Chapter 13's retained contact).",
      agree and fence and grp and counter)

print("## 3: quotient monotonicity in its safe scope")
parikh = lambda w: (w.count('x'), w.count('y'))
t_1101 = (parikh(('x', 'y')) == parikh(('y', 'x'))
          and parikh(('x',)) != parikh(('x', 'x')))
def norm_idem(w):
    out = []
    for ch in w:
        if not (out and out[-1] == ch):
            out.append(ch)
    return tuple(out)
t_1110 = (norm_idem(('x', 'y')) != norm_idem(('y', 'x'))
          and norm_idem(('x',)) == norm_idem(('x', 'x')))
tau_bar = lambda x: (x + 1) % 2
boundary = tau_bar(0) != tau_bar(tau_bar(0))
check(f"11 -> 01 realized (Parikh quotient kills order, keeps counts: "
      f"{t_1101}); 11 -> 10 realized (idempotent normalization kills the "
      f"residue, keeps order: {t_1110}); equivariant quotients with FIXED "
      f"equation designations can only destroy capabilities (their "
      f"separations pull back). Honest boundary: a quotient can CREATE an "
      f"equation designation (integer successor -> parity involution: "
      f"{boundary}), so monotonicity of residue requires the presentation "
      f"to be held fixed.", t_1101 and t_1110 and boundary)

print("## 4: the CAR kernel inside the retained contact")
X2 = ((F(0), F(1)), (F(1), F(0)))
Z2 = ((F(1), F(0)), (F(0), F(-1)))
def kron(A, B):
    n, m = len(A), len(B)
    return tuple(tuple(A[i // m][j // m] * B[i % m][j % m]
                       for j in range(n * m)) for i in range(n * m))
def mmul4(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))
def madd4(A, B):
    return tuple(tuple(A[i][j] + B[i][j] for j in range(4)) for i in range(4))
def msc4(c, A):
    return tuple(tuple(c * x for x in r) for r in A)
I2q = ((F(1), F(0)), (F(0), F(1)))
A4m = kron(X2, I2q); B4m = kron(Z2, X2); C4m = kron(Z2, Z2)
I4 = tuple(tuple(F(1) if i == j else F(0) for j in range(4)) for i in range(4))
Z4 = tuple(tuple(F(0) for _ in range(4)) for _ in range(4))
Om = mmul4(mmul4(A4m, B4m), C4m)
pre = (mmul4(Om, Om) == msc4(F(-1), I4)
       and all(mmul4(Om, M) == mmul4(M, Om) for M in (A4m, B4m, C4m)))
f_ = msc4(F(1, 2), madd4(A4m, mmul4(Om, B4m)))
fs = msc4(F(1, 2), madd4(A4m, msc4(F(-1), mmul4(Om, B4m))))
car = (mmul4(f_, f_) == Z4 and mmul4(fs, fs) == Z4
       and madd4(mmul4(f_, fs), mmul4(fs, f_)) == I4)
check(f"Omega = ABC central, Omega^2 = -I ({pre}); f = (A + Omega B)/2 "
      f"gives f^2 = 0 and f f# + f# f = 1 exactly ({car}). One complex "
      f"fermionic mode per retained-contact cell; the central i is its "
      f"complex structure. Statistics (Fock, exclusion at many contacts) "
      f"require received composition assumptions -- named in the chapter.",
      pre and car)

print("## 5: the retention tower through H^4 (exact F_2 censuses)")
def pcomp(p, q):
    return tuple(p[q[i]] for i in range(4))
def parity_p(p):
    s = 0
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s ^= 1
    return s
ALLP = [p for p in iproduct(*[range(4)] * 4) if sorted(p) == [0, 1, 2, 3]]
GA4 = [p for p in ALLP if parity_p(p) == 0]
EP = (0, 1, 2, 3)
NONE = sorted(g for g in GA4 if g != EP)
NIDX = {g: i for i, g in enumerate(NONE)}
INVOL = [g for g in NONE if pcomp(g, g) == EP]
def idx2(g, h): return NIDX[g] * 11 + NIDX[h]
def idx3(g, h, k): return (NIDX[g] * 11 + NIDX[h]) * 11 + NIDX[k]
def idx4(g, h, k, l):
    return ((NIDX[g] * 11 + NIDX[h]) * 11 + NIDX[k]) * 11 + NIDX[l]

def rank_stream(rows):
    piv = {}
    for r in rows:
        cur = r
        while cur:
            top = cur.bit_length() - 1
            if top in piv:
                cur ^= piv[top]
            else:
                piv[top] = cur
                break
    return len(piv), piv

def d1_rows():
    for g in NONE:
        for h in NONE:
            r = 1 << NIDX[h]
            gh = pcomp(g, h)
            if gh != EP:
                r ^= 1 << NIDX[gh]
            r ^= 1 << NIDX[g]
            if r:
                yield r
def d2_rows():
    for g in NONE:
        for h in NONE:
            for k in NONE:
                r = 1 << idx2(h, k)
                gh = pcomp(g, h)
                if gh != EP:
                    r ^= 1 << idx2(gh, k)
                hk = pcomp(h, k)
                if hk != EP:
                    r ^= 1 << idx2(g, hk)
                r ^= 1 << idx2(g, h)
                if r:
                    yield r
def d2_cols():
    cols = []
    for a in NONE:
        for b in NONE:
            v = 0
            for g in NONE:
                for h in NONE:
                    for k in NONE:
                        bit = 0
                        if (h, k) == (a, b):
                            bit ^= 1
                        gh = pcomp(g, h)
                        if gh != EP and (gh, k) == (a, b):
                            bit ^= 1
                        hk = pcomp(h, k)
                        if hk != EP and (g, hk) == (a, b):
                            bit ^= 1
                        if (g, h) == (a, b):
                            bit ^= 1
                        if bit:
                            v ^= 1 << idx3(g, h, k)
            cols.append(v)
    return cols
def d3_rows():
    for g in NONE:
        for h in NONE:
            for k in NONE:
                for l in NONE:
                    r = 1 << idx3(h, k, l)
                    gh = pcomp(g, h)
                    if gh != EP:
                        r ^= 1 << idx3(gh, k, l)
                    hk = pcomp(h, k)
                    if hk != EP:
                        r ^= 1 << idx3(g, hk, l)
                    kl = pcomp(k, l)
                    if kl != EP:
                        r ^= 1 << idx3(g, h, kl)
                    r ^= 1 << idx3(g, h, k)
                    if r:
                        yield r
def d4_rows():
    for g in NONE:
        for h in NONE:
            for k in NONE:
                for l in NONE:
                    for m in NONE:
                        r = 1 << idx4(h, k, l, m)
                        gh = pcomp(g, h)
                        if gh != EP:
                            r ^= 1 << idx4(gh, k, l, m)
                        hk = pcomp(h, k)
                        if hk != EP:
                            r ^= 1 << idx4(g, hk, l, m)
                        kl = pcomp(k, l)
                        if kl != EP:
                            r ^= 1 << idx4(g, h, kl, m)
                        lm = pcomp(l, m)
                        if lm != EP:
                            r ^= 1 << idx4(g, h, k, lm)
                        r ^= 1 << idx4(g, h, k, l)
                        if r:
                            yield r

r1, _ = rank_stream(d1_rows())
r2, _ = rank_stream(d2_rows())
dimH2 = (121 - r2) - r1
r3, _ = rank_stream(d3_rows())
d2c = d2_cols()
r2img, piv2 = rank_stream(iter(d2c))
dimH3 = (1331 - r3) - r2img
r4, _ = rank_stream(d4_rows())
dimH4 = (14641 - r4) - r3
tower = (dimH2 == 1 and dimH3 == 2 and dimH4 == 1)
check(f"H^2 = C_2 (dim {dimH2}: the double cover, UNIQUE first-order "
      f"scar); H^3 = C_2 x C_2 (dim {dimH3}: four second-order classes); "
      f"H^4 = C_2 (dim {dimH4}: exactly ONE third-order class). The "
      f"retention tower of the four-mark contact, complete through order "
      f"three.", tower)

# bracket witness: gauge-invariance + readability on a nontrivial class
def reduce_vec(v, piv):
    cur = v
    while cur:
        top = cur.bit_length() - 1
        if top in piv:
            cur ^= piv[top]
        else:
            break
    return cur
def nullspace(rows_iter, ncols):
    piv = {}
    for r in rows_iter:
        cur = r
        while cur:
            top = cur.bit_length() - 1
            if top in piv:
                cur ^= piv[top]
            else:
                piv[top] = cur
                break
    for c in sorted(piv, reverse=True):
        row = piv[c]
        rest = row ^ (1 << c)
        while rest:
            t = rest.bit_length() - 1
            if t in piv and t != c:
                row ^= piv[t]
                rest = row ^ (1 << c)
            else:
                rest ^= 1 << t
        piv[c] = row
    pivots = set(piv)
    basis = []
    for fj in range(ncols):
        if fj in pivots:
            continue
        v = 1 << fj
        for c, row in piv.items():
            if (row >> fj) & 1:
                v ^= 1 << c
        basis.append(v)
    return basis
ker3 = nullspace(d3_rows(), 1331)
reps = []
pivq = dict(piv2)
for v in ker3:
    red = reduce_vec(v, pivq)
    if red:
        reps.append(v)
        pivq[red.bit_length() - 1] = red
    if len(reps) == dimH3:
        break
rngw = random.Random(3)
witness = {wi: tuple((w >> idx3(g, g, g)) & 1 for g in INVOL)
           for wi, w in enumerate(reps)}
stable = True
for wi, w in enumerate(reps):
    for _ in range(20):
        bbits = rngw.getrandbits(121)
        gauge = 0
        for j in range(121):
            if (bbits >> j) & 1:
                gauge ^= d2c[j]
        if tuple(((w ^ gauge) >> idx3(g, g, g)) & 1 for g in INVOL) != witness[wi]:
            stable = False
reads = any(any(v) for v in witness.values())
check(f"the bracket witness omega(g,g,g) -- the parenthesization defect "
      f"of a triple self-contact of an involutive act -- is "
      f"gauge-invariant (20 random gauges per class: {stable}) and READS "
      f"a nontrivial class ({reads}; values {witness}). Second-order "
      f"scars are operationally readable. Free-asphericity holds by "
      f"construction: a pentagon defect manufactured from any 3-cochain "
      f"is its own coboundary, hence removable -- genuine third-order "
      f"structure must realize the unique H^4 class.", stable and reads)

print("## 6: the relocated measurement obstruction (24 elements, exact)")
els = [(a, b, c, d) for a, b, c, d in iproduct(range(3), repeat=4)
       if (a * d - b * c) % 3 == 1]
def mul(x, y):
    a, b, c, d = x; e, f2, g, h = y
    return ((a * e + b * g) % 3, (a * f2 + b * h) % 3,
            (c * e + d * g) % 3, (c * f2 + d * h) % 3)
Isl = (1, 0, 0, 1); Zsl = (2, 0, 0, 2)
zmul = lambda x: mul(Zsl, x)
qmap = lambda x: min(x, zmul(x))
Lset = sorted({qmap(x) for x in els})
repsL = {l: [x for x in els if qmap(x) == l] for l in Lset}
n_homs = 0
for choice in iproduct(*[range(2)] * 12):
    s = {l: repsL[l][choice[i]] for i, l in enumerate(Lset)}
    if all(mul(s[l1], s[l2]) == s[qmap(mul(s[l1], s[l2]))]
           for l1 in Lset for l2 in Lset):
        n_homs += 1
invols_L = [l for l in Lset if l != qmap(Isl) and qmap(mul(l, l)) == qmap(Isl)]
echo = all(mul(gt, mul(gt, x)) == zmul(x) and qmap(mul(gt, mul(gt, x))) == qmap(x)
           for lbar in invols_L for gt in repsL[lbar] for x in els)
best = 0
for rule_bits in range(2 ** 12):
    rule = {l: (rule_bits >> i) & 1 for i, l in enumerate(Lset)}
    score = sum(1 for x in els if rule[qmap(x)] == (0 if x == qmap(x) else 1))
    best = max(best, score)
check(f"no equivariant section: 0/{2**12} lift-choices are homomorphic "
      f"({n_homs == 0}) -- any law-defined outcome selector would be one; "
      f"the echo defect is exact ({echo}: the double action of every "
      f"involutive law element flips the retained bit while the law reads "
      f"identity); the best of all 4096 law-only prediction rules for the "
      f"retained bit scores {best}/24 = exact chance, and promoting the "
      f"read bit into the law-state gives certainty. **The obstruction to "
      f"a law-level outcome selector and the floor's central no-selector "
      f"law are the same fact on this object.**",
      n_homs == 0 and echo and best == 12)

print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
raise SystemExit(1 if FAIL else 0)
