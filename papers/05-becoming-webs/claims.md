# Chapter 5 — Claim Snapshot (as of the v0.5.0 release tag)

This file freezes the claim-register rows this chapter rests on, exactly as
they stand at the release tag. The *live* view — including any later
promotion, demotion, or withdrawal — is the
[public claim register](../../docs/public-claim-register.md). If the two ever
differ, the register is current and this snapshot is historical; that is by
design.

| ID | Short name | Status | Scope | Evidence state |
|---|---|---|---|---|
| FCT-34 | Torsor time: lawful, origin-free | `THEOREM` | Z_n heaps exhaustive (n = 5, 6, 7) | `shipped` |
| FCT-35 | The helix: law-time covers visible-time | `THEOREM` | Period-4 visible cycle, grade truncation | `shipped` |
| FCT-36 | Arrow without thermodynamics | `THEOREM` (exhaustive) | Reversible Z_4 rotation + step ledger, words to length 8 | `shipped` |
| FCT-37 | Lawfulness without foundation | `THEOREM` (witnesses) | Guarded streams to depth 4; Mobius 3-patch cover | `shipped` |

Full row text, verbatim from the register at the tag, follows.

---

## FCT-34 - Torsor Time: Lawful, Origin-Free

Status: `THEOREM`
Scope: `Z_n` under `[x, y, z] = x - y + z`, exhaustive for `n = 5, 6, 7`.
Evidence state: `shipped` (`becoming_webs.py`).

Public statement:

The time fiber modeled as a heap satisfies all heap axioms; choosing any
element as origin recovers a group and all such choices are equivalent; the
translation action is free and transitive, so no element is invariant —
there is no derivable "now". Differences, translations, and durations are
lawful without an origin; an origin is a selection on a symmetric fiber,
which chapter 3 (FCT-27/T-19) proves underivable and prices at
`ceil(log2 m)` receipt bits.

Evidence:

- shipped: T-26 checks in `becoming_webs.py`.

Checks / controls:

- heap identities and para-associativity exhaustive;
- group recovery checked at every origin;
- fixed-point-freeness of every nontrivial translation checked.

Residuals:

- finite cyclic models only; the reading of the private floor's time fiber
  as this torsor is cited program context.

## FCT-35 - The Helix: Law-Time Covers Visible-Time

Status: `THEOREM`
Scope: period-4 visible cycle with unit grade step; finite grade
truncation.
Evidence state: `shipped`.

Public statement:

A cyclic visible dynamics lifts to an ascending helix: the projection is a
covering; finite visible paths lift uniquely given a start; one traversal
of the visible cycle raises the grade by exactly the deck step `q`
(monodromy), and deck translations commute with the dynamics, acting freely
and transitively on fibers. The visible cycle is the quotient of the helix
by its deck group: a system can be exactly periodic in every visible
observable while its law-history strictly ascends.

Evidence:

- shipped: T-27 checks in `becoming_webs.py`.

Checks / controls:

- lifting, monodromy (from every basepoint), and deck commutation checked
  directly.

Residuals:

- one covering model at small scope; the identification of the private
  floor's law hysteresis with this helix is cited.

## FCT-36 - Arrow Without Thermodynamics

Status: `THEOREM` (exhaustive)
Scope: reversible rotation on `Z_4` coupled to a per-step ledger; all step
words through length 8.
Evidence state: `shipped`.

Public statement:

With both step directions admitted (fully reversible visible dynamics) and
a ledger that counts steps taken, the visible state returns often (170
returning words at the tested scope) but the joint (visible, ledger) state
never returns for any nonempty word; the ledger gap between visits to the
same visible state equals exactly the number of steps asked. An arrow of
time from pure bookkeeping — no probabilities, no entropy, no
coarse-graining. Undoing a step is another step.

Evidence:

- shipped: T-28 checks in `becoming_webs.py`.

Checks / controls:

- exhaustive over all 510 words to length 8; joint-return counter asserted
  zero; visible-return counter asserted positive (the contrast is the
  content).

Residuals:

- a possibility theorem: an arrow *can* arise this way; no claim that
  nature's arrow does — that reading is cited program context.

## FCT-37 - Lawfulness Without Foundation

Status: `THEOREM` (witnesses)
Scope: guarded/unguarded stream equations at truncation depths 1..4; the
Mobius-twisted 3-patch `Z_2` cover, exhaustive.
Evidence state: `shipped`.

Public statement:

Guarded self-reference is productive: `x = cons(a, x)` has exactly one
solution at every truncation depth, reached from every initial guess — no
base case, no foundation; the unguarded `x = tail(x)` has multiple
solutions at every depth, so uniqueness is the guard's doing. Separately:
the Mobius-twisted three-patch cover has perfect local sections and *no*
global section (exhaustive over all candidates; the untwisted control has
exactly two): a consistent global "now" can fail topologically while every
local time is flawless.

Evidence:

- shipped: T-29 checks in `becoming_webs.py`.

Checks / controls:

- fixed-point uniqueness verified from every initial condition;
- global-section exhaustion over all eight candidates, with the untwisted
  control run alongside.

Residuals:

- the general guarded-corecursion and gerbe/gluing framings are cited
  program context, not shipped mathematics.
