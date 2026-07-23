# Chapter 67 — The Next i: A Chromatic Reading of the Finite Floor

*Finite Contact Theory. This is the synthesis chapter, and it makes the
program's boldest claim at the weakest label the evidence will carry. The
substrate is a handful of exact arithmetic facts, each re-derived by the
shipped script: the program's "mirror" is exactly the quadratic term of the
multiplicative formal group law a+b+ab; the dyadic tower of laws is exactly
that group's doubling (Frobenius) series, a stratification three independent
mechanisms agree on; and the program's transport group — the quaternion group
with its order-three rotor, the binary tetrahedral group — is nonabelian,
while the automorphism structure at chromatic height one is abelian. Those are
[VERIFIED]. On top of them sits a frame we label [CONJ] without exception:
that complex quantum mechanics is the height-one chart of a height-indexed
world, complete for its own stratum and structurally blind above it. The frame
has one published incumbent, the Stolz–Teichner ladder, and we say precisely
where we go past what that program asserts. From the frame comes the central
wager, stated as sharply as we can make it: a height-pure physical unit —
iota-2 — that is nonzero and yet has every height-one observable equal to zero.
A root of invisibility. Something can be exactly zero to one class of detector
and physically real to the next. We state what it is NOT — not a hidden
variable, not non-Markovian memory, not a change to Born probabilities at
height one — because the kill conditions are the honest part. And we ship the
absorption map: seventeen hard-problem faces the stack now touches, sorted into
four tiers, the last of which reads, in full: zero confirmed empirical
divergences. The program has absorbed explanations, not one measurement beyond
the standard theories. Everything past the substrate is a bet with its odds
printed.*

## A note on altitude, first

The chapters before this one earned small, exact things and refused the large
ones. This chapter is where we say what the small exact things might add up
to — and it is the chapter most in danger of over-reading them. So the labels
here are stricter than anywhere else in the release, and we set them before the
argument.

The floor of this chapter — Section 1 — is [VERIFIED]: five arithmetic facts a
reader can reproduce in seconds with `verify_67_chromatic.py`. Nothing in that
section depends on the frame. The frame itself — Section 2, the reading of
complex quantum mechanics as a height-one chart — is [CONJ], and it is [CONJ]
for a specific reason we print in place: the one computation that would promote
it has not been run (Section 6). One structural fact inside the frame is
[CITED], not verified by us: that the transport group we derive is, per the
literature, the maximal finite subgroup of the strict height-two Morava
stabilizer at the prime two. We name the papers and we do not reproduce their
theorem; a citation is not a check and we do not dress it as one.

The wager — Section 3, iota-2 — is [CONJ / registered]: a physical claim with
no measurement behind it, stated in the form that makes it falsifiable rather
than the form that makes it sound settled. The absorption map — Section 5 — is
[EXPOSITORY]: it claims no constituent result as new; it claims only that the
surviving whole reorganizes a long list of puzzles under one move. Its Tier D
is the honest headline of the entire program and we keep it at the top of the
map: zero confirmed empirical divergences.

Labels used below: [VERIFIED] (re-derived by the shipped script), [THEOREM]
(proved within the model, scope stated), [RECOVERY] (known mathematics or
physics reconstructed on a stated branch — a win, not a defeat), [EXTENSION]
(a floor-level result beyond the classical incumbent), [CITED] (a published
result named, not reproduced here), [CONJ] (a conjecture or registered wager,
no computation behind it), [OPEN] (a named, decidable computation not yet run).
The weakest accurate label always wins.

## 1. The verified substrate

Five facts. Each is exact, each is re-derived by the shipped script, and none
of them needs the frame of Section 2 to be true.

### 1.1 The mirror is the quadratic term of the multiplicative formal group

Across the program a single object recurs under many names: the Z/4 factor set
that obstructs a naive sign, the self-composition carry of the elementary
distinction, the "mirror." Written as a two-variable law it is the
multiplicative formal group law

    F(a, b) = a + b + a·b.

