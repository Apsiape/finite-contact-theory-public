# Release Notes — v0.10.0

**Finite Contact Theory v0.10: Negative-Gram Identity Holonomy — The Program's First Divergence.**

Tenth public release, and a different *kind* of release. Chapters 1–9 all
**recovered** known structure from the finite-contact floor. This chapter is
the program's **first extension**: it predicts a possible *violation* of
Hilbert-space positivity. It recovers nothing, and it is **not** a claimed
discovery. Two things are published, held rigidly apart — an unconditional
theorem, and a conditional, preregistered, experiment-open prediction.

## The new live release ceiling

This supersedes the v0.9 ceiling as the live ceiling; the v0.1, v0.2, v0.7,
v0.8, and v0.9 ceilings remain quoted, unchanged, in their frozen chapters and
release notes. Quoted identically in the README, the claim register, the
chapter-10 paper, and here:

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
> protocol, nulls, and kill conditions — under which the quantum boundary is a
> floor theorem at binary-Bell finite-carrier scope, the preparation gap is an
> exact theorem at KCBS-pentagon scope, the interface reconstruction is a
> finite model-scope recovery on a real-quantum cell, the multi-floor closures
> are model-scope recoveries whose forcing boundary is exactly mapped, the
> accessible-positivity theorem is unconditional while its physical realization
> is a conditional, bridge-premise-gated prediction awaiting a dedicated
> experiment and external expert review, and every unearned generalization —
> complex quantum mechanics, the actuality of one outcome, the universal Born
> rule, whether nature realizes any of these structures, which world-phase is
> selected, and whether nature contains the odd identity-holonomy sector — is
> left open by name; this chapter is an archival priority record of a
> mathematically closed conditional prediction, not an empirical discovery.

## What is new

- **Chapter 10**:
  [papers/10-negative-gram-holonomy/](papers/10-negative-gram-holonomy/paper.md)
  — negative-Gram identity holonomy, the program's first divergence.
  - **The theorem (A), unconditional** — FCT-60 / T-44, `THEOREM /
    UNCONDITIONAL / EXTENSION-MATH`. A three-contact class function with a
    negative sign-sector eigenvalue (`1 − 3r² − 2r³ < 0` for `r > 1/2`)
    nonetheless keeps every passive-linear-optical probability nonnegative: the
    accessible amplitudes are the monomials `z_σ = ∏_i A[i][σ(i)]` of one
    complex `3×3` interferometer matrix, they obey the toric identity
    `∏_even z = ∏_odd z`, and at `r = 3/5` the exact inequality
    `152‖z‖² + 9|per A|² − 36|det A|² ≥ (7/2)‖z‖² ≥ 0` holds for every `A`. So
    the sector is a lawful probabilistic model that lies **outside** the
    positive-semidefinite Hilbert Gram cone — global Hilbert PSD fails while
    operational block positivity survives.
  - **The prediction (B), conditional and experiment-open** — FCT-61 / T-45,
    `CONDITIONAL EXTENSION / EXPERIMENT-OPEN / BRIDGE-PREMISE-GATED`. On the
    received anchor `r = 3/5` and the odd `Z₂` identity-holonomy sector
    (`Φ = π`), `Δ₃ = (1−2r)(1+r)² = −64/125 < 0`, where ordinary QM forces
    `Δ₃ ≥ 0` (the PSD cone caps `Φ ≤ arccos(5/27) ≈ 79.3°` at `r = 3/5`). The
    registered joint count vector `(Δ₃, W, Q₃) = (−64/125, −128/1125, −12/125)`
    both excludes the PSD Gram class and rejects the matched pairwise-only null
    (`Q₃ = 0`). A preregistered bet with a frozen protocol and kill conditions,
    **not** a discovery.
- **New shipped verification** (frozen under the chapter, dependency-free):
  `verification/scripts/negative_gram_holonomy.py` — the core numbers and the
  analytic proof-lemmas exact, the toric identity, and the
  accessible-positivity margin verified exactly over small-rational and
  Gaussian-rational matrices plus a large well-conditioned float sweep. Wired
  into `run_all.py` (now fifteen scripts).
- **README, claim register, theorem bank, and audit** updated to the v0.10
  state (ten chapters; the migrated live ceiling; new required files;
  divergence-tuned overclaim bans forbidding any settled-discovery phrasing).

## Scope and honesty

The recovery/divergence fence is the load-bearing discipline of this chapter,
and it is stated up front. The **theorem (A)** needs no physics and is closed.
The **prediction (B)** rests on bridge premises that are **not** floor
theorems and are named as such: that a physical particle class carries `Z₂`
identity holonomy; that photons receive it (the natural home is
**anyonic/topological matter** — path-relative exchange — with photons the
*clean-grammar long shot*); and that passive linear optics is the complete
measurement grammar. The decisive **mixed-state, mode-mismatch, multiphoton
PSD-exclusion** is the **open crux** and has **not** been vetted by a
quantum-optics expert; external expert review is the gate before any outreach.
`r = 3/5` is a received apparatus anchor, not a fundamental constant. No
suitable public trial-level dataset currently closes the experiment.

*The campaign has produced a complete, internally consistent, dimensionless
extension prediction, but not yet an empirical discovery.* This DOI is an
archival / priority record, not a discovery claim.

## Verify

```powershell
python verification\scripts\run_all.py    # expects: ALL SHIPPED VERIFICATION: PASS
python scripts\release_audit.py           # expects: PUBLIC RELEASE AUDIT: PASS
```

## Citation

Cite the program by its concept DOI
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591); the
v0.10.0 version DOI is recorded in
[papers/10-negative-gram-holonomy/RELEASE.md](papers/10-negative-gram-holonomy/RELEASE.md)
and [CITATION.cff](CITATION.cff) at mint.
