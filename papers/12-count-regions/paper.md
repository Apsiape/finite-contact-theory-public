# Chapter 12 — The Exact Quantum Count Regions and the Limits of Counting

**Release:** v0.12.0 · **Status of the chapter:** a stack of proof-backed,
independently reproduced quantum-information theorems (no theory buy-in), plus
one **registered, experiment-open** protocol. It also upgrades Chapters 10–11:
the negative-Gram inequality is shown to be *the* complete boundary of quantum
three-photon tritter statistics.

---

## The live release ceiling

This chapter carries the program's live ceiling, quoted identically in the
README, the claim register, and the v0.12.0 release notes:

> Finite Contact Theory is a finite reconstruction program with a scoped theorem
> stack on three published recovery lines — a quantum-facing axis, from one-use
> contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell
> boundary, a carrier grammar grown from one-use contact, and a
> behavior-conditioned contextual capacity with an exact strict preparation gap;
> a finite-epistemics axis, from the identifiability and debt calculus to the
> inquiry calculus and its second law of asking, four theorems separating the
> structure of time, and a measured generative floor; and a contact-interface
> reconstruction, in which a retained interface forces a quaternionic
> state/receiver cell whose self-dual closure is the 24-cell and the F_4 root
> system and whose finite measurement calculus forces the quadratic Born frame
> rule (a finite Gleason theorem) exactly where a triality Kochen-Specker
> obstruction forbids a global noncontextual assignment, and in which
> independently generated cells recover the E_8–hexacode closure spine under
> named receiver laws that a forcing audit shows the floor does not select over
> matched lawful alternatives, so the floor forces the atlas of lawful closures
> and the terminal self-dual class but never the specific member, and the
> selection of a world-phase is a conserved, received input — a fourth,
> first-extension line that is conditional and experiment-open: an unconditional
> accessible-positivity theorem exhibits a three-contact sector whose every
> passive-linear-optical probability is nonnegative yet which lies outside the
> positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor
> this predicts a possible violation of Hilbert-space positivity — a negative
> three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics
> forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill
> conditions, and a clean mixed-state exclusion theorem then proves the
> gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative
> for every partially-distinguishable Hilbert model whether pure or mixed, so
> the registered negative-Gram vector lies outside the entire clean
> partial-distinguishability class by the raw-count test P111 + D2 >= 2/3,
> closing the clean core of the exclusion while multiphoton, detector,
> transfer-matrix, and source-drift nuisances remain the experimental layer for
> an external expert — and a fifth line mapping the exact quantum count regions:
> for n indistinguishable bosons in the n-mode Fourier interferometer the
> achievable region of count statistics is an exact simplex for n <= 4 (at n = 3
> the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the
> registered protocol reduces to tritter counts alone), central-projector
> positivity is insufficient at n = 4 with six new raw-count laws, and a
> structural phase transition at n = 5 produces an emergent logical qubit from
> permutation symmetry and counting alone, where a rebit-blindness theorem shows
> single-shot cyclic counts cannot expose sigma_y and a single-source
> real/complex/quaternionic counting no-go holds, both overcome by general
> passive networks, culminating in a registered, experiment-open single-source
> conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per
> setting) that excludes a named real-internal-states plus mode-only-optics
> model class but does not falsify all real quantum mechanics — under which the
> quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the
> preparation gap is an exact theorem at KCBS-pentagon scope, the interface
> reconstruction is a finite model-scope recovery on a real-quantum cell, the
> multi-floor closures are model-scope recoveries whose forcing boundary is
> exactly mapped, the accessible-positivity and mixed-state exclusion theorems
> and the count-region theorems are unconditional and independently reproduced,
> while the physical realizations — the negative-Gram prediction and the
> conjugation witness — are conditional, bridge-premise-gated, experiment-open
> registered protocols awaiting a dedicated experiment and external expert
> review, and every unearned generalization — complex quantum mechanics, the
> actuality of one outcome, the universal Born rule, whether nature realizes any
> of these structures, which world-phase is selected, whether nature contains
> the odd identity-holonomy sector, whether the apparatus nuisances close the
> full exclusion, and whether any experiment realizes the conjugation witness —
> is left open by name; these chapters are an archival priority record of
> mathematically closed theorems and registered conditional protocols, not
> empirical discoveries.