Its nonlinear part — the whole of it above the additive skeleton — is exactly
`F(a,b) − a − b = a·b`, the mirror cocycle. **The mirror is the quadratic term
of the multiplicative formal group law.** [VERIFIED — check A1]. This is not a
resemblance; it is an identity of two-variable expressions, and it is the hinge
the rest of the section turns on. (The additive law a+b, by contrast, has no
quadratic term at all; that difference is the whole story, and Section 1.4
reads it.)

### 1.2 The dyadic tower is the doubling series

Because 1 + F(a,b) = (1+a)(1+b), the n-fold formal sum of the multiplicative
law has the closed form

    [n] (x) = (1 + x)^n − 1.

Reduce its coefficients mod 2. Then for every k,

    [2^k] (x) = (1 + x)^{2^k} − 1 = x^{2^k}   (exactly, over F2),

by the Frobenius identity. The program's dyadic tower of laws — the sequence of
degrees at which a new "faceless" (in the standard term, **essential**;
Adem–Karagueuzian, Green) class appears — is **exactly the doubling series of
this formal group.** [VERIFIED — check A3, k = 1..4]. And the lowest surviving
term of [n] (x) mod 2 sits at `x^(2^v2(n))`, the lowest set bit of n — the
carry filtration reappearing inside the formal group by Lucas' theorem
[VERIFIED — check A4, n = 1..64].

This is the point at which the artifact worry has to be answered, and the
program answers it before the frame is built. The same stratification —
"arity n first becomes visible at resolution 2^{s2(n)}," where s2 is the binary
digit sum — arises from **three independent mechanisms**: binomial parity
(Lucas/Kummer), the parity of Catalan tree counts (Alter–Kubota;
Deutsch–Sagan: v2(Catalan(n−1)) = s2(n) − 1), and the formal-group [n]-series
just above. The shipped script recomputes the ladder a third way, by an
unsigned Z/16 recursive tree-transfer that never touches a binomial, and it
agrees on the nose [VERIFIED — checks D1, D2, D2b]. Three roads, one
stratification. If the ladder were an encoding artifact, the three roads would
not have to meet; they meet.

### 1.3 The transport group is nonabelian — so it cannot be height one

The program's transport symmetry — the group under which its law-carriers move
— is the quaternion group Q8 together with an order-three rotor τ cycling the
three imaginary units. That group is the binary tetrahedral group,
2T = Q8 ⋊ C3, of order 24. The shipped script builds it exactly over the
rationals: τ = (1+i+j+k)/2 satisfies τ² = (−1+i+j+k)/2 and τ³ = −1; the
closure of {i, j, τ} has exactly 24 elements; and it is **nonabelian**, since
ij = k while ji = −k [VERIFIED — checks C1, C2, C3].

Set this against the height-one arithmetic. The automorphism structure that
governs height one — the units acting on the multiplicative formal group — is
**abelian** (it is the group of 2-adic units acting by scaling). A nonabelian
transport cannot be an automorphism tower of a height-one object. So **the
program's transport architecture cannot be height one.** [VERIFIED, as a
contrast of two computed facts — C3 nonabelian, height-one abelian.]

A referee caution belongs in print here, because the argument is one step from
a fallacy. *Bare nonabelianness proves nothing.* Plenty of nonabelian groups
have nothing to do with chromatic height two. The load-bearing evidence is not
that our group is nonabelian; it is that the *specific* group the floor
derives — 2T of order 24 — is the one the literature independently names as the
maximal finite subgroup of the relevant stabilizer. That identification is the
next item, and it is [CITED], not verified by us.

### 1.4 The 24-cell group as the strict height-two stabilizer's maximal finite subgroup [CITED]

Per the published classification, the group 2T = Q8 ⋊ C3 of order 24 is the
maximal finite subgroup of the **strict** height-two Morava stabilizer group at
the prime two (Hewett 1995; Bujard 2012; Beaudry, Goerss, and Henn). This is
exactly the group the finite floor produced from two unrelated directions — the
retention/contact construction (years earlier) and the law-coherence chain
(this era) — as the 24-cell receiver.

