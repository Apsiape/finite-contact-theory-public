# Chapter 11 — The Clean Mixed-State Exclusion

**Release:** v0.11.0 · **Status of the chapter:** one unconditional theorem
that closes the *clean core* of the open crux Chapter 10 left for an external
expert. It is not a discovery; it is a proof that the Chapter-10 divergence
cannot be faked by clean-grammar quantum mechanics.

---

## The live release ceiling

This chapter carries the program's live ceiling, quoted identically in the
README, the claim register, and the v0.11.0 release notes:

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
> received apparatus anchor this predicts a possible violation of Hilbert-space
> positivity — a negative three-state Gram discriminant Delta_3 < 0 where
> ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its
> protocol, nulls, and kill conditions, and a clean mixed-state exclusion
> theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals
> (2/9) det G, nonnegative for every partially-distinguishable Hilbert model
> whether pure or mixed, so the registered negative-Gram vector lies outside
> the entire clean partial-distinguishability class by the raw-count test
> P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton,
> detector, transfer-matrix, and source-drift nuisances remain the experimental
> layer for an external expert — under which the quantum boundary is a floor
> theorem at binary-Bell finite-carrier scope, the preparation gap is an exact
> theorem at KCBS-pentagon scope, the interface reconstruction is a finite
> model-scope recovery on a real-quantum cell, the multi-floor closures are
> model-scope recoveries whose forcing boundary is exactly mapped, the
> accessible-positivity and mixed-state exclusion theorems are unconditional
> while the physical realization is a conditional, bridge-premise-gated
> prediction awaiting a dedicated experiment and external expert review, and
> every unearned generalization — complex quantum mechanics, the actuality of
> one outcome, the universal Born rule, whether nature realizes any of these
> structures, which world-phase is selected, whether nature contains the odd
> identity-holonomy sector, and whether the apparatus nuisances close the full
> exclusion — is left open by name; this chapter is an archival priority record
> of mathematically closed theorems and a conditional prediction, not an
> empirical discovery.

---

## 0. What this chapter closes

Chapter 10 registered a divergence — a three-particle sector with a negative
Gram discriminant `Δ₃ = −64/125`, where ordinary quantum mechanics forces
`Δ₃ ≥ 0` — and named its decisive open crux honestly: *could a mixed / mode-
mismatched source reproduce the registered counts with ordinary quantum
mechanics, so that a measured `Δ₃ < 0` had a mundane explanation?* This chapter
answers the **clean core** of that question, and the answer is no — provably,
for the entire partially-distinguishable Hilbert class, pure and mixed.

The result is a single identity. Define the gauge-free raw-count witness
`W = P111 + D2 − 2/3` (affine in the measured occupation probabilities: the
balanced-tritter coincidence `P111` and the pooled symmetric pairwise
distinct-output statistic `D2`). Then **for every partial-distinguishability
model at the Fourier tritter,**

> `W = (2/9) det G`,

where `G` is the `3×3` internal-state Gram matrix — and `det G ≥ 0` is forced
by Gram positivity. So `W ≥ 0` for every Hilbert model, while the extension
predicts `W = (2/9)Δ₃ = −128/1125 < 0`. The registered vector lies **outside**
the whole class, and the exclusion is one raw-count inequality:

> **`P111 + D2 ≥ 2/3`** (the extension gives `622/1125 < 750/1125`).

This is not a discovery. It is the theorem that upgrades the Chapter-10
divergence from "a mixed-state source might fake it" to "no clean-grammar
Hilbert model of any purity can."

## 1. The count witness equals the Gram determinant

Represent each particle's internal (spectral / temporal / polarization) state
by a vector `|φ_i⟩`; the pairwise overlaps are `g_ij = ⟨φ_i|φ_j⟩` and the Gram
matrix `G` has unit diagonal. Writing `S = Σ|g_ij|²` (the three pairwise
squared overlaps) and `τ = Re(g₁₂ g₂₃ g₃₁)` (the genuine three-particle cyclic
term), the standard partial-distinguishability formulas for the balanced
Fourier tritter are

```
P111 = (2 − S + 4τ)/9,    D2 = 2/3 − S/9.
```

The coincidence probability `P111` is **derived from first principles** in the
shipped verifier (creation operators through the tritter with the internal
degrees of freedom traced, not asserted); `D2 = 2/3 − S/9` is the standard
pooled pairwise (HOM-type) distinct-output statistic, taken as given.

(These reproduce the Chapter-10 registered values exactly: at `S = 27/25`,
`τ = −27/125` they give `P111 = 7/1125`, `D2 = 41/75`.) Therefore

