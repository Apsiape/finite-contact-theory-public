#!/usr/bin/env python3
"""Chapter 54: the obstruction spectrum and the amalgamation completion (exact).

Standard library only. Four groups:
  O1  The one-hot debt atlas: five sectors, every single-axis marginal fiber
      nonempty, the joint intersection empty (the source law forbids the zero
      vector).
  O2  The write-only diamond: the map S(t,p,h) = (t,0,p) is positive on the
      cone t >= |p|+|h|, preserves the visible tester span, and admits no
      invariant complement to the hidden line (nonsplit extension).
  O3  The even-parity code: the two cosets have identical single-bit and
      pairwise marginals; the dual codeword 111 separates them.
  O4  The bracket 3-cocycle (-1)^(q1 q2 q3) on Z2: normalized, closed, and not
      a coboundary (exhaustive over all normalized 2-cochains).
"""
from fractions import Fraction as F
from itertools import product

fails = []
def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" {detail}" if detail else ""))
    if not ok:
        fails.append(label)

# ---- O1: one-hot atlas ----
AXES = 5
sectors = [tuple(1 if j == i else 0 for j in range(AXES)) for i in range(AXES)]
check("O1a source law: every sector books exactly one defect", all(sum(d) == 1 for d in sectors))
marginals_ok = all(any(d[i] == 0 for d in sectors) for i in range(AXES))
check("O1b every single-axis marginal fiber is nonempty (choose any other sector)", marginals_ok)
joint = [d for d in sectors if all(d[i] == 0 for i in range(AXES))]
check("O1c the joint intersection is empty (the zero vector is forbidden)", joint == [])

# ---- O2: the diamond ----
def in_cone(t, p, h): return t >= abs(p) + abs(h)
def S(t, p, h): return (t, F(0), p)
samples = [(F(a), F(b), F(c)) for a in range(0, 4) for b in range(-3, 4) for c in range(-3, 4)
           if in_cone(F(a), F(b), F(c))]
check("O2a S maps the cone into the cone (exhaustive small rational grid)",
      all(in_cone(*S(t, p, h)) for (t, p, h) in samples), f"({len(samples)} points)")
check("O2b u compose S = u and pi_p compose S = 0",
      all(S(t, p, h)[0] == t and S(t, p, h)[1] == 0 for (t, p, h) in samples))
# nonsplit: an invariant complement to the hidden line must be a graph h = a t + b p;
# invariance forces p = a t for all (t, p) -- refuted by two exact points
def graph_invariant(a, b):
    for (t, p) in [(F(1), F(0)), (F(1), F(1))]:
        h = a * t + b * p
        t2, p2, h2 = S(t, p, h)
        if h2 != a * t2 + b * p2:
            return False
    return True
check("O2c no invariant complement (graph condition fails for every rational a, b sample)",
      not any(graph_invariant(F(na, 7), F(nb, 7)) for na in range(-14, 15) for nb in range(-14, 15)))

# ---- O3: the even-parity code ----
Ccode = [(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
coset = [tuple((z[i] + (1 if i == 2 else 0)) % 2 for i in range(3)) for z in Ccode]
def marg1(S_, i): return F(sum(z[i] for z in S_), len(S_))
def marg2(S_, i, j): return F(sum(z[i]*z[j] for z in S_), len(S_))
check("O3a identical single-bit marginals",
      all(marg1(Ccode, i) == marg1(coset, i) == F(1,2) for i in range(3)))
check("O3b identical pairwise marginals",
      all(marg2(Ccode, i, j) == marg2(coset, i, j) == F(1,4) for i in range(3) for j in range(i+1,3)))
h = (1,1,1)
sy = lambda z: (-1) ** (sum(h[i]*z[i] for i in range(3)) % 2)
check("O3c the dual codeword 111 separates the cosets",
      all(sy(z) == 1 for z in Ccode) and all(sy(z) == -1 for z in coset))

# ---- O4: the bracket cocycle ----
w = lambda a, b, c: (-1) ** (a * b * c)
def delta_w(a, b, c, d):
    return (w(b,c,d) * w(a,(b+c)%2,d) * w(a,b,c)) * (w((a+b)%2,c,d) * w(a,b,(c+d)%2))
check("O4a normalized 3-cocycle (delta w = 1 at all 16 tuples)",
      all(delta_w(a,b,c,d) == 1 for a,b,c,d in product((0,1), repeat=4)))
def is_coboundary():
    # normalized 2-cochains beta on Z2 with values in {+-1}: beta(x,y)=1 if x=0 or y=0
    for b11 in (1, -1):
        beta = {(x, y): (b11 if (x, y) == (1, 1) else 1) for x in (0,1) for y in (0,1)}
        db = lambda a, b_, c: beta[(b_, c)] * beta[((a+b_)%2, c)] * beta[(a, (b_+c)%2)] * beta[(a, b_)]
        if all(db(a,b_,c) == w(a,b_,c) for a,b_,c in product((0,1), repeat=3)):
            return True
    return False
check("O4b not a coboundary (exhaustive over both normalized 2-cochains)", not is_coboundary())
check("O4c the discriminator: w = -1 exactly at (1,1,1)",
      w(1,1,1) == -1 and all(w(a,b,c) == 1 for a,b,c in product((0,1), repeat=3) if (a,b,c) != (1,1,1)))

print(f"obstruction_spectrum: {'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