---

## 0. What this chapter is

Fix `n` indistinguishable bosons, one entering each input of the `n`-mode
**Fourier interferometer**, and record only the **count statistics** (the
occupation pattern at the outputs). As the internal (distinguishability) state
of the sources ranges over all quantum possibilities, the achievable count
vectors sweep out an exact convex region. This chapter computes those regions,
finds where the counting grammar hits its own limits, and turns one limit into
a lab-realistic experiment. Everything is standalone quantum-information
mathematics — no theory buy-in — that also sharpens Chapters 10–11.

The results, section by section: (1) the `n = 3` region is an explicit
tetrahedron whose **only** non-trivial facet is the negative-Gram sign
inequality — so Chapter 11's `P111 + D2 >= 2/3` is *the* complete boundary and
the registered protocol simplifies to tritter counts; (2) the `n = 4` region is
a 9-simplex, central-projector positivity is provably **insufficient**, and six
new raw-count laws appear; (3) at `n = 5` there is a structural **phase
transition** — an emergent logical qubit — with a **rebit-blindness** theorem;
(4) a single-source **ℝ/ℂ/ℍ counting no-go**; (5) the sequential-closure
resolution and a **registered conjugation-witness experiment**.

All exact numbers are machine-checked from a clean clone
(`verification/count_regions.py`, 10/10).

## 1. n = 3: the complete region, and the negative-Gram boundary (upgrades Ch10–11)

In cyclic-orbit coordinates `B = P300+P030+P003` (full bunching),
`R = P201+P012+P120`, `L = P210+P102+P021` (the two chiralities), `C = P111`
(with `B+R+L+C = 1`), the exact achievable region is the tetrahedron

```
{ B, R, L >= 0,   C - B/2 >= 0 }.
```

**The sign inequality `C >= B/2` is the only facet not inherited from raw
probability nonnegativity.** It is exactly the negative-Gram boundary: the
gauge-free count witness satisfies

```
P111 + D2 - 2/3 = (4/3)(C - B/2) = (2/9) det G,
```

where `D2 = 2/3 + C/3 - 2B/3` is **redundant** with the tritter counts and `det
G` is the internal-state Gram determinant of Chapter 11. Hence `C - B/2 =
(1/6) det G`, and Chapter 11's inequality `P111 + D2 >= 2/3` is **the complete
boundary of quantum three-photon statistics at the tritter** — a single
scalar-block ("sign") facet `Tr(P_sign ρ) >= 0`. The irrep functionals are
`Tr P_(3) = (3/2)B`, `Tr P_(2,1) = R + L`, `Tr P_(1³) = C - B/2`. The four
vertices are the trivial `(2/3,0,0,1/3)`, the sign vertex `(0,0,0,1)`, and the
two standard vertices `(0,1,0,0)`, `(0,0,1,0)`. The maximal violation of the
sign facet on the raw simplex is `W_min = -2/3` (at `B = 1`); the registered
Chapter-10 point sits at `W = -128/1125`, about **17%** (`= 64/375`) of maximal
depth.

**Upgrade to the register.** The Chapter-11 exclusion (FCT-62) is now identified
as the complete `n = 3` boundary, and the FCT-61 protocol simplifies to tritter
counts alone; the corresponding rows are cross-referenced accordingly.

## 2. n = 4: the 9-simplex, and the insufficiency of central positivity

With ten cyclic-orbit coordinates `x1..x10` (representatives `4000, 3001, 2200,
3100, 3010, 2011, 2101, 2020, 2110, 1111`), the region is a **9-simplex** whose
complete facet description is the ten **primitive-projector** positivities
`α_a >= 0`. **Only the trivial and sign central irreps give facets** (a facet
comes from an irrep exactly when its dimension is 1); the multidimensional
irreps split into primitive facets, because the Fourier counts resolve a
maximal abelian subalgebra inside each irrep block while central characters are
blind to block-internal directions.

