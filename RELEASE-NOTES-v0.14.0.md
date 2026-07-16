# Release Notes — v0.14.0

**Chapter 13 — From the Floor to the Interface: What Forces the Quaternions.**

This release closes, one honest layer down, the deepest corpus dependency the
repository had: Chapter 8's starting datum (the "three retained quarter-turns,"
disclosed as a private-corpus citation at v0.13, FCT-45). Chapter 13 ships that
link as an exact finite forcing chain from three named hypotheses — a ternary
contact (S), future-readable order scars (R), internally-carried retention
(SH) — to the quaternionic interface: exactly three anticommuting involutive
identity modes (a two-sided pincer), the central `i` as their oriented volume
element, the quaternions as their even sector, exact `1/2` reflection weights,
the double cover selected by retention, and the minimal receiver `ℍ` with the
`1+3` split and unique Euclidean form. The residual is named, not hidden: (R)
is the program's standing received fork (proven not-forced), (S) is measured,
(SH) is a named axiom, and one orientation bit is a received `C₂` torsor.
GIVEN these, the interface is forced — the placement of the forced/received
boundary is the result.

## The live release ceiling

Quoted identically in the README, the claim register, and the chapter-13
paper:

> Finite Contact Theory is a finite reconstruction program with a scoped theorem stack on three published recovery lines — a quantum-facing axis, from one-use contact to counting, one-receiver gluing, rational Born weights, the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and a behavior-conditioned contextual capacity with an exact strict preparation gap; a finite-epistemics axis, from the identifiability and debt calculus to the inquiry calculus and its second law of asking, four theorems separating the structure of time, and a measured generative floor; and a contact-interface reconstruction, in which a retained interface forces a quaternionic state/receiver cell whose self-dual closure is the 24-cell and the F_4 root system and whose finite measurement calculus forces the quadratic Born frame rule (a finite Gleason theorem) exactly where a triality Kochen-Specker obstruction forbids a global noncontextual assignment, and in which independently generated cells recover the E_8–hexacode closure spine under named receiver laws that a forcing audit shows the floor does not select over matched lawful alternatives, so the floor forces the atlas of lawful closures and the terminal self-dual class but never the specific member, and the selection of a world-phase is a conserved, received input, and in which a floor-to-interface theorem now closes the chain one layer down: given a ternary contact whose order scars stay future-readable and whose retention is carried internally, exactly three mutually anticommuting involutive identity modes are forced — their oriented volume element is a central square root of minus one, their even sector is the quaternions, their reflection symmetry forces exact one-half weights, and the retained central residue forces the minimal faithful receiver to be the quaternions with the 1+3 split and the unique Euclidean form — while the residual inputs are named as received: the readability of order, the measured ternary arity, the internal-retention axiom, and one orientation bit — a fourth, first-extension line that is conditional and experiment-open: an unconditional accessible-positivity theorem exhibits a three-contact sector whose every passive-linear-optical probability is nonnegative yet which lies outside the positive-semidefinite Hilbert Gram cone, and on one received apparatus anchor this predicts a possible violation of Hilbert-space positivity — a negative three-state Gram discriminant Delta_3 < 0 where ordinary quantum mechanics forces Delta_3 >= 0 — preregistered with its protocol, nulls, and kill conditions, and a clean mixed-state exclusion theorem then proves the gauge-free count witness W = P111 + D2 - 2/3 equals (2/9) det G, nonnegative for every partially-distinguishable Hilbert model whether pure or mixed, so the registered negative-Gram vector lies outside the entire clean partial-distinguishability class by the raw-count test P111 + D2 >= 2/3, closing the clean core of the exclusion while multiphoton, detector, transfer-matrix, and source-drift nuisances remain the experimental layer for an external expert — and a fifth line mapping the exact quantum count regions: for n indistinguishable bosons in the n-mode Fourier interferometer the achievable region of count statistics is an exact simplex for n <= 4 (at n = 3 the negative-Gram inequality P111 + D2 >= 2/3 is the complete boundary and the registered protocol reduces to tritter counts alone), central-projector positivity is insufficient at n = 4 with six new raw-count laws, and a structural phase transition at n = 5 produces an emergent logical qubit from permutation symmetry and counting alone, where a rebit-blindness theorem shows single-shot cyclic counts cannot expose sigma_y and a single-source real/complex/quaternionic counting no-go holds, both overcome by general passive networks, culminating in a registered, experiment-open single-source conjugation-witness protocol (gap 5 sqrt2 / 256, about 1304 trials per setting) that excludes a named real-internal-states plus mode-only-optics model class but does not falsify all real quantum mechanics — under which the quantum boundary is a floor theorem at binary-Bell finite-carrier scope, the preparation gap is an exact theorem at KCBS-pentagon scope, the interface reconstruction is a finite model-scope recovery on a real-quantum cell, the multi-floor closures are model-scope recoveries whose forcing boundary is exactly mapped, the floor-to-interface chain is an exact finite theorem conditional on its four named received inputs, the accessible-positivity and mixed-state exclusion theorems and the count-region theorems are unconditional and independently reproduced, while the physical realizations — the negative-Gram prediction and the conjugation witness — are conditional, bridge-premise-gated, experiment-open registered protocols awaiting a dedicated experiment and external expert review, and every unearned generalization — complex quantum mechanics, the actuality of one outcome, the universal Born rule, whether nature realizes any of these structures, which world-phase is selected, whether nature contains the odd identity-holonomy sector, whether the apparatus nuisances close the full exclusion, and whether any experiment realizes the conjugation witness — is left open by name; these chapters are an archival priority record of mathematically closed theorems and registered conditional protocols, not empirical discoveries.

