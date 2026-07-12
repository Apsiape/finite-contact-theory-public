# Behavior-Conditioned Contextual Capacity and an Exact Strict Preparation Gap

**Finite Contact Theory — Chapter 2 (v0.2 technical note)**

Status: release narrative for the v0.2 chapter. The controlling claim rows are
[`claims.md`](claims.md) (snapshot) and the live
[public claim register](../../docs/public-claim-register.md) (FCT-21 through
FCT-25). The centerpiece certificate ships as a dependency-free script:
[`verification/exact_gap_certificate.py`](verification/exact_gap_certificate.py)
(frozen copy; the live copy runs in the repository suite).

## The release ceiling

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack — from one-use contact to counting, to one-receiver gluing, to
> rational Born weights, to the CHSH/Pell boundary, to a carrier grammar grown
> from one-use contact, to a behavior-conditioned contextual capacity with an
> exact strict preparation gap — under which the quantum boundary is a floor
> theorem at **binary-Bell finite-carrier scope**, the preparation gap is an
> exact theorem at **KCBS-pentagon scope**, and every unearned generalization
> is left open by name.

This chapter is deliberately written in standard quantum-foundations language.
Its mathematics stands or falls inside ordinary contextuality theory; the
finite-contact reading is confined to one section near the end and adds no
load-bearing assumption.

## Abstract

Fix an exclusivity graph `G` with vertex weights `w_i > 0` and a *behavior*
`p = (p_1, ..., p_n)` — the full list of outcome probabilities a quantum model
must reproduce with sharp (projective) measurements obeying the exclusivity
structure. Standard contextuality quantifiers evaluate `p` itself. We study a
different object: the **behavior-conditioned capacity**

```text
kappa_G(p) = inf { || sum_i w_i P_i ||_op : (rho, P) a sharp realization of p }
```

— the smallest operator-norm capacity any sharp quantum model *must* carry in
order to show the behavior `p` — and the **preparation gap**

```text
Delta_prep(p) = kappa_G(p) - beta(p),      beta(p) = sum_i w_i p_i .
```

`beta(p)` is what the preparation actually extracts; `kappa_G(p)` is what the
measurement system must be able to supply. We prove `beta <= kappa` always
(FCT-21/T-14); we reduce `kappa` to a faithful semidefinite program whose
feasible set is the Gram fiber of the behavior, and prove a compression
theorem showing rank-one pure realizations suffice (T-14); we map the tight
set `Delta_prep = 0` and its phase boundary on the pentagon (FCT-24/T-16); we
prove a headroom law — every sharp implementation of a gapped behavior carries
re-extractable capacity at least `Delta_prep` above what the given preparation
uses, so the gap is a receiver-certified *re-preparation resource*
(FCT-23/T-16); and, as the centerpiece, we exhibit a rational pentagon
behavior with a **hand-checkable exact certificate** that *every* sharp
realization in *every* dimension has capacity strictly above `beta`
(FCT-22/T-15). No floating-point number is load-bearing anywhere in the
certificate: realizability is proved by an exact rational LDL factorization,
and impossibility by an exact rational rigidity-plus-witness argument.

Unrestricted (unsharp) POVMs make the gap vanish (`E_i = p_i * I`), so
`Delta_prep` is a *sharpness-conditioned* invariant — it prices what
projective measurement structure must hold in reserve beyond what the
behavior spends (FCT-25 wording; T-14 residuals).

## 1. The object

### 1.1 Scenario

Everything in this chapter lives at the following scope, stated once and
meant: **exclusivity-graph contextuality with sharp measurements; all exact
results on the pentagon `C_5` (the KCBS scenario) with unit weights; the
definitions, the universal inequality, the SDP reduction, and the compression
theorem hold for general finite `G`.**

A *sharp realization* of a behavior `p` on `G = (V, E)` is a state `rho` and
projectors `{P_i}` on some finite-dimensional Hilbert space with

- `Tr(rho P_i) = p_i` for every vertex (the behavior is reproduced exactly);
- `P_i P_j = 0` for every edge `ij` (exclusivity is operational, not
  statistical).

No dimension bound, no rank bound, no purity assumption: the infimum ranges
over the *entire* realization fiber of `p`.

### 1.2 Why capacity

`sum_i w_i P_i` is the total measurement operator of the scenario; its
operator norm is the largest weighted event-mass any single preparation could
extract. `beta(p) = sum_i w_i p_i` is the mass the *given* preparation
extracts. The question `kappa_G(p) = ?` asks: can a quantum model be built
that shows `p` while holding **no more capacity than `p` uses** — or does
showing this behavior force the measurement system to keep a strict reserve?