**Central-projector positivity is insufficient at `n = 4`.** The exact
counterexample `x = (3/80, 1/20, 1/10, 1/20, 1/20, 3/10, 1/5, 1/16, 0, 3/20)`
has all five central weights `(1/10, 3/10, 1/5, 3/10, 1/10) >= 0`, yet the
primitive positivity `α_211A = x9 - x2 = -1/20 < 0`. So a would-be quantum count
vector can pass every central test and still be non-physical.

**Six new raw-count inequalities** every quantum model obeys — the six
non-central primitive positivities:

```
x9 >= x2,   x6 >= x4,   x7 >= x8 + x1,   3·x10 >= x3 + x5,   2·x3 >= x5,   3·x8 >= x1.
```

## 3. n = 5: the phase transition — an emergent qubit and rebit-blindness

The commutant of the cyclic shift inside `ℂ[S_n]` has dimension `4, 10, 28` for
`n = 3, 4, 5`. For `n <= 4` every cyclic multiplicity is `<= 1` (hence the
regions are simplices). At `n = 5` the irrep `(3,1,1)` (dimension 6,
five-cycle character `+1`) acquires multiplicity two — two standard tableaux
collide at major-index residue `0` — so the commutant becomes
`ℂ²⁴ ⊕ M_2(ℂ)`: **an emergent logical qubit from permutation symmetry and
counting alone.**

On that qubit fiber, exactly five cyclic count effects are nonzero; in a real
orthonormal basis they are `(1/5)I` plus real multiples of `σ_x` and `σ_z`
only:

```
F[00131] = (1/5)I + (1/(5√5))(2σ_x - σ_z),   F[00212] = (1/5)I + (1/(5√5))(σ_x + 2σ_z),
F[01022] = (1/5)I - (1/(5√5))(σ_x + 2σ_z),   F[01103] = (1/5)I - (1/(5√5))(2σ_x - σ_z),
F[11111] = (1/5)I.
```

Coherence witnesses `Δ1 = p00131 - p01103`, `Δ2 = p00212 - p01022` invert to
`x = (√5/2)(2Δ1 + Δ2)`, `z = (√5/2)(-Δ1 + 2Δ2)`.

> **Rebit-blindness theorem.** No linear functional of single-shot cyclic counts
> exposes `σ_y`. The single-shot operator system on the fiber is exactly
> `{I, σ_x, σ_z}` (dimension 3); `σ_y` is invisible.

But it is not lost — *multiplication* recovers it. The generated `*`-algebra is
the full 28-dimensional commutant:
`[F00131, F00212]|_{M_2} = (1/125)[2σ_x - σ_z, σ_x + 2σ_z] = -(2i/25) σ_y`, and
the block projector is `P_{M_2} = (625/4)[A,B]^† [A,B] = I`. Single-shot
counting is a *linear* readout and misses `σ_y`; the algebra it generates does
not.

**The exact convex body `K_5`** has affine dimension 25: the 24 scalar-block
vertices span a 23-simplex, and the coherence cross-section is a **disk** (not a
ball). A hidden-center identity places the fiber's maximally-mixed count vector
as an exact convex combination of two classical vertices, one of them the sign
representation: `w0 = (5/6) v_(3,2),0 + (1/6) v_(1⁵),0`. The disk radius is
`τ(β) = min{(6/5) β_(3,2),0, 6 β_(1⁵),0}`, with two second-order-cone sheets
meeting on the ridge `β_(3,2),0 = 5 β_(1⁵),0`.

## 4. The single-source ℝ/ℂ/ℍ counting no-go

Keep the same Fourier interferometer and restrict the internal states to real,
complex, or quaternionic cones. **Then `K_ℝ = K_ℂ = K_ℍ` exactly.** Every count
effect is real-symmetric on the fiber (it has no `σ_y` component, §3), so a
quaternionic off-diagonal `q = a + ib + jc + kd`, or a complex one, contributes
only its real part; the achievable count bodies coincide (measured affine
dimension 25 in all three; Hausdorff distance zero; the common dimension is
robustly certified from 26 preparations with `σ_min ≈ 0.128764`, valid for
internal error `ε < 0.0128`).

