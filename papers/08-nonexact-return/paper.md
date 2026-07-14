# Chapter 8 — The Non-Exact-Return Reconstruction: Finite Born Valuation and Contextuality from a Retained Contact Interface

**Release:** v0.8.0 · **Status of the chapter:** a finite model-scope
reconstruction on a real-quantum cell. Every load-bearing statement is
exact and machine-checked from a clean clone; every generalization beyond
the stated scope is held open by name.

---

## The live release ceiling

This chapter carries the program's live ceiling, quoted identically in the
README, the claim register, and the v0.8.0 release notes:

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
> Gleason theorem) exactly where a global noncontextual assignment is
> impossible (a triality Kochen-Specker obstruction) — under which the
> quantum boundary is a floor theorem at binary-Bell finite-carrier scope,
> the preparation gap is an exact theorem at KCBS-pentagon scope, the
> interface reconstruction is a finite model-scope recovery on a
> real-quantum cell, and every unearned generalization — complex quantum
> mechanics, the actuality of one outcome, the universal Born rule, and
> every nature-facing prediction — is left open by name.

---

## 0. What this chapter adds, and what it does not

The earlier chapters grew quantum *structure* from a finite one-use floor
along two lines: a quantum-facing axis (counting, gluing, rational Born
weights, the CHSH/Pell boundary, a native carrier grammar, an exact
preparation gap) and a finite-epistemics axis (the debt and inquiry
calculi, four theorems separating time, a measured generative floor).
This chapter opens a third line and follows it to a single finite object.

The line is short. A finite contact that remains *consequential* cannot
let a second use quietly become a non-use; it retains a return that its
visible configuration has already completed. Call this **non-exact
return**. Read minimally, non-exact return supplies three retained
quarter-turns, and from nothing more than "these are the retained
comparison directions of one cell" a chain of forced closures follows:

1. the primitive receiver is the **quaternions** `H` (minimal, unique);
2. its unit-state orbit is the **24-cell**, whose polar dual is again a
   24-cell — an exact self-hosting state/receiver fixed point;
3. the combined 48 vectors are the **F_4 root system**;
4. every state/receiver contact has the same dimensionless overlap `1/2`;
5. the finite family of measurement contexts **forces the quadratic Born
   frame rule** (a finite Gleason theorem), with no continuum and no
   continuity assumption; and
6. the same finite family admits **no global noncontextual outcome
   assignment** — a Kochen-Specker obstruction that is irreducibly
   three-way (D_4 triality), and that lives entirely at the
   state/receiver interface.

The result is one finite theorem-pair: **the valuation is uniquely
lawful exactly where a global pointing is impossible.** Probability here
is not ignorance about a hidden global assignment; the quadratic
valuation exists precisely where such an assignment cannot.

**The scope, stated up front and enforced throughout.** The receiver is
real: the operators are real-symmetric on `R^4`, a *real-quantum* cell.
This chapter does **not** derive complex quantum mechanics, the actuality
of any single outcome, or the universal Born rule; and it makes no
nature-facing claim. The objects it lands on — the Hurwitz units and the
24-cell, the F_4 root system, Gleason's theorem in finite real form, the
Peres 24-ray Kochen-Specker set and its Kernaghan-type nine-basis parity
proofs — are known mathematics. They are **recovered here in a
derivational role**, as forced closures of a retained contact interface
rather than as posited apparatus. That recovery, and the reading that
Born valuation and contextuality are the two faces of one finite
closure, is the chapter's content; the objects themselves are not
claimed as new.

---

## 1. Setup: non-exact return and the retained cell

A one-use contact leaves a difference. When that difference stays
consequential, a second, order-reversing use of the *same* comparison
direction cannot return the cell to where a first use left it: the cell
retains a sign of its own return. Three such retained directions,
composed, satisfy the relations of the quaternion imaginary units — each
squares to the retained central return `z` (represented on the receiver
as `-1`), and any two anticommute. The minimal real carrier faithful on
`z` is four-dimensional. (The finite chirality analysis that isolates
this retained lift, and the sense in which the projective sign is a
capability of a four-mark ternary contact rather than a compulsion, is
program context cited from the private corpus; this chapter takes the
three retained quarter-turns as its starting datum and proceeds
entirely by exact finite checks from there.)

