# Chapter 10 — Negative-Gram Identity Holonomy: The Program's First Divergence

**Release:** v0.10.0 · **Status of the chapter:** one unconditional theorem
and one *conditional, preregistered, experiment-open* prediction. Every prior
chapter was a **recovery** of known structure from the finite-contact floor.
This chapter is the program's **first extension** — it predicts a possible
*violation* of Hilbert-space positivity. It recovers nothing, and it is **not**
a claimed discovery.

---

## The live release ceiling

This chapter carries the program's live ceiling, quoted identically in the
README, the claim register, and the v0.10.0 release notes:

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack on three published recovery lines — a quantum-facing axis,
> from one-use contact to counting, one-receiver gluing, rational Born
> weights, the CHSH/Pell boundary, a carrier grammar grown from one-use
> contact, and a behavior-conditioned contextual capacity with an exact strict
> preparation gap; a finite-epistemics axis, from the identifiability and debt
> calculus to the inquiry calculus and its second law of asking, four theorems
> separating the structure of time, and a measured generative floor; and a
> contact-interface reconstruction, in which a retained interface forces a
> quaternionic state/receiver cell whose self-dual closure is the 24-cell and
> the F_4 root system and whose finite measurement calculus forces the
> quadratic Born frame rule (a finite Gleason theorem) exactly where a triality
> Kochen-Specker obstruction forbids a global noncontextual assignment, and in
> which independently generated cells recover the E_8–hexacode closure spine
> under named receiver laws that a forcing audit shows the floor does not
> select over matched lawful alternatives, so the floor forces the atlas of
> lawful closures and the terminal self-dual class but never the specific
> member, and the selection of a world-phase is a conserved, received input —
> and a fourth, first-extension line that is conditional and experiment-open:
> an unconditional accessible-positivity theorem exhibits a three-contact
> sector whose every passive-linear-optical probability is nonnegative yet
> which lies outside the positive-semidefinite Hilbert Gram cone, and on one
> received apparatus anchor this predicts a possible violation of
> Hilbert-space positivity — a negative three-state Gram discriminant
> Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 —
> preregistered with its protocol, nulls, and kill conditions — under which the
> quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the
> preparation gap is an exact theorem at KCBS-pentagon scope, the interface
> reconstruction is a finite model-scope recovery on a real-quantum cell, the
> multi-floor closures are model-scope recoveries whose forcing boundary is
> exactly mapped, the accessible-positivity theorem is unconditional while its
> physical realization is a conditional, bridge-premise-gated prediction
> awaiting a dedicated experiment and external expert review, and every
> unearned generalization — complex quantum mechanics, the actuality of one
> outcome, the universal Born rule, whether nature realizes any of these
> structures, which world-phase is selected, and whether nature contains the
> odd identity-holonomy sector — is left open by name; this chapter is an
> archival priority record of a mathematically closed conditional prediction,
> not an empirical discovery.

---

## 0. What this chapter adds — and the recovery/divergence fence

Chapters 1–9 all did the same *kind* of thing: they **recovered** known
mathematics or physics (the CHSH bound, a finite Gleason theorem, the `E_8`
spine) from a deeper finite-contact floor. A recovery is tested by "does it
match the known answer?", and matching is success.

This chapter is different in kind. It is an **extension**: it asks whether a
genuinely non-classical feature of the floor — *locally exact identity
contacts that fail to glue into one global carrier* — yields a concrete,
dimensionless, falsifiable prediction that **differs** from ordinary
complex-Hilbert quantum mechanics. It does. An extension is **not** tested by
reduction to the incumbent; it is tested by internal rigor, self-consistency,
and a sharp observable divergence. Judging it by "does it reduce to standard
QM?" would be a category error — the divergence is the whole point.

Two things are published here, and they must be held rigidly apart:

- **(A) THE THEOREM — unconditional.** A three-contact class function with a
  negative sign-sector eigenvalue nonetheless keeps *every* physically
  accessible (passive-linear-optical) probability nonnegative. So it is a
  lawful probabilistic sector that lies **outside** the positive-semidefinite
  (PSD) Hilbert Gram cone. This is a closed mathematical fact, stated with
  confidence.
