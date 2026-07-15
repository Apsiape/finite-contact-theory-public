# Chapter 11 — Claims Snapshot (as of the v0.11.0 tag)

The exact claim-register rows this chapter rests on. The live view is
[`../../docs/public-claim-register.md`](../../docs/public-claim-register.md).
One dependency-free script verifies the chapter from a clean clone:
`verification/mixed_state_exclusion.py`.

This chapter closes the **clean core** of the open crux Chapter 10 named. It is
an unconditional theorem, not a discovery.

---

## FCT-62 — The Clean Mixed-State Exclusion

Status: `THEOREM / UNCONDITIONAL / EXTENSION-MATH`
Scope: the partially-distinguishable Hilbert model (pure and mixed) at the
Fourier tritter, at the registered anchor `r = 3/5`.
Evidence: `shipped`.

For every partial-distinguishability model, the gauge-free raw-count witness
`W = P111 + D2 − 2/3` satisfies `W = (2/9) det G`, where `G` is the `3×3`
internal-state Gram matrix (with `P111 = (2−S+4τ)/9`, `D2 = 2/3 − S/9`,
`S = Σ|g_ij|²`, `τ = Re(g₁₂g₂₃g₃₁)`, and `det G = 1 − S + 2τ`; the count formula
is derived from first principles in the verifier). Gram positivity forces
`det G ≥ 0`, hence `W ≥ 0` for every pure config, hence (by convexity, `W`
affine in the counts) for every **mixed** state, certified operator-level by the
antisymmetrizer `A₋ = (1/6)Σ sgn(π)P_π` (a positive projector) via
`W = (4/3)Tr(A₋Ω) ≥ 0`. The registered extension point has
`W = (2/9)Δ₃ = −128/1125 < 0`, so it lies **outside** the entire class; the
exact separating raw-count test is `P111 + D2 ≥ 2/3`. Fence: this closes the
**clean** mixed-state + mode-mismatch exclusion only; multiphoton, detector,
transfer-matrix, and source-drift nuisances remain the external experimental
layer, and the Chapter-10 bridge premises are unchanged.

## FCT-61 — Negative-Gram Identity Holonomy (The Prediction) — residual updated

Status: `CONDITIONAL EXTENSION / EXPERIMENT-OPEN / BRIDGE-PREMISE-GATED`
(unchanged). The residual is updated by FCT-62: the **clean** mixed-state
PSD-exclusion is now **closed (proven)** — no partially-distinguishable Hilbert
model, pure or mixed, reproduces the registered `(Δ₃, W, Q₃)`; the remaining
open part of the crux is the apparatus-nuisance layer (multiphoton, detector,
transfer-matrix, drift), which stays with the external quantum-optics expert.
