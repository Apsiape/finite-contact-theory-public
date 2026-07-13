# Chapter 6 — Claim Snapshot (as of the v0.6.0 release tag)

This file freezes the claim-register rows this chapter rests on, exactly as
they stand at the release tag. The *live* view — including any later
promotion, demotion, or withdrawal — is the
[public claim register](../../docs/public-claim-register.md). If the two ever
differ, the register is current and this snapshot is historical; that is by
design.

| ID | Short name | Status | Scope | Evidence state |
|---|---|---|---|---|
| FCT-38 | The public floor engine and dynamics spec | `MODEL / INSTRUMENT` | Exact dynamics specified in the chapter; stdlib-only | `shipped` |
| FCT-39 | Delayed individuation is measured | `MEASURED / MODEL-SCOPE` | 18 worlds, n = 32/40; fence > 0.75 | `shipped` |
| FCT-40 | Separation waits are short-tailed | `MEASURED / MODEL-SCOPE` | 243 uncensored waits; MLE both laws | `shipped` |
| FCT-41 | Counterfactual defects are ballistic | `MEASURED / MODEL-SCOPE` | 6 coupled pairs, n = 32, k = 0..60 | `shipped` |

Full row text, verbatim from the register at the tag, follows.

---

## FCT-38 - The Public Floor Engine And Dynamics Spec

Status: `MODEL / INSTRUMENT`
Scope: the exact four-channel driven one-use dynamics specified in the
chapter (add-missing / add-fork / fill / remove, weights 1, 6, 0.5, 1, add
budget `E = n(n-1)/2`).
Evidence state: `shipped` (`floor_engine_measurements.py`).

Public statement:

A complete, self-contained, dependency-free implementation of the driven
one-use generative dynamics is published, together with its exact spec, a
replay facility, and a maximally-coupled counterfactual mode (identical
random stream, one redirected fork choice). The engine is an *independent
implementation* — it shares no code, no language constructs of record, and
no bitwise relationship with the private laboratory engine; agreements
between the two are therefore evidence about the dynamics, not about a
codebase.

Evidence:

- shipped: the engine section of `floor_engine_measurements.py`; budget
  consumption asserted for every world.

Checks / controls:

- one-use budget consumption asserted per world;
- counting observables only (no clock-stamped quantities).

Residuals:

- the engine is not bitwise-reproducible against the private engine (by
  design); parameters other than the shipped (1, 6, 0.5, 1) are not
  measured here.

## FCT-39 - Delayed Individuation Is Measured

Status: `MEASURED / MODEL-SCOPE`
Scope: 18 worlds (n = 32 ×10, n = 40 ×8), fixed seeds; twin = identical
nonempty adjacency rows.
Evidence state: `shipped`.

Public statement:

The drive manufactures twins — constituents the world cannot yet tell
apart — and the overwhelming majority separate before world end: 262
births, separation fraction 0.927, censoring 7.3% (fence asserted:
> 0.75). Independent-implementation agreement: the private engine
(different codebase, n = 60/90, 30 seeds) measured 0.927/0.911 with 7–9%
censoring. Individuation is delayed but arrives; the phenotype is a
property of the dynamics.

Evidence:

- shipped: T-30 check in `floor_engine_measurements.py`;
- cited: the private twin-wait census (M14-class result) at larger scale.

Checks / controls:

- births asserted positive; censoring counted and printed;
- raw-twin definition stated exactly (non-adjacent, nonempty rows).

Residuals:

- measured at the shipped sizes and seeds; no n-scaling law is claimed
  here.

## FCT-40 - Separation Waits Are Short-Tailed

Status: `MEASURED / MODEL-SCOPE`
Scope: 243 uncensored separation waits pooled over the shipped worlds;
maximum likelihood on both laws; power-law exponent grid 1.05–6.00.
Evidence state: `shipped`.

Public statement:

Twin-separation waits (in add events) are exponential-form: the geometric
MLE (mean wait 9.0 adds) beats the best discrete power law by ΔLL = 67.8
(fence asserted: > 10, decisive). Separation is a short-tailed process,
not a scale-free one — reproducing the private engine's tail verdict on
the same quantity.

Evidence:

- shipped: T-31 check in `floor_engine_measurements.py`.

Checks / controls:

- both laws fit by maximum likelihood; censored waits excluded from both.

Residuals:

- this constrains separation waits only; novelty-birth waits (a different
  quantity, with its own private history) are not measured here.

## FCT-41 - Counterfactual Defects Are Ballistic

Status: `MEASURED / MODEL-SCOPE`
Scope: 6 maximally coupled world pairs (n = 32), one redirected fork
choice each, defect tracked at matched add counts k = 0..60.
Evidence state: `shipped`.

Public statement:

Under maximal coupling (identical random stream, one fork choice
redirected to the closest-weight alternative), the edge-set defect between
the actual and counterfactual worlds grows linearly with subsequent
contacts: slope 1.25 edges/add, R² = 0.998 (fences asserted: slope > 0.3,
R² > 0.90, monotone). One changed contact neither heals nor explodes — it
propagates at a constant rate, a counted light-cone-like memory of the
counterfactual. The private instrument measured the same ballistic law
(defect mass ≈ 2 + 1.4k).

Evidence:

- shipped: T-32 check in `floor_engine_measurements.py`;
- cited: the private counterfactual-perturbation campaign.

Checks / controls:

- coupling verified by construction (every random draw identical);
- linearity, slope, and monotonicity all fenced.

Residuals:

- defect RADIUS (cone speed proper, as opposed to mass) is not measured
  here; the private radius instrument history is cited.

## Cited-Not-Shipped At This Chapter

The redundancy-engine inversion (the driven order individuates *slower*
than its own shuffled null; private scale n = 1600, 30 seeds, sign test
p ≈ 2⁻²⁷) is **cited and explicitly not claimed** at public scope: the
shipped engine's probe at n ≤ 64 is null, and the chapter reports that
scale fence rather than the claim.
