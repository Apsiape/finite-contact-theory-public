# Chapter 9 — The Multi-Floor Worldweave: A Forcing Audit of the E_8-Hexacode Spine

**Release:** v0.9.0 · **Status of the chapter:** a positive forcing theorem
with named recoveries. Every finite statement is exact and machine-checked
from a clean clone; every generalization beyond the stated scope is held
open by name.

---

## The live release ceiling

This chapter carries the program's live ceiling, quoted identically in the
README, the claim register, and the v0.9.0 release notes:

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack on three published lines — a quantum-facing axis, from
> one-use contact to counting, one-receiver gluing, rational Born weights,
> the CHSH/Pell boundary, a carrier grammar grown from one-use contact, and
> a behavior-conditioned contextual capacity with an exact strict
> preparation gap; a finite-epistemics axis, from the identifiability and
> debt calculus to the inquiry calculus and its second law of asking, four
> theorems separating the structure of time, and a measured generative
> floor; and a contact-interface reconstruction, in which a retained
> interface forces a quaternionic state/receiver cell whose self-dual
> closure is the 24-cell and the F_4 root system and whose finite
> measurement calculus forces the quadratic Born frame rule (a finite
> Gleason theorem) exactly where a triality Kochen-Specker obstruction
> forbids a global noncontextual assignment, and in which independently
> generated cells recover the E_8–hexacode closure spine under named
> positive, integral, triality-covariant, self-dual, and delocalizing
> receiver laws while a forcing audit proves those laws are not selected by
> the floor over matched lawful alternatives — so the floor forces the atlas
> of lawful closures and the terminal self-dual class but never the specific
> member, and the selection of a world-phase is a conserved, received input
> — under which the quantum boundary is a floor theorem at binary-Bell
> finite-carrier scope, the preparation gap is an exact theorem at
> KCBS-pentagon scope, the interface reconstruction is a finite model-scope
> recovery on a real-quantum cell, the multi-floor closures are model-scope
> recoveries whose forcing boundary is exactly mapped, and every unearned
> generalization — complex quantum mechanics, the actuality of one outcome,
> the universal Born rule, whether nature realizes any of these structures,
> which world-phase is selected, and every nature-facing prediction — is
> left open by name.

---

## 0. What this chapter proves

Chapter 8 closed a single non-exact-return cell. This chapter asks how
independently generated cells become one world — and answers it as a
**forcing audit**, the program's signature move: it maps exactly what the
finite-contact closure does and does not force.

The answer has a positive and a negative half, and the negative half is a
theorem, not a hedge:

> **The floor forces the atlas of lawful closures and the terminal
> self-dual class, but never the specific member.** Under named positive,
> integral, triality-covariant, self-dual, and delocalizing receiver laws,
> the multi-cell closure problem recovers the `E_8`–hexacode spine (§1). But
> those five laws are **not** selected by the floor over matched lawful
> alternatives — not statically (§2, counterworlds) and not dynamically
> (§3, a selection-equivalence theorem). Selection of a world-phase is a
> **conserved, received input**: making the dynamics richer only relocates
> the selector into a potential or rate law; it never creates one.

There is a clean complement (§4): the floor cannot select *which* phase
exists, but *given* an actual phase it forces the phase's internal law —
the Born response and the interaction arity — by counting terminal
witnesses, with no primitive state vector and no added Born postulate. So
the division is sharp: **which world-phase is received historical
actuality; how an actual phase distributes its futures is forced.**

Everything below is exact and machine-checked
(`verification/multifloor_worldweave.py` for §1;
`verification/forcing_audit.py` for §§2–4). The named objects — the `E_8`
root system, the octonions, the hexacode, the classification of doubly-even
self-dual `[24,12]` codes, the MacWilliams identity, Lyapunov / detailed
balance, and Delsarte's dual-distance bound — are known mathematics,
recovered here in a derivational role.

## 1. The closure atlas (the recovered spine)

Each non-exact-return cell carries a `D_4` triality boundary
`K = C_2 × C_2` (with `S_3` triality on `{v,s,c}`); for `N` cells the
boundary space is `K^N`, a bridge ecology is an additive glue code
`H ≤ K^N`, and — **under the named receiver laws** — the debt-free and
receiver-complete closures recover a specific spine
(`verification/multifloor_worldweave.py`):

