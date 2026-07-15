# Expected Output — negative_gram_holonomy.py

Frozen at the v0.10.0 release. Dependency-free; exact where it can be
(`fractions.Fraction` over `Q(sqrt 3)`): the core numbers, the foundational
Fourier identity, positivity on rational toric witnesses, the unitary-core
reduction and strict margin, the -495 kill, and separable-loss covariance are
exact; an independent adversarial descent over the full toric set corroborates
the universal theorem. Runs in a few seconds. Run from this directory (or from
`verification/scripts/` — the live copy is identical):

```powershell
python negative_gram_holonomy.py
## A: the (conditional, preregistered) prediction -- exact numbers
  [PASS] Delta_3 = 1-3r^2-2r^3 = -64/125 = -64/125, factors as (1-2r)(1+r)^2 (True), negative exactly for r > 1/2 (True); r = 3/5 received, negative sign is the odd Z_2 holonomy consequence.
  [PASS] tritter probs P111=7/1125(7/1125), P300=206/3375(206/3375), P210=152/1125(152/1125), nonnegative, normalized (1=1).
  [PASS] D_2=41/75(41/75); W = P111+D_2-2/3 = -128/1125 = (2/9)Delta_3 (True); Q_3 = P111-D_2+4/9 = -12/125 = (4/9)b (True); pairwise-only null gives Q_3 = 0 (b->0).
  [PASS] Delta_3 = det G = 1-3r^2+2r^3 cosPhi; PSD forces cosPhi >= (3r^2-1)/(2r^3) = 5/27(5/27), i.e. Phi <= 79.3 deg, while the extension reaches Phi = pi. So Delta_3 = -64/125 < 0 is OUTSIDE the PSD Hilbert Gram cone.
## B: the passive-linear-optics toric identity prod_even z = prod_odd z
  [PASS] the even and odd permutation triples each cover every (row,col) once (True); so prod_even z = prod_odd z = prod(all entries): 223092870 = 223092870 = 223092870 (True).
## C: universal accessible positivity -- 152N + 9|per|^2 - 36|det|^2 >= 0 for EVERY A
  [PASS] the foundational identity Q = 152N - 243M + 810 Re(alpha conj delta) holds exactly on 4000 Gaussian-rational (x,y) (True) -- the C_3-Fourier reduction the proof rests on.
  [PASS] POSITIVITY is exact on 5853 nonzero rational toric witnesses (x0x1x2 = y0y1y2 enforced exactly; Q >= 0 in exact Q(sqrt3) arithmetic): True.
  [PASS] an INDEPENDENT adversarial descent over the full toric set (200k broad + 300 restarts) finds NO Q/N below zero: min broad 6.1636, min descent 3.2601 (both > 0, strict). The proof's conclusion Q > 0 on every nonzero toric vector is corroborated by a hostile numerical hunt.
  [PASS] the (7/2)-margin ARBITRARY-matrix statement is FALSE (stays killed): A=[[-4,-1,1],[-7,1,-3],[6,-3,-5]] has N=3722, per=-6, det=124, 152N+9|per|^2-36|det|^2-(7/2)N = -495 (-495 < 0); yet it obeys the toric identity (True) and still satisfies the PROVEN zero-margin 152N+9|per|^2-36|det|^2 = 12532 >= 0.
## D: on the lossless unitary core U(3), the strict margin 152N+9|per|^2-36|det|^2 >= (7/2)N
  [PASS] on the unitary core the exact reduction 33N+2|per|^2-8 = (3/2)(7s+180D) and the strict margin hold on 120 rational Cayley unitaries (True) and all six permutation matrices (True); the Fourier tritter (exact) has N=2/9, |per|^2=1/3 and SATURATES at 33N+2|per|^2=8 (True).
## E: separable input/output loss A = D_L U D_R is covered (exact covariance)
  [PASS] every monomial of A = D_L U D_R picks up the same factor kappa (True); hence N, |per|^2, |det|^2 all scale by |kappa|^2 (True); the degree-6 form scales by |kappa|^2, so positivity transfers to every separably attenuated unitary -- and, with the universal theorem, to every passive-linear-optical apparatus.

# RESULT: 11 passed, 0 failed
# (A) universal accessible positivity: PROVEN + verified (exact + adversarial).
# (B) the physical Delta_3 < 0 prediction is CONDITIONAL, preregistered,
#     experiment-OPEN -- an archival/priority record, not a discovery.
```

Reminder on scope: **(A)** the accessible-positivity theorem is
unconditional and PROVEN for every complex 3x3 matrix (hence every passive
linear-optical apparatus, lossless or lossy); **(B)** the physical
`Delta_3 < 0` prediction is conditional, preregistered, and experiment-open —
an archival/priority record, not a discovery.
