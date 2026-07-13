# Chapter 6 — A Measured Generative Floor: Delayed Individuation, Short-Tailed Separation, and Ballistic Counterfactual Defects

Status: frozen at `v0.6.0`. Claim rows: FCT-38..FCT-41. Theorem rows:
T-30..T-32 (all `MEASURED / MODEL-SCOPE`). Shipped verification:
`floor_engine_measurements.py` (engine + measurement suite in one file).

## Ceiling for this chapter

This chapter is the program's *experimental* face at public scope: it ships
a complete, self-contained implementation of a driven one-use generative
dynamics (the "floor"), specifies that dynamics exactly, and reports three
measured phenomena of it, each with a pre-stated quantitative fence that
the shipped script asserts. The claims are measured facts about the
specified dynamics — not about nature. The chapter's strongest
methodological point is *independent-implementation agreement*: the shipped
engine shares no code with the private laboratory engine (different
language constructs, different RNG usage, no bitwise relationship), and the
headline measurement lands on the same value.

## 1. The dynamics, exactly

One world: `n` vertices, the `E = n(n-1)/2` vertex pairs, an initially
empty simple graph, and a one-use contact budget of `E` add events. Four
channels compete each step, drawn proportionally to their weights
(`alpha, gamma, phi, rho = 1, 6, 0.5, 1`):

- **add-missing** `alpha * #missing` — a uniform missing pair is added;
- **add-fork** `gamma * sum(forkweights)` — a missing pair is added with
  probability proportional to its *fork weight* = number of common
  neighbors (the drive: contact begets contact where structure overlaps);
- **fill** `phi * max(0, triangles - filled)` — a bookkeeping channel
  draining the triangle surplus;
- **remove** `rho * #removable` — a uniform removable edge is deleted;
  `(u, v)` is removable iff `u` or `v` has a *private* neighbor (a
  neighbor other than the partner that is not a common neighbor).

The world ends when the add budget `E` is consumed (deleted pairs may be
re-added and consume budget, so the final graph is generally not
complete). All observables below are counting observables — occupancy,
twin censuses, waits in add-counts, symmetric differences; nothing is
clock-stamped. This gauge discipline is inherited from the wider program:
event indices and timestamps are calendar-gauge-dependent; counts are not.

## 2. Measurement I: delayed individuation (T-30)

A *twin* is a pair of vertices with identical nonempty adjacency rows
(`N(u) = N(v)`; necessarily non-adjacent) — two constituents the world
cannot yet tell apart. The drive *manufactures* twins (the fork channel
concentrates contact where neighborhoods already overlap), and the
measurement is what happens to them.

**Result.** Across 18 worlds (n = 32 ×10, n = 40 ×8): 262 twin births;
**92.7% separate before world end** (censoring 7.3%, reported). Fence
asserted by the script: separation fraction > 0.75.

**Independent-implementation agreement.** The private laboratory engine —
a different codebase measured at n = 60 and n = 90 with 30 seeds — returned
separation fractions 0.927 and 0.911 with 7–9% censoring. The shipped
independent engine returns **0.927**. The phenotype (individuation is
delayed but overwhelmingly arrives) is a property of the dynamics, not of
an implementation.

## 3. Measurement II: separation waits are short-tailed (T-31)

For each separated twin, the *wait* is the number of add events between
birth and separation.

**Result.** Over 243 uncensored waits: mean wait 9.0 adds; the geometric
(exponential-form) law beats the best discrete power law by
**ΔLL = 67.8** (maximum likelihood both sides; power-law exponent grid
1.05–6.00). Fence asserted: ΔLL > 10. Separation is a short-tailed
process, not a scale-free one — reproducing the private engine's tail
verdict on the same quantity.

## 4. Measurement III: ballistic counterfactual defects (T-32)

The engine supports *maximally coupled counterfactual pairs*: rerun a
world with the identical random stream, but at one chosen fork event
redirect the choice to the closest-fork-weight alternative. Every
subsequent random draw is numerically identical; only the consequences of
the one changed contact differ. The *defect* is the symmetric difference
between the two worlds' edge sets at matched add counts.

**Result.** Averaged over 6 coupled pairs (n = 32): the defect mass grows
**linearly** with subsequent contacts — slope **1.25 edges/add**,
R² = 0.998 over k = 0..60. Fences asserted: slope > 0.3, R² > 0.90,
monotone. The private engine's counterfactual instrument measured the same
ballistic law (defect mass ≈ 2 + 1.4k). One changed contact neither heals
nor explodes: it propagates at a constant rate — a light-cone-like memory
of the counterfactual, measured in counts.

## 5. What is cited, not shipped

- **The redundancy-engine inversion.** At private scale (n = 1600, 30
  seeds) the driven order individuates *slower* than the same final graph
  in shuffled order (sign test p ≈ 2⁻²⁷): the drive over-produces twins
  early relative to its own null. This effect is a few percent and needs
  large worlds; our public-scale probe (n ≤ 64) is *null* — the shipped
  engine cannot resolve it, and the chapter therefore does not claim it.
  It is recorded here as cited, with its scale fence stated.
- The program-facing readings of these measurements (receiver genesis,
  redundancy-weighted actuality, the consequence cone) are cited context.

## 6. Falsifiers at this chapter's scope

Mechanical, asserted by the shipped script on every run: a world that
fails to consume its budget; a separation fraction at or below 0.75; a
wait census where the power law matches or beats the geometric within
ΔLL = 10; a defect series that is sublinear (R² ≤ 0.90), flat
(slope ≤ 0.3), or non-monotone. Changing the seeds is encouraged; the
fences are meant to survive it.

## Claims

See [`claims.md`](claims.md) for the exact register rows (FCT-38..FCT-41)
with labels, scopes, and residuals.
