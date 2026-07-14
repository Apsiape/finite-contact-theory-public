# Chapter 9 — Claims Snapshot (as of the v0.9.0 tag)

The exact claim-register rows this chapter rests on. The live view is
[`../../docs/public-claim-register.md`](../../docs/public-claim-register.md).
All rows are `shipped`. Two dependency-free scripts verify them from a clean
clone, exactly and exhaustively, in a fraction of a second:
`verification/multifloor_worldweave.py` (the closure atlas, FCT-51..56) and
`verification/forcing_audit.py` (the forcing audit, FCT-57..59).

---

## FCT-51 — The Triality Boundary and the Bridge-Code Model

Status: `MODEL-SCOPE / SCHEMA`
Scope: the boundary of a single non-exact-return cell and the additive
glue-code model of multi-cell binding.
Evidence: `shipped` (Section 1).

Each cell carries a `D_4` triality boundary `K = C_2 × C_2` (with `S_3`
triality on `{v,s,c}`); a bridge ecology is an additive glue code
`H ≤ K^N`, with bridge debt `2N − 2·dim H`. Operational receiver-
completeness is a separating dual pole `H ⊊ H^⊥` (not self-duality);
self-duality `H = H^⊥` is the terminal class an equivariant dynamics can
force (FCT-58), and it does not pick a member (FCT-57). Fence: a structural
model under named closure assumptions; not a claim that nature runs this
code; do not read "completeness" as "self-duality".

## FCT-52 — E_8 as the Unique Debt-Free Two-Cell Closure

Status: `MODEL-SCOPE / RECOVERY`
Scope: the bridge geometry of two cells.
Evidence: `shipped` (Section 2).

The two cells' triality boundaries close into the `E_8` root system:
`240 = 48 (D_4⊕D_4) + 3×64` triality-matched bridges, reflection-closed,
with the glue-lattice determinant ladder `16 → 4 → 1` (debt `4→2→0` bits).
`E_8` is the unique debt-free two-cell world — the complete bridge geometry,
**not** an installed physical gauge group. Recovery: the `E_8` root system.

## FCT-53 — Octonionic Fusion; a Three-Contact Receipt

Status: `RECOVERY`
Scope: the local fusion algebra of two quaternionic cells.
Evidence: `shipped` (Section 3).

Fusing two quaternionic receivers gives the octonions `O = H ⊕ Hℓ`; of the
35 imaginary-unit triples exactly 7 associate and 28 do not, so
nonassociativity is a pure three-contact order receipt — every pair looks
quaternionic while the triple retains information belonging to no pair.
Recovery: the octonions and the Fano-line structure.

## FCT-54 — Normed Fusion Stops at the Octonions

Status: `RECOVERY`
Scope: the Cayley–Dickson tower above the octonions.
Evidence: `shipped` (Section 4).

The sedenions have zero divisors ((e₁+e₁₀)(e₄−e₁₅)=0, both factors nonzero)
while the octonions have none, so positive normed monolithic fusion
terminates at `O`; larger populations cannot be one division algebra and
must remain a code worldweave. Recovery: sedenion zero divisors (the
specific indices are Cayley–Dickson-convention-dependent; existence is the
structural point).

## FCT-55 — Self-Dual Worlds are the Unitary Orbit GU(k,2)

Status: `MODEL-SCOPE / RECOVERY`
Scope: triality-covariant Hermitian self-dual standard-form codes on `N`
cells.
Evidence: `shipped` (Section 5).

The self-dual code census is `|GU(N/2, 2)|`: `3` for `N=2`, `18` for `N=4`,
`648` for `N=6` — the exhaustive standard-form search confirmed by the
finite-unitary-group closed form. Recovery: `GU(k, 2)`.

## FCT-56 — Six Cells: the First Hidden World (the Hexacode)

Status: `MODEL-SCOPE / RECOVERY`
Scope: the minimum-distance structure of six-cell self-dual codes.
Evidence: `shipped` (Section 6).

Of the `648` self-dual six-cell codes, `162` have minimum distance 2 and
`486` have minimum distance 4; the distance-four phases (canonically the
hexacode `[6,3,4]`, weight enumerator `1 + 45y⁴ + 18y⁶`, Hermitian
self-dual) have no one-, two-, or three-cell bridge words, so a complete
six-cell world can be invisible to every pairwise and triple probe. `N=6`
is the first such hidden collective world. Recovery: the hexacode.
Residual: whether nature realizes any code, and any metric/spectrum/constant,
are held open.

## FCT-57 — Static Forcing Audit: The Closure Laws Are Not Forced

Status: `THEOREM / MODEL-SCOPE`
Scope: the five receiver laws behind the E_8–hexacode spine.
Evidence: `shipped` (forcing_audit.py, Section A).

Each closure law has a matched lawful counterworld: a doubly-even self-dual
[24,12,4] code (Golay's parity is extra, not forced; A_4=6 code constructed
+ MacWilliams-verified); the bridge family det (1−t²)⁴ (positive at
irrational √2/2, indefinite at 2); both V₄ and C₃ as export quotients; a
dual pole H ⊊ H^⊥ with the self-dual codes an S₃ orbit; and E_8³ with 720
roots. Recoveries: Pless–Sloane, MacWilliams, Leech rootlessness.

## FCT-58 — Dynamic Selection Equivalence: Selection Is A Conserved Input

Status: `THEOREM / MODEL-SCOPE`
Scope: deterministic-settling and reversible-stochastic dynamics on a finite
phase set (the floor's gradient-on-a-potential dynamics is inside it).
Evidence: `shipped` (forcing_audit.py, Section B).

Unique strict dynamic selection ⟺ a preferred scalar ranking: exactly 64 of
256 maps on four phases strictly settle (the rooted-tree count n^{n−1}),
each Lyapunov; reversible dynamics has π ∝ e^{−V}. Dynamics relocates a
conserved selector, never creates one (two potentials → integral vs
irrational attractor; λ* = 2 − log₂3). Positive: self-duality forceable as a
terminal class, but its S₃-transitive members get uniform 1/3.

## FCT-59 — Actualization By Counting: The Internal Law Of An Actual Phase

Status: `THEOREM / MODEL-SCOPE / RECOVERY`
Scope: the internal statistics of a given (actual) code phase.
Evidence: `shipped` (forcing_audit.py, Section C).

Given an actual phase, the internal law is forced by witness counting: the
24-cell response kernel K=(1/3)|⟨p,q⟩|² (values {0,1/12,1/3}, row-stochastic,
trace 4, rank 10 = dim Sym(4,ℝ)) — the Born response with no primitive state
vector; and the first visible global binding arity equals the dual distance
(uniform marginals below it; hexacode 4, [24,12,4] 4, Golay 8). Which phase
exists is received; how it distributes futures is forced. Recovers Delsarte.
