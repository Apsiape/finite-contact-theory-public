# Chapter 2 — Claim Snapshot (as of the v0.2.0 release tag)

This file freezes the claim-register rows this chapter rests on, exactly as
they stand at the release tag. The *live* view — including any later
promotion, demotion, or withdrawal — is the
[public claim register](../../docs/public-claim-register.md). If the two ever
differ, the register is current and this snapshot is historical; that is by
design.

| ID | Short name | Status | Scope | Evidence state |
|---|---|---|---|---|
| FCT-21 | Behavior-conditioned capacity and the universal inequality | `THEOREM` | General exclusivity graphs, sharp realizations | `cited` (+ shipped support) |
| FCT-22 | Exact strict preparation gap | `THEOREM` (exact) | KCBS pentagon, unit weights; all sharp realizations, any dimension | `shipped` |
| FCT-23 | Headroom law: the gap is a re-preparation resource | `THEOREM` | Inequality general; canonical closed form pentagon-scope | `cited` |
| FCT-24 | Pentagon tightness phase geometry | `THEOREM` + `MEASURED` | `C_5` only (two-margin machinery pentagon-fenced) | `cited` |
| FCT-25 | Sharpness boundary and novelty posture | `THEOREM` (construction) + `INTERNAL-BLIND` posture | POVM trivialization general; novelty claim graded | `cited` |

Full row text, verbatim from the register at the tag, follows.

---

## FCT-21 - Behavior-Conditioned Capacity And The Universal Inequality

Status: `THEOREM`
Scope: general finite exclusivity graphs `G` with positive weights; sharp
(projective, operationally exclusive) realizations of a fixed behavior.
Evidence state: `cited`, with shipped support via the FCT-22 certificate
script.

Public statement:

For a behavior `p` on `G`, the behavior-conditioned capacity
`kappa_G(p) = inf ||sum_i w_i P_i||_op` over sharp realizations satisfies
`beta(p) = sum_i w_i p_i <= kappa_G(p)`. The capacity reduces faithfully to a
Gram-fiber semidefinite program (bordered-Gram reconstruction both ways), and
rank-one pure realizations suffice: purify-and-project compresses any sharp
realization behavior- and exclusivity-preservingly without increasing
capacity.

Evidence:

- shipped: the FCT-22 certificate exercises the SDP fiber and the
  compression step end-to-end at pentagon scope;
- cited: private verification suite (SDP round-trips, 20 reconstruction
  cases; 30 random-realization compression checks).

Checks / controls:

- the inequality is a one-line trace bound; faithfulness is a Schur-complement
  construction in both directions;
- compression verified on random mixed/higher-rank realizations.

Residuals:

- the compression theorem is fenced to this positive weighted-capacity
  objective; rank matters for other contextuality quantities;
- general-graph claims beyond the definitions, inequality, SDP, and
  compression are not made.

## FCT-22 - Exact Strict Preparation Gap

Status: `THEOREM` (exact rational arithmetic; hand-checkable)
Scope: the pentagon (KCBS) exclusivity scenario with unit weights; the named
rational behavior; all sharp realizations in all finite dimensions.
Evidence state: `shipped`.

Public statement:

The behavior `p = (49/100, 25/81, 16/25, 36/121, 4/9)` with
`beta = 2137213/980100` is realizable by a sharp quantum model, and every
sharp realization satisfies `||sum_i P_i||_op > beta` strictly; hence
`Delta_prep(p) > 0`. Realizability is proved by an exact rational LDL
factorization; impossibility by exact rigidity (unique real part, determinant
`112/495`) plus an exact rational negative witness that kills the entire
Hermitian completion family. No floating-point number is load-bearing.

Evidence:

- shipped: `verification/scripts/exact_gap_certificate.py` and
  `verification/results/FCT-22-exact-gap-certificate-RESULTS.md`; frozen
  chapter copy under `papers/02-behavior-conditioned-capacity/verification/`.

Checks / controls:

- every load-bearing step is `fractions.Fraction` arithmetic;
- the first search candidate failed realizability and was discarded —
  realizability is checked, not assumed;
