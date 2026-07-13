# Chapter 5 — Becoming Webs: Lawful Time Without Foundation

Status: frozen at `v0.5.0`. Claim rows: FCT-34..FCT-37. Theorem rows:
T-26..T-29. Shipped verification: `becoming_webs.py`.

## Ceiling for this chapter

This chapter separates four features of time that are usually bundled — an
origin, an arrow, a global simultaneity, and a well-founded past — and
shows, as finite machine-checkable mathematics, that each has an
independent status: (1) the time fiber is a *torsor* — fully lawful with no
derivable origin, so any origin is a received selection priced by the
chapter-3 debt; (2) *law-time covers visible-time* — a cyclic visible
dynamics lifts uniquely to an ascending helix whose monodromy is a
conserved grade step; (3) an *arrow needs no thermodynamics* — a fully
reversible visible dynamics with a question ledger never returns jointly,
and the ledger gap is exact bookkeeping of asking; (4) *lawfulness needs no
foundation* — guarded self-reference has unique solutions without any base
case, and local time can be globally obstructed (a Möbius twist) while
every local section is perfect. All statements are theorems or explicit
witnesses at finite-model scope. The chapter does not claim these models
are nature's time; the program-facing readings are `cited`.

## 1. Torsor time: lawful, origin-free (T-26)

A *heap* is a set with a ternary operation `[x, y, z]` satisfying
para-associativity and the identities `[x, x, y] = y = [y, x, x]`. The
integers under `[x, y, z] = x - y + z` are the motivating case: a timeline
with differences and translations but *no zero*.

**Theorem.** `Z_n` under `x - y + z` satisfies all heap axioms (verified
exhaustively for `n = 5, 6, 7`); choosing any element `e` as origin
recovers a group via `x + y := [x, e, y]`, and all such groups are
isomorphic; the translation action is free and transitive, so *no element
is invariant* — there is no derivable "now".

Reading (cited): the floor's time fiber is lawful without an origin. An
origin is a selection on a symmetric fiber — exactly the object chapter 3
proved underivable (T-19) and priced at `ceil(log2 m)` receipt bits.
Everything physics needs from time survives (differences, translations,
duration); only the pointing "this moment" must be received.

## 2. The helix: law-time covers visible-time (T-27)

Take a visible dynamics that cycles with period `p` and a *grade* that
counts how often the cycle closes: states `(theta, n)`, dynamics
`(theta, n) -> (theta + 1 mod p, n + [theta = p - 1])`.

**Theorem.** The projection `(theta, n) -> theta` is a covering of the
visible cycle by the helix: fibers are `Z`-indexed; every finite visible
path lifts uniquely given a start; traversing the visible cycle once
raises the grade by exactly `q = 1` (monodromy); and the deck translations
`n -> n + q` commute with the dynamics and act freely and transitively on
fibers. The visible cycle is the quotient of the helix by its deck group.

Reading (cited): a system can be exactly periodic in every visible
observable while its law-history strictly ascends. "State-time" is the
shadow; "law-time" is its universal cover; the grade step is the deck
translation. Two systems identical at every visible moment can be at
different heights of the same helix.

## 3. The arrow without thermodynamics (T-28)

Couple a *reversible* visible dynamics (rotation on `Z_p`, steps `+1` and
`-1` both admitted) to a *ledger* that increments by one per step taken —
regardless of direction. No probabilities, no entropy, no coarse-graining.

**Theorem.** Exhaustively over all step words up to length 8: the visible
state returns often (any word with net displacement `0 mod p`), but the
*joint* (visible, ledger) state never returns except for the empty word;
the ledger gap between two visits to the same visible state equals exactly
the number of steps asked in between. The joint dynamics is
time-injective: an arrow, from pure bookkeeping of asking.

Reading (cited): the program's "law hysteresis" — visible reversal is not
law reversal; undoing a step is another step. The arrow here is neither
statistical nor thermodynamic; it is the non-erasability of the question
ledger, i.e. chapter 4's cost calculus run forward.

## 4. Lawfulness without foundation (T-29)

Two shipped witnesses:

**(a) Guarded self-reference is productive.** The stream equation
`x = cons(a, x)` — self-referential, no base case — has exactly one
solution at every finite truncation depth, reached from *every* initial
guess within `depth` iterations; the unguarded equation `x = tail(x)` has
multiple solutions at every depth (every constant stream). Uniqueness is
the guard's doing, not a foundation's. Well-foundedness of the past is a
*convenience of description*, not a precondition of lawfulness.

**(b) Local time can be globally twisted.** Cover a cycle by three patches
with `Z_2` transition data `g01 = g12 = +1`, `g20 = -1`. Every patch has
perfect local sections; every overlap agrees up to the declared twist;
*no global section exists* (exhaustive over all eight candidates), while
the untwisted control admits exactly two. A consistent global "now" can
fail for topological reasons while every local experience of time is
flawless.

## 5. What this chapter does not claim

- These are finite models exhibiting possibility and impossibility
  theorems about time-like structure; no claim that nature's time *is* any
  one of them.
- The torsor/covering/ledger readings of the private floor measurements
  are `cited` context.
- Continuum time, relativistic structure, and quantitative arrows are not
  touched here.

## Falsifiers at this chapter's scope

Mechanical: a heap-axiom violation or an invariant element under
translation; a visible path with two distinct lifts or a monodromy other
than `q`; a nonempty step word returning the joint (visible, ledger) state;
a second solution to the guarded equation or a global section of the
twisted cover. The shipped script searches for each and must find none.

## Claims

See [`claims.md`](claims.md) for the exact register rows (FCT-34..FCT-37)
with labels, scopes, and residuals.
