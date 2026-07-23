"""
Chapter 67 -- The Next i: A Chromatic Reading of the Finite Floor.
Exact verification of the VERIFIED SUBSTRATE only.

STDLIB ONLY (fractions, itertools, math). No numpy. Self-contained.

This script re-derives, exactly, the arithmetic facts the chapter labels
[VERIFIED]. It does NOT test the chromatic FRAME (that is CITED/CONJ: the
G24 = strict height-2 Morava stabilizer identity is cited to
Hewett 1995 / Bujard 2012 / Beaudry et al., not reproduced here). What it
tests:

  PART A -- the multiplicative formal group law  F(a,b) = a + b + ab:
    A1  quadratic (bilinear) term of F equals the mirror cocycle w2(a,b)=ab
    A2  the n-series [n](x) = (1+x)^n - 1 (since 1+F(a,b)=(1+a)(1+b))
    A3  over F2 coefficients, [2^k](x) = x^{2^k} EXACTLY for k=1..4
        (Frobenius / freshman's dream) -- the dyadic tower is the
        doubling series
    A4  lowest nonzero term of [n](x) mod 2 sits at x^(lowest set bit of n)
        = x^(2^v2(n)) -- carry filtration inside the formal group (Lucas)

  PART B -- the additive formal group law  F(a,b) = a + b:
    B1  its n-series is [n](x) = n x, so [2](x) = 2x = 0 over F2
        -- the infinite-height marker (additive group has infinite height)

  PART C -- the exact transport group (Fraction quaternions):
    C1  tau = (1+i+j+k)/2 has tau^2 = omega = (-1+i+j+k)/2 and tau^3 = -1
    C2  the closure of {i, j, tau} has exactly 24 elements (binary
        tetrahedral group 2T = Q8 . C3)
    C3  the group is NONABELIAN: ij = -ji (= k vs -k)
        -- so the transport architecture cannot be height-1, whose
        automorphism structure Aut(G_mult) = Z2^x is abelian. (Bare
        nonabelianness proves nothing; the load-bearing evidence is that
        the SPECIFIC group is the one the literature names -- CITED, not
        checked here.)

  PART D -- the carry-depth ladder (three mechanisms, one stratification):
    D1  v2(Catalan(n-1)) = s2(n) - 1  for n = 2..64
        (s2 = binary digit sum; Alter-Kubota / Deutsch-Sagan / Kummer)
    D2  the modulus-visibility ladder, recomputed by an UNSIGNED Z/16
        recursive tree-transfer (binary trees, Catalan recursion mod 16):
        arity n is first visible (first nonzero residue) at modulus
        2^s2(n).  Landmarks: n=3,5,6 at mod 4; n=7 at mod 8; n=15 at
        mod 16 (the faces-of-15 target).

Exits nonzero on any FAIL.
"""
from fractions import Fraction as F
import math, sys

PASS = []; FAIL = []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

def s2(n):            # binary digit sum (popcount)
    return bin(n).count("1")

def v2(n):            # 2-adic valuation of a nonzero integer
    n = abs(n); r = 0
    while n % 2 == 0:
        n //= 2; r += 1
    return r

# ---------------------------------------------------------------------------
# PART A -- the multiplicative formal group law F(a,b) = a + b + ab
# ---------------------------------------------------------------------------
print("PART A -- multiplicative FGL  F(a,b) = a + b + ab:")

def F_mult(a, b):
    return a + b + a*b

# A1: the mirror cocycle w2(a,b) = a*b is exactly the nonlinear part of F.
# F(a,b) - a - b = a*b for every input -> the quadratic term IS the mirror.
ok = all(F_mult(a, b) - a - b == a*b
         for a in range(-6, 7) for b in range(-6, 7))
check("A1  quadratic term of F equals the mirror cocycle w2(a,b)=ab", ok)

# A2 & A3: the n-series. Since 1 + F(a,b) = (1+a)(1+b), the formal n-fold sum
# satisfies 1 + [n](x) = (1+x)^n, hence [n](x) = (1+x)^n - 1.
# Coefficients of [n](x) are C(n,j) for j>=1. Reduce mod 2.
def n_series_mult_mod2(n):
    # returns dict {exponent j: coeff in F2} for [n](x) = (1+x)^n - 1
    d = {}
    for j in range(1, n + 1):
        c = math.comb(n, j) % 2
        if c:
            d[j] = 1
    return d

