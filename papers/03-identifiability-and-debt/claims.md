# Chapter 3 — Claim Snapshot (as of the v0.3.0 release tag)

This file freezes the claim-register rows this chapter rests on, exactly as
they stand at the release tag. The *live* view — including any later
promotion, demotion, or withdrawal — is the
[public claim register](../../docs/public-claim-register.md). If the two ever
differ, the register is current and this snapshot is historical; that is by
design.

| ID | Short name | Status | Scope | Evidence state |
|---|---|---|---|---|
| FCT-26 | The waist: identifiability biconditional | `THEOREM` | Finite descriptions/purposes; two-sided core through 3x3 exhaustive | `shipped` |
| FCT-27 | Selector debt and the no-equivariant-selector theorem | `THEOREM` | Finite alternative sets; symmetry groups without common fixed point | `shipped` |
| FCT-28 | Continuation sufficiency | `THEOREM` | Finite completion models | `shipped` |
| FCT-29 | No universal tomography depth | `THEOREM` (construction) | Explicit certificates d = 1..8; general statement elementary | `shipped` |

Full row text, verbatim from the register at the tag, follows.

---

## FCT-26 - The Waist: Identifiability Biconditional

Status: `THEOREM`
Scope: finite sets, arbitrary descriptions `pi : X -> D`, arbitrary purpose
equivalences `~_T`; two-sided (biextensional) form exhaustive for binary
pairings through 3x3.
Evidence state: `shipped` (`identifiability_debt_calculus.py`).

Public statement:

A purpose-respecting reconstruction from a description exists iff the
description's kernel is contained in the purpose's indifference relation
(`ker pi` within `~_T`); both directions are elementary and are verified on
400 randomized finite models per run with exhaustive per-model
counterexample search. The two-sided form: mutual-indistinguishability
quotients of a finite pairing yield a canonical biextensional core
independent of reduction order (verified exhaustively for all binary
pairings through 3x3 under four reduction orders).

Evidence:

- shipped: T-18 checks in `identifiability_debt_calculus.py`.

Checks / controls:

- both biconditional directions tested independently on every model;
- reduction-order independence tested against four distinct orders.

Residuals:

- infinite-model and structured-category versions are not claimed;
- which purposes any physical system runs is not claimed.

## FCT-27 - Selector Debt And The No-Equivariant-Selector Theorem

Status: `THEOREM`
Scope: finite alternative sets; receipt schemes into binary strings;
symmetry groups acting without a common fixed point.
Evidence state: `shipped`.

Public statement:

Exact later identification of which of `m` pairwise future-inequivalent
alternatives occurred requires at least `ceil(log2 m)` binary receipt
values, and this is attained (verified for `m = 2..8`). Separately: when a
symmetry group of the alternative set preserves all admitted structure and
fixes no alternative, no equivariant selection of a single alternative
exists (an equivariant point selection is a fixed point of the action); the
minimal two-element case is shipped with both candidate selections shown to
break equivariance while the alternative *set* and all symmetric
functionals remain invariant.

Evidence:

- shipped: T-19 checks in `identifiability_debt_calculus.py`.

Checks / controls:

- attainment and un-improvability both checked (the bound is exact, not
  merely a bound);
- selector non-existence checked by exhaustion over all candidate maps in
  the minimal case.

Residuals:

- the theorem forbids *derived, symmetry-respecting* selection; it does not
  assert that selection cannot occur, only that its record carries an
  irreducible cost and its rule is not a consequence of the admitted
  structure.

## FCT-28 - Continuation Sufficiency

Status: `THEOREM`
Scope: finite completion models (lawful completions restricted to present
boundaries; all-future protocol equivalence).
Evidence state: `shipped`.

Public statement:

A present boundary is future-complete iff all of its lawful completions are
future-equivalent — i.e. the restriction kernel on its fiber is contained
in all-future protocol equivalence. This is the waist (FCT-26) applied to
the description "present boundary" and the purpose "all future protocols";
verified as a biconditional on 400 randomized completion models per run.

Evidence:

- shipped: T-20 checks in `identifiability_debt_calculus.py`.

Checks / controls:

- both directions tested independently per fiber, all fibers per model.

Residuals:

- what counts as a lawful completion for any physical system is not
  claimed; the theorem is conditional on the completion model.

## FCT-29 - No Universal Tomography Depth

Status: `THEOREM` (construction)
Scope: explicit certificates for depths 1..8; the general construction is
elementary at all finite depths.
Evidence state: `shipped`.

Public statement:

For every depth `d` there exist completion pairs that agree under every
protocol of depth `< d` and separate at depth `d`; hence no finite protocol
family certifies future-completeness in general. Shipped as explicit
certificate pairs for `d = 1..8`.

Evidence:

- shipped: T-21 checks in `identifiability_debt_calculus.py`.

Checks / controls:

- each certificate's first separation depth computed and asserted equal to
  its advertised `d`.

Residuals:

- none at this scope; the statement is a construction.