```
W = P111 + D2 − 2/3 = (2/9)(1 − S + 2τ).
```

But `1 − S + 2τ` is exactly the determinant of the three-state Gram matrix,

```
det G = 1 − |g₁₂|² − |g₂₃|² − |g₃₁|² + 2 Re(g₁₂ g₂₃ g₃₁) = 1 − S + 2τ.
```

Hence the identity

> **`W = (2/9) det G`.**

Since any Hilbert-space Gram is positive semidefinite, `det G ≥ 0`, so
`W ≥ 0` for every pure configuration. (The verifier checks all of this exactly:
the first-principles count formula on a rational witness, the determinant
identity, and the algebra.)

## 2. Mixed states, and an operator certificate

A mixed internal source is any convex combination of pure configurations,
`Ω = Σ_λ p_λ Ω_λ`. Because the counts are *linear* in the input density
operator, `W` — being affine in the counts — is the convex combination
`W(Ω) = Σ_λ p_λ W(Ω_λ) = (2/9) Σ_λ p_λ det G_λ ≥ 0`. Convexification cannot
cross `W = 0`.

There is also a direct operator certificate. Let `A₋ = (1/6) Σ_{π∈S₃}
sgn(π) P_π` be the three-particle antisymmetrizer. It is a **positive
projector** (`A₋† = A₋`, `A₋² = A₋`, verified in `Q[S₃]`), and by the Leibniz
determinant formula

```
⟨φ₁φ₂φ₃| A₋ |φ₁φ₂φ₃⟩ = (1/6) Σ_π sgn(π) ∏_i ⟨φ_i|φ_{π(i)}⟩ = (det G)/6.
```

Therefore

> **`W = (4/3) Tr(A₋ Ω) ≥ 0`**,

the separating count functional realized as the operational image of a
positive-semidefinite projector — an exact certificate with no numerical
tolerance. `⟨A₋⟩ = ‖A₋(φ₁⊗φ₂⊗φ₃)‖² ≥ 0` is precisely why `det G ≥ 0`.

## 3. The exclusion and the raw-count test

The registered extension point has `W = (2/9)Δ₃ = (2/9)(−64/125) = −128/1125 <
0`. No partial-distinguishability Hilbert model — pure, mixed, or any convex
mode-mismatch mixture consistent with the measured pairwise overlaps — can
produce it. The exact separating hyperplane is the raw-count inequality

```
P111 + D2 ≥ 2/3,
```

which the extension violates by `128/1125`. An experiment therefore has a
single, model-independent exclusion test on raw counts: a measured
`P111 + D2 < 2/3` is outside the entire clean partial-distinguishability class.

## 4. ⚠ Scope — what is closed, and what is not

**Closed (proven here):** the *clean* mixed-state and mode-mismatch
PSD-exclusion. Every partially-distinguishable Hilbert model at the Fourier
tritter — including arbitrary mixed internal states and mode mismatch — has
`W ≥ 0`, so none reproduces the registered negative-Gram vector.

**Still open (the external experimental layer):** this does **not** close
multiphoton contamination, detector response and loss imbalance, transfer-
matrix (tritter) uncertainty, or source drift. Those apparatus nuisances remain
part of the full experimental analysis and the external quantum-optics expert's
gate before any nature-facing claim. The **bridge premises** of Chapter 10 (that
a physical particle class carries `Z₂` identity holonomy; that a receiver
instantiates it — the natural home is anyonic / topological matter, photons the
clean-grammar long shot) are unchanged and still held open.

So the crux moves from "open" to **clean-core closed (proven), apparatus-nuisance
layer open** — a real strengthening of the Chapter-10 divergence, and still not
an empirical discovery.

## 5. What is proven, what is not

**Proven exactly / from first principles**
(`verification/mixed_state_exclusion.py`, 7/7): the partial-distinguishability
`P111` formula derived from first principles (exact rational witness plus a
numerical sweep); `det G = 1 − S + 2τ`; the count-witness identity
`W = (2/9) det G`; the antisymmetrizer certificate `⟨A₋⟩ = det G/6` with the
projector property in `Q[S₃]`; `W ≥ 0` on exact rational PSD Grams and under an
adversarial descent; convexity for mixtures; and the registered point's
exclusion with the raw-count test.

**Not claimed:** that the *full* nuisance-robust exclusion is closed (it is
not — see §4); that any experiment has been performed; that nature realizes the
odd-holonomy sector; or that this is an empirical discovery. It is an
unconditional theorem that closes the clean core of the crux.

The claim-register rows this chapter rests on are frozen in
[`claims.md`](claims.md); the freeze record is in [`RELEASE.md`](RELEASE.md).