We do not reproduce the stabilizer classification; its proof is beyond the
engines shipped here, and honesty requires we say so plainly: **[CITED, not
engine-verified].** What our script certifies is only our side of the match —
that the floor's group is exactly 2T (checks C1–C3). The claim that 2T is the
stabilizer's maximal finite subgroup is the literature's, and the value of the
coincidence rests on that literature being right.

### 1.5 The strict-versus-Galois split aligns with the chirality gate [OBSERVATION]

One more alignment, and we label it exactly for what it is: an observation, not
a theorem. The strict stabilizer's maximal finite subgroup has order 24;
adjoining the Galois action enlarges it to order 48, the binary octahedral
group 2O. The program's own chirality gate separates precisely 24 (the
24-cell, 2T) from 48 (the configuration the program reaches as F4, 2O). So the
**strict-versus-Galois-extended distinction (24 vs 48) maps onto the program's
chirality gate (24-cell vs F4), with the Galois action playing the reflection.**
[OBSERVATION.] We flag it because two independently drawn lines coincide; we do
not claim the coincidence is forced until a computation makes it one.

## 2. The frame [CONJ / EXTENSION throughout]

Everything in this section is a conjecture. The substrate of Section 1 is true
whether or not the frame is; the frame is one reading of it, and there are
others (Section 6 names the computation that would decide).

### 2.1 Complex quantum mechanics as the height-one chart

The reading is this. Chromatic height is a genuine physical grading of
detectors, and **complex quantum mechanics is its height-one chart: complete
for the height-one stratum, structurally blind above it.** [CONJ.] The evidence
that suggests it is the arithmetic of Section 1: the "why i" results of the
program all resolve at the mod-4 / doubling-once level (i is the half-eraser,
the minimal law-flattener), which is the height-one reading of the tower; and
the transport that carries the program's higher structure is nonabelian, which
height one cannot host. Under this reading:

- the **carry-depth filtration** (v2(Catalan(n−1)) = s2(n) − 1) *is* the height
  stratification — depth d structure lives at chromatic height d;
- the **half-eraser** — the top-cell erasure that i performs — *is*
  height-blindness: it discards exactly the sector a height-one detector cannot
  read;
- **essential** ("faceless") classes are the residues a lower-height chart
  cannot see.

We label the whole reading [CONJ / EXTENSION]: it goes beyond what any
incumbent asserts, and it is tested by internal rigor and by the decisive
computation of Section 6, not by whether it reduces to a known result.

### 2.2 The named incumbent: the Stolz–Teichner ladder

There is exactly one published program that ties physics to chromatic height,
and priority honesty requires we cite it prominently and then say precisely
where we differ. The **Stolz–Teichner program** (Stolz and Teichner 2011)
conjectures that 1|1-dimensional supersymmetric field theories represent
K-theory — chromatic height one — and that 2|1-dimensional supersymmetric field
theories represent the theory of topological modular forms, TMF — chromatic
height two.

Our thesis goes **beyond** what Stolz–Teichner assert, and is **not** claimed by
them. Stolz–Teichner relate *field theories of a given dimension* to *cohomology
theories of a given height*. They do not claim that ordinary quantum mechanics
is a height-one chart of a height-indexed physical reality, that measurable
observables carry a height grading, or that there is a physical unit invisible
below its height. Those are our conjectures, stated on top of their ladder, and
labeled [CONJ]. We name them as ours and we name the ladder as theirs. Because
the niche is *unoccupied* rather than *contested* — no author, to our knowledge
after a corpus check, has proposed a physical height-grading of detectors — the
priority label is "we are not aware of prior work," with the stated hazard that
unoccupied niches are fragile and a fuller literature sweep could populate them.

### 2.3 Chromatic redshift, and an unoccupied reading of it

