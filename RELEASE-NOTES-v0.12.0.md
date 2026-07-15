# Release Notes — v0.12.0

**Finite Contact Theory v0.12: The Exact Quantum Count Regions and the Limits of Counting.**

Twelfth public release. Standalone quantum-information mathematics — no theory
buy-in — that also upgrades Chapters 10–11: the negative-Gram inequality is
shown to be *the* complete boundary of quantum three-photon tritter statistics.

## The new live release ceiling

This supersedes the v0.11 ceiling as the live ceiling; the v0.1, v0.2, v0.7,
v0.8, v0.9, v0.10, and v0.11 ceilings remain quoted, unchanged, in their frozen
chapters and release notes. Quoted identically in the README, the claim
register, the chapter-12 paper, and here:

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

## What is new

- **Chapter 12**:
  [papers/12-count-regions/](papers/12-count-regions/paper.md)
  — the exact quantum count regions (FCT-63..67 / T-47..50). For `n`
  indistinguishable bosons in the `n`-mode Fourier interferometer:
  - **n = 3 (FCT-63):** the exact region is a tetrahedron whose only non-raw
    facet is the negative-Gram sign inequality; `P111 + D2 - 2/3 = (4/3)(C - B/2)
    = (2/9) det G`, so Chapter 11's `P111 + D2 >= 2/3` is THE complete boundary
    and the FCT-61 protocol simplifies to tritter counts.
  - **n = 4 (FCT-64):** a 9-simplex; central-projector positivity is
    **insufficient** (an exact counterexample with all five central weights `>= 0`
    yet `alpha_211A = x9 - x2 = -1/20 < 0`); six new raw-count inequalities.
  - **n = 5 (FCT-65):** an **emergent logical qubit** from permutation symmetry
    and counting alone; the **rebit-blindness** theorem (single-shot cyclic
    counts cannot expose `sigma_y`; multiplication recovers it,
    `[F00131,F00212]|M2 = -(2i/25) sigma_y`); the exact body `K_5` (affine
    dimension 25, disk cross-section, hidden-center identity).
  - **the ℝ/ℂ/ℍ no-go (FCT-66):** `K_R = K_C = K_H` exactly — single-source
    Fourier counting cannot discriminate real, complex, and quaternionic QM.
  - **sequential closure + the witness (FCT-67):** general passive networks span
    all of `C[S_5]`; one network exposes `sigma_y` (`G1` with trace `21/512`,
    rank 1, `|y| = 5 sqrt2/512`); a **registered, experiment-open**
    conjugation-witness (gap `5 sqrt2/256`, ~1304 trials/setting) excludes a
    named real-internal-states + mode-only-optics model class.
- **New shipped verification** (frozen under the chapter, dependency-free):
  `verification/scripts/count_regions.py` — the n=3 bosonic occupation
  cross-check from first principles (exact on a rational witness), the n=4
  counterexample and six inequalities, the n=5 rebit-blindness commutator, the
  `K_5` identities, the ℝ/ℂ/ℍ no-go, and the `G1` / conjugation-gap facts. Wired
  into `run_all.py` (now seventeen scripts).
- **FCT-61/FCT-62 cross-referenced**: the negative-Gram inequality is the
  complete `n = 3` boundary and the registered protocol reduces to tritter counts.
- **README, claim register, theorem bank, and audit** updated to the v0.12 state
  (twelve chapters; the migrated live ceiling; new required files).

## Scope and honesty

The region theorems (n=3/4/5, the ℝ/ℂ/ℍ no-go, the sequential closure) are
proof-backed and independently reproduced. The **conjugation-witness** is a
**registered, experiment-open** protocol: it excludes the **real-internal-states
+ mode-only-passive-optics** model class, and it does **not** falsify every real
reformulation of quantum mechanics — the McKague–Mosca–Gisin realification
restores simulation if optical transformations may act on a universal rebit,
which is not implementable in the fixed grammar (mode unitaries generate only
the permutation actions `P_pi`, never `J . P_pi`). It is **not a performed
experiment and not a claim about nature**.

## Verify

```powershell
python verification/scripts/run_all.py    # expects: ALL SHIPPED VERIFICATION: PASS
python scripts/release_audit.py           # expects: PUBLIC RELEASE AUDIT: PASS
```

## Citation

Cite the program by its concept DOI
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591); the
v0.12.0 version DOI is recorded in
[papers/12-count-regions/RELEASE.md](papers/12-count-regions/RELEASE.md)
and [CITATION.cff](CITATION.cff) at mint.
