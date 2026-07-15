# Release Notes — v0.11.0

**Finite Contact Theory v0.11: The Clean Mixed-State Exclusion.**

Eleventh public release. It closes the *clean core* of the open crux that
Chapter 10 left for an external expert — and it is a **proof**, not a bet. No
partially-distinguishable Hilbert model, pure or mixed, can reproduce the
registered negative-Gram counts.

## The new live release ceiling

This supersedes the v0.10 ceiling as the live ceiling; the v0.1, v0.2, v0.7,
v0.8, v0.9, and v0.10 ceilings remain quoted, unchanged, in their frozen
chapters and release notes. Quoted identically in the README, the claim
register, the chapter-11 paper, and here:

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

## What is new

- **Chapter 11**:
  [papers/11-mixed-state-exclusion/](papers/11-mixed-state-exclusion/paper.md)
  — the clean mixed-state exclusion (FCT-62 / T-46, `THEOREM / UNCONDITIONAL /
  EXTENSION-MATH`). The gauge-free raw-count witness `W = P111 + D2 - 2/3`
  equals `(2/9) det G` for every partial-distinguishability model at the Fourier
  tritter (with `P111 = (2 - S + 4τ)/9` and `D2 = 2/3 - S/9` the standard
  formulas — `P111` derived from first principles in the verifier — and
  `det G = 1 - S + 2τ`). Gram positivity forces `det G ≥ 0`, so `W ≥ 0` for
  every pure config, and — since `W` is affine in the counts — for every
  **mixed** state by convexity, certified operator-level by the antisymmetrizer
  projector `A₋` via `W = (4/3) Tr(A₋ Ω) ≥ 0`. The registered extension has
  `W = (2/9)Δ₃ = -128/1125 < 0`, so it lies **outside** the entire class; the
  exact separating raw-count test is `P111 + D2 ≥ 2/3`.
- **New shipped verification** (frozen under the chapter, dependency-free):
  `verification/scripts/mixed_state_exclusion.py` — the first-principles count
  formula (exact rational witness + numerical sweep), the determinant identity,
  the count-witness identity, the antisymmetrizer certificate with the `Q[S₃]`
  projector property, `W ≥ 0` on exact rational PSD Grams and under an
  adversarial descent, convexity, and the exclusion. Wired into `run_all.py`
  (now sixteen scripts).
- **FCT-61's residual updated**: the clean mixed-state PSD-exclusion is now
  closed (proven); the remaining open part of the crux is the
  apparatus-nuisance layer.
- **README, claim register, theorem bank, and audit** updated to the v0.11
  state (eleven chapters; the migrated live ceiling; new required files).

## Scope and honesty

This closes the **clean** mixed-state + mode-mismatch exclusion: no
partially-distinguishable Hilbert model at the Fourier tritter reproduces the
registered counts. It does **not** close multiphoton contamination, detector
response and loss imbalance, transfer-matrix (tritter) uncertainty, or source
drift — those apparatus nuisances remain part of the full experimental analysis
and the external quantum-optics expert's gate. The Chapter-10 **bridge
premises** (that a physical particle class carries `Z₂` identity holonomy; that
a receiver instantiates it — the natural home is anyonic / topological matter,
photons the clean-grammar long shot) are unchanged and still held open. So the
crux moves from "open" to **clean-core closed (proven), apparatus-nuisance layer
open** — a real strengthening of the Chapter-10 divergence, and still not an
empirical discovery.

## Verify

```powershell
python verification\scriptsun_all.py    # expects: ALL SHIPPED VERIFICATION: PASS
python scriptselease_audit.py            # expects: PUBLIC RELEASE AUDIT: PASS
```

## Citation

Cite the program by its concept DOI
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591); the
v0.11.0 version DOI is recorded in
[papers/11-mixed-state-exclusion/RELEASE.md](papers/11-mixed-state-exclusion/RELEASE.md)
and [CITATION.cff](CITATION.cff) at mint.
