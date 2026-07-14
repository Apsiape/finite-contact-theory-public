# Chapter 9 — The Multi-Floor Worldweave: Bridge Codes, the E_8 Closure, and Octonionic Fusion

**Release:** v0.9.0 · **Status of the chapter:** a structural model-scope
result under named closure axioms. Every finite statement is exact and
machine-checked from a clean clone; every generalization beyond the stated
scope is held open by name.

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
> generated cells combine not by tensor product but as a self-dual triality
> bridge code whose unique debt-free two-cell closure is the E_8 root
> system, whose local fusion is octonionic, and whose first hidden six-cell
> world is the hexacode — under which the quantum boundary is a floor
> theorem at binary-Bell finite-carrier scope, the preparation gap is an
> exact theorem at KCBS-pentagon scope, the interface reconstruction is a
> finite model-scope recovery on a real-quantum cell, the multi-floor
> worldweave is a structural model-scope result under named closure axioms,
> and every unearned generalization — complex quantum mechanics, the
> actuality of one outcome, the universal Born rule, whether nature realizes
> any of these structures, and every nature-facing prediction — is left open
> by name.

---

## 0. The question, and the scope

Chapter 8 closed a single non-exact-return cell: its receiver is the
quaternions, its states are the 24-cell, its measurement calculus is the
Born frame rule sitting exactly on a triality Kochen–Specker obstruction.
That chapter deliberately left one thing open by name: **how independently
generated cells become one world.** This chapter answers the structural
version of that question, and the answer is not the expected one.

> **Independently generated cells do not combine by tensor product. Each
> cell carries a D_4 triality boundary; cells become one world by settling
> those boundary debts into a self-dual code.**

The native global object is therefore an **evolving bridge code**, not a
tensor product and not one monolithic state space. Everything below is
exact and machine-checked, but the reading rests on named closure
assumptions (positivity, integral receipt-preserving closure, triality
covariance, self-dual completion); it is a **structural** result at model
scope. It does **not** show that nature realizes `E_8`, the hexacode, or
any particular code, and it derives no metric, spectrum, or dimensionful
constant. What is closed is the structural question.

## 1. The triality boundary (Section 1 of the script)

**Claim (MODEL-SCOPE / RECOVERY).** Each cell's `D_4` triality boundary is
the Klein four-group `K = {0, v, s, c} ≅ C_2 × C_2`, with `S_3` triality
permuting `{v, s, c}`.

The three eight-dimensional representations of `D_4` (vector, spinor,
cospinor) label three boundary sectors; their fusion group is Klein-four,
and the outer `S_3` symmetry permutes the three sectors. For `N` cells the
native boundary space is `K^N`; a bridge ecology is an additive glue code
`H ≤ K^N`; its unresolved bridge debt is `2N − 2·dim_{F_2} H` bits; and a
**receiver-complete world is a self-dual code**, `H = H^⊥`.

## 2. Two cells close uniquely into E_8 (Section 2)

**Claim (MODEL-SCOPE / RECOVERY).** The unique debt-free closure of two
cells is the `E_8` root system.

Two cells contribute `48` internal roots (`D_4 ⊕ D_4`). Their three
triality-matched bridge sectors — `(8v,8v)`, `(8s,8s)`, `(8c,8c)` —
contribute `64` roots each. The verification script confirms exactly:

```
240 roots  =  48 (D_4 + D_4)  +  64 (8v,8v)  +  64 (8s,8s)  +  64 (8c,8c),
```

reflection-closed, and the glue-lattice determinant ladder
`D_4² → D_8 → E_8 = 16 → 4 → 1` (bridge debt `4 → 2 → 0` bits): a single
spinor bridge added to the vector-bridged `D_8` phase catalyzes the rest of
`E_8` under closure. So **`E_8` is the unique debt-free two-cell world** —
the complete bridge geometry of two contact cells, recovered here in a
derivational role. It is emphatically **not** installed as a physical gauge
group, and no such claim is made.

## 3. Local fusion is octonionic (Section 3)

**Claim (RECOVERY).** The local dynamics of a fused cell is octonionic,
and its nonassociativity is a pure three-contact order receipt.

Fusing two quaternionic receivers under a positive multiplicative norm
gives the octonions `O = H ⊕ Hℓ`. The decisive feature is not that
octonions appear but *where* the new receipt lives: any two octonionic
directions generate an associative subalgebra, so the new information is
carried only by **triples**. Of the `C(7,3) = 35` triples of imaginary
units, exactly `7` associate (the Fano lines) and `28` do not. Every pair
looks quaternionic while the triple retains information belonging to no
pair — an exact dynamical realization of collective binding that is
invisible pairwise.

