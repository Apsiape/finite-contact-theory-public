# Chapter 23 — claim snapshot (as of the v0.20.0 release tag)

Four claim-register rows; live view in
[`docs/public-claim-register.md`](../../docs/public-claim-register.md).

## FCT-112 — The Rational Decay Spectrum

- Status: `THEOREM / MODEL-SCOPE` (mechanism = recovery: triangular
  stochastic matrices and Lyapunov-graded chains — Kemeny–Snell
  1960, Miclo 2021 cited; the closed form and the
  quantization-by-grading reading are the claims)
- Statement: no temporal cycles (recurrence = fixed points, all 34
  five-mark classes); the class-transition operator is triangular in
  the tolerance grading; the spectrum is the diagonal of laziness
  fractions with closed form [C(a,2)+C(b,2)+C(u,2)]/[C(n,2)−ab],
  reproducing the full measured wounded-K6 spectrum.
- Evidence: shipped — `decay_of_worlds.py` sections 1–2.

## FCT-113 — The Urn Identification

- Status: `THEOREM / MODEL-SCOPE` (all quantitative laws are
  classical urn output — Eggenberger–Pólya 1923, Johnson–Kotz 1977
  cited; the sweep located no prior for the IDENTIFICATION of a
  rewrite system's decay sector as an exact urn, inverting the
  growth-side representations of Berger–Borgs–Chayes–Saberi 2014)
- Statement: the wounded clique's reachable classes are exactly the
  W(a,b,u) family; spends recruit at a/(a+b) — the Eggenberger–Pólya
  urn from (1,1); uniform fission profile, branching 2/(n−1) and
  1/(n−1), healthy law 2(s−1)/((n−1)(n−2)), certain separation;
  exact lifetimes 479/72, 809/90, 459/40 (n = 6, 7, 8).
- Evidence: shipped — `decay_of_worlds.py` sections 7–9 (wound's
  law, urn equivalence, urn spectrum).

## FCT-114 — The Self-Location Split

- Status: `THEOREM / MODEL-SCOPE / RECOVERY` (the Sebens–Carroll
  self-locating-uncertainty position and its standard critique —
  Sebens–Carroll 2018, Elga 2004, Kent 2010 cited — recovered as an
  exact finite theorem; the exact split is the contribution)
- Statement: for any line-conserving dynamics, self-location is
  mass-weighted by linearity of expectation (stated as trivial;
  verified on an asymmetric world); given ANY branch weighting,
  self-location has zero residual freedom (no self-location key)
  while the weighting itself is free.
- Evidence: shipped — `decay_of_worlds.py` sections 4–6.

## FCT-115 — Fate Laws and Breeding Wounds

- Status: `THEOREM / MODEL-SCOPE` (occupation-rate ergodics and
  single-run non-identifiability = recoveries, cited; the exact
  per-line fate laws, their conservation linkage, 76/495, and the
  octahedron profile law are model-specific exact content; one
  registered arity bound killed by the engine and scored)
- Statement: clock rates {0, 1, 2/3, 1/2, 2/5} identify fate;
  wound-adjacent lines draw fates uniformly, healthy lines
  size-biasedly (linked by conservation); two disjoint wounds
  produce 3-fission at 76/495 (oppositions are minted — wounds
  breed); the octahedron sector: (3,3) at 4/5, (2,2,2) at 1/5, no
  isolation.
- Evidence: shipped — `decay_of_worlds.py` sections 3, 10.