- **(B) THE PREDICTION — conditional, preregistered, experiment-open.** On a
  single *received* apparatus anchor, that sector predicts a negative
  three-state Gram discriminant `Delta_3 < 0`, where ordinary QM forces
  `Delta_3 >= 0`. This is a **registered bet with a protocol**, not a result.
  Whether nature contains such a sector is untested, and the decisive
  mixed-state / full-nuisance exclusion has **not** been vetted by a
  quantum-optics expert.

Everything numeric below is exact where it can be, and machine-checked from a
clean clone (`verification/negative_gram_holonomy.py`).

## 1. The theorem (A): accessible positivity without a global PSD carrier

The incumbent complex-Hilbert model represents three internal states by
vectors with normalized Gram matrix `G` (unit diagonal, off-diagonal
`r_{ij} e^{i φ_{ij}}`). A global Hilbert realization requires `G ⪰ 0`, hence
`det G ≥ 0`. For three states,

```
det G = 1 − r12² − r23² − r31² + 2 r12 r23 r31 cos Φ,   Φ = φ12 + φ23 + φ31,
```

with `Φ` gauge-invariant under local rephasings. The proposed sector keeps the
pairwise overlaps but does **not** require the local charts to arise as
restrictions of one positive global carrier; it can reach `det G < 0`.

The immediate danger is that the underlying distinguishability functional `J`
on `S_3` has a **negative sign-sector eigenvalue** (`λ_sign = 1 − 3r² − 2r³`,
negative for `r > 1/2`). If arbitrary six-vectors in the permutation-amplitude
space were physically accessible, some would give negative probabilities. They
are not: passive three-particle linear optics produces only the **monomials**
of one complex `3×3` interferometer matrix `A`,

```
z_σ = ∏_i A_{i, σ(i)},   σ ∈ S_3,
```

which obey the **toric identity** `∏_{σ even} z_σ = ∏_{σ odd} z_σ` (both equal
the product of all nine entries; `verification`, Section B). The real question
is block positivity on this toric variety, and it holds — **universally, using
only the toric relation:**

> **Universal accessible positivity theorem.** For every complex `3×3` matrix
> `A`, at the registered point `r = 3/5`,
> ```
> 152 ‖z‖² + 9 |per A|² − 36 |det A|² ≥ 0,
> ```
> with equality only at `A = 0`.

Since `Σ z_σ = per A` and `Σ sgn(σ) z_σ = det A`, this says **every admitted raw
probability is nonnegative for every interferometer**. The proof needs *no
unitarity*: writing `x = (z_σ)_{σ even}`, `y = (z_σ)_{σ odd}`, the toric
constraint is `x₀x₁x₂ = y₀y₁y₂`; a `C₃`-Fourier change of coordinates turns the
form into `Q = 152N − 243M + 810 Re(αδ̄)` (with `α = (Σx)/3`, `δ = (Σy)/3` the
sector means and `M = |α|² + |δ|²`), and a cubic-deviation bound closes `Q ≥ 0`
on the toric variety. The shipped script verifies the foundational
identity and positivity **exactly** on rational toric witnesses, and an
independent adversarial descent over the full toric set finds no violation
(`verification`, Section C). This is the campaign's principal mathematical
novelty:

> **Global Hilbert PSD fails, while operational block positivity survives.**

**Two consequences fix the scope precisely.** First, because the form is
degree-6 homogeneous, `Q(cA) = |c|⁶ Q(A)`, so positivity on *all* matrices is
equivalent to positivity on all *contractions* — i.e. on **every passive
linear-optical transfer matrix, lossless or lossy** (a lossy multiport is a
submatrix of a larger unitary, hence a contraction). The model is internally
consistent for *any* such apparatus; there is no lossless-only restriction.
Second, on the lossless unitary core `U(3)` a **sharper** strict margin holds,
`152 ‖z‖² + 9 |per A|² − 36 |det A|² ≥ (7/2) ‖z‖²`, saturated exactly by the
Fourier tritter (`verification`, Section D). The stronger `(7/2)`-margin is
**false for arbitrary matrices** — the explicit witness
`A = [[−4,−1,1],[−7,1,−3],[6,−3,−5]]` gives `−495` — and that boundary stays on
the record (`verification`, Section C4); it is exactly why the *universal*
theorem is the zero-margin one. The theorem is careful about its reach: it
proves consistency for the declared passive-linear-optical grammar, not for
arbitrary hypothetical measurements outside it.

