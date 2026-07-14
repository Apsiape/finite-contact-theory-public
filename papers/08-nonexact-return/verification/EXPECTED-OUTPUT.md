# Expected Output — nonexact_return_reconstruction.py

Frozen at the v0.8.0 release. Dependency-free; run from this directory (or
from `verification/scripts/` — the live copy is identical):

```powershell
python nonexact_return_reconstruction.py
```

Runtime is a few seconds (exhaustive exact arithmetic). Expected output,
verbatim:

```text
## 1: the primitive receiver is the quaternions H
  [PASS] the three retained quarter-turns satisfy I^2=J^2=K^2=-1 and IJ=K=-JI (quaternion relations: True); their real commutant has dimension 4 = H (a division algebra, so the 4-real-dimensional carrier is irreducible and minimal); the invariant symmetric positive form is unique up to scale (dimension 1) = c*I_4, forcing the isotropic quadratic evaluation N=c(x0^2+..+x3^2). The receiver carries a forced 1+3 split: one return-even direction plus three noncommuting quarter-turns.
## 2: the 24-cell state orbit and its self-dual receiver pole
  [PASS] the 24 unit states are the Hurwitz units (the 24-cell); exhaustive polar enumeration over all C(24,4)=10626 supporting quadruples gives conv(states)^o = the 24 receiver vectors (True) and conv(receivers)^o = the 24 states (True). States generate receivers and receivers regenerate the states: an exact self-hosting state<->receiver fixed point.
## 3: the 48 vectors are the F_4 root system
  [PASS] the 48 combined state+receiver vectors are reflection-closed (True) with integer Cartan numbers (True); the four simple reflections generate a group of order 1152 = 1152 = |W(F_4)|. The exceptional root system arises as the reflection closure of the state/receiver polarity, not as an installed symmetry.
## 4: the first forced scale-free interface magnitude is 1/2
  [PASS] every nonzero state/receiver overlap has |<p,r>| = 1 exactly (True); with |p|^2=1 and |r|^2=2 the dimensionless contact ratio |<p,r>|^2/(|p|^2|r|^2) = 1/2 for every contact (a pi/4 angle). This is a forced, scale-free, gauge-free interface invariant -- the first nontrivial magnitude the closure generates. Scope: this 24-cell closure, not nature.
## 5: FINITE GLEASON -- the Born frame rule is forced
  [PASS] the 24 rays carry exactly 24 orthonormal tetrad contexts; the context-incidence rank is 15, so normalized frame valuations form a 9-dimensional affine family -- the dimension of real symmetric trace-one 4x4 operators; the 24 ray projectors span all of Sym(4) (rank 10) and every context resolves the identity (True). Therefore every normalized frame valuation is uniquely f(x)=tr(rho P_x). The quadratic Born frame rule is forced by the finite context family alone -- no continuum, no continuity.
## 6: TRIALITY CONTEXTUALITY -- probability lives where pointing cannot
  [PASS] no global deterministic noncontextual assignment exists (True, exhaustive); there are exactly 16 minimal nine-context parity proofs, ALL inside the state<->receiver interface (True) and each using three contexts from every D_4 triality sector (True); any one or two sectors admit a global assignment (True) while all three together do not (True). Neither pole is contextual alone -- contextuality is an irreducibly three-way (triality) obstruction generated at the interface. The valuation is uniquely lawful exactly where a global pointing is impossible.

# RESULT: 6 passed, 0 failed
```

The script exits `0` on all-pass and nonzero if any check fails. Every
load-bearing quantity is exact (`fractions.Fraction`); the polar duality,
the reflection closure, the Gleason rank, and the Kochen–Specker parity
census are all exhaustive.
