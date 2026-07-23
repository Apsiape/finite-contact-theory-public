# Chapter 63 — The Closure Charge and Its Witnesses: A Fusion Algebra, a Photonic Boundary, and Two Spoof-Closed Detectors

*Finite Contact Theory. A triad of three prepared states carries a single sign
— the product of the three pairwise overlap signs around the loop. We call it
the closure charge χ, and this chapter is the record of what it is, what it is
not, and how one would ever catch it. What it is: a gauge-invariant Z₂
holonomy class, and — the one genuinely new piece — it obeys a fusion algebra
we verify to the last digit (six exact model-theorems: multiplicativity,
exact odd-odd cancellation, screening at a sharp wall, survival). What it is
not: forced by the floor. Every honestly instrumented probe of the floor's own
data glues — sits at the boundary, never across it — so the existence of the
charge in nature is an EXTENSION wager with, we state it plainly, zero
observations. And here is the hardest honesty in the chapter: real photons
always have positive-semidefinite overlap Grams, so no photonic experiment can
ever show the charge above the wall — the wager needs a non-photonic
realization we cannot yet build. Below the wall the whole fusion algebra is
QM-legal and photonically testable now, and we spell out that recovery-grade
protocol. We also kill our own flagship detector: a global route-phase is
invisible to full process tomography yet flips an interferometer (Oi 2003), so
the naive assembly-sign experiment is forgeable — and we rebuild it two ways,
a commutator witness and a sector-conditional correlator, that close the
spoof. The tritter amalgamability boundary is a one-line corollary of a
positive-semidefinite Gram (RECOVERY, with citation). Everything exact is
verified by the shipped script `verify_63_charge.py`.*

## A note on altitude, first

We would have liked to report that the floor forces the closure charge. It
does not, and that verdict is at the top so nothing below reads as a hedge
after the fact. On the floor's own reading law, native counting is
nonnegative, the assembled overlap Gram is always positive-semidefinite, and
χ = +1 everywhere the floor can reach. We ran the cheap probes — a depth-3
twin split, a per-pair relational overlap Gram, a full sweep over reading-law
"coats" — and every one returned the same answer: the floor produces the seat
where a charge could sit (margin-zero twins, the mirror, the boundary) and
never produces the charge. So the charge in nature is an EXTENSION, a
registered wager, and we carry it as one throughout.

What we can defend is smaller and harder than the wager, and it is real. The
sign χ is a genuine gauge invariant — a holonomy class, not a convention — and
it composes: two independently prepared odd triads, fused by product
preparation, cancel their charges exactly, multiplicatively, on a schedule we
compute in advance. That fusion algebra is a THEOREM at model scope, six
checks, all exact, all in the shipped script. It is the difference between a
single suspicious minus sign (which any calibration defect can fake) and an
algebra of signs (which a defect has no reason to obey).

Labels here are load-bearing and we use the weakest accurate one every time:
THEOREM (model) for a proven fact about the fusion algebra or the Gram;
RECOVERY for a reconstruction of known physics on a stated branch (the tritter
boundary); EXTENSION for a floor-level wager beyond the incumbent (the charge
in nature); CONDITIONAL for a result that holds given a named hypothesis;
REGISTERED for a protocol or prediction filed before data; CONJ / OPEN for
what is unsettled; KILLED for a design we scored and discarded. Two of these —
the KILLED flagship detector and the photons-always-glue wall — are the
chapter's most valuable lines.

## 1. The charge: an odd-cycle holonomy, gauge-invariant, with an exact wall

Fix the smallest arena the question needs: three prepared states, pairwise
overlaps g₁₂, g₂₃, g₃₁, unit diagonal (each state normalized). This 3×3
matrix G — the indistinguishability Gram of the triad (Tichy 2015; Brod,
Galvão et al. 2019 for the multiphoton Gram formalism) — is the whole object.
Define the **closure charge**

    χ(G) = sign(g₁₂) · sign(g₂₃) · sign(g₃₁),

the product of the three edge signs around the loop.

**χ is a gauge invariant, not a sign convention (THEOREM, model).** Each
state carries a private phase we do not control; rephasing state *i* by a sign,
ψ_i ↦ −ψ_i, flips every edge incident to *i*, hence flips exactly two of the
three edges in the loop, hence leaves the product χ unchanged. Over all eight
local rephasings χ is invariant — it is the Z₂ odd-cycle holonomy class of the
triad, the element of H¹(C₃; Z₂) that records whether the loop's sign pattern
is trivializable by any choice of local phases. A charge of −1 means it is
not: the frustration lives in the loop, not on any edge. Verified over all
eight rephasings by `verify_63_charge.py` (check A1).

