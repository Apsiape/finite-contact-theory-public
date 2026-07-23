# Open Problems

This is the single index of every open problem in Finite Contact Theory. The
problems were previously scattered — across [`docs/roadmap.md`](docs/roadmap.md),
[`docs/hold-register.md`](docs/hold-register.md), the held rows of
[`docs/public-claim-register.md`](docs/public-claim-register.md), the "reopen
only if" conditions of [`docs/correction-ledger.md`](docs/correction-ledger.md),
and dozens of inline *"named open"* / *"held open by name"* statements in the
chapters. This file gathers them in one place, each with a stable ID, a
statement precise enough to attack, and honest tags.

**How to read the tags.**

- **Difficulty** — `accessible` (a determined newcomer with the right
  background can make real progress), `substantial` (a serious project), `hard`
  (a genuine research frontier, possibly open-ended).
- **Prerequisites** — the background actually needed. Several problems need
  *nothing from this theory* — they are stated entirely in standard mathematics.
- **Self-containedness** — `framework-free` (statable and solvable without any
  commitment to this theory's vocabulary — pure math), `framework-light` (needs
  a few defined objects or target numbers, but the incumbent side is standard),
  `framework-native` (posed inside the theory's own reconstruction).

**Advertised up front:** the flagship positivity problem (**OP-01**) needs
**zero buy-in to this theory**. It is a semidefinite / real-algebraic
feasibility question about `3×3` complex matrices; you can attack it knowing
nothing about "one-use contact" or "floors." The same is true of **OP-04** and
**OP-05**. The three most attackable framework-free problems are listed first.

**How to engage.** Solutions, counterexamples, partial results, and sharper
statements are all welcome. Write to **apsiape@gmail.com** (the address in the
[README](README.md)). If your contribution kills or narrows a claim, see
[`CONTRIBUTING.md`](CONTRIBUTING.md) — a reported kill with a runnable witness
is the most valued contribution the program accepts.

**License.** This repository is released under
[CC BY-NC-SA 4.0](LICENSE.md). Building on these problems — attacking them,
extending the theorems, publishing on them — is an *invited* use. Attribution
and share-alike apply; commercial use needs the author's permission.

---

## Lead: the most attackable framework-free problems

### OP-01 — Strict-margin universal accessible-positivity bound
**Difficulty:** accessible · **Prerequisites:** semidefinite programming and/or
real algebraic geometry (positivstellensatz-style certificates); **no
commitment to the theory's vocabulary required** · **Self-contained:**
framework-free · **Source:** [Chapter 10 §5](papers/10-negative-gram-holonomy/paper.md),
[roadmap](docs/roadmap.md), correction [C-17](docs/correction-ledger.md).

The zero-margin bound `152‖z‖² + 9|per A|² − 36|det A|² ≥ 0` is **proven** for
every complex `3×3` matrix `A` (where `z` is the accessible count vector built
from `A`; the proof uses only the toric Fourier identity, no unitarity). The
strict `7/2`-margin version — `152‖z‖² + 9|per A|² − 36|det A|² ≥ (7/2)‖z‖²` —
was **falsified** for arbitrary matrices (the witness
`A = [[-4,-1,1],[-7,1,-3],[6,-3,-5]]` gives `−495`, and it lies on the accessible
toric variety), but it **holds on the lossless unitary core `U(3)`**, saturated
by the Fourier tritter. **Open:** does *any* strict positive margin
`≥ ε‖z‖²` with `ε > 0` hold for all `3×3` complex `A`, and what is the largest
such `ε`? A proof or a sharp counterexample both settle it. This is a clean SDP
/ real-algebraic feasibility question; the `−495` witness ships as a regression
test.

### OP-04 — General proof (or counterexample) of the refusal iff
**Difficulty:** substantial · **Prerequisites:** cyclotomic arithmetic; vanishing
sums of roots of unity (Lam–Leung theory); binomial coincidences · **Self-contained:**
framework-free · **Source:** [Chapter 48 §2](papers/48-arithmetic-of-refusal/paper.md).

A world "refuses" an outcome exactly when a certain binomial mass vector forms
a vanishing combination of `n`-th roots of unity at some reachable depth. The
program has verified the criterion only on the grid `c ∈ {1,2,3,4}`,
`n ∈ {2,4,6,8}` to depth 12 — a **grid-verified conjecture in Lam–Leung
territory, not a proven iff.** The obstruction to a general proof is
multi-term cancellations requiring binomial coincidences
`C(d,k₁) = C(d,k₂) = C(d,k₃)`, which do not arise at low depth but are not
excluded in general. **Open:** prove the iff in general, or exhibit a
counterexample. Pure algebra; no theory needed beyond the stated masses.

### OP-05 — Causal-ceiling family: the `k=4` ancilla and global optimality
**Difficulty:** substantial · **Prerequisites:** semidefinite / see-saw
optimization; process-matrix formalism for indefinite causal order (standard) ·
**Self-contained:** framework-free · **Source:** [Chapter 51 §3](papers/51-causal-ceiling-family/paper.md).

For a marginal, order-averaged causal game at local dimension `d=3`, a see-saw
optimization over process matrices and instruments with three-dimensional
ancillas (`k=3`) reaches `p₃ = 0.738466 > 2/3 = β_causal(3)`, a genuine
violation; qubit ancillas (`k=2`) return only `0.569`, below the bound.
The reported value is an honestly-labeled **see-saw lower bound**: global
optimality is *not* certified, there is no closed form, and **`k=4` is open,
with possible upside**. **Open:** certify the global optimum at `d=3`,
determine whether `k=4` ancillas raise the value, and find a closed form if one
exists. Standard quantum-information optimization; the theory supplies only the
game's normalization.

---

## Positivity and linear-optics core

### OP-02 — A tighter characterization of the accessible set than the toric variety
**Difficulty:** substantial · **Prerequisites:** real algebraic geometry; toric
varieties; permanents/immanants of `3×3` matrices · **Self-contained:**
framework-free · **Source:** [Chapter 10](papers/10-negative-gram-holonomy/paper.md),
[roadmap](docs/roadmap.md).

The accessible count vectors currently sit inside a toric variety cut out by the
identity `∏_even z = ∏_odd z`. The universal positivity bound (OP-01) is proven
on this whole variety, but the variety is likely larger than the truly
realizable set. **Open:** characterize the accessible set more tightly than "the
toric variety," which would sharpen OP-01's achievable margin. Related to, but
independent of, OP-01.

### OP-03 — Mixed-state / mode-mismatch / multiphoton PSD-exclusion (the open crux)
**Difficulty:** hard · **Prerequisites:** semidefinite feasibility over
Hilbert–Gram cones; partial-distinguishability / multiphoton-interference
formalism (Tichy, Shchesnovich, Brod–Galvão); density matrices, loss models ·
**Self-contained:** framework-light (needs the registered count vector
`(Δ₃, W, Q₃)`; the incumbent side is entirely standard quantum optics) ·
**Source:** [Chapter 10 §4](papers/10-negative-gram-holonomy/paper.md),
[Chapter 11](papers/11-mixed-state-exclusion/paper.md).

The negative-Gram theorem proves the extension model is *internally* consistent
(every passive-linear-optical probability is nonnegative). The **decisive open
step** is the opposite exclusion: show that **no** positive-Hilbert model —
including mixed internal states, spectral/temporal/polarization
distinguishability, multiphoton contamination, loss, and tritter imperfection —
can reproduce the registered counts. Chapter 11 closes the **clean core** (the
pure-state, mode-matched, single-photon case). **Open:** the full-nuisance
exclusion. This is the gate before any nature-facing claim on the divergence.
It is a large but well-posed SDP / feasibility question.

### OP-22 — Chapter 10 bridge premises (the physical instantiation)
**Difficulty:** hard · **Prerequisites:** anyonic / topological matter; identity
statistics; quantum optics · **Self-contained:** framework-light, nature-facing ·
**Source:** [Chapter 10 §3](papers/10-negative-gram-holonomy/paper.md).

Three premises carry the negative-Gram prediction from math to nature, and are
held open by name: (1) a physical particle class may carry `Z₂` identity
holonomy; (2) photons may be an appropriate receiver of that sector; (3) passive
linear optics may be the complete relevant measurement grammar. The floor
*permits* the odd-holonomy sector but does not *force* any known particle class
to instantiate it. The natural home is anyonic/topological matter, not photons
(ordinary photons have PSD Gram matrices by construction). **Open:** identify a
physical class that carries the sector, or rule the candidates out.

---

## Contextuality, capacity, and combinatorics

### OP-06 — Contextual-capacity boundary beyond the pentagon fence
**Difficulty:** substantial · **Prerequisites:** contextuality / exclusivity
graphs; the cycle scenarios `C_n`; commutator obstructions · **Self-contained:**
framework-light · **Source:** [Chapter 2 §7](papers/02-behavior-conditioned-capacity/paper.md).

The exact strict preparation-gap machinery (`Δ_prep`) is proven with a
two-margin boundary construction that is **pentagon-fenced** (`C_5`). What
survives on `C_7`, `C_9`, and non-cycle graphs is open — and the `n = 7, 9`
commutator kill is flagged as "a warning, not an accident." **Open:** extend or
bound the capacity result off the pentagon.

### OP-07 — The robust-bridge conjecture (C1)
**Difficulty:** hard · **Prerequisites:** contextuality measures; rigidity /
self-testing near the quantum boundary · **Self-contained:** framework-light ·
**Source:** [Chapter 2 §7](papers/02-behavior-conditioned-capacity/paper.md).

Conjecture: `Δ_prep(p) ≥ c·A(p) − ε_rigidity(S)` with universal constants,
`ε → 0` approaching the quantum boundary. Stated as a conjecture; nothing in
Chapter 2 rests on it. **Open:** prove, refute, or sharpen.

### OP-08 — The general topology-dependent minting-capacity formula
**Difficulty:** substantial · **Prerequisites:** combinatorics / graph theory;
selection rules from conserved labels (Mermin-style) · **Self-contained:**
framework-light · **Source:** [Chapter 24 §4](papers/24-particles-of-floor/paper.md).

Isolation capacity is **topology-dependent, not count-dependent**: the
octahedron (`K₆` minus a perfect matching) caps at 4 accumulated oppositions
where a two-wound configuration reaches 5, via an exhaustion bound on
opposition minting. **Open:** a general capacity formula as a function of wound
topology. Combinatorial; the theory supplies the setup, the question is graph
theory.

---

## Structural: extensionality, amalgamation, genealogy

### OP-09 — Decidability / efficient certificate for the amalgamation obstruction
**Difficulty:** hard · **Prerequisites:** universal algebra; amalgamation;
decision-problem complexity · **Self-contained:** framework-native · **Source:**
[Chapter 54](papers/54-obstruction-spectrum/paper.md).

The genealogy witness is a receipt-preserving amalgamation obstruction
`O_amal`. Its decision problem is open, so no efficient certificate for
`O_amal = 0` is claimed or shipped. **Open:** decidability and, if decidable, an
efficient certificate.

### OP-10 — Computable native criterion for canonical extensionality
**Difficulty:** hard · **Prerequisites:** category theory; sheaf-style
computations over finite floors · **Self-contained:** framework-native ·
**Source:** [Chapter 54 §](papers/54-obstruction-spectrum/paper.md).

Canonical (receipt-inclusive) extensionality of an admitted cell is carried as
a completion law: the completion equivalence is stated, but its **computable
native criterion is open**. **Open:** supply the computable criterion, reducing
the completion law to a shipped decision.

### OP-11 — All-size naturality of the genealogy datum (`K = −I`)
**Difficulty:** substantial · **Prerequisites:** natural transformations;
finite-size induction · **Self-contained:** framework-native · **Source:**
[Chapter 56](papers/56-fixed-point-and-receipts/paper.md).

The genealogy datum is carried at `K = −I` with **all-size naturality named
open**: the finite instances are checked, the uniform-in-size naturality is not.
**Open:** prove (or refute) naturality across all sizes.

---

## The interface reconstruction: actuality and complex QM

### OP-12 — Complex quantum mechanics: the phase that complexifies the cell
**Difficulty:** hard · **Prerequisites:** the interface reconstruction (Chapters
8–9, 13); real vs. complex quantum mechanics · **Self-contained:**
framework-native · **Source:** [Chapter 8 §8](papers/08-nonexact-return/paper.md),
[Chapter 9 §5](papers/09-multifloor-worldweave/paper.md),
[Chapter 13](papers/13-floor-to-interface/paper.md).

The floor forces a real amplitude calculus (the sign scar reaches only
`|1 ± 1|² ∈ {0, 4}`); the quantum value `|1 + i|² = 2` is a **separate added
ingredient**. **Open:** the projective phase that would complexify the cell —
is complex quantum mechanics forced by some floor-native mechanism, or is it a
received input?

### OP-15 — Force the arrow-`J` from a floor-native mechanism
**Difficulty:** hard · **Prerequisites:** as OP-12; time-orientation structure ·
**Self-contained:** framework-native · **Source:** correction
[C-06](docs/correction-ledger.md), [Chapter 8](papers/08-nonexact-return/paper.md).

The conditional unification of the arrow of time, local complex structure, and
complex composition survives **only when the arrow-`J` is admitted**; `J` itself
remains admission data. **Open:** a floor-native mechanism that forces `J`
(closely tied to OP-12).

### OP-13 — The actuality / update law
**Difficulty:** hard · **Prerequisites:** measures over records; no-signaling-in-
time; the actuality protocol · **Self-contained:** framework-native · **Source:**
[Chapter 8 §8](papers/08-nonexact-return/paper.md),
[Chapter 35](papers/35-actuality-protocol/paper.md).

Which measure over the floor's records plays the role of "what happens"? Chapter
35 registers three candidates — classical counting, a linear amplitude reading,
the squared (Born) reading — separated by three exact tables with per-candidate
kill conditions. **Open:** whether a matched **non-Born occurrence kernel**
survives, or whether one law is forced. The discrimination package is a
registered target suite; its bridge premises name that no physical substrate is
yet identified.

### OP-14 — The Born magnitude law (`α = β`): forced or received?
**Difficulty:** substantial · **Prerequisites:** the actualization layer of
Chapter 9 · **Self-contained:** framework-native · **Source:**
[Chapter 9 §5](papers/09-multifloor-worldweave/paper.md).

Given an actual phase, counting forces the *form* of its statistics (a
one-parameter equivariant family), but the Born **magnitude** law `α = β` is not
forced — asymmetric tickets `(2,1)` and `(1,2)` are equally lawful phases.
**Open:** force `α = β`, or prove it is irreducibly received (the same
underdetermination Gleason's theorem exhibits).

---

## Selection and realization

### OP-16 — The general quantum selector theorem
**Difficulty:** hard · **Prerequisites:** almost-quantum sets; Śliwa
inequalities; the native carrier grammar · **Self-contained:** framework-native ·
**Source:** [hold-register](docs/hold-register.md),
[roadmap](docs/roadmap.md), claim register held rows.

The native carrier result is proven at **binary-Bell finite carrier scope**
only. **Open:** a general selector theorem beyond the tested binary/projective
carrier scope — or a clean public statement that it stays open. The
Śliwa-23/41 separators identify where one-receiver and finite tensor-stageable
bodies differ; the general theorem is not in hand.

### OP-17 — `q ≥ 3` outcomes, more settings, non-projective extensions
**Difficulty:** substantial · **Prerequisites:** the native lift construction ·
**Self-contained:** framework-native · **Source:** [hold-register](docs/hold-register.md).

The native lift currently scopes to binary two-setting sites. **Open:** extend
to `q ≥ 3` outcomes, more settings, and non-projective measurements.

### OP-18 — Cross-site interlocking and CHSH-weight selection
**Difficulty:** hard · **Prerequisites:** multipartite Bell scenarios; the
reservoir-to-behavior dynamics · **Self-contained:** framework-native ·
**Source:** [hold-register](docs/hold-register.md).

Super-classical CHSH weights on the staged arena need cross-site interlocking,
which the flat floor does not supply. **Open:** a floor-native interlocking
mechanism (and weight selection) that is not laundered terminalized model scope.

### OP-19 — Which world-phase is selected; whether nature realizes `E_8` / the hexacode / any code
**Difficulty:** hard · **Prerequisites:** the `E_8`–hexacode–Golay–Leech spine;
self-dual codes; nature-facing bridge · **Self-contained:** framework-native,
nature-facing · **Source:** [Chapter 9 §5](papers/09-multifloor-worldweave/paper.md),
[roadmap](docs/roadmap.md).

Under named receiver laws the floor recovers the `E_8`–hexacode spine, but a
forcing audit shows it does **not** select those laws over matched lawful
alternatives: the floor forces the *atlas* of lawful closures and the terminal
self-dual *class*, never the specific *member*. **Open:** which world-phase is
selected (received actuality), and whether nature realizes `E_8`, the hexacode,
or any code.

---

## Alien floor, preclusion, and repetition

### OP-20 — Is measure uniformity necessary for preclusion?
**Difficulty:** substantial · **Prerequisites:** Sorkin preclusion; stoquasticity
/ positivity · **Self-contained:** framework-native · **Source:**
[Chapter 37](papers/37-permission-map/paper.md).

At censused scope, mortality ⇒ no cancellation is an *observed* implication, and
positivity of each phase-mass (not heterogeneity alone) does part of the work.
The converse — that measure **uniformity is necessary** for preclusion — is not
proven and is named open. The alien floor's all-depth positivity is a conjecture
with three-start, depth-3 support. **Open:** prove or refute the necessity
direction; settle the all-depth positivity conjecture.

### OP-21 — The repetition anomaly (firing the same contact twice)
**Difficulty:** substantial · **Prerequisites:** sequential / temporal
correlations (Fritz's temporal CHSH; Budroni et al.) · **Self-contained:**
framework-native · **Source:** [Chapter 37](papers/37-permission-map/paper.md).

One census support lies beyond the affine ∩ weight-union grammar entirely,
minted only by firing the *same* contact twice — a sequential self-dependence
correlation structure. The adjacent genre is known, but the specific statement
is model-internal and untranslated. **Open:** place it against the temporal-
correlation literature, or prove it genuinely new.

---

## All-`n` closures and remaining named stones

### OP-23 — All-`n` / all-sizes structural proofs replacing census-exhaustive checks
**Difficulty:** substantial · **Prerequisites:** the relevant chapter's finite
construction; structural induction · **Self-contained:** framework-native ·
**Source:** [Chapter 25](papers/25-the-up/paper.md),
[Chapter 38](papers/38-price-of-separability/paper.md),
[Chapter 33](papers/33-the-codes-of-the-coat/paper.md).

Several results are census-exhaustive rather than structurally proven for all
sizes: the Chapter 25 all-`n` statement; the Chapter 38 all-sizes separability
proof (census-exhaustive, not yet structural); whether Chapter 33's code
distances exceed 2 at any scale. **Open:** replace the finite censuses with
all-size structural theorems.

### OP-24 — The reconstruction horizon: spacetime, gravity, the continuum, observers, constants
**Difficulty:** hard · **Prerequisites:** varies (general relativity; the
continuum; observer models) · **Self-contained:** framework-native · **Source:**
[roadmap](docs/roadmap.md), corrections
[C-12, C-14, C-16](docs/correction-ledger.md).

The older reconstruction targets, each held open by name and each with a
retired over-claim in the ledger: graph-floor gravity was demoted from "generic
divergence from general relativity" (C-12); the completed continuum is an
admitted overlay, not a native object (C-14); level-2 sourcing / Einstein
gravity is scoped, with sourcing open (C-16). **Open:** a portable, pre-
registered gravitational projection; a completed-real structure required by a
physical prediction with no finite reconstruction; a powered within-geometry
sourcing instrument. Any dimensionful constant, metric, or spectrum is likewise
underived.

### OP-25 — The quantum-dividend question
**Difficulty:** substantial · **Self-contained:** framework-native · **Source:**
[Chapter 45](papers/45-quantum-dividend/paper.md).

Named open: if a world need not interfere to be observed, what marks it as
observed? **Open:** the criterion.

### OP-26 — Habitability: gossip-sector economics beyond the tested horizon
**Difficulty:** substantial · **Self-contained:** framework-native · **Source:**
[Chapter 26](papers/26-habitability/paper.md).

The gossip sector's upkeep economics are measured only to a finite horizon
(caches sufficed at the tested depth; deeper horizons named open). **Open:** the
sector economics beyond that horizon.

### OP-27 — Mortal-observer larger-body fix; breathing-floor disjoint confound
**Difficulty:** substantial · **Self-contained:** framework-native · **Source:**
[Chapter 39](papers/39-mortal-observer/paper.md),
[Chapter 40](papers/40-breathing-floor/paper.md).

Two localized named-open stones: the mortal-observer result needs a larger-body
fix (identified but not carried out); the breathing-floor result names one
disjoint confound rather than absorbing it. **Open:** discharge each.

### OP-28 — Nature-facing scar reader
**Difficulty:** hard · **Self-contained:** framework-native, nature-facing ·
**Source:** [Chapter 14 §5](papers/14-atlas-of-floors/paper.md),
[roadmap](docs/roadmap.md).

The floor's history space is complete as law and incomplete as history; asking
the law to produce the outcome is a type error, not a dynamical puzzle. The
nature-facing form is named open: could any physical scar reader separate what
state-complete tomography calls identical? **Open:** with heavy controls, a
physical instrument that separates the lifts — or a proof that none can.

## New from the chapters 62-67 arc (the next-i era)

### OP-29 — The formal-group extraction gate (the chromatic frame's second leg)
**Difficulty:** hard · **Prerequisites:** formal group laws; Lubin–Tate / Morava
theory; the program's carry/composition algebra · **Self-contained:**
framework-native · **Source:** [Chapter 67](papers/67-the-next-i/paper.md).

The chromatic height-2 identification currently rests on the stabilizer
architecture plus a Galois/chirality alignment — a single leg, because the
exponent test cannot distinguish repeated height-1 doubling from a native
height-2 series. **Open:** extract a formal group law natively from the program's
composition algebra and compute its 2-series. Height-2 is confirmed iff a sector
exists with `[2] (x) = 2x + u₁x² + x⁴ + …` (the deformation form) with the
stabilizer group acting as its automorphisms; if the algebra only ever yields the
multiplicative law, the honest verdict is "height-1 physics with height-2
symmetry decoration." Finite and decisive.

### OP-30 — The HKR character-theory check on the essential ("faceless") classes
**Difficulty:** substantial · **Prerequisites:** Hopkins–Kuhn–Ravenel character
theory; essential cohomology (Adem–Karagueuzian; Green) · **Self-contained:**
framework-light · **Source:** [Chapter 65](papers/65-from-anomaly-to-e8/paper.md),
[Chapter 67](papers/67-the-next-i/paper.md).

The facelessness-as-height claim is "one HKR check from downgrade." **Open:** does
the essential/faceless tower fit HKR character theory — height *n* detected at
rank *n*? A positive result gives the chromatic identification its second leg from
established machinery; a negative one downgrades the height reading of
facelessness. Corroboration or kill; either resolves the label.

### OP-31 — The no-cloning-distinction check on the contextuality derivation
**Difficulty:** accessible · **Prerequisites:** contextuality (CSW, exclusivity
graphs); no-cloning / monogamy arguments · **Self-contained:** framework-light ·
**Source:** [Chapter 63](papers/63-the-closure-charge/paper.md).

The program derives the graph-exclusivity structure of contextuality from two
conservation laws (no-duplication + no-unreceipted-erasure) — flagged
PLAUSIBLY-NEW with a named hazard. **Open:** verify the derivation does not
silently collapse into a repackaged no-cloning / monogamy argument. An in-house,
finite check; a positive collapse would demote the novelty grade, a clean
separation would confirm it.

### OP-32 — The twin governing law: why chords kill and tails breed
**Difficulty:** hard · **Prerequisites:** the exact-twin census; the coat algebra
· **Self-contained:** framework-native · **Source:**
[Chapter 62](papers/62-equality-is-an-event/paper.md).

The census exhibits a stable pattern — certain "chord" configurations annihilate
exact twins while "tail" configurations multiply them — verified case by case but
not explained by a governing statement. **Open:** state and prove the law behind
the chord-kills/tails-breed dichotomy, or exhibit the boundary case that breaks
it. Currently a measured regularity in search of its theorem.

### OP-33 — The moduli of contractions as an object of independent study
**Difficulty:** substantial · **Prerequisites:** homotopy transfer (Kadeishvili;
Merkulov; Markl); A-infinity gauge; BV formalism (Mnev; Costello) ·
**Self-contained:** framework-light · **Source:**
[Chapter 66](papers/66-the-carry-engine/paper.md).

The space of contractions used by the carry engine is a 117-dimensional moduli
object with arity-3 rigidity; the blind sweep found "the space of contractions as
a moduli object of independent study appears genuinely underexplored." **Open:**
characterize this moduli space intrinsically (dimension formula, rigidity locus,
the QFT-native gauge-fixing/propagator reading), independent of the program's
vocabulary. Pure homotopy-algebra; the theory supplies only the motivating
example.

### OP-34 — The witnessed-Witt definition problem
**Difficulty:** hard · **Prerequisites:** Witt vectors (Witt; Serre); necklace/
Metropolis–Rota constructions · **Self-contained:** framework-light · **Source:**
[Chapter 66](papers/66-the-carry-engine/paper.md).

The carry engine's mirror is a Z/4 extension class read as the first Witt carry;
the blind sweep found "Witt vectors with remembered provenance: no matching
construction, no priority obstruction — novelty contingent on a precise
definition." **Open:** give a precise definition of Witt vectors that retain the
provenance (transport vs fresh mint) of each ghost component, and determine
whether it is genuinely new or an existing construction in disguise. The novelty
of the whole witness layer is contingent on this definition.

### OP-35 — The substructural identity-type calculus
**Difficulty:** hard · **Prerequisites:** substructural type theory (linear /
affine logic); homotopy type theory; proof-relevance (Hofmann–Streicher; HoTT
Book) · **Self-contained:** framework-light · **Source:**
[Chapter 62](papers/62-equality-is-an-event/paper.md).

Three blind lanes independently located the same open ground: no existing
substructural type theory grades the equality *witness itself* — all grade terms,
never the identity type. The program's root ("identity/use is an event") demands
exactly such a calculus: an equality witness that carries a usage grade, cannot
be contracted, and leaves receipts. **Open:** construct this calculus (formation,
introduction, elimination, and the substructural rules on the identity type) and
prove its basic metatheory. This is the deepest certified-new ground of the era.

### OP-36 — The seven-body and faces-of-15 witnesses
**Difficulty:** substantial · **Prerequisites:** the carry-depth filtration; the
faces-of-15 architecture; the arity-visibility ladder · **Self-contained:**
framework-native · **Source:** [Chapter 66](papers/66-the-carry-engine/paper.md),
[Chapter 67](papers/67-the-next-i/paper.md).

The arity-visibility ladder predicts quantities visible only at detector arity *k*
and exactly zero below it; the near-term instances are the seven-body witness and
the faces-of-15 scale-simplex (dimension *d* ↔ modulus `2^{d+1}`). **Open:**
construct the explicit seven-body and faces-of-15 witnesses at the level of a
runnable protocol, and register their nulls and kill conditions before any
apparatus is built. This is the constructive front of the next-i experimental
program.

---

*36 problems indexed. Corrections that reopened or bounded a claim are tracked
in the [correction ledger](docs/correction-ledger.md); the "reopen only if"
column there is itself a source of attackable conditions. If you find an open
problem stated in a chapter that is missing here, that omission is itself worth
reporting.*