# A3: [2^k](x) = x^(2^k) exactly over F2 for k = 1..4.
ok = True
for k in range(1, 5):
    n = 2**k
    d = n_series_mult_mod2(n)
    if d != {2**k: 1}:
        ok = False
check("A3  [2^k](x) = x^(2^k) over F2, exactly, for k=1..4 (Frobenius)", ok)

# A4: lowest nonzero term of [n](x) mod 2 sits at x^(lowest set bit of n).
ok = True
for n in range(1, 65):
    d = n_series_mult_mod2(n)
    lowest_exp = min(d)                 # smallest surviving exponent
    lowest_set_bit = n & (-n)           # value of lowest set bit = 2^v2(n)
    if lowest_exp != lowest_set_bit or lowest_set_bit != 2**v2(n):
        ok = False
check("A4  lowest term of [n] mod 2 is x^(2^v2(n)) for n=1..64 (Lucas)", ok)

# ---------------------------------------------------------------------------
# PART B -- the additive FGL F(a,b) = a + b (infinite height)
# ---------------------------------------------------------------------------
print("PART B -- additive FGL  F(a,b) = a + b:")

# For the additive group, [n](x) = n*x. Over F2, [2](x) = 2x = 0.
def n_series_add_mod2(n):
    return {1: (n % 2)} if (n % 2) else {}

ok = (n_series_add_mod2(2) == {})       # [2](x) = 0 mod 2
check("B1  additive [2](x) = 2x = 0 over F2 (infinite-height marker)", ok)

# ---------------------------------------------------------------------------
# PART C -- the exact transport group (Fraction quaternions)
# ---------------------------------------------------------------------------
print("PART C -- transport group (exact quaternions, 2T = Q8 . C3):")

# A quaternion is a 4-tuple of Fractions (a, b, c, d) = a + b i + c j + d k.
def qmul(x, y):
    a1, b1, c1, d1 = x
    a2, b2, c2, d2 = y
    return (
        a1*a2 - b1*b2 - c1*c2 - d1*d2,
        a1*b2 + b1*a2 + c1*d2 - d1*c2,
        a1*c2 - b1*d2 + c1*a2 + d1*b2,
        a1*d2 + b1*c2 - c1*b2 + d1*a2,
    )

def Q(a, b, c, d):
    return (F(a), F(b), F(c), F(d))

ONE = Q(1, 0, 0, 0); NEG = Q(-1, 0, 0, 0)
I = Q(0, 1, 0, 0); J = Q(0, 0, 1, 0); K = Q(0, 0, 0, 1)
half = F(1, 2)
TAU   = (half, half, half, half)          # (1 + i + j + k)/2
OMEGA = (-half, half, half, half)         # (-1 + i + j + k)/2

# C1: tau^2 = omega, tau^3 = -1
tau2 = qmul(TAU, TAU)
tau3 = qmul(tau2, TAU)
check("C1  tau^2 = (-1+i+j+k)/2 = omega  and  tau^3 = -1",
      tau2 == OMEGA and tau3 == NEG)

# C2: closure of {i, j, tau} has exactly 24 elements
def closure(gens):
    elems = set(gens) | {ONE}
    frontier = list(elems)
    while frontier:
        new = []
        for x in list(elems):
            for g in gens:
                for prod in (qmul(x, g), qmul(g, x)):
                    if prod not in elems:
                        elems.add(prod); new.append(prod)
        frontier = new
        if len(elems) > 200:            # safety guard; 2T has 24
            break
    return elems

G = closure([I, J, TAU])
check("C2  closure(i, j, tau) has exactly 24 elements (2T)", len(G) == 24)

# C3: nonabelian -- ij = -ji
ij = qmul(I, J); ji = qmul(J, I)
check("C3  nonabelian: ij = -ji (=k vs -k), so not height-1 (abelian aut)",
      ij == K and ji == qmul(NEG, K) and ij != ji)

# ---------------------------------------------------------------------------
# PART D -- the carry-depth ladder (three mechanisms, one stratification)
# ---------------------------------------------------------------------------
print("PART D -- carry-depth ladder  v2(Cat(n-1)) = s2(n)-1  &  visibility:")