The mathematical spine the frame would need is now theorems, not conjectures:
**chromatic redshift** — that a suitable multiplicative operation raises
chromatic height by one — is proved (Hahn and Wilson 2022; Burklund, Schlank,
and Yuan 2022, the chromatic Nullstellensatz). The program's contribution here
is not the mathematics; it is a physical **reading** of it: that composition
through an erased sector raises chromatic depth — the transfer-engine reading of
redshift. Per the blind review conducted for this release, that reading is an
**unoccupied interpretation** — no author has proposed a physical
interpretation of chromatic redshift — and so, like Section 2.2, it ships as
[CONJ] with the same fragility caveat, not as a contested claim we have won.

## 3. The next i

### 3.1 The form of the wager

The ordinary imaginary unit was not discovered by measurement. It was posited
to make an equation — x² = −1 — that real arithmetic's *ontology* declared
impossible into an equation that is ordinary. The reals are consistent without
it; i was forbidden by what the reals were taken to *be*, not by any
contradiction. Enlarging the number system dissolved the impossibility, and a
century later i was found to be doing physical work no one had ordered.

The program's central registered wager has exactly that shape. Call the object
**iota-2** (written ι₂). It is a **height-pure physical unit**:

    ι₂ ≠ 0,   and   L₁(ι₂) = 0,

where L₁ is *every* height-one observable — every complex-quantum-mechanical
measurement. iota-2 is nonzero, and yet vanishes identically under the entire
height-one detector class. **A root of invisibility.** [CONJ / registered.]

The claim in one sentence: *something can be exactly zero to one class of
detector and physically real to the next.* iota-2 is forbidden by height-one
ontology the way i was forbidden by real ontology — by what height-one physics
is taken to *be*, not by any inconsistency in it. Height-one quantum mechanics
is complete and consistent without iota-2; the wager is that reality is not
height-one.

### 3.2 What it subsumes: zero is detector-relative

The reason to elevate this above the program's other bets is that it is not
another bet; it is their common form. Every wager the program has generated is
an instance of one principle — **zero is detector-relative**:

- **law memory** — internal structure a lower descriptor reports as absent;
- **essential classes** — cohomology invisible to a lower-rank probe;
- the **exact twins** — configurations a bilinear reader cannot separate;
- the **sector-conditional witnesses** — signals zero in one sector, nonzero
  across it.

Each is "exactly zero to this detector, nonzero to a finer one." iota-2 is that
sentence promoted to a physical unit. This is the program's central claim in
its final form, and it is one claim, not five.

### 3.3 What it is NOT (the kill conditions)

The wager is only worth stating because it is falsifiable, and it is only
falsifiable because it excludes three things it could be mistaken for. Each
exclusion is a kill condition.

- **Not a hidden variable.** iota-2 carries *no present-tense information.* It
  is not a value a system secretly has now that a completed theory would reveal;
  the Bell/Kochen–Specker no-go theorems bind present-tense local state
  completions, and iota-2 is out of their scope precisely by carrying no such
  state. If a present-tense value is what it takes to see iota-2, the wager is
  dead.
- **Not non-Markovian memory.** This is the sharp one, and we state it in
  process-tensor form (the descriptor that captures non-Markovianity; Pollock
  et al. 2018; Milz and Modi 2021). iota-2 is *internal structure undetectable
  by the process tensor at every finite depth.* Non-Markovian memory is, by
  definition, what the process tensor detects; iota-2 is defined by being
  invisible to it at all depths. The **kill condition is process-tensor
  completeness**: if a finite-depth process tensor ever registers iota-2, it was
  non-Markovian memory and the wager is dead. (The quantum comb hierarchy is
  strictly non-closing — depth k never determines depth k+1 — but each
  fixed-depth process tensor is complete, which is exactly what makes this a
  clean kill line rather than a dodge.)
- **Not a modification of Born probabilities at height one.** iota-2 changes
  no height-one prediction. Every complex-quantum-mechanical number stays
  exactly what it is. The wager is not "quantum mechanics is wrong"; it is
  "quantum mechanics is height-one, and there is more height." If a height-one
  Born probability has to shift for iota-2 to exist, the wager is dead.