**The charge exists at every overlap; it becomes Gram-visible only past a
sharp wall (THEOREM, model).** Take the canonical odd triad with equal
magnitudes and one frustrated edge, G_odd(v) with off-diagonal signs (+, +,
−). Its determinant factors exactly:

    det G_odd(v) = 1 − 3v² − 2v³ = −(2v − 1)(v + 1)².

Since (v + 1)² > 0 on the whole range, the determinant is negative — the Gram
fails to be positive-semidefinite, so the triad has **no common carrier** —
precisely when v > 1/2. Below v = 1/2 the charge χ = −1 is still there (the
loop is still frustrated), but the Gram is positive-semidefinite and the
charge is *invisible* to any test that only sees whether the states glue. The
wall is v = 1/2, exact. Verified at v ∈ {1/4, 2/5, 1/2, 3/5, 3/4, 9/10} by
`verify_63_charge.py` (check A2): det < 0 iff v > 1/2, to the last fraction.

This is the whole tension of the chapter in one line: **charge is cheap and
carried at every overlap; visibility costs crossing a wall that the floor's
own data never crosses.**

## 2. The fusion algebra (six model-theorems, all exact)

The single number χ would be easy to dismiss as a labeling artifact. The
reason it is not is that it *composes*, and composes in a way no calibration
defect has a reason to imitate. Fuse two triads by product preparation — the
Hadamard (entrywise) product of their Grams, which is what preparing the two
triads jointly and multiplying overlaps gives — and the charge obeys an
algebra. All six statements below are model-theorems, verified exactly in
`verify_63_charge.py`.

