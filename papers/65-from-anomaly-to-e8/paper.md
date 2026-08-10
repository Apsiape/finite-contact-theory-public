# Chapter 65 — From the Essential Class to the 24-Cell and E8: A Forcing Sequence, and the McKay Firewall

*Finite Contact Theory. This chapter takes one object the program has already
certified — an essential degree-4 cohomology class over Z2, the "faceless"
curvature of assembly space — and follows where it is forced to go. The result
is a single chain: the class lives on the pentagon of a four-fold product; its
anticommuting lift is the quaternion group Q8; adjoining the triadic symmetry
of the three transports closes, minimally, to the 24 Hurwitz units — the
24-cell; admitting the reflective triad instead gives the binary octahedral
group, whose 48 units are the F4 root system, so the program's received
chirality is exactly what selects 24 over 48; and pairing two copies of the
24-cell under the only glue the mirror admits forces E8. Every link is a
THEOREM at model scope or a RECOVERY of standard mathematics we cite by name;
the constituents — Mac Lane coherence, the Hurwitz units, D4 glue theory, the
uniqueness of the even unimodular lattice in dimension 8 — are all classical
and none is claimed as new. What we have not seen assembled before is this
particular forcing sequence, driven from the essential class, with the received
datum named at each gate. The honest hazard is that a reader will hear "2T and
E8" and think of the McKay correspondence, which is a different construction
that pairs 2T with E6 and pairs E8 with the binary icosahedral group; we build
a mandatory firewall section to keep the two apart, and a second note keeping
our E8 distinct from the E8 of chiral topological phases. Every count in the
chain is re-derived exactly, in stdlib arithmetic with no floating point, by
the shipped script `verify_65_e8.py`.*

## A note on altitude, first

The strongest thing in this chapter is a *sequence*, not any one of its links.
Each link, taken alone, is either a theorem inside our model or a piece of
textbook mathematics, and we label it that way in the weakest accurate terms.
2T is the Hurwitz units — Coxeter and Conway–Smith worked that out long ago. The
pentagon is Mac Lane's, and reading its edges as a group-cohomology coboundary
is the standard cocycle bookkeeping of graded monoidal categories
(Etingof–Gelaki–Nikshych–Ostrik). That D4 glues to E8 and that E8 is the unique
even unimodular lattice in dimension 8 is Conway–Sloane. None of that is ours,
and we say so at every step.

What we are claiming as the program's contribution is narrow and precise: that
you can *start* from the essential class the earlier chapters certified and be
*carried*, gate by gate, to E8 — with the physics of each gate (why the mirror
excludes the odd glues, why chirality cuts F4 down to the 24-cell, which datum
is received rather than forced) named in our own language. A blind review of
this chain returned the verdict we adopt as our label: *we are not aware of
prior work assembling this particular forcing sequence from a graded essential
anomaly.* That is a priority claim about the assembly, scoped to the public
label; it is never a claim on the constituents and never a claim of physical
inevitability. No divergence from established physics is asserted anywhere in
this chapter. Where the chain reproduces known structure, that is RECOVERY, and
recovering a known object from a deeper starting point is the win we are after.

Labels are load-bearing here. THEOREM (model scope) marks an exact fact about
the finite structures we build, verified by the shipped script. RECOVERY marks
a classical result reconstructed on a stated branch, cited by name. RECEIVED
marks a fork the floor stages and does not resolve — a genuine choice, enumerated
but not forced. EXTENSION marks a structural claim beyond the classical
incumbent. OPEN and CONJ mark what we have not closed. *"The single most important label in the chapter is RECEIVED, and it appears
**at three RECEIVED gates**: chirality (24 vs 48), the glue element (which
triality automorphism), and — upstream — the choice of scalar lift. **Two
further inputs are SUPPLIED BY THE MODEL rather than received — the order-three
symmetry acting on the law transports, and the doubling under a debt-free
self-duality condition — and are named as such in §4.** Received inputs are
enumerated forks the floor stages and does not resolve; supplied inputs are
construction moves, not choices, and the distinction matters for what the chain
claims."*

## 1. The law-bundle model: the pentagon is the coboundary

### 1.1 Assembly space, and where the first loop is

Take a product of several objects and ask in how many ways it can be bracketed.
The rebracketings, joined by single re-associations, form the associahedra —
assembly space. Its shape at small size is the whole point of this section, so
we count it exactly (`verify_65_e8.py`, and the Tamari census tabulated
below).

