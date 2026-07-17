# Chapter 23 — The Decay of Worlds: The Rational Spectrum, the Urn, the Clock Address, and the Self-Location Theorem

**Release:** v0.20.0 · **Status:** the genesis floor's decay physics,
solved exactly. Thirty checks, all exact or exhaustive, in one
shipped verifier (`verification/scripts/decay_of_worlds.py`). The
live release ceiling is carried by Chapter 24 of this release.

Setting: the genesis floor of Chapter 21 (a contact consumes both
parents and mints two offspring wired to the intersection of the
parents' neighborhoods plus each other; labels persist as LINES).
Crystals (disjoint unions of cliques) are exact fixed points; a
WOUND is one missing tolerance.

---

## 1. The arrow is absolute; the spectrum is rational

Two theorems fix the shape of decay. (i) NO TEMPORAL CYCLES: every
contact either reproduces the world's class (iff the parents are
adjacent twins) or strictly decreases total tolerance — recurrence
is fixed-points-only (exhaustive over all 34 five-mark classes).
(ii) TRIANGULARITY: the class-transition operator is therefore
triangular in the tolerance grading, so its spectrum is the diagonal
of laziness fractions — every decay constant an exact rational, with
the closed form [C(a,2)+C(b,2)+C(u,2)]/[C(n,2)−ab] on the wounded
family. The wounded-K6 sector's full spectrum {1, 1/3, 3/11, 3/7,
4/13, 4/9, 6/11} is reproduced by the formula.

**Classification (per the blind sweep):** the mechanism is classical
— triangular stochastic matrices have their diagonal as spectrum,
and a strict Lyapunov grading forbids cycles (Kemeny–Snell 1960;
Miclo 2021 for monotone chains) — labeled a recovery; the
model-specific closed form and the quantization-by-grading reading
are the chapter's layer.

## 2. The urn (the mechanism, identified)

The wounded clique's reachable classes are EXACTLY a
two-sides-plus-undecided family W(a,b,u): within-side and
within-undecided contacts are lazy; every spend recruits an
undecided mark to a side with probability a/(a+b) — the
**Eggenberger–Pólya urn started (1,1)**, exactly and
class-by-class. Everything follows as textbook urn output: the
fission profile is uniform (the classical uniform limit, verified
by exact recursion to n=60), branching ratios are 2/(n−1)
(asymmetric) and 1/(n−1) (symmetric), the healthy line's
final-home law is the linear size-biased 2(s−1)/((n−1)(n−2)), and
the wound's two lines always separate. Exact sector lifetimes:
479/72, 809/90, 459/40 contacts at n = 6, 7, 8.

**Classification:** the urn and every quantitative law are classical
(Eggenberger–Pólya 1923; Johnson–Kotz 1977) and labeled so. The
sweep's verdict on the one uncatalogued item: the structural
IDENTIFICATION — a graph-rewriting system's *decay* sector as an
exact Pólya urn — inverts the known growth-side urn representations
of graph processes (Berger–Borgs–Chayes–Saberi 2014) and was not
located in the literature; it is presented as a bridge to 1923, not
a divergence.

## 3. The self-location theorem (a boundary, recovered and priced)

For any line-conserving dynamics, P(a uniform-random line ends in a
size-m home) equals the expected mass fraction in size-m components
— linearity of expectation, stated as trivial and verified even on
a fully asymmetric world. The force is the boundary it draws: given
ANY branch weighting, self-location has ZERO residual freedom (a
biased weighting flips the branching ratios and the self-location
law tracks it exactly) — there is no self-location key — while the
branch weighting itself remains free (Chapter 22).

**Classification:** this is the Sebens–Carroll self-locating-
uncertainty position together with its standard critique (Kent;
Dawid–Thébault) — that self-location fixes credence only GIVEN a
measure — recovered as an exact floor theorem (Sebens–Carroll 2018;
Elga 2004; Kent 2010 cited). The chapter's contribution is the
exact finite split, not the dialectic.

## 4. The clock address and the fate laws

The asymptotic participation rates in the fission products (2/m per
line in a size-m home: 0, 1, 2/3, 1/2, 2/5) are all distinct — an
observer-line's own waiting times identify both its fission channel
and its home; isolation reads as silence. A mortal single run
identifies world structure (a clique lifetime is a census) but
provably not a measure (Chapter 22's bound — the sweep confirms
this as the correct sample-complexity logic, cited to the
Everettian single-run debate). The fate laws: wound-adjacent lines
draw their futures uniformly; healthy lines inherit size-biasedly —
and the two laws are conservation-linked (the healthy law is
derived from wounded uniformity, a decomposition stated in the
verifier).

**Classification:** occupation-rate ergodics and one-sample
non-identifiability are standard (Kemeny–Snell; Kent) — recoveries;
the exact per-line fate laws and their conservation linkage are the
chapter's layer.

## 5. Multi-wound worlds: wounds breed

Two disjoint wounds produce THREE-way fission with exact
probability 76/495 — a registered arity bound was killed by this
engine and scored: intersection inheritance MINTS new oppositions
(the sparsification arrow's other face), so fission arity is not
bounded by wound count. The urn is the law of the ISOLATED wound.
The most constrained sector is K6 minus a perfect matching (the
octahedron): five classes, profiles (3,3) at 4/5 and (2,2,2) at
1/5, and no isolation channel at all.

**Classification:** the mechanism (more independent defects open
higher-arity channels, multi-color-urn style) is catalogued
(Athreya–Karlin 1968; Blackwell–MacQueen 1973; Bertoin 2006 for
fragmentation framing — all cited); the exact rationals are
model-specific enumeration.

## 6. Scope

All results exact at stated finite scopes. The reference measure
(uniform contact choice) is a declared convention; Chapter 22's
weight freedom is untouched and re-verified here. Nothing about
nature is claimed; "vacuum," "decay," and "fission" are structural
readings whose physics-facing development is Chapter 24's, under
its own fences.