> **Single-source Fourier counting provably cannot discriminate real, complex,
> and quaternionic quantum mechanics** — retroactively explaining why the
> Renou-et-al. real-QM test required *networks*, not a single source.

## 5. Sequential closure, and the conjugation-witness experiment (registered)

Rebit-blindness is a property of the cyclic-Fourier POVM, **not** of bosonic
counting. Allowing general passive networks, the effects of all finite protocols
span *all* of `ℂ[S_5]` (two explicit networks, 252 effects, exact rank 120).
Already one passive network exposes `σ_y`: the gates `B^R_03, B^R_13, B^i_01,
B^i_14` (with `B^R = [[1,1],[-1,1]]/√2`, `B^i = [[1,i],[i,1]]/√2`), detecting
`s = (0,3,1,1,0)`, compress on the fiber to

```
G1 = (21/1024) I - (1/256) σ_x - (5√2/512) σ_y - (15/1024) σ_z,
```

with trace `21/512`, rank 1, and a nonzero `σ_y` coefficient `|y| = 5√2/512`
(machine-verified exactly).

**The experiment.** There is a conjugation law: for *any* real-symmetric
internal state, `p_𝒫 = p_𝒫̄` exactly (conjugate every unitary in the network,
keep the detectors). A **complex** preparation `ρ+ = (I + σ_y)/2` breaks it:

```
p   = (21 - 10√2)/1024,     p̄  = (21 + 10√2)/1024,     |p - p̄| = 5√2/256 ≈ 0.0276.
```

One source, two conjugate network settings, one count event each. Robustness:
certification holds for per-probability error `ε < 5√2/1024 ≈ 0.0069`; ideal
Bernoulli `5σ` at about **1304 trials per setting**. (A two-stage Fourier
variant gives gap `√2/100 ≈ 0.0141`.)

> **⚠ Scope fence (mandatory).** This excludes the **real-internal-states +
> mode-only-passive-optics** model class. It does **not** falsify every real
> reformulation of quantum mechanics: the McKague–Mosca–Gisin realification
> restores simulation *if* optical transformations may act on a universal rebit
> — which is **not implementable in the fixed grammar** (mode unitaries generate
> only the permutation actions `P_π`, never `J·P_π`). See McKague et al.
> (arXiv:0810.1923) and Renou et al. (arXiv:2101.10873); broader operational
> real formulations exist that reproduce arbitrary sequential protocols.

## 6. Appendix — exposure sparsity and growth quantization

Two clean, citation-free structural facts (both machine-checked). **Exposure
sparsity:** the number of cyclic count coordinates is `(N_5, C_5) = (26, 28)`
and `(N_6, C_6) = (80, 136)` against the commutant dimension — the count-visible
fraction of the emergent structure shrinks with `n`. **Growth quantization:**
for connected stationary finite-dimensional inclusion towers, Perron growth
rates below 4 are ADE-quantized `r = 4cos²(π/h)`; the smallest non-integer rate
is `φ² = (3+√5)/2` (the `A_4`/Fibonacci tower, rooted capacities `1,1,2,5,13,34`
with `D_(ℓ+2) = 3 D_(ℓ+1) - D_ℓ`). (The super-exponential fiber-growth
asymptotic is held for a future release pending an external citation check; no
unverified citation is shipped here.)

## Verification status

*Every exact claim above was independently reproduced by a second implementation
(and the tritter formulas by a from-scratch bosonic computation assuming no
formulas). The `n = 3/4` region theorems, the `n = 5` commutant and `K_5`
geometry, the rebit-blindness and its sequential resolution are proof-backed
with verifier scripts; the experiment is a **REGISTERED, EXPERIMENT-OPEN**
protocol with a precisely named target model class — not a performed experiment
and not a claim about nature.*

The claim-register rows this chapter rests on are frozen in
[`claims.md`](claims.md); the freeze record is in [`RELEASE.md`](RELEASE.md).