- Three leaves: 2 bracketings, joined by one edge. It is an *interval*. There is
  no loop — b1 = 0.
- Four leaves: 5 bracketings, 5 edges, forming a *pentagon* — the first closed
  cycle in assembly space, b1 = 1. This is Mac Lane's pentagon (Mac Lane 1963).
- Five leaves: 14 bracketings, 21 edges, the three-dimensional associahedron;
  its 2-cells are 6 pentagons and 3 squares, and b1 = 8 with Euler characteristic
  14 − 21 + 9 − 1 = 1, a ball, as it must be.
- Six leaves: 42 bracketings, 84 edges, b1 = 43 — the K6 coherence arena, fully
  enumerated and ready.

The Catalan numbers 2, 5, 14, 42 are the vertex counts; the census is exact and
runs in the shipped verification. The one structural fact we need from it is the
first line: **there is no cycle in assembly space below four leaves.** The first
place any holonomy can live is the four-leaf pentagon.

### 1.2 The five edges evaluate the coboundary — RECOVERY

Grade every object by a charge bit in Z2. A *grading-local reassociation rule*
is a function f that reads the three subtree charge-bits of a fused triple and
decides a sign — a 3-cochain f : (Z2)^3 → F2. There are 2^8 = 256 of them.

Walk the pentagon and multiply the five edge-signs the rule assigns. The
product around the loop is, edge for edge,

    (δf)(a,b,c,d) = f(b,c,d) + f(a+b,c,d) + f(a,b+c,d) + f(a,b,c+d) + f(a,b,c)   (mod 2),

which is exactly the group-cohomology coboundary of the 3-cochain f — five
terms, five edges. **The pentagon's five edges evaluate δ.** This is the
standard pentagon-cocycle bookkeeping of graded monoidal categories: the
associator is a 3-cochain, the pentagon is its cocycle condition, and the
anomaly is its class in H^4 (Etingof–Gelaki–Nikshych–Ostrik 2015, *Tensor
Categories*; Mac Lane's coherence theorem is the statement that a trivial class
means all bracketings are canonically identified). We claim none of this as new;
it is RECOVERY, and we set it down explicitly because the next result needs the
correspondence to be exact rather than analogical. Verified for all 256 rules
across all 16 charge sectors by the shipped script (check a1).

### 1.3 No local rule generates the essential class — THEOREM (model scope)

The essential curvature the earlier chapters certified is the degree-4 class

    ω4(a,b,c,d) = a·b·c·d   (mod 2),

the cup power x^4 that generates H^4(Z2; F2). It is nontrivial — not a
coboundary — which is the standard notion of an *essential* class in the sense
of Adem–Karagueuzian and Green (a class not in the image of any transfer /
coboundary from a proper structure). "Faceless" is our word for the same thing;
we use both.

The exact statement, and the one worth the section: **0 of the 256
grading-local rules reproduce ω4.** Sweep every rule and every sector — no local
assignment of signs to fused triples has δf = ω4 on all 16 sectors (check a2).
The essential curvature *cannot be generated by any local reassociation move*.
It has to be **PRESCRIBED** — it is a property of the region's law, not of the
moves available inside it. That is the model content of "faceless": the class is
real, it is degree-4, and no amount of local bracketing convention produces it.

Coherence at five objects confirms the prescription is consistent: δω4 = 0 on
all thirty-two five-module sectors, so the prescribed, sector-conditional
pentagon curvature extends over the K5 associahedron (and upward by cocycle
degree). The minimal law-bundle model is then honestly small: ordinary positive
states within each sector, a trivial associator, and a Z2-connection on assembly
space carrying this prescribed curvature on its pentagons while its squares stay
flat. No indefinite carriers and no nonassociative operators are needed — the
content is *curvature of assembly space*. This is a THEOREM at model scope,
verified exactly.

### 1.4 The i-dressing flattens it — and why that is "why i"

There is a local resource that *does* trivialize ω4, and it is not a sign. Dress
the all-odd triple with a phase: g(1,1,1) = 1 as an exponent of i, i.e. a
3-cochain valued in Z/4 rather than F2. Its μ4 coboundary satisfies

    (δg)(a,b,c,d) = 2·ω4(a,b,c,d)   (mod 4)