- **Two cells → `E_8`.** The triality boundaries close into the `E_8` root
  system: `240 = 48 (D_4 ⊕ D_4) + 3 × 64` triality-matched bridges,
  reflection-closed, with the glue-lattice determinant ladder
  `16 → 4 → 1` (debt `4 → 2 → 0` bits). `E_8` is the unique debt-free
  two-cell closure — the complete bridge geometry, **not** an installed
  physical gauge group.
- **Local fusion is octonionic.** Fusing two quaternionic receivers gives
  `O = H ⊕ Hℓ`; of the 35 imaginary-unit triples exactly 7 associate and
  28 do not, so nonassociativity is a pure three-contact order receipt.
- **Fusion stops at `O`.** The sedenions have zero divisors; normed
  monolithic fusion cannot continue, so a population is code-like, not one
  algebra.
- **Self-dual worlds and the hexacode.** The triality-covariant Hermitian
  self-dual standard-form census is `|GU(N/2, 2)| = 3, 18, 648` through six
  cells; at six cells `486` of the `648` codes reach minimum distance four,
  canonically the hexacode `[6,3,4]` — the first population that can be one
  world invisible to every pairwise and triple probe.

This is the atlas. It is a genuine recovery of a rigid mathematical spine
from the contact closure problem. The rest of the chapter asks the question
the program always asks next: **is that spine forced, or received?**

## 2. Forcing audit, static: the closure laws are not forced

Each of the five receiver laws that produce §1 has a **matched lawful
counterworld** — a floor-legal alternative the closure problem does not
rank below the spine (`verification/forcing_audit.py`, Section A):

- **Golay is not forced.** A matched "local-kernel" binary refinement of the
  *same* hexacode, six cells, and four ports yields a doubly-even self-dual
  `[24,12,4]` code with weight enumerator `1 + 6y⁴ + 735y⁸ + 2612y¹² +
  735y¹⁶ + 6y²⁰ + y²⁴` — its six weight-four words are exactly the six local
  port receipts. The script exhibits this code explicitly (found by an
  exhaustive port-map search), verifies it is MacWilliams-self-dual and
  doubly-even, and confirms an independent `[24,12,4]` witness. Golay's
  parity condition is an **extra, delocalizing** law, not a forced one.
  (Recovery: the Pless–Sloane classification — exactly nine doubly-even
  self-dual `[24,12]` codes, Golay the unique `d = 8`.)
- **Positivity, integrality, and magnitude are not forced.** The bridge
  family `G_t = [[I₄, tI₄],[tI₄, I₄]]` has determinant `(1 − t²)⁴`: it is
  positive-definite for `|t| < 1` (including the *irrational* `t = √2/2`),
  indefinite for `|t| > 1` (e.g. `t = 2`), and degenerate only at `t = 1`.
  No-silent-loss singles out none of positivity, integrality, or a magnitude
  — the scale-free ceiling, from the multi-floor side.
- **The triality alphabet is not unique.** Both `Q₈/{±1} ≅ V₄` and
  `2T/Q₈ ≅ C₃` are valid export quotients; the floor does not rank `V₄` as
  the unique inter-floor alphabet.
- **Self-duality is not implied by completeness.** An *operationally*
  complete receiver is a **separating dual pole** `H ⊊ H^⊥` (verified: the
  isotropic seed over `GF(4)` has `|H| = 4` strictly inside `|H^⊥| = 64`),
  not a self-dual code. Self-duality `H = H^⊥` is an extra condition, and it
  still does not pick a member: the two-cell self-dual codes are three, in a
  single `S_3` orbit.
- **Rootlessness is separate.** `E_8 ⊕ E_8 ⊕ E_8` is positive, integral,
  even, and unimodular in 24 dimensions, yet has 720 roots. The Leech
  lattice's rootlessness is an additional minimum-norm law, not implied by
  even-unimodular completion.

## 3. Forcing audit, dynamic: making the floor dynamic does not rescue forcing

A natural rescue is to let a dynamics *settle* onto the spine. It cannot
create a selector — it can only **relocate a conserved one**
(`verification/forcing_audit.py`, Section B):

> **Selection equivalence.** Unique strict dynamic selection is equivalent
> to a preferred scalar ranking.