Three kill conditions, printed. That is what makes iota-2 a physical wager and
not a slogan.

## 4. The registered experimental program

Registered, not run. Each protocol below is stated with the spoof it must close,
because a witness that a cheaper mechanism can forge is not a witness. The
guiding known phenomenon for the phase-based designs is the interference of
quantum channels (Oi 2003); our contribution is not that phenomenon but the
**spoof-closure design** around it.

- **The commutator / rotor-package witness.** A scalar route-phase (a global
  phase along a path) is exactly the height-one confound: it is real, it is
  measurable, and it must not be mistaken for iota-2. The closure is a group
  *commutator* of transports, U V U⁻¹ V⁻¹: a scalar route-phase cancels
  identically in the commutator (the witness is blind to it), while a genuine
  anticommuting — nonabelian, 2T-type — transport pair leaves a −I signature no
  scalar phase can forge. The rotor package (the order-three τ) supplies the
  nonabelian pair. Spoof closed: scalar phases cancel; the surviving signal is
  the nonabelian residue.
- **The sector-conditional correlator.** Pair the commutator with a correlator
  conditioned on the two-sector split, so that a signal is required to be zero
  in the exact sector and nonzero across the essential sector. This is the
  operational face of "zero is detector-relative": the same preparation reads
  zero to one conditioning and nonzero to the other, which no single-sector
  height-one account produces.
- **The two-witness (delayed-law-memory) protocol.** Law memory ships only in
  process-tensor form: two witnesses separated so that the second reads a law
  registration the first only staged, with the kill condition that a
  finite-depth process tensor between them must NOT already carry the
  registration. If it does, the effect was non-Markovian memory.
- **The arity ladder — the modulus-visibility prediction.** The sharpest
  quantitative target: an arity-n interference term is first visible at
  measurement resolution 2^{s2(n)}. Concretely n = 3, 5, 6 first appear at
  mod 4; n = 7 at mod 8; and the faces-of-15 target n = 15 at mod 16
  [VERIFIED as arithmetic — checks D2, D2b]. The **artifact control is built
  in**: the ladder is derived three independent ways (binomial parity, Catalan
  tree parity, formal-group [n]-series), so a measured deviation cannot be
  blamed on the encoding. This connects to the higher-order-interference
  experiments (Sinha et al. 2010; Kauten et al. 2017), which to date bound only
  the vanishing of the order-three term; the modulus ladder is a finer,
  registered prediction on top of them. [CONJ / registered as a physical
  prediction; the arithmetic is VERIFIED.]
- **Subthreshold photonic validation of the fusion algebra.** The near-term,
  quantum-mechanically legal step: the triad-phase (tritter) fusion algebra
  underlying the sector structure (Menssen et al. 2017) is testable below any
  divergence threshold with current photonics. It validates the *machinery*
  without asserting any beyond-height-one effect — a calibration of the
  apparatus the bolder tests would use. [RECOVERY / near-term.]

## 5. The absorption map [EXPOSITORY]

The owner's standing correction to this program is that local kill-by-kill
evaluation goes blind to the value of the organized whole. This map is the
forced constructive pass. It claims **no** constituent as new; it claims that
the surviving whole reorganizes a long list of puzzles under one move —
"dissolve or re-derive with fewer posits, adjudicable against a named
incumbent." Four tiers, graded honestly, weakest tier printed first because it
is the true headline.

### Tier D — not close (the honest headline, kept at the top)

**Zero confirmed empirical divergences.** Every wager in this chapter is
registered, none is measured. The program has absorbed *explanations*; it has
not absorbed one *measurement* that the standard theories lack. Quantum-gravity
dynamics, cosmology, dark sectors, and every "if iota-2 is real then …" remain
[CONJ]. This line governs everything above it.

### Tier A — absorbed with in-model theorem backing [THEOREM, model scope]