on every one of the 16 sectors (check a3) — 2 because −1 = i^2. So over μ4 the
essential class becomes a coboundary: **i flattens the pentagon holonomy into
convention.** No μ2 (±1) rule can do this — that is precisely §1.3 — and the
minimal thing that can is a fourth root of unity applied to the all-odd fusion.
This is an independent reading of "why i": complex amplitudes are the regime in
which the assembly connection has been *flattened*, and i is the flattener. It
exists only for the even (law) rungs; it is the operational face of the
half-eraser from the law-tower chapter. Verified exactly. (The physical wager
that this is *the* reason nature's amplitudes are complex remains a registered
EXTENSION, fenced; the in-model flattening is the theorem.)

Facelessness, then, is the topology of assembly space: there is no cycle below
four leaves (§1.1), so the essential class first appears exactly at the four-leaf
pentagon and nowhere smaller — "the first invisible rung at n = 4" is a fact
about associahedra, not a coincidence. The HKR character-theoretic reading of
the same class — whether ω4 is the degree-4 Hopkins–Kuhn–Ravenel character of
the corresponding transfer — we have not verified; it is OPEN.

## 2. The 24-cell, derived

### 2.1 Q8 from the anticommuting lift — THEOREM (model scope)

The essential law Π = −1 has two realizations (the Two-Lift result of the
law-tower chapter). The scalar realization is the i-dressing of §1.4. The other
is non-scalar: two law transports U, V with U^2 = V^2 = −1 and UV = −VU. Two
anticommuting square roots of minus one generate, with no further input, the
quaternion group

    ⟨U, V⟩ = Q8 = {±1, ±i, ±j, ±k},

eight elements (check b1, exact quaternion arithmetic over the rationals). The
three imaginary units enter here strictly as group elements — the notation must
not be read as smuggling any vector algebra; at this stage i, j, k are the
generators I, J, K of Q8 and nothing more. This is a THEOREM at model scope.

### 2.2 Adjoin the triad: 2T = the 24-cell, minimally — THEOREM/RECOVERY

The three transports are on the same footing, so the triadic symmetry that
cyclically permutes them — the 3-cycle of the three participants — must act on
the lift. Adjoin it as ω, the order-3 unit (−1 + i + j + k)/2 whose conjugation
cycles the axes i → j → k → i. The closure is exact:

    ⟨i, j, ω⟩ = 24 elements = the Hurwitz units = 2T = Q8 ⋊ C3,

the vertices of the 24-cell (checks b2–b4). The 24 are the 8 Lipschitz units
{±1, ±i, ±j, ±k} together with the 16 half-integer units (±1 ± i ± j ± k)/2, and
the generated closure equals that constructed set exactly. That 2T is the
binary tetrahedral group and coincides with the Hurwitz unit group and the
24-cell's vertices is classical — Coxeter's regular polytopes, Conway–Smith's
quaternion account — so the identification is RECOVERY. What is ours is the
*derivation from the essential class*: Q8 as the anticommuting lift, C3 as the
triad of transports.

**Minimality is exact.** The index [2T : Q8] = 3 is prime, so no group sits
strictly between; concretely, every one of the 16 units outside Q8 regenerates
all 24 (check b5). There is no smaller closure: **Q8 plus any triadic symmetry
is the 24-cell, forced** — a THEOREM at model scope.

### 2.3 The rotor: the pentagon sign has a cube root inside the receiver

The unit τ = (1 + i + j + k)/2 is the rotor of the derived receiver. Exactly
(checks b6–b9):

    τ^2 = ω,   τ^3 = −1,   τ^6 = 1,

and conjugation by τ cycles the three transports i → j → k → i. Read τ^3 = −1
with §1: the pentagon *sign* is −1, and τ is a cube root of it living inside the
derived 24-cell. The order-6 rotor is the triadic symmetry realized as an
element of the very group the lift generates — the law's sign, the law's triad,
and the receiver are one object. This closes the loop the program opened years
ago from the other end: the retention/quaternion route found ℍ → 24-cell → F4 as
forced closures of contact, and the law side now reaches the same 24-cell from
the essential class. Two derivations, opposite ends, one object.

## 3. The chirality gate: F4 is the gate itself

Admit instead the *reflective* triad symmetry — a transposition of two axes,
which requires (i + j)/√2, a unit *outside* the Hurwitz order. The closure jumps
to the binary octahedral group 2O of order 48. And 48 is not an arbitrary
number here: 2O splits exactly as

    24 Hurwitz units (the 24-cell)  +  24 units (±1 ± 1)/√2 (the dual, scaled)
      = 24 long roots + 24 short roots = the F4 root system