The certificate: of the `256` deterministic maps on four phases, exactly
`64` strictly settle to a single terminal phase — the rooted-tree count
`4³ = n^{n−1}` — and *every one* carries a Lyapunov ranking
`V(F(x)) = V(x) − 1`. For reversible stochastic dynamics, detailed balance
gives the stationary law `π ∝ e^{−V}`, i.e. `V = −log π`. So the dynamics
does not create the selector; it encodes the conserved one in a potential
/ transition kernel / rate law. The same bridge family, under two passive
potentials `V₀(t) = t²` and `V_irr(t) = (t² − ½)²`, settles onto an
integral versus an irrational attractor; the `V₄`-vs-`C₃` scalarization
crossover sits at `λ* = 2 − log₂ 3 = 0.4150375…`. (Scope of the theorem,
stated honestly: it covers deterministic-settling and reversible-stochastic
dynamics; the floor's own gradient-descent-on-a-potential dynamics is inside
that class.)

**The one positive.** Self-duality *can* be forced — but only as a terminal
**class** (`H = H^⊥` is a well-defined attractor set), never as a specific
**member**: the three two-cell self-dual codes form one `S_3` orbit, so a
target-blind equivariant dynamics can only assign the uniform `1/3` to each.
The class is forced; the member is received.

## 4. Actualization by counting: the internal law of an actual phase is forced

The floor cannot select which phase exists. But *given* an actual phase, it
forces the phase's internal law by counting terminal witnesses
(`verification/forcing_audit.py`, Section C) — the positive complement:

- **Born by counting.** On the 24-cell, the response kernel counted from
  terminal witnesses is `K = (1/3)|⟨p,q⟩|²`, with values `{0, 1/12, 1/3}`,
  row-stochastic, trace 4, and rank `10 = dim Sym(4,ℝ)`. The quadratic Born
  response is *counted*, with no primitive state vector and no added Born
  postulate — the multi-floor echo of Chapter 8's finite Gleason theorem.
- **Correlation arity.** For an actual linear-code phase with dual distance
  `d_⊥`, every marginal on `≤ d_⊥ − 1` coordinates is exactly uniform, so
  the first visible global binding arity is `d_⊥` (verified: hexacode
  `d_⊥ = 4`, uniform through three floors and breaking at four; the matched
  `[24,12,4]` counterworld `d_⊥ = 4`; Golay `d_⊥ = 8`). A population can
  possess exact global binding while every lower-arity observer sees maximum
  local randomness. (Recovery: Delsarte — dual distance = orthogonal-array
  strength `+ 1`.)

So: **which world-phase exists is received historical actuality; how an
actual phase distributes its futures is forced by witness counting.**

## 5. The reframed statement, scope, and what is held open

**The honest-replacement statement.** *Under positive, integral,
triality-covariant, self-dual, and delocalizing receiver laws, the
finite-contact closure problems recover the `E_8`–hexacode(–Golay–Leech)
spine. The floor has not selected those laws over matched lawful
alternatives.* What the floor forces is the **atlas** of lawful closures,
the terminal self-dual **class**, and — given an actual phase — its internal
**statistics**. What it does not force, statically or dynamically, is the
**member**; that is a conserved, received input.

**On "receiver-complete."** Do not read any statement as "completeness
forces self-duality." Operational receiver-completeness is a separating dual
pole `H ⊊ H^⊥` (§2). Self-duality is the terminal class an equivariant
dynamics can force (§3), never a specific self-dual code.

**Recoveries, named.** The `E_8` root system, the octonions, the hexacode,
the doubly-even self-dual `[24,12]` classification (Pless–Sloane), the
MacWilliams identity, the rooted-tree count and Lyapunov / detailed-balance
theory, and Delsarte's bound are known mathematics, recovered in a
derivational role; the novelty is the *composition* and the *forcing
boundary*, graded in the claim register.

**Held open by name.** Which world-phase is selected (received actuality);
whether nature realizes `E_8`, the hexacode, or any code; a metric,
spectrum, or dimensionful constant (none is derived); and the hinges
inherited from Chapter 8 (complex quantum mechanics, the actuality of one
outcome, the universal Born rule).

The claim-register rows this chapter rests on are frozen in
[`claims.md`](claims.md); the freeze record is in [`RELEASE.md`](RELEASE.md).