`Delta_prep(p) > 0` says the reserve is mandatory. The behavior itself —
everything the device's statistics reveal — *underdetermines* the capacity of
the systems that produce it, and the shortfall is quantitatively pinned from
below.

## 2. Theorem stack

Labels are from [`status-labels.md`](../../docs/status-labels.md); each row is
controlled by the claim register.

**T-14a (universal inequality — `THEOREM`, general `G`).**
`beta(p) <= kappa_G(p)` for every behavior with a sharp realization: for any
realization, `beta = Tr(rho * sum w_i P_i) <= ||sum w_i P_i||_op`. One line,
and everything else in the chapter prices the slack in it.

**T-14b (Gram SDP faithfulness — `THEOREM`, general `G`).** For rank-one pure
realizations, with `v = sqrt(p)` entrywise,

```text
kappa^(1)(p) = min { lambda_max(H) : H Hermitian, H_ii = 1,
                     H_ij = 0 for ij in E,  H >= v v^T }
```

and the reduction is *faithful*: any feasible `H` reconstructs an actual
realization by a Schur-complement extension (the bordered Gram matrix
`[[1, v^T], [v, H]]` is PSD, hence realizable by unit vectors plus a state),
and the operator norm of the realization equals `lambda_max` of its Gram
matrix. The feasible set is exactly the Gram fiber of the behavior.

**T-14c (sharp compression — `THEOREM`, general `G`; scope fence).**
`kappa_sharp(p) = kappa^(1)(p)`: purify-and-project (`u_i` proportional to
`P_i Psi`, sub-projectors `Q_i <= P_i`) maps any mixed-state, any-rank sharp
realization to a rank-one pure one, preserving the behavior and the
exclusivity, without increasing capacity. **Fence:** this compression is
specific to this positive weighted-capacity objective; rank matters in other
contextuality quantities, and no generalization is claimed.

**T-15 (exact strict-gap certificate — `THEOREM`, exact, pentagon; the
centerpiece).** The rational behavior

```text
p    = (49/100, 25/81, 16/25, 36/121, 4/9)
v    = sqrt(p) = (7/10, 5/9, 4/5, 6/11, 2/3)
beta = 2137213/980100  ~  2.18060708
```

is realizable by a sharp quantum model, and every sharp realization of it —
any ranks, mixed states allowed, any finite dimension — satisfies
`||sum_i P_i||_op > beta` strictly. Hence `Delta_prep(p) > 0`. The numerical
SDP value of the gap is `~ 0.0096474`; the certificate proves *strictness*,
the SDP only supplies the magnitude.

The proof is four exact steps (full detail in the script header, every
inequality checked in rational arithmetic):

1. **Realizability.** An explicit rational `H_feas` (diagonal 1, edge entries
   0) has `H_feas - v v^T` positive definite by exact LDL — all five pivots
   positive as fractions — so the bordered Gram matrix is PSD and a rank-one
   pure realization exists in `R^6`.
2. **Rigidity.** Any feasible `H` with `lambda_max(H) <= beta` must have `v`
   as a top eigenvector (Rayleigh forcing through `H >= v v^T`). For real
   `v`, `Hv = beta v` splits into real and imaginary parts; the real part
   plus the constraints is a square 5x5 linear system with determinant
   exactly `112/495 != 0`, so `Re(H) = H*` is **unique**.
3. **Obstruction.** The rational witness
   `y = (-15/19, 11/51, 1, 7/34, -23/32)` gives
   `y^T H* y = -17658032557963925693/179590693860103680000 < 0` exactly. For
   real `y` and Hermitian `H`, `y^T H y = y^T Re(H) y` — so *every* Hermitian
   completion with real part `H*` fails PSD, and the imaginary freedom cannot
   rescue feasibility.
4. **Conclusion.** The feasible set is compact and nonempty, so the minimum
   exists and exceeds `beta`; T-14c extends the bound from rank-one pure to
   all sharp realizations. QED.

A correction discovered *by* this certificate is part of the public record
(see §5): the naive uniqueness claim for the full Hermitian `H*` is false —
the imaginary rigidity subsystem is singular for **every** behavior vector
(the cyclic product of coupling ratios is identically 1), and floating-point
arithmetic had silently selected the `Im = 0` member of a one-parameter
family. The certificate is immune: a real witness kills the whole family.