Write the three quarter-turns as the left-multiplications `I, J, K`. The
verification script confirms `I^2 = J^2 = K^2 = -1` and `IJ = K = -JI`
exactly.

---

## 2. The receiver is the quaternions (Section 1 of the script)

**Claim (MODEL-SCOPE / RECOVERY).** The minimal real receiver faithful on
the retained return is `H`, four-dimensional and irreducible, with a
unique invariant positive form.

Faithfulness on `z` rules out real dimensions one and two (a
one-dimensional real representation sends every square to a positive
number and can never represent `z = -1`; the two-dimensional real
representation has Frobenius–Schur indicator `-1`, i.e. quaternionic
type, so it is not real-orthogonally a sum of the required kind). The
four-dimensional carrier exists, and its commutant inside the real
`4×4` matrices is exactly `H` — a real division algebra — so the
representation has no proper invariant subspace and is minimal. The
space of symmetric forms `G` with `M^T G M = G` for `M ∈ {I,J,K}` is
one-dimensional, spanned by the identity: the invariant positive
evaluation is forced to the isotropic quadratic
`N(ψ) = c(x_0^2 + x_1^2 + x_2^2 + x_3^2)`, with the scale `c > 0` free
and the quadratic exponent and isotropy fixed.

The carrier therefore arrives with a forced **1+3** split: one
return-even identity direction and three mutually noncommuting
quarter-turn directions. This is an algebra grading, not a metric; it is
not spacetime, and nothing in this chapter treats it as such.

---

## 3. The 24-cell and the self-hosting state/receiver fixed point (Section 2)

**Claim (MODEL-SCOPE / RECOVERY).** The unit states form the 24-cell, and
its polar dual is again a 24-cell — an exact fixed point of the
state → receiver → state map.

The unit-norm states generated by the retained structure are the 24
**Hurwitz units**: `±e_i` (eight) and `½(±1,±1,±1,±1)` (sixteen). These
are the vertices of the regular 24-cell. Enumerate every extremal
positive linear question that separates this state polytope — its polar
dual — by exhaustively solving all `C(24,4) = 10626` supporting
constraint quadruples in exact arithmetic. The vertices of the dual are
the 24 vectors `±e_i ± e_j`: another 24-cell (the receiver pole). Taking
the polar again returns the original states exactly.

States generate their receivers, and receivers regenerate their states.
This is the self-hosting **state/receiver fixed point** that the
program's earlier reception analysis sought — realized here on one finite
object, with the fixed-point identity checked by exhaustive polar
enumeration rather than asserted.

---

## 4. The F_4 root system (Section 3)

**Claim (RECOVERY).** The 48 combined state and receiver vectors are the
F_4 root system; its reflection group has order 1152.

The 24 state vectors and 24 receiver vectors together are reflection-
closed and have integer Cartan pairings — they are exactly the 48 roots
of `F_4` (24 short, 24 long). The four simple reflections generate a
group of order `1152 = |W(F_4)|`, checked by direct generation. The
exceptional root system is not installed as a symmetry; it is the
**reflection closure of the state/receiver polarity**. (The two-floor
extension of this closure — where two such cells glue along their
triality boundary into the `E_8` root system — is the subject of the
next chapter and is not claimed here.)

---

## 5. The first forced scale-free magnitude (Section 4)

**Claim (MODEL-SCOPE).** Every nonzero state/receiver contact has
`|⟨p,r⟩|^2 / (|p|^2 |r|^2) = 1/2`.

Across all `24 × 24` state/receiver pairs, every nonzero overlap
`|⟨p,r⟩|` equals exactly `1`; with `|p|^2 = 1` and `|r|^2 = 2` the
dimensionless contact ratio is exactly `1/2` — a `π/4` contact angle.
This is a forced, scale-free, gauge-free interface invariant: the first
nontrivial *magnitude* the closure generates. It is a **ratio**, which is
the only kind of magnitude the program's scale-free structure can force,
and its scope is exactly this 24-cell closure — not nature.

---

## 6. Finite Gleason: the Born frame rule is forced (Section 5)