## What changed

- `papers/13-floor-to-interface/` — the chapter, its claim snapshot
  (FCT-68..71), freeze record, and frozen verifier copy with expected output.
- Claim rows **FCT-68..71** and theorem rows **T-51..53**.
- `verification/scripts/floor_to_interface.py` wired into `run_all.py`
  (eighteen scripts): twelve exact checks — the reader/anticommutation
  identity; the exact anticommutant and no-third-involution conclusion; the
  integer anticommuting triple; the reverse-oddtown ladder and `n = 3`
  uniqueness; centrality, `Ω² = −I`, the quaternion relations, the projector
  swap and the `1/2`; the mod-4 plateau; both `H²` censuses with both
  extension classes constructed; the dimension kills, the commutant, the
  invariant form; the spinor return.
- The **new live ceiling** (adds the floor-to-interface line); the v0.12
  ceiling is now frozen in its chapter and notes locations.
- One honesty fix from an adversarial review: the Chapter-8 README framing
  "Born and contextuality are two faces of one finite closure" is restated as
  **co-residence** of two independently-proven theorems; no common-generator
  theorem is claimed.

## Release gate (checklist, this release)

- **Scope freeze** — new ceiling stated in one paragraph; identical in
  README, register, chapter, and these notes; everything beyond it held open
  by name. ✔
- **Claim register** — four new rows, each with status, scope, evidence
  class, source, controls, residuals; weakest accurate label (`THEOREM /
  MODEL-SCOPE / RECOVERY`, conditionality named in-row); no ID reused. ✔
- **Theorem bank** — T-51..53 added with their conditions. ✔
- **Corrections** — none required this release. ✔
- **Verification** — `run_all.py` (eighteen scripts) passes on a clean clone;
  the new script's expected output is frozen in the chapter directory. ✔
- **Chapter** — directory convention followed; recovery anchors named
  (Babai–Frankl; Sarkar–van den Berg; Hurwitz–Radon; Lounesto; Conway–Smith;
  Serre; Baez); scope fences and demotion conditions stated in §9. ✔
- **Novelty protocol (§2a)** — the blind sweep was run for the chapter's
  literatures (extremal combinatorics; anticommuting-operator families;
  Clifford algebra; group cohomology / double covers; quaternionic QM and
  reconstruction programs); nearest precedents named in §7, including the
  Moretti–Oppio reduction engaged directly; the composition graded
  INTERNAL-BLIND. ✔
- **Rights** — all new text and code rights-clean; the private corpus is
  named, not copied. ✔
- **Metadata** — CHANGELOG, CITATION.cff, `.zenodo.json`, and these notes. ✔
- **Clean-clone audit** — `scripts/release_audit.py` passes. ✔
- **Tag and deposit** — version DOI recorded in the chapter's RELEASE.md and
  CITATION.cff at mint. ✔

## Scope, in one line

The chain is conditional and says so; what is new is the composed
derivation — to our knowledge (INTERNAL-BLIND) the first that forces the
quaternions from a retention/irreversibility hypothesis rather than
postulating them or deriving complex theory from reversibility — and the
exact, machine-checked placement of the forced/received boundary.