## 4. Fusion stops at the octonions (Section 4)

**Claim (RECOVERY).** Positive normed monolithic fusion terminates at the
octonions; larger populations cannot be one division algebra.

The next Cayley–Dickson doubling is the 16-dimensional sedenions, which
contain zero divisors: the script exhibits `(e₁+e₁₀)(e₄−e₁₅) = 0` with both
factors nonzero, while confirming the octonions have none of this form.
Silent annihilation of consequential distinctions is disallowed without an
external settlement receipt, so a population **cannot** collapse into one
ever-larger normed algebra. It must remain a **worldweave of octonionic
cells**, globally bound by bridge codes — which is exactly why the larger
object is code-like rather than one giant algebra.

## 5. Receiver-complete worlds are a unitary orbit (Section 5)

**Claim (MODEL-SCOPE / RECOVERY).** The triality-covariant Hermitian
self-dual standard-form codes on `N` cells number `|GU(N/2, 2)|`.

An exhaustive search over all standard-form generator matrices gives `3`
self-dual codes for `N = 2`, `18` for `N = 4`, and `648` for `N = 6` —
exactly the orders of the finite unitary groups `GU(k, 2)` for `k = N/2`
(`3, 18, 648`). Receiver-complete worlds are the unitary orbit over
`GF(4)`, and the exhaustive combinatorial search is confirmed by this
closed form.

## 6. Six cells: the first hidden collective world (Section 6)

**Claim (MODEL-SCOPE / RECOVERY).** Six cells are the first population that
can form a complete world invisible to every pairwise and triple probe;
the hexacode is a canonical phase.

The minimum weight of a bridge code is the first visible interaction arity.
Through four cells every self-dual code has minimum distance two (pair
bridges are always exposed). At six cells, of the `648` self-dual codes
exactly `162` have minimum distance two and `486` have minimum distance
four. The distance-four phases have **no one-, two-, or three-cell bridge
words**: their global worldhood is invisible to every pairwise and triple
glue probe. A canonical phase is the **hexacode** `[6, 3, 4]` over `GF(4)`,
with weight enumerator `1 + 45 y⁴ + 18 y⁶`, Hermitian self-dual, whose
`D_4^6` glue lattice is globally self-dual — yet which creates no new
cross-cell roots (its visible root system stays `D_4^6`). So six locally
separate-looking cells can already constitute one complete global world
whose unity lives only in the higher code.

## 7. The dynamic law, and what is held open

At stage `t` reality carries a bridge code `H_t`; hereditary bridge genesis
gives `H_t ⊆ H_{t+1}`. Adding an independent generator lowers determinant
debt; reaching `H = H^⊥` creates a receiver-complete world; exporting a
generator can split a world; codeword support fixes interaction arity; the
weight enumerator is the binding spectrum. That is a **structural** dynamics
of the global object — the code, not a state vector.

**The pattern across the arc.** Within a cell (Chapter 8): non-exact return
generates quantum-like valuation. Between two cells: triality debt closes as
`E_8`. Inside a fusion cell: ordered contact is octonionic. Across a
population: worldhood is a self-dual glue code. The unifying reading is that
the native global object of the theory is an evolving bridge code.

**Held open by name.** Whether nature realizes `E_8`, the hexacode, or any
code; a metric, particle spectrum, or dimensionful constant (none is
derived); the nonlinear/continuum behavior of the code dynamics; and the
open hinges inherited from Chapter 8 (complex quantum mechanics, the
actuality of one outcome, the universal Born rule) and the rest of the
program's horizon.

**Recoveries, named.** The `D_4` triality group, the `E_8` root system, the
octonions and Cayley–Dickson tower, the hexacode, and the unitary groups
`GU(k, 2)` are known mathematics, recovered here in a derivational role; the
novelty claim is the *composition* (cells as triality-boundaried code
generators, worldhood as a self-dual code), graded in the claim register.

Everything above is verified by
`verification/multifloor_worldweave.py` from a clean clone, in a few
seconds, in exact arithmetic. The rows this chapter rests on are frozen in
[`claims.md`](claims.md); the freeze record is in [`RELEASE.md`](RELEASE.md).
