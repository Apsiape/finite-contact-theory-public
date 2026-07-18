# Chapter 30 — Where i Lives

**Release:** v0.22.0 · **Status:** the spectral home of the native complex number, located by exact certificates. All checks exact,
exhaustive, or Sturm-certified, in one shipped dependency-free
verifier (`verification/scripts/where_i_lives.py`).

Per the blind sweep, absorbed in full: the exceptional-point
mechanism is classical (Kato; the stochastic/Liouvillian EP
literature; re-entrant PT windows — Bender lineage — all cited);
the 2-lift spectrum decomposition is Bilu–Linial, nonsplitness is
Zaslavsky's balance theory, and the frustrated sector's gap is the
known signed-graph phenomenon (Belardo; Martin;
Bandeira–Singer–Spielman) — cited as recovery, with gap sizes
reported, not claimed. The Z4 machinery is gain-graph and
covering-character theory (Reff; Mizuno–Sato; Diaconis), the
real-vs-complex sector dichotomy follows Frobenius–Schur
representation-type logic, and the conjugate-pair staging is
Galois conjugacy — automatic, cited. The artifacts: the
Sturm-certified window structure; the certified all-real sign
sector INSIDE the base's certified complex windows (a sign carries
mass but cannot rotate); and the certified non-real quarter-turn
sectors at the reversible point — complex structure enters through
the representation. Measured args (~pi/2) are kernel-inherited,
stated as such.

---

## 1. No phase without arrow: the reversible point's flow matrix is exactly symmetric; its spectrum is real (Sturm: 13/13 real roots).

## 2. The certified windows: exact Sturm certificates — 0, 2, 4 complex roots at beta = +1, −1, −4 (n=6); 2, 0 at beta = −2, +3 (n=5). Complex pairs live in windows bounded by real-eigenvalue collisions; a positive-side window near beta ≈ 3.5 is reported (irrational weights, not certified).

## 3. The sign cover: nonsplit (connected double cover) with the known frustration gap; Sturm-certified ALL-REAL at beta = 0, −1, −4, −2 — including inside the base's certified complex windows.

## 4. The quarter-turn sectors ring at equilibrium: charge-1/3 characteristic polynomials are exactly non-real in Gaussian rationals on both sectors, while charge-0/2 are real — the Frobenius–Schur-type dichotomy realized spectrally.

---

## Scope, received inputs, and open items

Everything above is a finite theorem, an exhaustive computation, or
an exact certificate at the stated sector scopes (n ≤ 6 worlds;
the C4/C5/C6 closures; the four named test worlds). Nature is not
claimed to realize any of it. Frozen bets that died are scored in
print inside the verifier's own output. The open items are named
in the release ceiling.

## Verification

Run `python verification/scripts/where_i_lives.py` from a clean clone
(no dependencies). The frozen copy and its expected output ship in
this chapter's `verification/` directory. Claim rows: FCT-139, FCT-140, FCT-141 in
`docs/public-claim-register.md`.
