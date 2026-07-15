# Chapter 10 — Claims Snapshot (as of the v0.10.0 tag)

The exact claim-register rows this chapter rests on. The live view is
[`../../docs/public-claim-register.md`](../../docs/public-claim-register.md).
One dependency-free script verifies both rows from a clean clone, exactly
where possible and by exhaustive/large sampling for the analytic inequality:
`verification/negative_gram_holonomy.py`.

This is the program's **first extension** chapter. FCT-60 is an unconditional
theorem; FCT-61 is a conditional, preregistered, experiment-open prediction —
**not** a settled result and **not** a discovery.

---

## FCT-60 — Universal Accessible Positivity (The Theorem)

Status: `THEOREM / UNCONDITIONAL / EXTENSION-MATH`
Scope: the passive-linear-optical grammar on one complex `3x3` interferometer
submatrix, at the registered point `r = 3/5`.
Evidence: `shipped` (Sections C, D).

A three-contact class function with a negative sign-sector eigenvalue
(`1 − 3r² − 2r³ < 0` for `r > 1/2`) still yields only nonnegative accessible
probabilities, for **every** interferometer. The accessible amplitudes
`z_σ = ∏_i A[i][σ(i)]` obey the toric identity `∏_even z = ∏_odd z`, and for
every complex `3×3` `A`, `152‖z‖² + 9|per A|² − 36|det A|² ≥ 0` (equality only
at `A = 0`) — proven using **only** the toric relation (no unitarity), via a
`C₃`-Fourier reduction `Q = 152N − 243M + 810 Re(αδ̄)` (`α, δ` the sector
means, `M = |α|²+|δ|²`) closed by a cubic-deviation bound. Being degree-6 homogeneous, positivity on all matrices =
positivity on all contractions = **every passive-linear-optical apparatus,
lossless or lossy**. So the sector is a lawful probabilistic model on the
complete grammar that lies **outside** the PSD Hilbert Gram cone: global
Hilbert PSD fails while operational block positivity survives. On the lossless
`U(3)` core the sharper strict `(7/2)‖z‖²` margin holds (Fourier saturates);
the `(7/2)` margin for arbitrary matrices is **false** (`−495` witness) and
stays killed. Unconditional. Fence: the model's *internal* consistency — the
empirical mixed-state PSD-exclusion (whether a Hilbert model fits the data) is
a separate, open question (FCT-61).

## FCT-61 — Negative-Gram Identity Holonomy (The Prediction)

Status: `CONDITIONAL EXTENSION / EXPERIMENT-OPEN / BRIDGE-PREMISE-GATED`
Scope: a preregistered three-particle experiment on the received fiber
`(r, χ, receiver) = (3/5, −1, Fourier tritter)`.
Evidence: `shipped` (the exact prediction numbers, Sections A–B) + `held`
(the experiment).

The program's first divergence. On the odd `Z₂` identity-holonomy sector
(`Φ = π`), `Δ₃ = 1 − 3r² − 2r³ = (1−2r)(1+r)² = −64/125 < 0`, where ordinary
QM forces `Δ₃ = det G ≥ 0` (the PSD cone caps `Φ ≤ arccos(5/27) ≈ 79.3°` at
`r = 3/5`). The registered joint count vector
`(Δ₃, W, Q₃) = (−64/125, −128/1125, −12/125)` both excludes the PSD Gram class
and rejects the matched pairwise-only null (`Q₃ = 0`). A preregistered bet with
a frozen protocol and kill conditions — **not** a discovery. Bridge premises
(a particle class carries `Z₂` identity holonomy; photons receive it; passive
linear optics is the complete grammar) are held open; the natural home is
anyonic/topological matter, photons the clean-grammar long shot. The
mixed-state / full-nuisance PSD-exclusion is the **open crux**, not vetted by a
quantum-optics expert; external review gates any outreach. `r = 3/5` is a
received apparatus anchor, not a fundamental constant. This DOI is an
archival/priority record.
