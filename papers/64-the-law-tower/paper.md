# Chapter 64 — The Law Tower: Two Sectors, One Generator, Doubly Sourced

*Finite Contact Theory. This chapter is an accounting exercise that turned into
a structure theorem. Our worlds write a graded charge at every arity — a sign
recording whether an all-odd fork closed with a twist — and we set out only to
catalogue those charges rung by rung. What the catalogue turned out to be is
the polynomial ring on a single generator: every charge and every law the
program has named is a power of the one elementary distinction, and the parity
of the power decides whether it is an appearance or a law. On that ring sits an
exact operator calculus — staging and receipt as a characteristic-two Weyl pair
— whose law sector admits four coinciding descriptions. The honest headline is
that essentially every constituent is textbook: the cohomology of the
two-element group, the Bockstein, the Weyl algebra in characteristic two, the
two-adic valuation of the Catalan numbers, the Witt vectors of the two-element
field. We claim none as new, and cite them by name at every step. What is ours
is the assembly — that these particular classical objects are the exact
skeleton of a floor built from a one-use discipline, and that they lock into one
picture in which every law is generated twice over: as the carry of the
appearance below it and the shadow of the appearance above it. We call that the
double-generation pincer, label it an expository unification, and prove each arm
with the shipped script. Nothing here forces a physical divergence; the one
place a divergence could live is named at the end and handed to a later
chapter.*

## A note on altitude, first

Read the labels before the results, because here the labels are most of the
honesty. Every exact statement in this chapter carries one of two tags.
**THEOREM (model scope)** means the claim is a proven fact about the specific
finite object the floor stages — the group cohomology of `Z2`, the polynomial
ring `F2[x]`, the operator pair on it — verified by the shipped script
`verify_64_tower.py`, and nothing more; it is a fact about our model, not a
claim about nature. **RECOVERY** means the object is a known piece of
mathematics that we reconstruct on the floor and attribute to its literature;
recovering it is the win, and pretending it were new would be the fraud. A few
assemblies of recovered parts get a third tag, **expository unification**,
which says exactly this: the pieces are all classical, the packaging is ours,
and the packaging is the only thing we are putting forward.

What we hoped for going in was that the graded charge would be *several*
independent objects — a distinct new invariant at each arity, so the higher
rungs would be genuinely new mathematics. That hope is retired, in print, at
the top: the whole tower is one generator's powers (§3). The compensation is
larger than the loss. A one-generator ring with a parity grading, carrying an
exact Weyl calculus whose law sector is at once a kernel, an image, a Frobenius
image, and an algebra centre, and whose every law is both a Bockstein carry from
below and a formal-derivative shadow from above, is a tighter and more forced
object than a pile of unrelated invariants would have been. We did not design
the coincidences; we found them and checked them.

One term needs stating up front. Throughout we use our house word **faceless**
for a cohomology class that is trivial on every proper face yet nontrivial
globally. The standard name for exactly this notion is an **essential class**,
and the study of essential cohomology is due to Adem and Karagueuzian, and to
Green (Adem–Karagueuzian, *J. Group Theory* 2001; D. J. Green, essential
cohomology of p-groups). We use both words and mean the standard one. Whether
the essential/faceless classes of our tower are detected by the Hochschild–
Kostant–Rosenberg / generalized character theory of the group is a question we
have **not** settled; it is marked **OPEN** and not used below.

## 1. The two-sector theorem

Fix the smallest arena where a genuine higher law can appear: the `n = 4`
world — four participants, the tetrahedron of their pairings and faces. Two
kinds of object live there, and the first result is that they are exactly two,
complementary, with nothing in between.

### 1.1 The exact sector: pair-identity gluing

Give each of the four triangular faces a triadic charge, and each edge a
receipt. The gluing curvature of the tetrahedron — the twist you accumulate
carrying the pair-identity data around the closed figure — is, by direct
enumeration of **all 4096** assignments of the twelve context-indexed pair
orientations, *identically* the product of the face charges:

    Pi_glue  =  product over edges  =  product over faces   (4096 / 4096).

This is the tetrahedral identity, and it is exact: the gluing curvature is the
**coboundary** of the face charges, `Pi_glue = (delta chi)`. Everything you
can build from pair-identity receipts lands in this **exact sector**, and it is
completely determined by the four triadic face charges. The immediate corollary
is the one that matters: **there is no assignment with all four faces even and
`Pi_glue = -1`.** A faceless — essential — pentagon *cannot* be manufactured
from pair-identity gluing. Every object this mechanism produces wears its faces
on the outside.

