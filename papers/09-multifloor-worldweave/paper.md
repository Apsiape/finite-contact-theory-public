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

There is a clean complement (§4), and it is careful about exactly how much
counting buys. The floor cannot select *which* phase exists; *given* an
actual phase, counting forces the **form** of that phase's internal law — a
one-parameter positive equivariant weight family and its sequential
composition, plus the interaction arity — but it does **not** force the Born
rule. Born is one point of that family (equal tickets), and equal-tickets is
an *added magnitude law*: precisely the relocated selector §3 guarantees. The
retained `Z₂` sign scar then upgrades counting to a genuine real amplitude
calculus (interference is restored), and two independent ingredients remain
received: the equal-ticket magnitude law and the enlargement to a complex
phase. So the division is sharp, with the actualization layer itself split:
**which world-phase exists is received; the *form* of an actual phase's
statistics is forced by counting; its Born *magnitude* and complex *phase*
are received.**

Everything below is exact and machine-checked
(`verification/multifloor_worldweave.py` for §1;
`verification/forcing_audit.py` for §§2–4; `verification/wcd_actualization.py`
for the §4 counting family, decoherence, and sign-scar amplitude calculus).
The named objects — the `E_8` root system, the octonions, the hexacode, the
classification of doubly-even self-dual `[24,12]` codes, the MacWilliams
identity, Lyapunov / detailed balance, Delsarte's dual-distance bound,
mutually-unbiased bases, and the count of order-4 Hadamard matrices — are
known mathematics, recovered here in a derivational role.

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
dynamics — the class that includes the floor's own
gradient-descent-on-a-potential dynamics. Genuinely **irreversible,
non-detailed-balance driven dynamics is out of scope and held open**: since
the program treats the floor as driven-dissipative, this is a real edge.
Driven dynamics still carries an entropy-production / burden functional —
itself a ranking — so the conserved-selector reading is *expected* to
extend, but that extension is not proved here.)

**The one positive.** Self-duality *can* be forced — but only as a terminal
**class** (`H = H^⊥` is a well-defined attractor set), never as a specific
**member**: the three two-cell self-dual codes form one `S_3` orbit, so a
target-blind equivariant dynamics can only assign the uniform `1/3` to each.
The class is forced; the member is received.

## 4. Actualization by counting: the *form* is forced, the Born rule is not

The floor cannot select which phase exists. *Given* an actual phase, counting
terminal witnesses forces the **form** of its internal law — but an earlier
version of this chapter overreached here, and the correction makes the result
sharper. Counting does **not** force the Born rule; it forces a
one-parameter family of which Born is one point
(`verification/wcd_actualization.py`; the equal-ticket point also appears as
Section C of `verification/forcing_audit.py`).

- **Counting forces the form, not Born.** The 24-cell response geometry is
  12 rays in three orthonormal frames, so the `144 = 12 × 12` ordered
  (source, target) histories split into `48` *return* (same-frame) and `96`
  *transfer* (cross-frame). The most general positive equivariant weight is a
  single ticket `α` on return and `β` on transfer, times the incidence
  `|⟨p,q⟩|²`. This is a lawful stochastic response for **every** `α, β > 0`,
  with closed form `P(p→p) = α/(α+2β)`, `P(cross) = β/(4α+8β)`, and
  `P(orthogonal) = 0`. The Born kernel `K = (1/3)|⟨p,q⟩|²` with values
  `{0, 1/12, 1/3}` occurs **only** at equal tickets `α = β` (algebraically,
  `P(p→p) = 1/3 ⟺ α = β`; e.g. `(α,β) = (2,1)` gives identity weight `1/2`).
  So counting forces the equivariant **form** and sequential composition;
  **equal-tickets is an added magnitude law** — exactly the conserved,
  relocated selector §3 predicts, now appearing at the actualization layer.
  There is no primitive state vector, but there *is* an added Born postulate,
  and naming it is the honest result.
