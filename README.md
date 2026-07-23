# Finite Contact Theory

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21253591.svg)](https://doi.org/10.5281/zenodo.21253591)

> **One rule: a finite thing touches what it cannot fully take in, and the
> contact leaves a mark that can be used once.** From that floor — no Hilbert
> space, no probability, no spacetime granted at the start — the program grows
> tiny universes and measures them with the discipline of experimental science.
> This release follows a single distinction all the way up: from the identity
> root (equality is an *event*, not a standing fact) through a law tower where
> every law is generated twice over, through a forced chain from a coherence
> anomaly to the 24-cell and E₈, to the program's central registered wager —
> **the next i**: a physical unit that is exactly *zero* to every
> complex-quantum observable yet nonzero to the next detector stratum. Every
> result ships as a dependency-free script; the flagship path runs in about a
> minute, the full suite in a few.

## A note from the author

I'm not a physicist. I work in AI and software and follow physics as an
outsider. It didn't start as a theory of physics: it started with one question
I couldn't put down — what is the least that has to exist when something finite
touches something it can't fully take in? A finite thing makes contact with
something larger than itself; the contact is real but partial, so it leaves a
difference, and that difference can't just be wiped away.

The way I chased it is unusual: over about seven months I built a setup where
several AI models work together as a research team and pointed it at that
question. The hardest part was never the physics; it was getting the models to
reach for something new instead of repeating what they were trained on. This is
the piece that has been made public so far, with more built out privately that
I'll share as it's ready. An AI-assisted theory from someone outside the field
is easy to doubt — that's fair, and it's exactly why everything here is scoped,
labeled, and runnable. If I've gotten something wrong, I want to know:
apsiape@gmail.com.

**Quick doors:** [start here (plain language)](docs/start-here-plain.md) ·
[plain-language glossary](docs/glossary.md) ·
[the correction ledger — what we killed, in public](docs/correction-ledger.md) ·
[how to read this repo](docs/how-to-read.md) ·
[what this says about reality](docs/ontology-and-interpretation.md) ·
[open problems — some framework-free](OPEN-PROBLEMS.md) ·
[how to contribute (try to kill something)](CONTRIBUTING.md) ·
[run it yourself](#run-it-yourself)

## The program at a glance

![The reconstruction map — what is derived from what](assets/reconstruction-map.svg)

![The reconstruction ladder — floor to Born rule, rung by rung](assets/reconstruction-ladder.svg)

The goal is a **taxonomy of inevitability**: which features of physical law
would appear in *any* universe grown from a generative floor, and which are
peculiar to ours — answered not as philosophy but as a measured table. The
lattice-era chapters (37–48) delivered the first full artifact of that goal: a
permission map across four genuinely rival dynamics, run through one matched
instrument suite. This release (chapters 62–67) does something different. It
takes the *one* distinction the floor cannot avoid and follows it, rung by rung,
as far as it goes — and it goes remarkably far.

## The spine of this release — one distinction, followed all the way up

### 1. The identity root: equality is an event

The whole program used to *posit* a tolerance relation on the floor — a way of
saying when two marks count as the same. This release removes the posit. From
one root — **using a thing's identity is an event, never free** — the tolerance
relation is now **derived**: tolerance is exactly equality *minus* free
transitivity. Classical mathematics quietly assumes identity is a standing fact
you may reuse at no cost; the floor charges for it. That single change is what
makes everything below it forced rather than chosen (verified by the shipped
census script; the twin-census correction is scored in public — see the ledger
below).

### 2. The law tower: every law generated twice over

One distinction, iterated, generates a tower. Its **even rungs are laws** and its
**odd rungs are appearances**, and the striking fact is that each law is
produced *two independent ways at once*:

- as the **carry** of the appearance just below it (a Bockstein operator — the
  arithmetic "carry bit" of the elementary distinction), and
- as the **shadow** of the appearance just above it (a differential).

Both are ordinary, named classical operators, and the shipped script checks the
identity that ties them together exactly (`DU + UD = 1`, with `ker D = im D =
im Frobenius` at the prime 2 — the uniqueness is a theorem at model scope). No
law is unsourced. The operator center of this tower is a **recovery** of a
classical result (Revoy 1973); the *doubling* — laws as both carry-below and
shadow-above — is, as far as our blind sweeps found, not something the
literature states, because no incumbent framework even asks where laws come
from.

### 3. From a coherence anomaly to the 24-cell and E₈

Follow the tower's coherence structure and a chain forces itself, each link a
recovery of a classical object, the *sequence* a derivation within the model:

- a graded coherence anomaly (the pentagon edges evaluate a coboundary; 0 of 256
  possible dressings survive without *i*, which flattens the curvature),
- through the **quaternion group Q₈** (the minimal anticommuting lift),
- to the **24-cell** — minimal, with **chirality selecting 24 over 48** (the
  binary tetrahedral group, not the binary octahedral one),
- to a **forced E₈ closure** (even, unimodular, self-dual in dimension 8), with
  the *residual* choices enumerated exactly: evenness, chirality, and a triality
  glue.

**This is not the McKay correspondence.** McKay sends the binary tetrahedral
group to E₆ and E₈ to the binary icosahedral group; our route is glue-forcing
and lands differently — the chapter ships a firewall subsection saying so, and a
note distinguishing this E₈ from the E₈ of Kitaev-type topological-phase
physics. The exceptional objects that "keep appearing" in physics for no stated
reason appear here as the closure shells of the law transports (verified by the
shipped derivation-chain script; constituent facts cited to Conway–Smith, SPLAG,
Nikulin, EGNO).

### 4. The carry engine: powers of two are only the ground floor

The famous powers-of-two structure that shows up across the interference
hierarchy turns out to be the **zero-carry stratum** of a full ladder. The
program derives a carry-depth filtration — the 2-adic valuation of the Catalan
numbers equals the binary digit sum minus one (`ν₂(Cat(n−1)) = s₂(n) − 1`;
Alter–Kubota, Deutsch–Sagan, Kummer) — and the physically-loaded reading is that
each carry depth is a stratum of its own. The modulus ladder `2^{s₂(n)}` is
derived three independent ways (binomial parity, Catalan-tree parity, and a
formal-group `[n]`-series) — the triple derivation is the artifact control — yet
the *physical* ladder still ships labeled CONJ/registered, because a clean
derivation is not yet a measured fact. Honest about that; loud about it.

### 5. The next i — the program's central registered wager

Here is the boldest claim in the program, stated plainly and at its weakest
accurate label.

The ordinary imaginary unit *i* did not describe a new measurement. It made an
impossible real equation (`x² = −1`) *ordinary* by enlarging the number system —
what was forbidden by the ontology of the reals, not by any inconsistency,
became a legal object one level up. **The program proposes the next
enlargement.** Call it **ℑ₂**: a physical unit that is exactly

> **ℑ₂ ≠ 0,  yet every height-1 (complex-quantum) observable reads ℑ₂ = 0.**

A *root of invisibility* — the statement that **zero is detector-relative**. It
subsumes every wager the program has generated (law memory invisible to the
process tensor at every finite depth; the faceless/essential classes; the
certified exact twins; the commutator witness) into one principle: a quantity
can be identically zero to one class of detector and real to the next. The
analogy to *i* is structurally faithful — *i* was forbidden by real arithmetic's
*ontology*, not its consistency; ℑ₂ is forbidden by height-1 ontology the same
way.

This comes with a **registered experimental program**, not a discovery:

- **spoof-closed witnesses** — designs (a commutator plus a sector-conditional
  correlator) built specifically to close the known route-phase spoofs (the
  underlying interference phenomenon is Oi 2003; our contribution is the
  spoof-closure design),
- an **arity-visibility ladder** — a faces-of-15 architecture in which a
  quantity visible only at detector arity *k* is exactly zero to every arity
  below it,
- a **near-term photonic validation** at the subthreshold end, runnable against
  existing linear-optics apparatus.

**Zero empirical divergences are claimed, to date.** Every seam that points
outside complex quantum mechanics is a *registered prediction* with a frozen
protocol, a null, and a kill condition — a bet, not a result. The height-2
identification underlying the frame currently stands on one leg (the stabilizer
architecture and a Galois/chirality alignment), and the decisive in-model
computation — extracting a formal group law from the program's own composition
algebra and reading its 2-series — is named in print as OPEN. Nothing chromatic
headlines a proof it hasn't earned.

## What this explains better

Drawn from the release's absorption map (tiers A and B): each row names a
question, the incumbent's standing, the program's answer, and the weakest
accurate label. "Explains better" means adjudicable against a *named* incumbent —
more structure forced, or a puzzle dissolved, with fewer posits — not a feeling.

| The question | Incumbent's status | The program's answer | Label |
|---|---|---|---|
| Why *both* bosons and fermions? | Spin-statistics assumes the dichotomy | One pre-sign relation `DU+UD=1`; commutator and anticommutator are its *only* two resolutions | THEOREM (model scope) |
| Why complex numbers / why *i*? | Complex QM postulated ("why complex?" open) | *i* = the unique local resource that flattens even law-curvature to gauge; four convergent derivations | THEOREM (model scope) |
| Why the exceptional objects (Q₈, 24-cell, F₄, E₈)? | Treated as unexplained coincidences | Derived as the closure shells of the law transports; chirality gates 24 vs 48 | derivation within the model (recovery of each constituent) |
| Where does contextuality's exclusivity come from? | CSW / KS *posit* exclusivity | Derived from two conservation laws (no-duplication + no-unreceipted-erasure) | EXTENSION / registered-novel (hazard: not a no-cloning repackaging — stated in print) |
| Why does everything hard break at 3? | Noted across fields, never unified | One answer: first assembly loop, first non-PSD matrix, first carry depth, first theater of transitivity all at *n* = 3 | expository unification |
| Where do laws come from? | No incumbent asks | Doubly generated: carry of the appearance below + shadow of the appearance above (two classical operators, exact) | THEOREM (model scope) |
| The measurement problem | Copenhagen/Everett/GRW add collapse, branching, or a constant | Fork is real, selector is received; no collapse dynamics, no branching ontology, no new constant | adjudicable reorganization (Tier B) |
| The arrow of time | Boltzmann derives it from a low-entropy past | Placed exactly as the reading-direction of an unoriented tower — RECEIVED, not derived (honest) | adjudicable reorganization (Tier B) |

The full map grades seventeen hard-problem faces across four tiers, including an
explicit "not close" honesty row (quantum-gravity dynamics, cosmology, and any
*confirmed* empirical divergence — still zero). See
[Chapter 67](papers/67-the-next-i/paper.md).

## The corrections ledger is a feature

This program kills its own results in public and ships the kills. A theory that
never discards anything is a mood, not a method. Three from this release:

- **The twin census (Chapter 62).** An early count of the exact "twins" (finite
  objects the floor cannot tell apart) conflated two distinct cases. The
  conflation was caught, the census re-derived, and the corrected count shipped
  with the script — the old headline does not survive under softer wording.
- **The chromatic height-2 reading (Chapter 67).** The exponent test cannot tell
  repeated height-1 doubling from a native height-2 series, so the height-2
  identification is demoted to a **single-legged conjecture**, gated in print on
  extracting a formal group law from the program's own algebra. The frame ships;
  the proof it would need does not yet exist, and we say so.
- **The carry engine's first mirror (Chapter 66).** The naive squared mirror did
  not square to zero; it required a Cartan repair, and the transverse sector came
  back *non-cohomological*. Two honest nulls, shipped in one chapter.

The [correction ledger](docs/correction-ledger.md) records every such kill with
its residue, its current public status, and the exact condition to reopen it.

## How we work

The ambition is large, so the rules are strict — the discipline *is* the method:

- **Predictions are frozen before engines run.** Expected numbers go into the
  design document first; the worlds regularly beat our bets, and a killed bet is
  scored in print.
- **Nothing load-bearing rests on one implementation.** Every claim that matters
  gets a second engine or a blind solver; about a dozen artifacts have been
  caught this way, several of them our prettiest.
- **Blind novelty sweeps run before every release.** Repo-barred referees grade
  each claim KNOWN / KNOWN-ADJACENT / PLAUSIBLY-NEW, and the public labels follow
  their verdicts. Recoveries are stated as recoveries — a recovery here means a
  piece of standard physics or mathematics re-derived from a floor that never
  assumed it, and that is the win condition, not a concession.
- **Exact arithmetic only.** Rational numbers and certified windows — no
  floating-point result is ever load-bearing.
- **Kills are public**, and scored proudly (see above).

## How to challenge this

Every heavy claim in this release has a **dependency-free script** that
re-derives its core exact results from scratch (standard-library Python, no
numpy, exact arithmetic). Run them. Each script ends with an explicit
falsifiability comment — the exact condition under which it would print `[FAIL]`
and exit nonzero. If a claim's script passes and you think the claim is still
wrong, the falsifiability line tells you precisely where to push. A reported kill
with a runnable witness is the most valued contribution the program accepts (see
[CONTRIBUTING.md](CONTRIBUTING.md)); write to apsiape@gmail.com.

## Start here

1. **The next i** — [Chapter 67](papers/67-the-next-i/paper.md): the program's
   central registered wager and the absorption map, at honest labels.
2. **Equality is an event** — [Chapter 62](papers/62-equality-is-an-event/paper.md):
   the identity root, and the tolerance relation derived rather than posited.
3. **The law tower** — [Chapter 64](papers/64-the-law-tower/paper.md): every law
   generated twice over, checked by one exact identity.
4. **From anomaly to E₈** — [Chapter 65](papers/65-from-anomaly-to-e8/paper.md):
   the forced derivation chain, with the McKay firewall.
5. **The permission map** — [Chapter 37](papers/37-permission-map/paper.md): the
   lattice era's whole question, answered in one table (10 minutes).
6. **The divergence** — [Chapter 10](papers/10-negative-gram-holonomy/paper.md) ·
   [Chapter 11](papers/11-mixed-state-exclusion/paper.md): the registered bet
   against the Hilbert Gram cone.
7. **The full index** — [papers/](papers/) (67 chapters) ·
   [theorem bank](docs/theorem-bank.md) ·
   [claim register](docs/public-claim-register.md) ·
   [glossary](docs/glossary.md) · [how to read](docs/how-to-read.md).

## Run it yourself

No dependencies beyond Python's standard library. The flagship path — one
representative exact result per major line — takes about a minute:

```powershell
python verification\scripts\run_all.py --fast
```

The full suite (parallel, with per-script progress) takes a few minutes:

```powershell
python verification\scripts\run_all.py
```

Expected final line: `ALL SHIPPED VERIFICATION: PASS`. Every shipped result line
has one dependency-free script, all exact arithmetic. Release hygiene (scope
language, links, overclaim phrases, the ceiling quoted verbatim) is itself
audited:

```powershell
python scripts\release_audit.py
```

## The fine print — the live ceiling

One sentence bounds everything this release is allowed to claim. It is quoted
identically here, in the [claim register](docs/public-claim-register.md), the
[synthesis chapter](papers/67-the-next-i/paper.md), and the
[release notes](RELEASE-NOTES-v0.36.0.md), and the audit enforces it verbatim.

The scope fence is the result, not an apology. In particular: complex quantum
mechanics in full, the actuality of one outcome, the universal Born rule, the
height-2 identification, whether nature realizes ℑ₂ or any of these structures,
and every *confirmed* nature-facing claim are open, and named as such.

## The ceiling — what is and is not claimed

> **Finite Contact Theory is a finite reconstruction program whose newest stack begins one layer below its own floor — the tolerance relation the program had always posited is derived from a single root, that identity is an event and is never free — and builds upward through an exactly verified tower on one generator, in which even rungs are laws and odd rungs are appearances, every law is generated twice over (as the Bockstein carry of the appearance below it and as the derivative shadow of the appearance above it), and the first law is at once the sign of exchange, the square of the generator, the factor set that glues the integers modulo four, and the first Witt carry; a two-sector theorem splits the fourth rung into gluing data reachable from faces and an essential class reachable from none; the essential class, through its anticommuting lift and triadic closure, forces the quaternion group and the 24 Hurwitz units of the 24-cell, reflection admits the F4 configuration and received chirality selects the half, and two such receivers under evenness and self-duality close to the 240 roots of E8 with the residual glue choice exactly a received triality element — a forcing chain distinct from the McKay correspondence; a carry-depth filtration organizes all arities by binary digit count with the powers of two as the zero-carry stratum, and the same dyadic skeleton is selected independently by binomial parity, by Catalan tree parity in a transfer engine that writes higher operations through the cohomologically invisible half of the cochain world, and by the doubling series of the multiplicative formal group; a moduli of contraction witnesses is rigid at arity three and first free at arity four; and the whole is read, at cited and conjectural labels only, as a chromatic proposal — complex quantum mechanics as the height-one chart of a stratified reality — whose central registered wager is the next i: a physical unit that is exactly zero to every height-one observable and nonzero to the next stratum, with spoof-closed witnesses registered in advance, every heavy claim shipped as a dependency-free script, every correction published, and zero empirical divergences claimed — under which the program remains a reconstruction with registered extensions, and every unearned generalization is left open by name.**

## The horizon

Named targets, explicitly not results: the formal-group extraction that would
give the chromatic frame its second leg; the HKR character-theory check on the
essential ("faceless") classes; the in-model no-cloning-distinction check on the
contextuality derivation; and the first confirmatory experiment for the next i —
reserved for whenever a dedicated apparatus meets the registered protocols. How
the repository grows without rewriting its past:
[EVOLUTION.md](EVOLUTION.md) · [roadmap](docs/roadmap.md) ·
[open problems](OPEN-PROBLEMS.md).

## Author

- Seth Douglas · ORCID: [0009-0007-4708-3252](https://orcid.org/0009-0007-4708-3252) · [github.com/Apsiape](https://github.com/Apsiape) · apsiape@gmail.com

## Citation

Archived and citable via Zenodo. Cite the program by its **concept DOI**
(always the latest version):
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591).
Version DOIs are recorded in [CITATION.cff](CITATION.cff) and each chapter's
freeze record.

## Rights

This work is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).
You may share it and build on it with attribution — the open problems are open on
purpose — as long as derivatives carry the same license; commercial use requires
the author's permission. See [LICENSE.md](LICENSE.md).