### 1.2 The non-exact sector: the essential class

There is a second object at `n = 4`, and it is precisely what the first
mechanism cannot reach. The class

    omega_4(a,b,c,d) = (-1)^{abcd}

is trivial on every proper face — set any one of `a,b,c,d` to the identity and
it is constant — yet it is **not** the coboundary of any normalized 3-cochain.
It is the standard nonzero generator of `H^4(Z2; Z2)`, an essential class in
the sense of §0, and it is the exact-support object at `n = 4`: reachable from
no rung-3 data whatsoever. This is a completely classical fact about the
cohomology of the two-element group, and we flag it as **RECOVERY**; the
generator, the ring it lives in, and its non-coboundary status are textbook.

The two sectors are complementary and disjoint. The exact sector is
`Pi_glue = delta chi`, buildable from faces, never faceless. The non-exact
sector is the essential `omega_4`, faceless by construction, unbuildable from
faces. **THE TWO-SECTOR THEOREM (model scope):** the `n = 4` world splits into
the exact sector (pair-identity gluing, fixed by the four triadic face charges)
and the non-exact sector (the essential `H^4(Z2;Z2)` class), and no assignment
of pair-identity receipts crosses between them. Its two ingredients — the
4096-assignment gluing identity and the non-coboundary of `omega_4` — are the
standard generator and a finite enumeration.

The non-exact sector carries the standard reading of a higher associativity
anomaly. An essential degree-four class of this kind is exactly the obstruction
datum of fusion-category / tensor-category coherence theory (Etingof, Nikshych,
and Ostrik, *Tensor Categories*, and the associativity obstruction of their
obstruction theory), and it is the object a physicist reads as an 't Hooft
anomaly for a `Z2` symmetry (Kapustin and Thorngren, on anomalies of discrete
symmetries and cobordism). We import that reading as **RECOVERY** — the class
is theirs, the interpretation is theirs — and note only that our floor produces
the same class from a one-use gluing discipline rather than from a chosen tensor
category.

## 2. The half-eraser: the top-cell lemma

Why does adjoining `i` to the coefficients — passing from the two-element sign
group to the fourth roots of unity — kill some rungs of this tower and not
others? The answer is one lemma about where a coboundary can land, and it is
exact at every rung.

A normalized `(n-1)`-cochain `L` on `Z2` has exactly **one** free value: it
vanishes whenever any argument is the identity, so it is determined by its value
`lambda` on the all-ones cell. Evaluate its coboundary on the top cell of
degree `n` — the all-ones `n`-tuple. Every middle term of the bar differential
merges two adjacent ones into a zero and is killed by normalization; only the
first and last terms survive, giving

    (delta L)(1,...,1)  =  lambda * (1 + (-1)^n).

**THE TOP-CELL LEMMA (THEOREM, model scope; verified rungs 2–6 by the shipped
script):** `1 + (-1)^n` is `2` for even `n` and `0` for odd `n`. Read off both
coefficient systems:

- **Over the sign group (mod 2):** `1 + (-1)^n ≡ 0` for *every* `n`. Nothing in
  any two-element-valued cochain can ever hit a top cell. So no rung is a
  coboundary mod 2 — every `omega_n` is nontrivial, at every arity.
- **Adjoin `i` (mod 4):** the top-cell coboundary is `2 lambda` for even `n`,
  and `lambda = 1` supplies exactly the value `2` that trivializes the
  even-rung class; for odd `n` it is still `0`, untouchable. So **adjoining `i`
  erases exactly the even rungs and cannot touch the odd ones.**

This is the half-eraser: complexification is an arity-parity-selective eraser,
and the lemma says precisely which half it erases and why — the even rungs
because their top cell is reachable by half a step once the coefficients admit
`i`, the odd rungs never, in *any* coefficient system, because their top cell
is unreachable identically. The shipped script enumerates the normalized
coboundaries at rungs 2–5 over both mod 2 and mod 4 and confirms the pattern
cell by cell. That `H^n(Z2; U(1))` is `Z2` for odd `n` and `0` for even `n` is
the classical fact underneath (**RECOVERY**); the top-cell lemma is our exact,
constructive account of *which* half and *why*.

## 3. The ring: one generator, graded by parity

