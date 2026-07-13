# Chapter 4 — Claim Snapshot (as of the v0.4.0 release tag)

This file freezes the claim-register rows this chapter rests on, exactly as
they stand at the release tag. The *live* view — including any later
promotion, demotion, or withdrawal — is the
[public claim register](../../docs/public-claim-register.md). If the two ever
differ, the register is current and this snapshot is historical; that is by
design.

| ID | Short name | Status | Scope | Evidence state |
|---|---|---|---|---|
| FCT-30 | Questions as residual operators; the Boolean shadow | `THEOREM` | Finitely supported series; count-only biconditional exhaustive at length-2 family | `shipped` |
| FCT-31 | The second law of asking: EC = H + KL + O | `THEOREM` (exact identity) | Binary decision-tree protocols over finite sources | `shipped` |
| FCT-32 | Adaptivity interest J >= 0 with strict witness | `THEOREM` + witness | Finite spaces; admitted-question families; witness = thresholds on 4 outcomes | `shipped` |
| FCT-33 | Self-question typing: paradox is type collapse | `THEOREM` (witnesses) | Two-element answer space; graded recursion | `shipped` |

Full row text, verbatim from the register at the tag, follows.

---

## FCT-30 - Questions As Residual Operators; The Boolean Shadow

Status: `THEOREM`
Scope: finitely supported weight functions (formal series) over a finite
alphabet; the count-only biconditional exhaustive over the length-2
coefficient family; randomized composition-law checks at longer horizons.
Evidence state: `shipped` (`inquiry_calculus.py`).

Public statement:

Asking acts on epistemic objects as residual operators
(`(a^-1 S)(w) = S(aw)`), which compose contravariantly
(`u^-1 (v^-1 S) = (vu)^-1 S`). The operator algebra is noncommutative in
general — an explicit two-letter witness is shipped — and commutes exactly
on count-only (order-blind) series: the classical/Boolean sector of asking
is precisely the sector where histories carry no more than their letter
counts.

Evidence:

- shipped: T-22 checks in `inquiry_calculus.py`.

Checks / controls:

- composition law on 300 randomized series;
- noncommutativity witness explicit;
- count-only biconditional exhaustive on the 81-member length-2 family.

Residuals:

- the biconditional is shipped at exhaustive small scope; the general-
  horizon statement is elementary but not exhaustively verified here;
- no claim that quantum measurement is this calculus (structural rhyme is
  cited program context).

## FCT-31 - The Second Law Of Asking

Status: `THEOREM` (exact identity)
Scope: binary decision-tree protocols identifying finite sources.
Evidence state: `shipped`.

Public statement:

For any binary decision-tree protocol with leaf depths `d_x` and Kraft
weight `Z = sum 2^(-d_x) <= 1`, the expected cost decomposes exactly as
`EC = H(p) + KL(p || q) + O` with implicit belief `q_x = 2^(-d_x)/Z` and
slack `O = -log2 Z >= 0`. Hence `EC >= H(p)` always: the cost of asking is
irreducible entropy plus belief mismatch plus unused resolving power, and
nothing identifies below the entropy. The chapter-3 selector debt
`ceil(log2 m)` is the uniform worst-case corner of this law.

Evidence:

- shipped: T-23 checks in `inquiry_calculus.py`.

Checks / controls:

- identity verified to 1e-12 on 300 random tree/source pairs;
- Kraft inequality in exact rational arithmetic;
- the equality case (dyadic source, full tree) witnessed separately.

Residuals:

- binary answer alphabets only (general alphabets rescale the logarithm);
- protocols are identification trees; interactive games with lies/noise
  are not covered.

## FCT-32 - Adaptivity Interest

Status: `THEOREM` + witness
Scope: finite outcome spaces with an admitted-question family; exhaustive
strategy search at |X| = 4; strict witness under threshold questions.
Evidence state: `shipped`.

Public statement:

With the admitted question family part of the model, the optimal adaptive
expected cost never exceeds the optimal fixed expected cost
(`J = EC_fixed* - EC_adaptive* >= 0`, strategy-space inclusion), and the
inequality is strict on a shipped witness: the uniform source on four
ordered outcomes under threshold questions has adaptive cost `2.0` and
best fixed cost `2.25`. Notably, with unrestricted subset questions and
early stopping, fixed matches adaptive at this size — the interest is a
property of asking under a constrained repertoire.

Evidence:

- shipped: T-24 checks in `inquiry_calculus.py`.

Checks / controls:

- both optima computed by exhaustive search (all adaptive trees via
  recursion; all fixed orders);
- J >= 0 checked across a source grid; the strict witness printed with
  both values.

Residuals:

- small-scope exhaustion only; asymptotic interest rates not claimed.

## FCT-33 - Self-Question Typing: Paradox Is Type Collapse

Status: `THEOREM` (witnesses)
Scope: two-element answer space; graded recursion over six steps.
Evidence state: `shipped`.

Public statement:

Ungraded self-identity `x = x` has exactly two solutions; ungraded
self-negation `x = 1 - x` has none; the graded recursion
`x_(n+1) = 1 - x_n` has exactly two lawful orbits and no contradiction.
Self-reference is lawful when the grade separating a live asking from its
recorded answer is kept; paradox is exactly what remains when that grade is
collapsed.

Evidence:

- shipped: T-25 checks in `inquiry_calculus.py`.

Checks / controls:

- exhaustive at the stated scope.

Residuals:

- the general guarded-recursion/type-level framing is cited program
  context, not shipped mathematics.