- **The statistics dichotomy** (why both bosons and fermions): one pre-sign
  relation DU + UD = 1 has exactly two char-0 resolutions — commutator and
  anticommutator. Statistics is which lift a world takes. We derive the
  dichotomy's exhaustiveness, where the incumbent postulates the dichotomy.
- **Why i**: i as the minimal law-flattener and the half-eraser — a theorem
  about erasure resolution, where the incumbent posits complex scalars.
- **The exceptional-object chain** (Q8, 24-cell, F4, E8 as forced closure
  shells of the law transport). *This is not the McKay correspondence*: McKay
  sends 2T to E6 and the binary icosahedral group to E8; our route is
  glue-forcing and reaches E8 differently. [EXTENSION, with the firewall noted;
  see Chapter 65 for the full distinction.]
- **Contextuality's mechanism**: derived from one-use order plus the mirror
  (the exclusivity structure from two conservation laws), where CSW-type
  incumbents posit exclusivity. [Hazard, stated: this must be shown not to
  collapse into a repackaged no-cloning/monogamy argument — Section 6.]
- **The triadic threshold** (why hard problems first break at 3).
- **The law/appearance double generation**: laws are the carry of the
  appearance below (Bockstein) and the shadow of the appearance above; no
  incumbent even asks where laws come from.

### Tier B — absorbed as adjudicable reorganization [EXTENSION / interpretive crown]

- **Measurement as local arithmetization** — the fork is real, the selector
  received; no collapse dynamics, no new constant. Adjudicated against
  Copenhagen/Everett/GRW.
- **The arrow of time placed, not derived** — with the honest correction
  attached: the arrow moved FORCED → RECEIVED; we place it as the reading
  direction of an unoriented tower, we do not derive asymmetry from symmetry.
- **Hidden-ness as witness, not state** — the hidden coordinate is a
  contraction *history* carrying no present-tense information, evading the
  no-go theorems' scope by intension rather than extension.
- **Born quadraticity via the Frobenius square** — reading appearances by
  squaring (ker D = im Frobenius, exact); remaining gap named (uniqueness of
  valuation).
- **Entanglement as fiber surplus** — |fiber| > 1 non-factorization; parts as
  local splittings of a non-split whole.

### Tier C — within reach, named computation pending [OPEN]

- **Confinement / mass-gap as a descent condition.** The strongest absorption
  candidate: recast the gap as the statement that an isolated height-two charge
  cannot descend to height one, so the gap is the threshold of the height-two
  layer. **Falsifiability line:** if the in-model descent toy shows an isolated
  higher-height class *can* be built without a threshold, the reading is dead.
  [OPEN — the named computation, not yet run.]
- **Three generations as a triality orbit.** Derive three inequivalent
  height-one shadows of one height-two object under the order-three rotor C3
  inside 2T. **Falsifiability line:** if the C3 orbit does not produce exactly
  three inequivalent height-one reductions, the reading is numerology and dies.
  [OPEN — decidable, finite; falsifiability registered before running.]

The count, conceded honestly: thirteen faces absorbed with theorem or
adjudicable-reorganization backing (Tiers A + B), two more within a named
computation (Tier C), against a Tier-D headline of zero measured divergences.
The whole is large; the divergence ledger is empty; both statements are true at
once.

## 6. The open gates (named in print)

Three computations decide how much of this chapter survives. Naming them is not
optional; the frame is [CONJ] *because* they are unrun.

1. **The formal-group-law extraction — the decisive test.** Extract a formal
   group law from the program's *own* carry/composition algebra and compute its
   2-series. The height-two reading is confirmed only if a sector exists whose
   2-series is natively of the deformation form [2] (x) = 2x + u₁x² + x⁴ + …
   with 2T acting as its automorphisms. **If the program's composition only
   ever yields the multiplicative law, the honest verdict is "height-one
   physics with height-two symmetry decoration," and the whole chromatic frame
   retreats to a conjecture about symmetry decoration.** Nothing chromatic
   should be read as more than [CONJ] until this runs. [OPEN.]