## 2. The prediction (B): a preregistered, experiment-open bet

On the *received* fiber `(r, χ(H_γ), receiver) = (3/5, −1, Fourier tritter)`,
every registered observable is a fixed rational (`verification`, Sections
A–B). The odd `Z_2` identity-holonomy class (`Φ = π`) gives

```
Delta_3 = 1 − 3r² − 2r³ = (1 − 2r)(1 + r)²  <  0   for r > 1/2,
Delta_3(3/5) = −64/125.
```

`r = 3/5` is not a fundamental constant — it is an **apparatus anchor**, chosen
only because `r > 1/2` places the odd sector outside the PSD cone. At `r = 3/5`
the incumbent positive-Hilbert cone forces `cos Φ ≥ 5/27`, i.e. `Φ ≤ ~79.3°`,
while the extension reaches `Φ = π`. That gap is the divergence: dimensionless,
gauge-invariant, and count-reconstructible.

**The registered joint decision vector.** A single negative determinant is not
accepted as sufficient — a structureless null defeated the earlier capstone.
The experiment must report the joint vector `(Delta_3, W, Q_3)` in gauge-free
raw counts, where (with tritter probabilities `P111 = 7/1125`,
`P300 = 206/3375`, `P210 = 152/1125`, exactly normalized, and pairwise
statistic `D_2 = 41/75`):

```
W  = P111 + D2 − 2/3 = (2/9) Delta_3 = −128/1125,
Q3 = P111 − D2 + 4/9 = (4/9) b       = −12/125.
```

The **matched pairwise-only null** (which keeps the pairwise overlaps but
deletes the cyclic class) predicts `Q3 = 0`. So the confirmatory criterion is
two-fold: the confidence region must **(1)** lie outside the entire PSD Gram
class *and* **(2)** reject `Q3 = 0` in the registered negative direction. This
is what makes the bet falsifiable rather than fitted.

**Protocol (frozen).** Three independently heralded high-purity single photons;
randomly interleaved settings `PAIR12 / PAIR23 / PAIR31 / TRITTER / flat-loop
control / cyclic-erased control`; late randomization after heralding;
number-resolving or calibrated detection; pairwise overlaps tuned to `r = 3/5`
within a pre-frozen tolerance; the cyclic target `Φ = π`. Analysis is a
blinded PSD-constrained profile-likelihood fit over the full nuisance family,
unblinded only after pipeline freeze, with an independent confirmatory block.

**Protocol amendment (append-only, 2026-08; see correction C-25).** The frozen
protocol above stands unchanged as the record of what was preregistered. The
**normative** analysis form is now Chapter 12's tritter-counts-alone reduction,
which the pair settings do not improve on and which removes an apparatus
exposure they carry:

```
W′ = (4/3) P111 − (2/3) q300,
Δ₃ = (9/2) W′,
Q₃ = q300 + W′/2 − 2/9.
```

Every registered quantity is thereby read from the TRITTER setting alone. The
**PAIR settings are retained** — but only as a cross-setting homogeneity
cross-check. Their residual

```
D2_meas − [ 2/3 − (T₊ − T₋)/3 ],   T₊ = (3/2) q300,  T₋ = (3/4) W′,
```

must be reported and must be consistent with zero; the settings are
over-determined by exactly one degree of freedom, and that residual *is* the
homogeneity test. **Cross-setting inhomogeneity — the tritter configuration
physically differing from the pair configuration in a way correlated with the
cyclic phase — is hereby added by name to the preregistered nuisance family.**
This amendment withdraws no theorem: FCT-62 and FCT-63 are untouched, and the
exclusion result is unchanged. It is reopened only if a two-setting form is
shown to carry information the tritter counts do not, or a bound on
`|S_tri − S_pair|` is derived from calibration.

**Kill conditions (any one kills the physical claim).** An admissible PSD Gram
fit exists; `Q3 = 0` is not rejected; late-randomization or drift correction
removes the effect; the sign depends on post-hoc binning; nuisance
restrictions are tightened after unblinding; a standard positive-Hilbert model
outside the preregistered nuisance family reproduces the result; or independent
replication fails.

