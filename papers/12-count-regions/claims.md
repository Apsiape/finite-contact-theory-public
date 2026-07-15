# Chapter 12 — Claims Snapshot (as of the v0.12.0 tag)

The exact claim-register rows this chapter rests on. The live view is
[`../../docs/public-claim-register.md`](../../docs/public-claim-register.md).
One dependency-free script verifies the chapter from a clean clone:
`verification/count_regions.py` (10/10). Each region theorem is proof-backed and
independently reproduced; the conjugation witness is a registered,
experiment-open protocol, not a performed experiment.

---

## FCT-63 — n=3: the complete region and the negative-Gram boundary

Status: `THEOREM / UNCONDITIONAL / QUANTUM-INFO` (upgrades FCT-61/FCT-62)
Scope: three indistinguishable bosons in the 3-mode Fourier interferometer.
Evidence: `shipped` (§A).

The exact count region is the tetrahedron `{B,R,L ≥ 0, C − B/2 ≥ 0}` in cyclic
orbit coordinates (`B` = full bunching, `C = P111`). The sign inequality
`C ≥ B/2` is the **only** facet not inherited from raw nonnegativity, and it is
the negative-Gram boundary: `P111 + D2 − 2/3 = (4/3)(C − B/2) = (2/9) det G`
(with `D2 = 2/3 + C/3 − 2B/3` redundant with tritter counts). So Chapter 11's
`P111 + D2 ≥ 2/3` (FCT-62) is the **complete** boundary of quantum three-photon
tritter statistics, and the FCT-61 protocol simplifies to tritter counts alone.
Four vertices; `W_min = −2/3`; the registered Ch10 point is at 17% (= 64/375) of
maximal depth.

## FCT-64 — n=4: the 9-simplex, insufficiency of central positivity, six laws

Status: `THEOREM / UNCONDITIONAL / QUANTUM-INFO`
Scope: four indistinguishable bosons in the 4-mode Fourier interferometer.
Evidence: `shipped` (§B).

The region is a 9-simplex whose complete facet description is ten
primitive-projector positivities; only the trivial and sign central irreps give
facets. Central-projector positivity is **insufficient**: the exact
counterexample `x = (3/80,1/20,1/10,1/20,1/20,3/10,1/5,1/16,0,3/20)` has all
five central weights ≥ 0 yet `α_211A = x9 − x2 = −1/20 < 0`. Six new nontrivial
raw-count inequalities every quantum model obeys: `x9 ≥ x2`, `x6 ≥ x4`,
`x7 ≥ x8+x1`, `3·x10 ≥ x3+x5`, `2·x3 ≥ x5`, `3·x8 ≥ x1`.

## FCT-65 — n=5: the emergent qubit, rebit-blindness, and K₅

Status: `THEOREM / UNCONDITIONAL / QUANTUM-INFO`
Scope: five indistinguishable bosons in the 5-mode Fourier interferometer.
Evidence: `shipped` (§C).

The cyclic-shift commutant has dimension 4, 10, 28 for n = 3, 4, 5; at n = 5 the
irrep `(3,1,1)` gains multiplicity two, so the commutant becomes
`ℂ²⁴ ⊕ M₂(ℂ)` — an emergent logical qubit from permutation symmetry and counting
alone. **Rebit-blindness theorem:** no linear functional of single-shot cyclic
counts exposes `σ_y` (the single-shot fiber operator system is exactly
`{I, σ_x, σ_z}`, dim 3); multiplication recovers it
(`[F00131,F00212]|M₂ = −(2i/25)σ_y`, `P_{M₂} = (625/4)[A,B]^†[A,B] = I`). The
exact body `K₅` has affine dimension 25; its coherence cross-section is a disk
(not a ball); hidden-center identity `w0 = (5/6)v_(3,2),0 + (1/6)v_(1⁵),0`.

## FCT-66 — the single-source ℝ/ℂ/ℍ counting no-go

Status: `THEOREM / UNCONDITIONAL / QUANTUM-INFO`
Scope: single-source Fourier counting with real/complex/quaternionic internal
cones.
Evidence: `shipped` (§D).

`K_ℝ = K_ℂ = K_ℍ` exactly — every count effect is real-symmetric on the fiber
(no `σ_y` component), so complex/quaternionic off-diagonals contribute only
their real part (affine dimension 25 in all three; Hausdorff distance zero;
`σ_min ≈ 0.128764`). Single-source Fourier counting provably cannot discriminate
real, complex, and quaternionic quantum mechanics — retroactively explaining why
the Renou-et-al. real-QM test required networks.

## FCT-67 — sequential closure and the conjugation-witness experiment

Status: `THEOREM (closure) / UNCONDITIONAL` + `REGISTERED / EXPERIMENT-OPEN`
(the witness)
Scope: general passive networks on five modes; a registered single-source
protocol.
Evidence: `shipped` (§E, the exact G1 invariants and gap) + `held` (the
experiment).

Rebit-blindness is a property of the cyclic-Fourier POVM, not of bosonic
counting: general passive networks span all of `ℂ[S₅]` (exact rank 120). One
network (`B^R_03, B^R_13, B^i_01, B^i_14`, detect `s=(0,3,1,1,0)`) exposes
`σ_y`: `G1 = (21/1024)I − (1/256)σ_x − (5√2/512)σ_y − (15/1024)σ_z`, trace
`21/512`, rank 1, `|y| = 5√2/512`. **The registered experiment:** a complex
preparation `ρ+ = (I+σ_y)/2` breaks the conjugation law with exact gap
`|p − p̄| = 5√2/256`; one source, two conjugate settings, ~1304 trials/setting at
5σ. **Scope fence:** excludes the real-internal-states + mode-only-passive-optics
class; does NOT falsify all real QM (the McKague–Mosca–Gisin realification
restores simulation via a universal rebit, not implementable in the fixed
grammar — mode unitaries generate only `P_π`, never `J·P_π`). REGISTERED /
EXPERIMENT-OPEN — not a performed experiment, not a claim about nature.