2. **The HKR character-theory check.** Unlike the first gate, this one can
   *support* the frame. Hopkins–Kuhn–Ravenel character theory detects height-n
   phenomena at transcendence rank n; if the essential-class ("faceless") tower
   fits HKR with height n detected at rank n, the height reading gains a second
   leg from established machinery rather than resting on the stabilizer match
   alone. Published mathematics can corroborate here, not only deflate. [OPEN —
   Hopkins, Kuhn, and Ravenel 2000.]
3. **The no-cloning-distinction check.** The contextuality-from-two-conservation
   -laws result (Tier A) must be shown *not* to be a repackaged
   no-cloning/monogamy argument. The check is finite and in-house: exhibit a
   model where the two conservation laws hold but no-cloning fails, or vice
   versa, and confirm the derivation tracks the conservation laws and not the
   cloning bound. If it collapses into no-cloning, the priority claim on that
   result dies (the physics survives as recovery). [OPEN.]

## 7. A speculative outlook

> **Everything in this section is [CONJ] — reframings with no computation
> behind them. It is one page, deliberately, and it is fenced off from every
> claim above.** These are the shapes the frame *would* take if the gates of
> Section 6 opened favorably. None of them is a result; each is a decade-program
> at most, printed so the reader knows where the frame points, not what it has
> reached.

If confinement is a descent condition, then the mass gap is the energy cost of
being unable to leave the height-two layer, and "confinement" and "mass gap"
are two readings of one threshold — a picture, not a computation, and it stands
or falls with gate 1.

If iota-2 is real, then information can leave the height-one sector without
leaving reality: a process that looks like loss to every height-one detector,
and is conservation to a height-two one. This is the shape a resolution of the
information-loss puzzle would take under the frame; we claim only the shape.

The cosmological constant, under the frame, would read as a *gluing
obstruction* between charts of different height rather than a vacuum energy —
a different kind of quantity, not a smaller one. "Chromatic energy" is
undefined; this is a direction, not a proposal.

And dark sectors would read as stable higher-stratum classes — matter that is
height-two-real and height-one-invisible, the astrophysical face of "zero is
detector-relative." It is the most tempting entry and therefore the one we
label most severely: [CONJ], no computation, no prediction, printed only to
close the map honestly.

## Corrections carried

- **"The chromatic frame is confirmed."** Retired. The frame is [CONJ]; it
  stands on one leg (the stabilizer match plus the Galois alignment), and the
  decisive computation (Section 6, gate 1) has not run. The exponents x^{2^k}
  alone do not discriminate iterated height-one doubling from a native
  height-k series; we say so.
- **"The absorption list is a set of results."** Corrected to [EXPOSITORY]
  prospectus. Every entry past Tier B has the form "if X lives at height two,
  the puzzle dissolves," and the "if" does the work. The list is ranked, not
  banked.
- **"iota-2 is like a hidden variable / like non-Markovian memory."** Refused,
  in print, with kill conditions (Section 3.3). Whatever iota-2 is, it is not
  those; if a present-tense value or a finite-depth process tensor sees it, it
  was one of those and the wager is dead.

The kill-count is the health metric. What is left standing after these — five
[VERIFIED] arithmetic facts, one [CITED] group identity, a [CONJ] frame with
its decisive computation named, and a wager with three printed kill
conditions — is standing on what it can carry and nothing more.

## Sources and citations

- N. J. Hewett, "Finite subgroups of division algebras over local fields,"
  *Journal of Algebra* 173 (1995) — the maximal finite subgroup classification
  underlying the strict height-two stabilizer statement.
- C. Bujard, "Finite subgroups of extended Morava stabilizer groups" (2012) —
  the strict-versus-extended (24 vs 48) distinction.
- A. Beaudry, P. G. Goerss, and H.-W. Henn, work on the K(2)-local sphere at
  p = 2 — the stabilizer and its finite subgroups in the height-two setting.