**Claim (THEOREM at model scope / RECOVERY of Gleason's theorem).** On the
24 rays, every normalized frame valuation is `f(x) = tr(ρ P_x)` for a
unique real-symmetric trace-one `ρ`.

The 24 rays (twelve state lines, twelve receiver lines — the Peres
24-ray configuration) carry exactly 24 orthonormal tetrad **contexts**.
The context-incidence matrix has rank 15, so normalized frame
valuations — assignments giving `1` in total to each context — form a
`24 − 15 = 9`-dimensional affine family. Real-symmetric trace-one
operators on `R^4` also form a nine-dimensional family; the 24 ray
projectors span all ten dimensions of `Sym(4,R)`, and every context is
an exact resolution of the identity. The two nine-dimensional families
therefore coincide, and the map `ρ ↦ (x ↦ tr(ρ P_x))` is a bijection
onto the frame valuations.

So the **quadratic Born frame rule is forced by the finite context
family alone** — a finite, exact form of Gleason's theorem, requiring
neither a continuum of rays nor any continuity assumption. What Gleason's
theorem obtains in infinite dimension from continuity, the finite
contact closure obtains here from the exact combinatorics of one
24-ray configuration.

---

## 7. Triality contextuality: probability where pointing cannot be (Section 6)

**Claim (THEOREM at model scope / RECOVERY of Kochen-Specker).** The same
24 rays admit no global deterministic noncontextual outcome assignment;
the obstruction is irreducibly three-way and lives at the interface.

A deterministic noncontextual assignment would give each ray a value in
`{0,1}` summing to `1` on every context. An exhaustive search shows none
exists. More sharply: there are exactly **16 minimal nine-context parity
proofs** of the obstruction — the Kernaghan-type proofs of the Peres set
— and every one of them lies entirely in the **state/receiver
("mixed")** contexts, using three contexts from each of the three `D_4`
triality sectors. Restrict to any one sector, or any two, and a global
assignment exists; only all three sectors together are obstructed. The
same statement, from the other side: the state pole alone is not
contextual, and the receiver pole alone is not contextual — contextuality
is *generated* when the two poles are forced to share one global
assignment, and it is irreducibly three-way.

Placing Sections 6 and 7 side by side gives the chapter's one sentence:

> **The valuation is uniquely lawful exactly where a global pointing is
> impossible.** The quadratic Born rule exists precisely on the finite
> configuration where a global noncontextual assignment does not. Born
> valuation and Kochen-Specker contextuality are not two separate quantum
> ingredients here; they are the positive and negative faces of one
> finite state/receiver closure.

---

## 8. Scope, fences, and what is held open

- **Real-quantum scope.** Operators are real-symmetric on `R^4`. Complex
  quantum mechanics is *not* derived; the projective phase that would
  complexify the cell is program context and is held open. The
  `1+3` split is an algebra grading, **not** a spacetime metric.
- **No actuality, no universal Born rule.** The chapter derives the
  frame rule (the shape of admissible valuations) and the impossibility
  of a global pointing. It does **not** derive the actuality of any
  single outcome, nor the universal Born rule for general measurements;
  the triality theorem is exactly the statement that the actual outcome
  must be contextual, history-bearing, explicitly received, or replaced
  by totalization — the program's standing open hinge.
- **Recoveries, named.** The Hurwitz units / 24-cell, `F_4`, Gleason's
  theorem, and the Peres/Kernaghan Kochen-Specker structure are known
  mathematics, recovered here in a derivational role. The novelty claim
  is only the *composition* — that a retained contact interface forces
  this exact object, and that Born and contextuality are its two faces —
  and it is graded accordingly in the claim register.
- **Held open by name.** Complex quantum mechanics; the actuality/update
  law (whether a matched non-Born occurrence kernel survives on this
  object is a registered next question); the two-floor `E_8` extension
  and the multi-floor structure (next chapters); and every nature-facing
  prediction.

Everything above is verified end to end by
`verification/nonexact_return_reconstruction.py` from a clean clone, in
a few seconds, in exact arithmetic. The claim-register rows this chapter
rests on are frozen in [`claims.md`](claims.md); the freeze record is in
[`RELEASE.md`](RELEASE.md).