Now the catalogue collapses. Compute the cup products of the rungs — every
one enumerated and checked by the shipped script — and they satisfy

    x cup x = x^2,   x^3 cup x = x^4,   x^3 cup x^3 = x^6,
    x^2 cup x^2 = x^4,   x cup x^4 = x^5,

with no relations beyond the free polynomial ones. **The tower is `F2[x]`, the
polynomial ring on a single generator** — the classical cohomology ring
`H*(Z2; Z2) = F2[x]` (**RECOVERY**; this is one of the first computations in
any group-cohomology course). The content we add is the identification of what
each power *is* in the program's own vocabulary:

- `x` — the elementary distinction (the one mark event; "identity is an
  event," the root of the whole program);
- `x^2` — the mirror, the first grammar/law class;
- `x^3` — the triadic charge `chi`;
- `x^4` — the pentagonator, the essential `n = 4` law of §1.

The parity of the exponent is the superalgebra grading, and it is the whole
appearance-versus-law distinction: **odd powers are appearances, even powers
are laws.** Two consequences are worth stating because the program had named
them separately before seeing they were the same fact. First, `x^4 = x^3 cup x`
— the essential law is the triadic appearance composed with one elementary
distinction; strip the `x` and you expose `chi`. Second, multiplication by the
single generator `x` is exactly the parity shift, so the operation that casts a
law from an appearance and an appearance from a law is one and the same — the
grading flip — and it is generated by the one distinction. That reality's
appearances and its laws are the parity-graded powers of a single generator is
the chapter's sharpest compression, and it is a compression of *recovered*
structure: we are not claiming `F2[x]` as new, we are claiming that this
particular floor's charge tower *is* it, on the nose.

## 4. The calculus: staging, receipt, and the law sector four ways

The ring has an operator calculus, and it is where the recovered pieces start
locking together. On `F2[x]` put

    U = staging   = multiply by x,
    D = receipt   = the formal derivative (characteristic two).

### 4.1 The characteristic-two Weyl relation

On every monomial, `D(x^k) = k x^{k-1}` and the two orders of composition sum
to the identity:

    D U + U D = 1        (THEOREM, model scope; verified deg 0–12).

This is the Weyl / canonical-commutation relation read in characteristic two —
where `[D, U] = 1` becomes `DU + UD = 1` because `-1 = 1` — and it is the exact
skeleton of the staging/receipt duality: staging then receipting, plus
receipting then staging, is the identity, so no information is created or
destroyed by the pair, only shifted in grade. The relation is classical
(**RECOVERY**); its identification with staging and receipt on the floor is the
model content.

### 4.2 Three coinciding descriptions of the law sector

The receipt operator `D` has a kernel and an image, and on `F2[x]` they
coincide with each other and with a third object:

    ker D  =  im D  =  im Frobenius  =  F2[x^2]  =  the law sector
    (THEOREM, model scope; verified deg 0–12).

A law is, simultaneously and provably: (i) **invariant under receipt** — a
fixed point of elementary distinction-variation, `D`-closed; (ii) a **shadow**
— the receipt of some higher appearance, in `im D`; and (iii) a **square** —
in the image of the Frobenius `x ↦ x^2`. The three characterizations of "even
degree" are not restatements of one definition; they are three genuinely
different operators whose relevant sets happen to be equal, and the shipped
script computes all three independently and checks the coincidence. Because
`ker D = im D`, the vertical receipt complex is **contractible**: it has no
homology, hence no absolute basement — every law is the receipt of something,
so no law is unsourced from above. The witness of contractibility is exact:

    x^4 = D(x^5)        (THEOREM, model scope; the vertical exactness of §5).

The essential `n = 4` law, unbuildable from its faces (§1), is nonetheless the
receipt of the rung-5 appearance. Horizontally faceless, vertically exact: the
Two-Sector Theorem gets its missing direction here.

### 4.3 The p = 2 uniqueness

The triple coincidence is a characteristic-two accident, and that is a feature.
Over `F3`, `ker D` (degrees divisible by 3) and `im D` (a different set of
degrees) do **not** coincide — the shipped script exhibits the mismatch. The
self-casting calculus in which every law is exactly a receipted appearance
exists at the prime **two alone**. This is the cleanest structural reason the
program has for the binariness of distinction: two is the only prime at which
the kernel and image of the receipt operator are the same object.

### 4.4 The operator centre (RECOVERY)

Write `A = F2[x]` as `B ⊕ xB` over `B = F2[x^2]`. There `U` and `D` are
explicit two-by-two matrices over `B`, the algebra they generate is the full
matrix algebra `M_2(B) = M_2(F2[x^2])`, and its **centre is exactly `B` — the
law sector**. A fourth description thus joins the three above: the law sector is
`ker D = im D = im Frobenius = Z(⟨U, D⟩)`, the centre of the whole operational
algebra, with the appearance sector `xB` its module. That a Weyl algebra in
characteristic `p` is Azumaya over its centre, the centre generated by `p`-th
powers (here squares), is the classical Frobenius-descent picture: we label the
operator-centre statement **RECOVERY** and cite Revoy (*Algèbres de Weyl en
caractéristique p*, C. R. Acad. Sci. Paris 1973) and the Azumaya/centre analysis
of Bezrukavnikov, Mirković, and Rumynin (localization in positive
characteristic). The recursion `B ≅ A` gives the tower
`M_2 → M_4 → M_8 → …` — `M_{2^k}` over the `k`-fold squares — whose centres
intersect in `F2`: **no global centre**, no law absolutely a law; refine deeply
enough and every law becomes an operator. Standard Frobenius descent, imported
and labelled as such.

## 5. The Bockstein carry theorem: laws are doubly sourced

The vertical calculus of §4 sources every law *from above*, as the receipt `D`
of the appearance one rung up. There is a second, independent generation of the
same laws *from below*, and identifying the two is the chapter's centrepiece.

### 5.1 The carry of the differential is the Bockstein

Signs enter one arithmetic layer up, at mod 4, where the mod-2 tower lifts as
two-torsion cocycles. Define the **carry of the differential** — the amount by
which the signed mod-4 coboundary of a lifted cochain overshoots the lift of
its mod-2 coboundary, divided by two:

    kappa(f) = ( delta_signed(lift f) - lift(delta_2 f) ) / 2   (mod 2).

Computed exactly on the group cochains of `Z2` — lift each mod-2 value to
`{0,1}`, take the signed coboundary over the integers, subtract the lift of the
mod-2 coboundary, halve, reduce — this operator is well defined (the difference
is always even; the shipped script checks divisibility at every cell) and it is
the classical **Bockstein** associated to `0 → Z2 → Z4 → Z2 → 0`. That the
Bockstein `beta` is textbook — the connecting homomorphism of the coefficient
sequence, equal to `Sq^1` on `H*(Z2;Z2)`, with `beta(x^n) = n x^{n+1}` — is
**RECOVERY**: Steenrod and Epstein, *Cohomology Operations*; Mosher and
Tangora, *Cohomology Operations and Applications in Homotopy Theory*. On the
tower, verified by the shipped script for `n = 1..6`:

    beta(x^n) = x^{n+1}  for odd n,     beta(x^n) = 0  for even n.

### 5.2 The pincer

Put the two generations side by side. From above, the vertical calculus of §4:
`x^{2k} = D(x^{2k+1})` — every law is the **receipt-shadow of the appearance
above it.** From below, the Bockstein carry: `beta(x^{2k-1}) = x^{2k}` — every
law is the **carry of the appearance below it.** The first law of the program,
the mirror `x^2`, is literally the carry of the elementary distinction:
`beta(x) = x^2` says two identical distinctions cancel at sign-resolution two
and deposit the mirror one grade up — "one plus one is zero here, and a law
upstairs." So:

> **THE DOUBLE-GENERATION PINCER.** Every law (even rung) is generated twice
> over — as the Bockstein carry of the appearance below it and as the receipt
> shadow of the appearance above it. The tower zips itself together from both
> directions; no law is unsourced.

We label the pincer an **expository unification**, and we mean the label
strictly. Every constituent is classical and separately recovered: the
Bockstein (Steenrod–Epstein), the formal-derivative / Weyl calculus (§4,
Revoy), the ring `F2[x]`. On this one-generator tower the two operators are even
related by the compact identity `beta = x^2 · D` (multiply the receipt by the
mirror and you get the carry), which is a one-line consequence of
`beta(x^n) = n x^{n+1}` and `D(x^n) = n x^{n-1}` — an observation, not a new
theorem. The blind review of this chapter flagged, correctly, that no
individual piece of the pincer is novel and that the packaging is the whole
contribution; we adopt that verdict as the label. What the packaging buys is a
statement that two independent readings the program reached separately — "laws
are carries" and "laws descend from above" — are the two arms of a single
operator identity.

### 5.3 The mirror three ways (folklore-unification)

The mirror `x^2` admits, beyond the two of the pincer, a third classical
identity that we record as a **folklore-unification**: every piece is standard,
the coincidence is the note.

- As the **extension class of `Z/4`**: the non-split extension
  `0 → Z2 → Z4 → Z2 → 0` has factor set `f(a,b) = a b` (the carry of binary
  addition), and this factor set is a genuine noncoboundary — the shipped
  script enumerates the two normalized 1-cochains and confirms neither
  coboundary equals it. The mirror is the obstruction to splitting `Z/4`.
- As the **first Witt carry polynomial**: the ring of length-two Witt vectors
  of the two-element field is `W_2(F2) = Z/4`, with addition
  `(a0,a1) + (b0,b1) = (a0 + b0, a1 + b1 + a0 b0)`. The carry polynomial in the
  second slot is exactly `a0 b0` — the same `ab`. The shipped script verifies
  that this Witt addition reproduces `Z/4` on all sixteen pairs. This is
  classical (**RECOVERY**): Serre, *Local Fields*, and Hazewinkel, *Formal
  Groups and Applications*, on Witt vectors.

So the mirror is at once the first law of the tower, the Bockstein carry of the
distinction, the extension class of `Z/4`, and the first Witt carry polynomial.
The identification is folklore assembled; the assembly is the note we are
making.

## 6. The carry-depth filtration

The odd/even alternation of §2 is the first two strata of a full filtration,
and naming it correctly closes the chapter.

### 6.1 Carry depth counts the same thing twice

The program has two independent parity mechanisms — a binomial/Hasse ladder and
a Catalan/tree transfer — and they are the **same carry counter**. Exactly:

    nu_2( Catalan(n-1) )  =  s_2(n) - 1
    (THEOREM, model scope; verified n = 2..40 by the shipped script),

where `s_2(n)` is the binary digit sum. This is classical two-adic combinatorics
(**RECOVERY**): the two-adic valuation of the Catalan numbers (Alter and Kubota,
*Prime and prime power divisibility of Catalan numbers*, J. Combin. Theory
1973; Deutsch and Sagan, *Congruences for Catalan and Motzkin numbers*, J.
Number Theory 2006), resting on Kummer's theorem that the valuation of a
binomial counts carries in base-`p` addition (Kummer 1852). The reading we add:
both program mechanisms *measure how many binary carries a composition costs*,
and the odd/even alternation is just their first two layers. The dyadic classes
`x^2, x^4, x^8, x^16, …` (arities with `s_2(n) = 1`) are the **zero-carry
stratum** — each essential/faceless, invisible to every proper contraction —
and the essential `x^4` of §1 is merely the first. Everything else is
stratified by carry depth: depth 0 at `n = 2,4,8,16,…`; depth 1 at
`n = 3,5,6,9,…`; depth 2 at `n = 7,11,13,14`; and so on.

There is a clean geometric gloss, recorded as interpretation over the exact
filtration: an arity is not a quantity but a **simplex of scales**, and carry
depth is its dimension — the six depth-one arities are edges, the four
depth-two arities `7,11,13,14` are the triangular faces of the first
tetrahedron `15` (depth 3). Dimension `d` first becomes visible at
sign-resolution `2^{d+1}`. The triadic charge `chi = x^3` sits at depth 1, a
mod-4 object: visible to complex phase (which has `i ∈ mu_4`) but not to bare
signs — the half-eraser of §2 seen as the depth-0-versus-depth-1 cut.

### 6.2 The mod-4 floor: the lift decides the depth

At mod 4 — the first arithmetic where signs exist — the transferred diagonal
operations depend on which sign resolution the floor takes, and the dependence
acts on the filtration itself. With a bosonic-scalar (`+`) lift the depth-one
stratum is visible at mod 4 (the arity-three operation carries the two-torsion
value); with a fermionic-signed (`−`) lift it is **exactly cancelled**. **The
two-lift fork acts on the carry filtration** (THEOREM-shape, model scope): the
carry-depth ladder of §6.1 is the `+`-lift ladder, and the `−` lift reorganizes
the strata. Which arities are visible is not fixed by the floor; it depends on
the lift. We tag one caveat plainly: the mod-4 value of the arity-four operation
is Merkulov-convention-dependent (it reads `+1` or `−1 ≡ 3` according to the
Koszul sign convention chosen), so we do **not** load-bear on it; the arity-three
cancellation, by contrast, needs only the *relative* sign of two trees, which
any convention fixes, and is convention-free.

### 6.3 The K-anomaly

One last exact fact, recorded because it is the door the program walks through
next. The mixed stage-receipt operator whose flat locus is the certified tower
is a projector at mod 2 but **fails to be a projector at mod 4 by an exact
two-torsion term**: `K^2 - K = 2 · (something)`. The identity-installation
machinery itself has a carry. The witness apparatus is subject to the same
filtration as the objects it witnesses — which is the honest reason we do not
treat the mod-2 projector as the last word.

## 7. What this is for

Nothing in this chapter is a physical claim. Every result above is either a
THEOREM about the finite object the floor stages, a RECOVERY of named classical
mathematics, or an expository packaging of recovered parts. The floor forces the
*structure* of the tower; it forces no charge value to disagree with anything
nature measures, and we register no such disagreement here.

The one place a divergence could lawfully live is the one thing the tower makes
precise: **an object can be exactly zero at one sign-resolution and nonzero one
carry-layer deeper.** The essential dyadic classes are invisible to every proper
face and to every coarser arithmetic; complex quantum theory, which reads at
mod 4 (it has `i`), sees depth at most one and is structurally blind to depth
two and beyond, whose first member is the seven-body closure. Whether nature's
resolution stops where complex theory's does or reads deeper into the same
one-generator tower is the program's registered wager — held at the external
workers' stated confidences, claimed as no divergence, and carried forward. The
mathematics of "exactly zero to one detector class and real to the next" is
built here; the reading that turns it toward experiment, at honest tiers, is the
subject of Chapter 67. We built the tower; we stop at its edge.

## Corrections carried

- **"The higher rungs are independent new invariants."** Retired. The whole
  tower is `F2[x]` on one generator (§3); there is one invariant and its powers.
  This is a compression, not a loss, and it is recovered classical structure.
- **"Complex quantum theory is the eraser of the anomaly tower."** Corrected to
  a *half*-eraser (§2). Adjoining `i` erases exactly the even (law) rungs and
  cannot touch the odd (appearance) rungs; the top-cell lemma says precisely
  which half and why.
- **The mod-4 arity-four sign** is Merkulov-convention-dependent and is **not**
  load-bearing (§6.2). The arity-three cancellation is convention-free and is.
- **The essential/faceless-versus-HKR-character question is OPEN** (§0) and is
  used nowhere below it.

The kill-count is the health metric. One hope retired, one claim corrected, two
fences and one open question stated in print — and what stands is standing on
the shipped script and on named classical theorems, not on hope.

## Sources and citations

- A. Adem and D. Karagueuzian, "Essential cohomology of finite groups," *J.
  Group Theory* (2001); D. J. Green, work on the essential cohomology of
  p-groups — the standard notion behind our word "faceless."
- P. Etingof, D. Nikshych, and V. Ostrik, *Tensor Categories* (AMS, 2015) — the
  associativity obstruction theory reading the essential `H^4` class.
- A. Kapustin and R. Thorngren, on anomalies of discrete symmetries / discrete
  gauge theory and cobordism — the 't Hooft anomaly reading of the same class.
- N. E. Steenrod and D. B. A. Epstein, *Cohomology Operations* (Princeton,
  1962); R. E. Mosher and M. C. Tangora, *Cohomology Operations and
  Applications in Homotopy Theory* (1968) — the Bockstein `beta = Sq^1` and its
  action on `H*(Z2;Z2)`.
- P. Revoy, "Algèbres de Weyl en caractéristique p," *C. R. Acad. Sci. Paris*
  (1973); R. Bezrukavnikov, I. Mirković, D. Rumynin, on localization and Azumaya
  algebras in positive characteristic — the operator-centre / Frobenius-descent
  picture.
- E. Alter and K. K. Kubota, "Prime and prime power divisibility of Catalan
  numbers," *J. Combin. Theory Ser. A* (1973); E. Deutsch and B. E. Sagan,
  "Congruences for Catalan and Motzkin numbers...," *J. Number Theory* (2006);
  E. E. Kummer (1852) — the two-adic valuation of Catalan numbers and the
  carry-counting theorem behind the filtration.
- J.-P. Serre, *Local Fields* (Springer); M. Hazewinkel, *Formal Groups and
  Applications* — Witt vectors and `W_2(F2) = Z/4`.
- All exact statements labelled THEOREM (model scope) are re-derived by the
  shipped `verify_64_tower.py` (stdlib only), which prints per-check PASS/FAIL
  and a falsifiability note.