**(1) Multiplicativity.** χ(A # B) = χ(A) · χ(B) under Hadamard fusion. Edge
signs multiply entrywise, so the loop product multiplies; over 500 randomized
sign-and-magnitude patterns the identity holds every time (check A4). This is
the load-bearing law: the charge is a *homomorphism* to Z₂.

**(2) Exact odd–odd cancellation.** Fuse two odd triads (each χ = −1). Every
edge sign squares to +, so the fused triad has χ = +1 and — the sharp part —
its determinant is

    det(A # B) = (1 − v)²(1 + 2v) > 0,   v = v_A · v_B,

a fully positive-semidefinite ordinary triad. Two charged, non-amalgamable
triads fuse into one that glues perfectly, with a determinant we predict in
advance (check A3). The anomaly does not merely average away; it *cancels*, on
a computed curve.

**(3) Screening below the wall.** Fuse an odd triad with an even one at
moderate magnitude (odd(3/5) # even(4/5)): the charge survives, χ = −1, but
the fused magnitude v = 12/25 < 1/2, so det > 0 — the charge is *screened*,
present but invisible (check A5). Screening happens exactly at the same v = 1/2
wall.

**(4) Survival against a strong even triad.** Fuse an odd triad with a strong
even one (odd(9/10) # even(9/10)): now v = 81/100 > 1/2, and the charge both
survives (χ = −1) and stays visible (det < 0) (check A6). A charge is not
washed out by fusing with an uncharged partner; only an odd partner cancels
it.

**(5) The tensor-fusion sign law.** For triads fused on a joint carrier (the
Kronecker product of Grams), det(A ⊗ B) = det(A)³ · det(B)³, so the visibility
sign multiplies as a cube — sign-preserving — and two signature-(2,1) triads
combine to a signature-(5,4) nine-dimensional Gram with even total charge
(check A6, exact 9×9 determinant).

**(6) The class is a holonomy, closed under all of the above.** Points (1)–(5)
are consistent because χ is the Z₂ class of §1: multiplicativity, cancellation,
screening, and the tensor law are all shadows of "edge signs multiply, the
loop product is the invariant."

The point of stating six laws rather than one number is the resource-gap
discipline the program runs on: a value-level anomaly (a single χ = −1) is
always forgeable by a relabeling or a calibration defect. An *algebra* of the
anomaly is not — a defect has no reason to compose multiplicatively across
independently randomized preparations, cancel pairwise on the exact curve
(1 − v_A v_B)²(1 + 2v_A v_B), screen at exactly v = 1/2, and survive
strong-even fusion. To spoof the algebra, the spoof would have to *be* the
charge. That is what upgrades the registered door from one conditional number
to a conditional charge with a proven composition law.

## 3. The tritter amalgamability boundary (RECOVERY, a one-line corollary)

The same Gram, read as three photons' internal states, has a completely
standard and photonically measurable face, and we label it plainly: RECOVERY,
a one-line corollary of Gram positive-semidefiniteness, presentational
contribution only. For equal pairwise overlap v and triad phase
θ = arg(r₁₂ r₂₃ r₃₁),

    det G(v, θ) = 1 − 3v² + 2v³ cos θ,

so the Gram is positive-semidefinite — the three states are jointly realizable
in one Hilbert space, i.e. the triad **amalgamates** — exactly when

    cos θ ≥ (3v² − 1) / (2v³),   i.e.   θ ≤ θ_max(v) = arccos[(3v² − 1)/(2v³)].

Two landmarks fall out exactly (both verified by `verify_63_charge.py`,
checks B1–B2, using exact fraction arithmetic on the cosine argument):

- **v = 1/2:** cos θ_max = −1, so θ_max = 180° — every triad phase glues. This
  is the same v = 1/2 wall as §1, now read as "below half-overlap, no phase
  can frustrate the triad."
- **v = 1/√3:** 3v² − 1 = 0, so cos θ_max = 0 and θ_max = 90° exactly.
- **v → 1:** θ_max → 0 — fully indistinguishable photons admit no triad
  frustration at all.

This makes the abstract "the whole triad is a single realizable object"
(the sheaf/common-carrier condition) into a plottable, measurable boundary in
the (v, θ) plane. Menssen et al. (PRL 118, 153603, 2017) measured the
collective triad phase θ; this corollary gives that measured number its
foundational reading — it is the coordinate that decides amalgamability — and
predicts that every real photonic triad sits *inside* the curve. The
constituent mathematics (a positive-semidefinite constraint on a 3×3 Gram) is
classical; the contribution here is presentational, drawing the boundary and
naming what it means.

## 4. The honest wall: photons always glue

Here is the line that fences the whole nature-facing wager, stated without
softening. **Real photonic states always have a positive-semidefinite Gram.**
They live in one common Hilbert space by construction, so their overlap matrix
is a genuine Gram matrix, so det G ≥ 0 always, so no photonic triad can reach
the (v > 1/2, θ = π) region where the charge is Gram-visible. **No photonic
experiment can ever exhibit the closure charge above the wall.** The tritter,
run as a divergence detector, confirms the recovery face — photonic reality
glues — and cannot confirm the extension.

So the charge-in-nature wager (EXTENSION, REGISTERED, zero observations)
requires a **non-photonic realization**: some physical process whose triads
are *not* guaranteed to descend from one common carrier, producing a
non-amalgamable triad no added modes or ancillas can repair (positive-
semidefiniteness is preserved under adding carriers, so more carriers cannot
fake it either). We do not have such a platform, and we do not claim one. This
is the sole registered SACRED door of the program — the one place the wall is
genuine physical measurement, not a matter we can settle in software — and it
is open, with an exact boundary, a robustness threshold, and a reduction
pipeline attached, but no data.

**Below the wall, though, the algebra is legal and testable now.** For v < 1/2
the entire fusion algebra of §2 lives inside ordinary quantum mechanics: the
Grams are positive-semidefinite, the triads are photonically preparable, and
the multiplicativity, cancellation, and screening laws are statements about
measured overlap signs that a photonic tritter can check today. Concretely, a
**recovery-grade validation protocol**:

1. Prepare two triads A, B independently, each at equal pairwise magnitude
   v < 1/2, each with its cyclic sign pattern set by triad-phase choices
   θ ∈ {0, π} on the three edges, so that χ_A, χ_B ∈ {±1} are known per
   preparation.
2. Measure each triad's edge signs (HOM-type two-photon visibilities give the
   magnitudes; the collective-phase method of Menssen et al. gives the loop
   sign) and confirm χ_A, χ_B independently.
3. Fuse by product preparation and measure the fused loop sign χ_{A#B}.
4. **Registered prediction (RECOVERY):** χ_{A#B} = χ_A · χ_B on every trial,
   with the fused Gram positive-semidefinite and det = (1 − v_A v_B)²
   (1 + 2 v_A v_B) exactly. Randomize the per-trial sign choices so no fixed
   defect can track them.

This does not test the divergence — below the wall nothing diverges — but it
validates that the closure charge is a real, composing, measurable invariant
of quantum triads, which is the empirical anchor the wager stands on. A defect
that could not reproduce the multiplicative law below the wall would kill the
whole reading before any non-photonic platform is ever built.

## 5. The witness stack: killing our own detector, then closing the spoof

The natural nature-facing experiment for the charge is an *assembly-order*
sign: build a composite two ways and ask whether the interferometric readout
picks up a relative −1. We attacked our own best version of this first, and it
died. Then we rebuilt it two ways.

### 5.1 The route-phase spoof (a known phenomenon — Oi 2003) — the naive witness is KILLED

A global phase on one route through a network is invisible to complete process
tomography — the Choi/process matrices of the identity channel and of the
channel that multiplies by a global phase are literally equal — and yet that
phase flips an interferometric readout when the route is recombined
coherently. This is not our discovery: it is exactly the interference-of-
quantum-channels effect of Oi (PRL 91, 067902, 2003), and it sits in the same
family as the vacuum-extension / superposition-of-channels analyses of
Kristjánsson, Chiribella and co-workers (quantum channels made to interfere
by a controlled vacuum extension carry a route phase invisible to the
channel's own tomography). The consequence for us is sharp: **ordinary quantum
mechanics can fake an assembly-order sign of −1 with every component
tomographically identical.** A route element −I is tomographically invisible
and flips the readout. So the naive single-readout assembly-sign experiment is
QM-forgeable, and we KILL it — filed loudly as a kill of our own flagship
design, before anyone builds it. (The two matrices' equality is a standard
fact; the point is what it does to the experiment.)

### 5.2 Spoof-closure design one: the commutator witness

The spoof lives entirely in *scalar* route phases — elements that act as a
global constant. Scalars cancel identically in a group commutator: for any
scalar U = zI and any transport V,

    U V U⁻¹ V⁻¹ = z z⁻¹ · V V⁻¹ = I.

So a witness built from a commutator of two transports is **structurally blind
to every scalar route-phase spoof** — the spoof contributes nothing to the
commutator, by algebra, not by calibration. A genuine noncommuting
charge-transport, by contrast, leaves a signature the scalar cannot forge: an
anticommuting pair (Pauli X and Z, self-inverse and unitary) has commutator
XZXZ = (XZ)² = −I. `verify_63_charge.py` demonstrates both exactly in 2×2
complex arithmetic over the Gaussian rationals (checks C1–C2): scalar-phase
commutator = I, anticommuting-pair commutator = −I. The witness reports −I
only for genuine noncommuting transport, never for a route phase.

### 5.3 Spoof-closure design two: the sector-conditional correlator K

The second design closes the spoof statistically rather than algebraically.
Use a **fixed apparatus** and **randomize the sector preparation** per trial:
choose χ_A, χ_B ∈ {±1} independently each shot (via the triad-phase choice
θ ∈ {0, π} at v < 1/2, QM-legal and photonically preparable now — §4), record
the interferometric sign, and form

    K = ⟨ sign · χ_A χ_B ⟩.

A fixed tomographically-invisible spoof produces a sign that is *independent*
of the randomized sector, so its correlation with χ_A χ_B averages to **K ≈ 0**
(a route-phase spoof measured this way gives K near zero). Genuine
charge-transport makes the sign *equal* χ_A χ_B, so **K = 1** exactly. A spoof
can reach K = 1 only by (a) measuring the sector in flight — a disturbance
caught by a standard monitor on the preparation stream — or (b) pre-knowing
the sector — killed by randomization. The correlator is a single number with a
spoof-closed dichotomy: **K = 0 is recovery, K = 1 is the end of associative,
subsystem-positive composition.**

We also register the sharp null the design must beat. In the exact fusion
calculus, early assembly (A # B) # (C # D) and late assembly ((A # C) # B) # D
are *identical entrywise* — Hadamard fusion is associative and commutative —
so any function of the face data, including its fusion order, predicts sign
≡ +1 and K = 0 exactly. **Any genuine assembly-order sign is therefore
necessarily non-face-data physics**, which is what makes K = 1 a real
dichotomy rather than a bookkeeping choice. The witness designs are REGISTERED
protocols; the floor does not force K = 1 (all prior floor verdicts stand),
and this is the extension wager's cleanest operational form.

## 6. The no-cloning distinction, stated in print

The deepest claim in the neighborhood is not the charge itself but *where its
exclusivity structure comes from*: the floor's two conservation laws —
**no-duplication** (a mark is used once; the ledger cannot copy it) and
**no-unreceipted-erasure** (nothing is discarded without a receipt) — are what
force triads to have the exclusivity/holonomy structure that carries χ at all.
On the blind-review sweep this derivation-of-exclusivity-from-two-conservation-
laws came back flagged as **not located in the existing literature**, and we
report it at the program's strongest available language: we are not aware of
prior work deriving contextuality-type exclusivity structure from a pair of
ledger conservation laws in this way.

We state the hazard in the same breath, because the strong label obliges it.
The named OPEN check is this: **it must be shown that this derivation does not
reduce to a repackaged no-cloning or monogamy-of-entanglement argument.**
No-cloning (the impossibility of copying an unknown quantum state) and
monogamy (the trade-off in how much a system can be correlated with several
others) are the obvious incumbents that also forbid a kind of "free
duplication," and a derivation that merely renamed one of them in ledger
language would be a RECOVERY wearing an EXTENSION's label — exactly the
pollution the program most guards against. We have not closed this check. It
is registered as OPEN, in print, as a condition on the novelty claim: until a
proof separates the two-conservation-laws route from a no-cloning/monogamy
repackaging, the concentration is claimed as *plausibly* novel, not
established-novel.

## 7. Kill conditions, and what survives

The whole package carries the registered kill conditions from its
registration. **Abandon the closure-charge direction if all three hold:**
(1) every physically accessible pairwise-consistent triad admits a globally
positive (amalgamable) carrier; (2) every claimed triadic anomaly reduces to
preparation context, postselection, or unrecorded classical correlation; and
(3) — the load-bearing one — no compositional conservation law exists for the
anomalous sign, in particular no odd-odd cancellation. Condition (3) is the
one the fusion algebra was built to meet: without the composition law the
negative-Gram sector is an isolated permissive model; with it, a candidate
physical charge. If a future audit shows the fusion multiplicativity itself is
an artifact of the Gram bookkeeping (a real hazard, since Hadamard products of
Grams are Grams), (3) flips and the door closes.

What survives adversary and honesty is exactly this, no more: the charge is a
gauge invariant (THEOREM), it obeys an exact fusion algebra at model scope
(THEOREM, six checks), the tritter boundary is a clean recovery with a
measurable meaning (RECOVERY), the below-wall algebra is photonically testable
now (REGISTERED, recovery-grade), and the two spoof-closed witnesses give the
nature-facing wager its cleanest operational form (REGISTERED protocols). What
does not survive: any claim that the floor forces the charge (it does not —
every floor probe glues), and any claim that a photonic experiment could show
it above the wall (none can). The exclusivity-from-two-conservation-laws
concentration is claimed as plausibly novel with its no-cloning-distinction
check registered OPEN. All exact results in this chapter are re-derived from a
clean clone by `verify_63_charge.py` — ten checks, all exact, exit nonzero on
any failure.

## References (plain-text)

- A. J. Menssen, A. E. Jones, B. J. Metcalf, M. C. Tichy, S. Barz,
  W. S. Kolthammer, I. A. Walmsley. *Distinguishability and many-particle
  interference*. Phys. Rev. Lett. 118, 153603 (2017).
- M. C. Tichy. *Interference of identical particles from entanglement to
  boson-sampling*. J. Phys. B 47, 103001 (2014).
- D. J. Brod, E. F. Galvão, and co-workers. *Witnessing genuine multiphoton
  indistinguishability* and related work on the multiphoton Gram matrix
  (2019).
- D. K. L. Oi. *Interference of quantum channels*. Phys. Rev. Lett. 91,
  067902 (2003).
- Á. Kristjánsson, G. Chiribella, and co-workers. Work on the superposition /
  interference of quantum channels via vacuum extension.
- W. K. Wootters and W. H. Zurek. *A single quantum cannot be cloned*. Nature
  299, 802 (1982) — the no-cloning incumbent named in the §6 open check.