**T-16a (tightness criterion and pentagon phase geometry — `THEOREM` +
`MEASURED`, pentagon).** `Delta_prep(p) = 0` iff the top-eigenvector Gram
feasibility problem (`H` PSD, `<= beta * I`, `Hv = beta v`, diagonal 1, edges
0) is solvable. On `C_5`: the full symmetric contextual line is tight
(`kappa = q` for `2 <= q <= sqrt(5)`); the tight set strictly contains the
symmetric orbit and has interior; explicit gapped behaviors exist; the
boundary is semialgebraic with two crossing modes (a Gram-positivity failure
and a maximality failure), and the symmetric spine is exactly the singular
locus of the rigidity system. **Fence (`C_5` only):** the two-margin form of
the criterion uses `#non-edges = #vertices`, a square real system special to
the pentagon; general graphs keep only the feasibility criterion.

**T-16b (headroom law — `THEOREM`, general `G` for the inequality; canonical
form on the pentagon).** For every sharp implementation `(rho, P)` of `p`,
the *headroom* `h = ||K||_op - Tr(rho K)` with `K = sum_i w_i P_i` satisfies
`h >= Delta_prep(p)`, and re-preparing the implementation at its top
eigenvector pays out exactly `h`. The gap is therefore an *operational
floor*: any device showing a gapped behavior can, by re-preparation alone, be
made to extract at least `Delta_prep` more weighted event-mass than it
currently does. On the canonical pentagon receiver the headroom takes the
closed form `h_can = g * (1 - F)` with `g = (3*sqrt(5) - 5)/2`, and obeys the
asymmetry bound `h_can >= ((5 - sqrt(5))/8) * A(p)`.

**T-17 (anchored dual — `THEOREM` derived + numerically verified).**

```text
kappa(p) = 1 + max { v^T B v - tr(B) :  A >= 0, B >= 0, tr(A) = 1,
                     (A - B)_ij = 0 for every non-adjacent i != j }
```

Strong duality verified numerically at three reference points to `1e-6`. The
behavior enters through an indefinite quadratic — not as vertex weights — and
the natural collapse candidates are refuted: `kappa(p)` equals neither the
weighted Lovász theta `theta(C_5, p)` nor `theta(C_5, sqrt(p))` (checked at
points where they differ decisively).

**Sharpness boundary (`THEOREM`, construction).** With unrestricted POVMs the
gap vanishes identically: `E_i = p_i * I` reproduces any behavior at capacity
`beta` and destroys the certifying exclusivity structure. `Delta_prep` prices
*projective* implementation; it is a sharpness-conditioned receiver
invariant, not a property of the behavior alone.

## 3. How to verify

```powershell
python verification/exact_gap_certificate.py     # this frozen chapter copy
python ../../verification/scripts/run_all.py     # the full shipped suite
```

The certificate script is Python-standard-library only; every load-bearing
check is `fractions.Fraction` arithmetic. Expected output is frozen in
[`verification/EXPECTED-OUTPUT.md`](verification/EXPECTED-OUTPUT.md). The
supporting numerical results (SDP values, phase-geometry scans, headroom
checks, dual verification) are `cited` evidence from the private research
corpus, per the [evidence manifest](../../verification/evidence-manifest.md);
public wording nowhere exceeds what the shipped exact script proves.

## 4. Novelty posture — stated honestly

**Evidence class: INTERNAL-BLIND.** No external human expert reviewed this
work before release. The novelty check was run as four independent,
repository-barred blind literature searches from a self-contained
mathematical specification (no framework language), each with a different
disciplinary lens, one refutation-first, with 77 distinct published query
strings. This is below an external referee's check and the release says so;
it is far above an unchecked claim.

The graded claim:

> To our knowledge — based on a four-lens adversarial literature search,
> whose queries we publish, but without access to expert referees — the
> functional `kappa_G(p)`, the preparation gap `Delta_prep`, its
> exact-certificate strict positivity, the tightness phase geometry, and the
> headroom law are new; every ingredient (theta bodies, exclusivity graphs,
> fiber optimization, self-testing rigidity) is standard, and the nearest
> precedents are Sikora–Varvitsiotis–Wei 2016, Moroder et al. 2013, and
> Bharti et al. 2019.

Nearest structures found, for the reader's own audit:

- **Galtman 2000** (J. Algebraic Combin. 12): the Lovász theta is the **max**
  of `lambda_max` over the *identical* feasible set — `kappa` is the
  unstudied min-with-anchor counterpart.
- **Sikora–Varvitsiotis–Wei** (PRL 117, 060401): minimum *dimension* over
  realizations of a fixed Bell behavior — the same fiber, a different
  objective.