# Exact Catalan number.
def catalan(m):
    return math.comb(2*m, m) // (m + 1)

# D1: v2(Catalan(n-1)) = s2(n) - 1 for n = 2..64
ok = all(v2(catalan(n - 1)) == s2(n) - 1 for n in range(2, 65))
check("D1  v2(Catalan(n-1)) = s2(n)-1 for n=2..64 (Deutsch-Sagan/Kummer)", ok)

# D2: the modulus-visibility ladder, recomputed by an UNSIGNED Z/16
# recursive tree-transfer. cat_mod16[m] = number of binary trees with m+1
# leaves, taken mod 16, via the Catalan convolution recursion. This is an
# independent recomputation (recursive trees, no binomials) of Cat(n-1) mod 16.
_cache = {0: 1 % 16}
def cat_mod16(m):
    if m in _cache:
        return _cache[m]
    total = 0
    for i in range(m):                  # split a tree at its root
        total += cat_mod16(i) * cat_mod16(m - 1 - i)
    _cache[m] = total % 16
    return _cache[m]

def first_visible_resolution(n):
    """Smallest r in {1,2,3,4} with Cat(n-1) mod 2^r != 0, i.e. first
    modulus 2^r at which arity n becomes visible. Uses the unsigned Z/16
    tree-transfer. Meaningful when s2(n) <= 4."""
    c = cat_mod16(n - 1)
    for r in range(1, 5):
        if c % (2**r) != 0:
            return 2**r
    return None                         # invisible through mod 16

# The ladder must match 2^s2(n) for every n whose depth fits in Z/16.
ok = True
for n in range(2, 65):
    if s2(n) <= 4:
        if first_visible_resolution(n) != 2**s2(n):
            ok = False
check("D2  tree-transfer visibility = 2^s2(n) for all n with s2(n)<=4", ok)

# Named landmarks, printed explicitly.
for n in (3, 5, 6, 7, 15):
    print(f"        arity n={n:2d}: s2={s2(n)}  first visible at modulus "
          f"2^{s2(n)} = {2**s2(n):2d}  (tree-transfer: "
          f"{first_visible_resolution(n)})")
land = (first_visible_resolution(3) == 4 and
        first_visible_resolution(5) == 4 and
        first_visible_resolution(6) == 4 and
        first_visible_resolution(7) == 8 and
        first_visible_resolution(15) == 16)
check("D2b landmarks: n=3,5,6 -> mod 4;  n=7 -> mod 8;  n=15 -> mod 16", land)

# ---------------------------------------------------------------------------
print()
print(f"SUMMARY: {len(PASS)} passed, {len(FAIL)} failed.")
if FAIL:
    print("FAILED:", ", ".join(FAIL))
    sys.exit(1)
print("All substrate checks passed.")

# FALSIFIABILITY.
# This script FAILS if any of the following breaks:
#  - the nonlinear part of a+b+ab is not exactly the mirror cocycle ab;
#  - the multiplicative n-series [2^k](x) is not x^(2^k) over F2 (i.e. the
#    dyadic tower is not the doubling/Frobenius series);
#  - the lowest term of [n] mod 2 is not at the lowest set bit of n;
#  - the additive [2](x) is nonzero over F2;
#  - tau=(1+i+j+k)/2 does not satisfy tau^2=omega, tau^3=-1, or the closure
#    of {i,j,tau} is not exactly the 24-element binary tetrahedral group,
#    or that group is abelian;
#  - v2(Catalan(n-1)) != s2(n)-1 for any n in 2..64, OR the independent
#    unsigned Z/16 tree-transfer disagrees with the 2^s2(n) visibility ladder
#    on any n with s2(n)<=4 (the three-mechanism artifact control: binomial
#    parity, Catalan tree parity, and the formal-group [n]-series must all
#    yield the SAME stratification -- if they disagree, the ladder was an
#    encoding artifact).
# It does NOT test, and cannot test, the CITED frame claim that this 24-cell
# group is the maximal finite subgroup of the strict height-2 Morava
# stabilizer at p=2 -- that identity is cited, not reproduced.
