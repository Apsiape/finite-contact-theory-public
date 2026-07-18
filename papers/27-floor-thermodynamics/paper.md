# Chapter 27 — The Thermodynamics of the Floor

**Release:** v0.22.0 · **Status:** the genesis dynamics' statistical mechanics, from counting alone. All checks exact,
exhaustive, or Sturm-certified, in one shipped dependency-free
verifier (`verification/scripts/floor_thermodynamics.py`).

Per the blind sweep, absorbed in full: the mechanisms here are
recoveries of standard stochastic-thermodynamics structure and are
cited as such — symmetric/doubly-stochastic stationarity
(Levin–Peres–Wilmer), surprisal-as-energy (Jaynes; Landauer), the
Cauchy-functional-equation route to exponential rate laws
(Arrhenius; Kramers), min-cost-over-mean stationary selection
(Freidlin–Wentzell; Catoni; Olivieri–Vares; Landauer's blowtorch
theorem), entropy production and cycle currents (Schnakenberg;
Hill; Seifert; Zia–Schmittmann). The chapter's own artifacts are
the exact finite objects: the 3660 = 61 × 60 state count behind
the sector's 1/61 ensemble, the exact free-move split (a frozen
mean-cost bet died here and is scored), the measured unimodal
dissipation profile (a frozen monotone bet died and is scored),
and the synthesis itself — the full Boltzmann/Arrhenius/
Schnakenberg apparatus realized in a counting-only substrate with
no imposed energy function.

---

## 1. The kernel symmetry and the microcanonical state count: the stationary law is uniform on labeled worlds; pi = orbit/3660; the 1/61 is a state count.

## 2. Detailed balance holds at the price-blind point only: beta = 0 is the unique reversible member of the rate family tested; the cycle's weight is strictly decreasing in beta; the anti-coupled chain protects the sparse class.

## 3. The Boltzmann identity (definitional, cited) and the forced form: cost is exactly additive over disjoint components, so price-only independent rate laws are exponential — form forced, temperature received.

## 4. The free-move law: redistribution is sorted exactly by possession of a certainty contact, not by mean cost; the self-retention lemma is exact (Cauchy–Schwarz).

## 5. Dissipation and the cost-pump: entropy production is zero exactly at equilibrium, measured unimodal across the sampled grid; the steady current is a divergence-free cycle through unequal costs.

---

## Scope, received inputs, and open items

Everything above is a finite theorem, an exhaustive computation, or
an exact certificate at the stated sector scopes (n ≤ 6 worlds;
the C4/C5/C6 closures; the four named test worlds). Nature is not
claimed to realize any of it. Frozen bets that died are scored in
print inside the verifier's own output. The open items are named
in the release ceiling.

## Verification

Run `python verification/scripts/floor_thermodynamics.py` from a clean clone
(no dependencies). The frozen copy and its expected output ship in
this chapter's `verification/` directory. Claim rows: FCT-128, FCT-129, FCT-130, FCT-131 in
`docs/public-claim-register.md`.
