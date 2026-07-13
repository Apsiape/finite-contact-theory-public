# Release Notes — v0.4.0

**Finite Contact Theory v0.4: Questions as Operators — the Inquiry Calculus
and a Second Law of Asking.**

Fourth public release; the third chapter shipped under the
[EVOLUTION.md](EVOLUTION.md) charter and the
[chapter directory convention](papers/README.md).

## The release ceiling

The live (v0.2) release ceiling is **unchanged** — it continues to control
the README and the claim register. Chapter 4 states its own ceiling in its
opening section and continues the finite-epistemics axis opened by
chapter 3 (v0.3.0): what asking *is*, what it *costs*, and where its
classical sector lies — all as finite, machine-checkable mathematics.

## What is new

- **Chapter 4**:
  [papers/04-inquiry-calculus/](papers/04-inquiry-calculus/paper.md) — the
  calculus of asking:
  1. **questions are operators** — asking acts by residuation on epistemic
     objects; the algebra is noncommutative in general, and its commutative
     sector is *exactly* the order-blind (count-only) sector: the Boolean
     shadow;
  2. **a second law of asking** — the expected cost of any binary question
     protocol decomposes *exactly* as `EC = H + KL + O`: irreducible
     entropy, belief mismatch, and slack, each nonnegative — so nothing
     identifies below the entropy; the v0.3 selector debt `ceil(log2 m)` is
     this law's uniform worst-case corner;
  3. **adaptivity is a resource** — adaptive questioning strictly beats the
     best fixed interrogation under a constrained question repertoire
     (shipped witness: uniform source, threshold questions, `2.0` vs
     `2.25`), while unrestricted repertoires erase the gap at small scope —
     the interest lives in the constraint;
  4. **paradox is type collapse** — self-reference is lawful when the grade
     separating a live asking from its recorded answer is kept; ungraded
     self-negation has no solution, graded recursion runs clean.
- Claim rows **FCT-30 through FCT-33**; theorem rows **T-22 through T-25**;
  results ledger
  [FCT-30-FCT-33-inquiry-calculus-RESULTS.md](verification/results/FCT-30-FCT-33-inquiry-calculus-RESULTS.md).
- Shipped verification: `verification/scripts/inquiry_calculus.py`
  (stdlib-only, deterministic, seven checks), wired into `run_all.py`, with
  a frozen copy and verbatim expected output in the chapter directory.

## Scope fences carried in this release

- No claim that quantum measurement *is* the residual calculus; the
  structural rhyme (noncommutative asking, commutative classical shadow) is
  cited program context only.
- Binary answer alphabets and identification trees only; no asymptotic
  adaptivity rates.

## Archive

Tagging this release triggers the Zenodo webhook; the version DOI is
recorded in [`papers/04-inquiry-calculus/RELEASE.md`](papers/04-inquiry-calculus/RELEASE.md)
and CITATION.cff once minted. Concept DOI for all versions:
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591).
