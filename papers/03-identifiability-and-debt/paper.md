# Chapter 3 — The Identifiability and Debt Calculus

Status: frozen at `v0.3.0`. Claim rows: FCT-26..FCT-29. Theorem rows:
T-18..T-21. Shipped verification: `identifiability_debt_calculus.py`.

## Ceiling for this chapter

This chapter proves, at finite-model scope, the three-part calculus that the
wider program uses as its load-bearing spine: (1) an exact identifiability
("waist") condition — a description is sufficient for a purpose exactly when
its kernel is contained in the purpose's indifference relation; (2) an exact
selector-debt bound — identifying one of `m` future-inequivalent alternatives
requires at least `ceil(log2 m)` binary receipt values, and no
symmetry-respecting rule can perform the selection on a symmetric fiber; and
(3) a continuation form — a present description is complete for the future
exactly when all of its lawful completions are future-equivalent. Every
statement here is a finite, machine-checkable theorem at the stated scope.
The chapter does not claim that any physical system realizes a particular
alternative set, and it does not derive which purposes nature runs.

## 1. Setting

All objects are finite. A *description* of a set `X` is a map
`pi : X -> D`. A *purpose* is an equivalence relation `~_T` on `X` (two
elements are purpose-equivalent when no admitted future protocol separates
them). The *kernel* of `pi` is the equivalence `ker pi` identifying `x, y`
with `pi(x) = pi(y)`.

These three primitives — description, purpose, kernel — are deliberately
austere. The private research corpus applies the calculus to receivers,
records, causal cuts, archives, merges, and scattering events; this chapter
ships the core on which all of those applications rest.

## 2. The waist (T-18)

**Theorem (identifiability).** A purpose-respecting reconstruction
`f : D -> X/~_T` with `f(pi(x)) = [x]` exists **iff** `ker pi` is contained
in `~_T`.

*Proof.* If the containment holds, `f([d]) := [any x with pi(x) = d]` is
well defined because two preimages of `d` are kernel-equivalent, hence
purpose-equivalent. Conversely, if some `x, y` have `pi(x) = pi(y)` but
`x !~_T y`, any candidate `f` must send the single value `pi(x)` to two
distinct purpose classes — impossible. ∎

The shipped script verifies both directions on randomized finite models
(400 models per run; every counterexample search exhaustive at model scope).

**Two-sided form (T-18, part b).** For a pairing `K : P x R -> V` (realizations
against receivers), quotienting each side by the other's indistinguishability
(`p ~ p'` iff `K(p, r) = K(p', r)` for all `r`, and dually) yields a
canonical biextensional core, and the reduction is order-independent. The
script verifies order-independence exhaustively for all binary pairings
through size 3x3.

## 3. Selector debt (T-19)

**Theorem (debt bound).** Let `x_1, ..., x_m` be pairwise
future-inequivalent alternatives. Any receipt scheme
`rho : {x_i} -> {0,1}^b` that permits exact later identification of which
alternative occurred requires `b >= ceil(log2 m)`.

*Proof.* Injectivity on `m` values needs at least `m` codewords;
`2^b >= m`. ∎ (Elementary; shipped exhaustively for small `m` so the bound's
attainment is also witnessed: `b = ceil(log2 m)` suffices.)

**Theorem (no equivariant selector).** If a group `G` of symmetries of the
alternative set acts without a common fixed point and preserves all admitted
structure, then no `G`-equivariant map from the structure to a single
alternative exists.

*Proof.* An equivariant point selection is a fixed point of the action. ∎

The script witnesses the minimal case (a two-element fiber exchanged by a
symmetry that preserves every admitted evaluation) and verifies that both
candidate selections violate equivariance, while the *set* of alternatives
and every symmetric functional over it remain invariant.

**Scope note.** The pair (debt bound, no-equivariant-selector) is the exact
public form of what the private corpus calls "the pointing": identifying
which alternative became actual is never free (the bound) and never derived
(the selector theorem); it must be received and paid for. The corpus records
eight independent arrivals of the same `ceil(log2 m)` price — at retention,
merges, gluing, law-provenance, and interaction receipts — all `cited`, not
shipped here.

## 4. Continuation sufficiency (T-20)

**Theorem.** Let `r : E -> B` restrict lawful completions to their present
boundaries and let `~_inf` be all-future protocol equivalence on
completions. A boundary `b` is *future-complete* iff the fiber `r^{-1}(b)`
lies within a single `~_inf` class — i.e. iff `ker r` restricted to the
fiber is contained in `~_inf`.

This is T-18 applied to the description "present boundary" and the purpose
"all future protocols": a present state is a sufficient description of its
own future exactly when its lawful completions are future-equivalent. The
script verifies the biconditional on 400 randomized completion models.

**Corollary (no universal tomography depth, T-21).** For every depth `d`
there exist completion pairs agreeing under every protocol of depth `< d`
and separating at depth `d`. (Shipped: explicit certificates for
`d = 1..8`.) No finite protocol family certifies future-completeness in
general.

## 5. What the calculus is for (cited)

The private corpus uses exactly these three theorems as the recurring test
of every proposed physical structure: records are sufficient descriptions
(T-18) of consequential pasts; scattering conserves a distinction profile
because outgoing kernels must contain incoming ones (T-18 at collisions);
actuality, unit identity, and scale each terminate in a T-19 obstruction;
and the completeness of a physical state is a T-20 statement, not an axiom.
Those applications are `cited` at their own scopes; nothing in this chapter
depends on them.

## 6. Falsifiers at this chapter's scope

The theorems are finite mathematics; their falsifiers are mechanical: a
finite model violating any biconditional direction, a receipt scheme
identifying `m` alternatives in fewer than `ceil(log2 m)` bits, or an
equivariant selector on a symmetric fiber. The shipped script searches for
all three and must find none.

## Claims

See [`claims.md`](claims.md) for the exact register rows (FCT-26..FCT-29)
with labels, scopes, and residuals.