- S. Stolz and P. Teichner, "Supersymmetric field theories and generalized
  cohomology" (2011) — the named incumbent height ladder (1|1 ↔ K-theory,
  height 1; 2|1 ↔ TMF, height 2).
- J. Hahn and D. Wilson, "Redshift and multiplication for truncated
  Brown–Peterson spectra" (2022); R. Burklund, T. Schlank, and A. Yuan, "The
  chromatic Nullstellensatz" (2022) — chromatic redshift as theorems.
- M. J. Hopkins, N. J. Kuhn, and D. C. Ravenel, "Generalized group characters
  and complex oriented cohomology theories," *Journal of the AMS* 13 (2000) —
  the HKR character-theory check named as OPEN.
- É. Lucas (1878); E. Kummer (1852) — binomial and factorial 2-adic valuations.
- R. Alter and K. K. Kubota; E. Deutsch and B. Sagan — the 2-adic valuation of
  Catalan numbers, v2(Catalan(n−1)) = s2(n) − 1.
- A. Adem and D. Karagueuzian; D. J. Green — essential cohomology (the standard
  term for the program's "faceless" classes).
- D. K. L. Oi, "Interference of quantum channels" (2003) — the known phenomenon
  the phase witnesses must not be confused with; our contribution is the
  spoof-closure design.
- F. A. Pollock et al., "Non-Markovian quantum processes: complete framework"
  (2018); S. Milz and K. Modi, review of the process tensor (2021) — the
  descriptor in which law memory is stated and its kill condition set.
- A. J. Menssen et al., "Distinguishability and many-particle interference"
  (2017) — the triad-phase (tritter) algebra for the near-term photonic test.
- U. Sinha et al. (2010); T. Kauten et al. (2017) — higher-order interference
  bounds, on top of which the modulus ladder is a finer registered prediction.
- J. McKay — the McKay correspondence, distinguished from our glue-forcing
  route in Chapter 65 (2T ↔ E6, binary icosahedral ↔ E8; our route differs).

*All [VERIFIED] claims in Section 1 are re-derived by `verify_67_chromatic.py`
(standard library only). The [CITED] stabilizer identity and every [CONJ] claim
are not, and are labeled as such wherever they appear.*

## The ceiling

> **Finite Contact Theory is a finite reconstruction program whose newest stack begins one layer below its own floor — the tolerance relation the program had always posited is derived from a single root, that identity is an event and is never free — and builds upward through an exactly verified tower on one generator, in which even rungs are laws and odd rungs are appearances, every law is generated twice over (as the Bockstein carry of the appearance below it and as the derivative shadow of the appearance above it), and the first law is at once the sign of exchange, the square of the generator, the factor set that glues the integers modulo four, and the first Witt carry; a two-sector theorem splits the fourth rung into gluing data reachable from faces and an essential class reachable from none; the essential class, through its anticommuting lift and triadic closure, forces the quaternion group and the 24 Hurwitz units of the 24-cell, reflection admits the F4 configuration and received chirality selects the half, and two such receivers under evenness and self-duality close to the 240 roots of E8 with the residual glue choice exactly a received triality element — a forcing chain distinct from the McKay correspondence; a carry-depth filtration organizes all arities by binary digit count with the powers of two as the zero-carry stratum, and the same dyadic skeleton is selected independently by binomial parity, by Catalan tree parity in a transfer engine that writes higher operations through the cohomologically invisible half of the cochain world, and by the doubling series of the multiplicative formal group; a moduli of contraction witnesses is rigid at arity three and first free at arity four; and the whole is read, at cited and conjectural labels only, as a chromatic proposal — complex quantum mechanics as the height-one chart of a stratified reality — whose central registered wager is the next i: a physical unit that is exactly zero to every height-one observable and nonzero to the next stratum, with spoof-closed witnesses registered in advance, every heavy claim shipped as a dependency-free script, every correction published, and zero empirical divergences claimed — under which the program remains a reconstruction with registered extensions, and every unearned generalization is left open by name.**