- the numerical SDP magnitude (`~ 0.0096474`) is quoted as context only; the
  shipped script proves strictness.

Residuals:

- one behavior, one scenario: no genericity claim rides on this row (see
  FCT-24 for the corrected geometry);
- magnitude is numerical, strictness is exact.

## FCT-23 - Headroom Law: The Gap Is A Re-Preparation Resource

Status: `THEOREM`
Scope: inequality at general scope; canonical receiver closed form at
pentagon scope.
Evidence state: `cited`.

Public statement:

Every sharp implementation of a behavior carries headroom
`h = ||K||_op - Tr(rho K) >= Delta_prep(p)`, and re-preparation at the top
eigenvector pays out exactly `h`. A strictly gapped behavior therefore
certifies, from the behavior alone, that any device showing it can extract at
least `Delta_prep` more weighted event-mass by re-preparation. On the
canonical pentagon receiver, `h_can = g(1 - F)` with `g = (3*sqrt(5)-5)/2`,
with an asymmetry lower bound `h_can >= ((5-sqrt(5))/8) * A(p)`.

Evidence:

- cited: private rigidity-bridge verification (8/8 checks).

Checks / controls:

- the inequality is immediate from the definition of `kappa` as an infimum;
- the payoff identity and canonical closed form verified numerically in the
  private suite.

Residuals:

- the robust bridge to asymmetry with universal constants is `OPEN` (C1);
- "resource" means the operational re-preparation payoff defined here, no
  more.

## FCT-24 - Pentagon Tightness Phase Geometry

Status: `THEOREM` (criterion) + `MEASURED` (geometry)
Scope: tightness criterion general; all geometry statements `C_5`-fenced.
Evidence state: `cited`.

Public statement:

`Delta_prep(p) = 0` iff the top-eigenvector Gram feasibility system is
solvable. On the pentagon: the full symmetric contextual line is tight
(`kappa = q`, `2 <= q <= sqrt(5)`); the tight set strictly contains the
symmetric orbit and has interior; explicit gapped behaviors exist; the
boundary is semialgebraic with two named crossing modes; the symmetric spine
is the singular locus of the rigidity system. The earlier "gap is generic"
reading was a sampling artifact and is corrected on the record.

Evidence:

- cited: private SDP + certificate suite (behavior-receipt, global-gap,
  rigidity-bridge scripts).

Checks / controls:

- boundary crossings certified on both sides (Gram-positivity failure vs
  maximality failure);
- the correction history is published (chapter §5).

Residuals:

- the two-margin boundary machinery uses `#non-edges = #vertices`, special to
  `C_5`; general graphs keep only the feasibility criterion;
- `n = 7, 9` behavior of pentagon-exact laws is a named warning.

## FCT-25 - Sharpness Boundary And Novelty Posture

Status: `THEOREM` (construction) for the boundary; graded `INTERNAL-BLIND`
posture for novelty.
Scope: POVM trivialization at general scope; novelty claim as worded, no
stronger.
Evidence state: `cited`.

Public statement:

Unrestricted POVMs trivialize the gap (`E_i = p_i I` reproduces any behavior
at capacity `beta` and destroys the certifying exclusivity structure), so
`Delta_prep` is a sharpness-conditioned receiver invariant. The novelty of
the object package is claimed only at INTERNAL-BLIND evidence class: a
four-lens, repository-barred, refutation-first literature search (77
published query strings) found the functional, the gap, the exact
certificate, the phase geometry, and the headroom law NOT-FOUND as a package,
with all ingredients standard and nearest precedents named
(Sikora–Varvitsiotis–Wei; Moroder et al.; Bharti et al.). No external expert
reviewed this before release, and the paper says so.

Evidence:

- cited: the published novelty review with search logs and residual risks.

Checks / controls:

- collapse candidates to weighted theta refuted numerically at reference
  points;
- the in-house anchored dual derived and verified (strong duality to 1e-6).

Residuals:

- the four published residual risks (appendix-buried lemmas; no
  citation-database access; recent-preprint aliases; extremal self-testing
  folklore) remain open and are quoted in the paper.