- **Positive counting is decohered; the sign scar restores interference.**
  Positive additive counting sums *probabilities*, so it can never produce
  interference: the minimal two-path witness has coherent
  `|½ + (−½)|² = 0` against decohered `¼ + ¼ = ½`, and across all `576`
  two-path configurations on the three frames the positive value differs from
  the coherent `|Σ amplitude|²` in every case — the destructive `0` is
  unreachable by counting. The retained `Z₂` sign scar (`z → −z`) supplies a
  sign alphabet `{+1,−1}`, under which the three frames are **three real
  mutually-unbiased bases**: their transition matrices have entries `±½` and
  compose exactly as a cocycle `U_ut · U_ts = U_us`, with the `768` real
  order-4 Hadamard matrices as the sign supply. Amplitudes now *add* and
  `P = |A|²` is applied after — genuine real coherent interference. (Recovery:
  real MUBs; the Hadamard count.)
- **Correlation arity, at the uniform-ticket measure.** Under the equal-ticket
  (`α = β`) measure, for an actual linear-code phase with dual distance
  `d_⊥`, every marginal on `≤ d_⊥ − 1` coordinates is exactly uniform, so the
  first visible global binding arity is `d_⊥` (verified: hexacode `d_⊥ = 4`,
  uniform through three floors and breaking at four; the matched `[24,12,4]`
  counterworld `d_⊥ = 4`; Golay `d_⊥ = 8`, cited). A population can possess
  exact global binding while every lower-arity observer sees maximum local
  randomness. (Recovery: Delsarte — dual distance = orthogonal-array strength
  `+ 1`.)

**Two gaps remain, held open and independent** (`wcd_actualization.py`,
Section 5): (a) the **magnitude law** `α = β` is not forced — asymmetric
tickets `(2,1)` and `(1,2)` are equally lawful phases; and (b) the
**complex phase** — the binary sign scar reaches only `|1 ± 1|² ∈ {0, 4}`,
so the quantum value `|1 + i|² = 2` is a separate added ingredient.

So the actualization division is itself layered: **which world-phase exists
is received; the *form* of an actual phase's statistics is forced by counting;
its Born *magnitude* (`α = β`) and its complex *phase* are received.**

## 5. The reframed statement, scope, and what is held open

**The honest-replacement statement.** *Under positive, integral,
triality-covariant, self-dual, and delocalizing receiver laws, the
finite-contact closure problems recover the `E_8`–hexacode(–Golay–Leech)
spine. The floor has not selected those laws over matched lawful
alternatives.* What the floor forces is the **atlas** of lawful closures,
the terminal self-dual **class**, and — given an actual phase — the **form**
of its internal statistics (a one-parameter equivariant counting family, with
a real amplitude calculus from the sign scar). What it does not force,
statically or dynamically, is the **member**; nor, at the actualization
layer, the Born **magnitude** (`α = β`) or the complex **phase**. Those are
conserved, received inputs.

**On "receiver-complete."** Do not read any statement as "completeness
forces self-duality." Operational receiver-completeness is a separating dual
pole `H ⊊ H^⊥` (§2). Self-duality is the terminal class an equivariant
dynamics can force (§3), never a specific self-dual code.

**Recoveries, named.** The `E_8` root system, the octonions, the hexacode,
the doubly-even self-dual `[24,12]` classification (Pless–Sloane), the
MacWilliams identity, the rooted-tree count and Lyapunov / detailed-balance
theory, Delsarte's bound, real mutually-unbiased bases, and the count of
order-4 Hadamard matrices are known mathematics, recovered in a derivational
role; the novelty is the *composition* and the *forcing boundary*, graded in
the claim register. The Born-measure underdetermination (form fixed, measure
free) is the same phenomenon Gleason's theorem exhibits.

**Held open by name.** Which world-phase is selected (received actuality);
whether nature realizes `E_8`, the hexacode, or any code; a metric,
spectrum, or dimensionful constant (none is derived); the Born **magnitude**
law (`α = β`) and the **complex phase**, both received at the actualization
layer; and the hinges inherited from Chapter 8 (complex quantum mechanics,
the actuality of one outcome, the universal Born rule).

The claim-register rows this chapter rests on are frozen in
[`claims.md`](claims.md); the freeze record is in [`RELEASE.md`](RELEASE.md).
