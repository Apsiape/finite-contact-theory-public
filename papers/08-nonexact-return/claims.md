# Chapter 8 — Claims Snapshot (as of the v0.8.0 tag)

The exact claim-register rows this chapter rests on. The live view is
[`../../docs/public-claim-register.md`](../../docs/public-claim-register.md);
if a row is later promoted, demoted, or withdrawn, the register (not this
frozen snapshot) carries its current status.

All rows are `shipped`: the single dependency-free script
`verification/nonexact_return_reconstruction.py` verifies every one from a
clean clone, exactly and exhaustively, in a few seconds.

---

## FCT-45 — Non-Exact Return and the Quaternionic Receiver

Status: `MODEL-SCOPE / RECOVERY`
Scope: the minimal real receiver faithful on the retained central return.
Evidence: `shipped` (Section 1).

The three retained quarter-turns satisfy the quaternion relations
(`I^2=J^2=K^2=-1`, `IJ=K=-JI`); the minimal real carrier faithful on the
retained return `z ↦ -1` is four-dimensional and irreducible (its
commutant is the division algebra `H`); the invariant positive form is
unique up to scale (`c·I_4`), forcing the isotropic quadratic evaluation
and a `1+3` split. Fence: an algebra grading, not a spacetime metric.

## FCT-46 — The Self-Hosting State/Receiver Fixed Point (24-cell)

Status: `MODEL-SCOPE / RECOVERY`
Scope: the unit-state polytope of the quaternionic cell and its polar dual.
Evidence: `shipped` (Section 2).

The unit states are the 24 Hurwitz units (the 24-cell); exhaustive polar
enumeration (all `C(24,4)=10626` supporting quadruples) gives
`conv(states)° = ` the 24 receiver vectors and `conv(receivers)° = ` the
24 states. States generate receivers and receivers regenerate states: an
exact self-hosting state/receiver fixed point (the reception chapter's
sought object, realized finitely). Recovery: the 24-cell self-duality.

## FCT-47 — The F_4 Closure of the State/Receiver Polarity

Status: `RECOVERY`
Scope: the 48 combined state+receiver vectors.
Evidence: `shipped` (Section 3).

The 48 vectors are reflection-closed with integer Cartan numbers — the
`F_4` root system — and the four simple reflections generate `W(F_4)` of
order 1152. The exceptional root system arises as the reflection closure
of the state/receiver polarity, not as an installed gauge symmetry.
Residual: the two-floor `E_8` extension is a later chapter, not claimed
here.

## FCT-48 — The Forced 1/2 Interface Magnitude

Status: `MODEL-SCOPE`
Scope: state/receiver overlaps on the 24-cell closure.
Evidence: `shipped` (Section 4).

Every nonzero state/receiver overlap has `|⟨p,r⟩| = 1`, so the
dimensionless ratio `|⟨p,r⟩|^2/(|p|^2|r|^2) = 1/2` for every contact (a
`π/4` angle) — a forced, scale-free, gauge-free interface invariant, the
first nontrivial magnitude the closure generates. Fence: it is a ratio,
and its scope is this closure, not nature.

## FCT-49 — Finite Gleason: the Born Frame Rule

Status: `THEOREM / MODEL-SCOPE / RECOVERY`
Scope: normalized frame valuations on the 24-ray Peres configuration.
Evidence: `shipped` (Section 5).

The 24 rays carry exactly 24 orthonormal tetrad contexts; the
context-incidence rank is 15, so frame valuations form a nine-dimensional
affine family equal to real-symmetric trace-one `Sym(4,R)` (the
projectors span, every context resolves the identity). Therefore every
normalized frame valuation is uniquely `f(x)=tr(ρ P_x)` — the quadratic
Born frame rule, forced by the finite context family with no continuum
and no continuity. Recovery: a finite, exact Gleason theorem. Residual:
does not derive the universal Born rule for general measurements.

## FCT-50 — Triality Contextuality; Born and Pointing Are Two Faces

Status: `THEOREM / MODEL-SCOPE / RECOVERY`
Scope: deterministic noncontextual assignments on the same 24 rays.
Evidence: `shipped` (Section 6).

No global deterministic noncontextual assignment exists; there are
exactly 16 minimal nine-context parity proofs (Kernaghan-type), all in
the state/receiver interface, each using three contexts from every `D_4`
triality sector; any one or two sectors are consistent, all three are
not. Neither pole is contextual alone — contextuality is an irreducibly
three-way (triality) obstruction generated at the interface. Placed
beside FCT-49: **the valuation is uniquely lawful exactly where a global
pointing is impossible** — Born valuation and Kochen-Specker
contextuality are the two faces of one finite closure. Recovery: the
Peres 24-ray Kochen-Specker set. Residual: the actual outcome must be
contextual, history-bearing, explicitly received, or totalized — the
standing open hinge; complex quantum mechanics and every nature-facing
prediction remain held open.