- **Moroder et al.** (PRL 111, 030501): device-independent entanglement
  quantification as an infimum over realizations of a full behavior — the
  closest formal template.
- **Bharti et al. 2019** (PRL 122, 250403) and 2022 (PRX Quantum 3, 030344):
  KCBS self-testing is Gram *uniqueness* on the fiber at the theta-optimal
  point — the boundary shadow of `Delta_prep = 0`. Every located self-testing
  theorem lives exactly in the gap-zero regime; the gap functional at
  interior behaviors is the unexplored side.
- Also checked and distinct: CSW exclusivity-graph theta (the max our object
  inverts), contextual fraction, memory cost, rank of contextuality, hidden
  nonlocality (the state-level cousin of headroom), spectra of sums of
  projections, minimal-norm completions without the PSD anchor.

Residual risks are published with the claim rows (FCT-25): appendix-buried
lemmas in robust self-testing papers; no citation-database access during the
sweep; recent preprints under unhit aliases; and the folklore possibility
that "every extremal behavior self-tests" formalizes in a way that computes
the gap *at extremal points* (interior-behavior results would stand).

## 5. What died on the way — the correction record

Filed per the [correction ledger](../../docs/correction-ledger.md) discipline;
these failures shaped the final claims:

1. The per-pair commutator law `||[P_k, P_{k+2}]||_HS^2 = chi` is exact at
   `n = 5` and **broken** at `n = 7, 9` — the pentagon is the unique
   single-incompatible-pair orbit, and the law was demoted from general to
   pentagon-specific.
2. A spectral-receipt "conversion" formula deflated to a known ceiling —
   equal to `chi_max` identically for exclusive realizations.
3. "The gap is generic" was corrected: the original sampling was
   boundary-biased; the true pentagon geometry is a tight bulk, a gapped
   near-extremal layer, and a tight symmetric spine.
4. "The tight set is the symmetric orbit" was refuted by an explicit interior
   nonsymmetric tight behavior.
5. "The Hermitian rigidity solution is unique" was corrected **by the exact
   certificate itself** — the imaginary subsystem is singular for every
   behavior vector, and float arithmetic had been silently selecting one
   member of a family. The published proof route (real witness kills the
   family) is the corrected one.

## 6. Place in the program — one section, no smuggling

In finite-contact language, a behavior `p` is what a floor stages: the full
outward record. The realization fiber over `p` is the set of lawful
completions the record does not distinguish, and this chapter's object is a
*fiber functional*: the least capacity any completion must carry. The
program's central law — the floor stages a fork and forces no selector — has
here a quantitative shadow: the strict gap certifies, in operator-norm units,
that the staged record *underdetermines* its completions and that every
completion must hold reserve capacity the record never spends. `Delta_prep`
is, in this reading, a paid instance of *selector debt* inside standard
quantum theory.

Nothing in sections 1–5 depends on this reading. A reader who deletes this
section loses no theorem.

## 7. Open, by name

- **C1 (robust bridge — `OPEN`).** Conjecture: `Delta_prep(p) >= c * A(p) -
  eps_rigidity(S)` with universal constants, `eps -> 0` approaching the
  quantum boundary. Stated as a conjecture; nothing in this chapter rests on
  it.
- **General-graph phase geometry.** The tightness criterion is general; the
  two-margin boundary machinery is pentagon-fenced. What survives on `C_7`,
  `C_9`, and non-cycle graphs is open (and the `n = 7, 9` commutator kill is
  a warning, not an accident).
- **Nature-facing use.** None claimed. `Delta_prep` is device-level and
  scenario-level; no cosmological or gravitational reading is licensed by
  this chapter.

## References

Cited fully in §4: Galtman (2000); Grötschel–Lovász–Schrijver (1986/88);
Cabello–Severini–Winter (PRL 112, 040401); Sikora–Varvitsiotis–Wei (PRL 117,
060401); Moroder–Bancal–Liang–Hofmann–Gühne (PRL 111, 030501); Bharti et al.
(PRL 122, 250403; PRX Quantum 3, 030344); Ray et al. (NJP 23, 033006);
Godsil–Roberson–Rooney–Šámal–Varvitsiotis (DCG 58, 2017);
Kruglyak–Rabanovich–Samoilenko (FAA 36, 2002; LAA 370, 2003);
Ramanathan–Horodecki (PRL 112, 040404); Kochen–Specker via the KCBS scenario
(Klyachko–Can–Binicioğlu–Shumovsky, PRL 101, 020403).