(Conway–Smith; the 48-unit / F4 identification is classical). So **F4 is the
pre-reception closure** — both chiralities of the triad together — and the
**24-cell is the received half.** The program's oldest orientation result is
that the floor receives one chirality; that received datum is exactly what cuts
F4 down to its orientation-preserving half. NXR found F4 as the receiver
symmetry from the contact side; the law side now says *why* F4 and not something
larger or smaller: F4 is the gate, chirality is the received datum passing
through it, and the 24-cell is what comes out. The selection of 24 over 48 is
**RECEIVED** — enumerated, not forced. The root-system facts are RECOVERY
(Conway–Smith, Coxeter); the reading of F4 *as the chirality gate of the derived
receiver* is the program's assembly.

## 4. E8, forced

### 4.1 The glue enumeration — THEOREM (model scope) over RECOVERY constituents

Take two copies of the 24-cell's lattice, D4 ⊕ D4, and ask which even unimodular
lattice they glue to. The gluing data lives in the discriminant group
(D4*/D4)^2 = (Z/2)^4, and a unimodular even overlattice needs an order-4 glue
subgroup. Enumerate them all (checks c1–c4):

- **All 35 order-4 subgroups**, the 2-dimensional subspaces of (Z/2)^4.
- **Exactly 6 are even.** The three nonzero classes of D4*/D4 (vector, the two
  spinors) all have odd minimal norm, so a glue is even iff it pairs
  equal-norm classes; the mirror — evenness, the x^2 gate of the law tower —
  *excludes the 29 one-sided glues*. Evenness is not decoration here; it is the
  same parity discipline that runs the whole spine, and it does the excluding.
- **All 6 even glues are graphs of automorphisms** of the D4 discriminant form.
  The automorphism group of that form is S3 — triality — so the glue-choice
  space *is* the triality group, exactly the 3! = 6 of them.
- **Every even glue yields 240 roots.** The count is 24 (roots in the first
  factor) + 24 (second factor) + 3 × 8 × 8 (each of the 3 nonzero classes
  contributes an 8 × 8 block of glued minimal vectors) = 240. Index-4 glue of a
  determinant-16 lattice gives determinant 1; even + unimodular in dimension 8
  forces E8, which is unique (Conway–Sloane, SPLAG; the discriminant-form
  machinery is Nikulin 1979).

**THEOREM (model scope): evenness (the mirror) plus self-duality (the debt-free
closure) force the double 24-cell to close to E8, and the residual choice of
glue is exactly a triality element — RECEIVED, not forced.** The signature shape
of the whole program — the form forced, the selector received — recurs at the E8
rung. A direct enumeration of E8's own norm-2 vectors confirms 240 with the
D4+D4-frame decomposition 24 + 24 + 64 + 128 (checks d1–d4), the 64 mixed-integer
and 128 half-integer roots together matching the glue's 3 × 8 × 8 = 192.

### 4.2 What is claimed, and what is cited

Everything constituent is classical and cited: D4 glue theory and the
even-unimodular-in-dimension-8 uniqueness are Conway–Sloane; discriminant forms
and the graph-of-automorphism picture of glue are Nikulin. This is worked-out
glue theory, applied. The contribution we claim, per the blind review, is the
**forcing narrative**: that the enumeration is driven *from the essential
class* — mirror ⇒ evenness gate ⇒ the 6 even glues; self-duality ⇒ unimodularity;
chirality ⇒ 24 over 48 — with the received datum named at every gate (the
chirality at 24|48, the triality element at the E8 glue). *"The chain essential class → Q8 → 2T → 24-cell → E8 is forced at every link
**given five named inputs**: three RECEIVED forks (the scalar lift; the
chirality; the triality glue) and two construction inputs SUPPLIED BY THE MODEL
(the order-three symmetry acting on the law transports; the doubling under a
debt-free self-duality condition). The first two are enumerated choices the
floor stages and does not resolve; the last two are not choices but imports,
and we name them as such. **The arrow from the identity root to the essential
class is not derived in this release and is struck from the chain statement
here.**"* That is a model-scope theorem
about our own construction, not a claim on the lattice theory it uses.

## 5. This is not the McKay correspondence (firewall)

A reader who sees "2T" and "E8" in the same chapter will think of the McKay
correspondence, and will be wrong to map our chain onto it. We state the
distinction in print so the conflation cannot happen.

**The McKay correspondence** (McKay 1980) attaches to each finite subgroup of
SU(2) an affine simply-laced Dynkin diagram, via the tensor structure of the
group's irreducible representations (the McKay quiver). Under it:

- the binary tetrahedral group 2T corresponds to **E6** — *not* E8;
- the lattice **E8** corresponds to the binary **icosahedral** group (order
  120) — *not* to 2T.

**Our construction is none of that.** We do not build a McKay quiver, we do not
read off a Dynkin diagram from representation theory, and we never send 2T to a
root system through irreducibles. Our route to E8 is **glue-forcing**: two
copies of the D4 lattice (the 24-cell's lattice), paired by the unique
even self-dual glue that the mirror admits, with a triality automorphism as the
received datum. It passes through the 24-cell / 2T at the *lattice* level, not
through 2T's representation category, and it lands on E8 by even-unimodular
uniqueness, not by any A-D-E dictionary. The two constructions share the symbols
"2T" and "E8" and nothing of their mechanism. Where McKay would pair 2T with E6,
our chain pairs *two 24-cells* with E8; where McKay would reach E8 from the
order-120 icosahedral group, we reach it from D4 + D4 + triality. **They are
different constructions with overlapping vocabulary.** No result in this chapter
is a restatement, a special case, or a corollary of the McKay correspondence.

**A second note, on the E8 of physics.** E8 also appears as the K-matrix of the
Kitaev-type E8 state — the chiral topological phase with 8 chiral bosons, no
gapless edge modes protected by symmetry, thermal Hall conductance 8 in the
appropriate units (Kitaev 2006; Plamadeala–Mulligan–Nayak and related). That is
the *same lattice* playing a *different role*: there E8 is the anyon-free chiral
phase's edge structure; here E8 is the terminus of a derivation chain from a
graded essential class. Our claim is about the **derivation chain**, not about
E8's physical relevance — we make no assertion that the finite-contact E8 *is*
the Kitaev E8 state, and we register no divergence in this area. The lattice is
famous enough to appear in several unrelated places; we are one of them, and we
say which one.

## 6. One forward pointer: the chromatic frame (Chapter 67 owns it)

One observation belongs on the record here but is developed only in the
synthesis chapter. The group derived in §2, 2T = Q8 ⋊ C3, is — per the
literature on the Morava stabilizer group at the prime 2 (Hewett 1995; Bujard
2012; Beaudry, Bobkova, Goerss, Henn and collaborators) — the **maximal finite
subgroup of the strict height-2 Morava stabilizer group at p = 2.** We state
this as a *cited observation*, not a result: the same finite group that the
essential class forces as the receiver is the one chromatic homotopy theory
identifies at strict height 2. The extended (Galois) stabilizer has a maximal
finite subgroup of order 48 rather than 24 — and the alignment with our own
chirality gate, which separates the 24 (received) from the 48 (F4, both
chiralities), is worth flagging: strict-vs-Galois-extended on their side, 24-vs-48
on ours. We label that alignment an **observation** and hand the analysis to
Chapter 67, which carries the chromatic frame at CITED/CONJ throughout.

## Corrections and honest limits carried

- The i-dressing result of §1.4 is a THEOREM *in the model* (δg = 2ω4 mod 4,
  verified). The claim that this is the physical reason amplitudes are complex is
  an EXTENSION, registered and fenced — not shown here.
- The "faceless" language is ours; the mathematical object is a standard
  **essential class** (Adem–Karagueuzian; Green). We use their term alongside
  ours to avoid coining. The HKR character-theoretic check of ω4 is **OPEN** — we
  have not run it.
- The 24-cell = 2T = Hurwitz units identification, the F4 root system, D4 glue
  theory, and the E8 uniqueness are **RECOVERY** — classical, cited (Coxeter,
  Conway–Smith, Conway–Sloane, Nikulin). Only the *forcing sequence* driven from
  the essential class, with the received datum named at each gate, carries the
  program's priority label — and that label is scoped, per the blind review, to
  "we are not aware of prior work assembling this sequence," never to the
  constituents.
- No divergence from established physics is claimed in this chapter. The chain is
  a RECOVERY of famous mathematical structure from a deeper starting point, plus
  three enumerated RECEIVED forks. Recovering E8 from the essential class is the
  result; the McKay firewall (§5) is there so the recovery is not mistaken for a
  restatement of a different one.

All counts above — 256 rules / 0 reproductions; the μ4 flattening; Q8 = 8;
2T = 24 with exact minimality; 35 glues / 6 even / 6 graphs / 240 roots each;
E8's 240 = 24 + 24 + 64 + 128 — are re-derived exactly, with no floating point,
by `verify_65_e8.py`. The script exits nonzero if a single count is off, and its
falsifiability note lists precisely which facts would break the chain.