## 3. Bridge premises — named, and held open

The theorem (A) needs no physics. The prediction (B) rests on **bridge
premises that are not floor theorems** and are stated as such:

1. a physical particle class may carry `Z_2` identity holonomy;
2. photons may be an appropriate receiver of that sector;
3. passive linear optics may be the complete relevant measurement grammar.

These are *strongly motivated but unproven* about nature. The floor **permits**
the odd-holonomy sector; it does not **force** photons — or any known particle
class — to instantiate it. That in-class membership is exactly what the
proposed experiment tests.

## 4. ⚠ The open crux, the natural home, and the status of this record

**The open crux (make no mistake about this).** The decisive step is a
**mixed-state, mode-mismatch, multiphoton PSD-exclusion**: one must show that
*no* positive-Hilbert model — including mixed internal states, spectral /
temporal / polarization distinguishability, multiphoton contamination, loss,
and tritter imperfection — can *fit the data*. This is a **different** claim
from the theorem of §1, and only the theorem is closed. §1 proves the
extension model's *own internal consistency* — every accessible probability is
nonnegative for **every** passive-linear-optical apparatus, lossless or lossy.
It does **not** show that a positive-Hilbert model cannot reproduce the
measured counts; that exclusion is exactly what remains open. **The apparatus-nuisance layer is
settled by exact computation on two independent engines plus refutation-first
adversarial review across model families; the one thing no review can supply is
MEASUREMENT, so the gate before any nature-facing claim is the experiment
itself, and outreach to an experimental group is a step toward that
measurement, not a validity gate.**

**The natural home is not photons.** The clean physical home for path-relative
exchange with nontrivial identity holonomy is **anyonic / topological matter**,
not photons. Photons are the *clean-grammar long shot* — attractive because
passive linear optics is exactly the grammar the theorem controls, but a long
shot because ordinary photons are prepared inside Hilbert-state models and
therefore have PSD Gram matrices by construction (so the bridge premise likely
fails for them). The bet is placed on structure, not on optimism.

**What this DOI is.** This chapter is an **archival / priority record** of a
mathematically closed conditional prediction. It is deliberately *not* an
empirical discovery, and nothing here should be read as one. No suitable public
trial-level dataset currently closes the experiment; the only decisive
remaining step is the preregistered, late-randomized, interleaved photon (or
topological-matter) measurement, gated by expert review.

## 5. What is proven, what is not

**Proven exactly** (`verification/negative_gram_holonomy.py`, 11/11):
`Delta_3 = (1−2r)(1+r)²`, negative for `r > 1/2`, `= −64/125` at `r = 3/5`; the
full tritter/pairwise count vector and its exact normalization; the count
witnesses `W = (2/9)Delta_3`, `Q3 = (4/9)b`; the pairwise-only null `Q3 = 0`;
the PSD cap `cos Φ ≥ 5/27` (`Φ ≤ ~79.3°`) that the extension exceeds; the toric
identity; the **universal** accessible-positivity theorem
`152‖z‖² + 9|per A|² − 36|det A|² ≥ 0` for every complex `3×3` matrix (the
foundational Fourier identity and positivity on exact rational toric witnesses,
plus an independent adversarial descent over the full toric set); the sharper
`U(3)` strict `7/2`-margin corollary saturated by the Fourier tritter; the
`−495` witness that kills the `(7/2)`-margin for arbitrary matrices; and exact
separable-loss covariance.

**Not claimed:** that `r = 3/5` is fundamental; that all quantum systems
violate global Hilbert positivity; that standard QM is numerically wrong in
already-tested flat sectors; that the floor uniquely predicts photons; that no
larger positive completion exists under an enlarged measurement grammar; that
existing three-photon data demonstrate the effect; or that mathematical
consistency constitutes empirical discovery.

**Final status.** *The campaign has produced a complete, internally
consistent, dimensionless extension prediction, but not yet an empirical
discovery.*

The claim-register rows this chapter rests on are frozen in
[`claims.md`](claims.md); the freeze record is in [`RELEASE.md`](RELEASE.md).
