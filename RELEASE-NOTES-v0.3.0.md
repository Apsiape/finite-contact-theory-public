# Release Notes — v0.3.0

**Finite Contact Theory v0.3: The Identifiability and Debt Calculus.**

Third public release; the second chapter shipped under the
[EVOLUTION.md](EVOLUTION.md) charter and the
[chapter directory convention](papers/README.md).

## The release ceiling

The live (v0.2) release ceiling is **unchanged** by this chapter — it
continues to control the README and the claim register, and remains quoted
verbatim there and in the frozen chapter-2 paper and v0.2.0 notes. Chapter 3
states its own ceiling in its opening section: everything it claims is a
finite, machine-checkable theorem at finite-model scope, and it does not
claim that any physical system realizes a particular alternative set.

This is deliberate: chapter 3 opens a second axis of the program — the
finite epistemics that the quantum-facing chapters (1 and 2) implicitly rest
on — rather than extending the quantum-boundary stack itself. A rewritten
program-wide ceiling is planned for the survey chapter.

## What is new

- **Chapter 3**:
  [papers/03-identifiability-and-debt/](papers/03-identifiability-and-debt/paper.md)
  — the three-part calculus the wider program uses as its load-bearing
  spine, published as finite mathematics:
  1. **the waist** — a description suffices for a purpose exactly when its
     kernel is contained in the purpose's indifference relation (with the
     order-independent biextensional core as the two-sided form);
  2. **selector debt** — identifying one of `m` future-inequivalent
     alternatives costs exactly `ceil(log2 m)` receipt bits, and no
     symmetry-respecting rule can perform the selection on a symmetric
     fiber;
  3. **continuation sufficiency** — a present boundary is complete for the
     future exactly when its lawful completions are future-equivalent, with
     explicit certificates that no finite tomography depth is universal.
- Claim rows **FCT-26 through FCT-29**; theorem rows **T-18 through T-21**;
  results ledger
  [FCT-26-FCT-29-identifiability-debt-calculus-RESULTS.md](verification/results/FCT-26-FCT-29-identifiability-debt-calculus-RESULTS.md).
- Shipped verification:
  `verification/scripts/identifiability_debt_calculus.py` (stdlib-only,
  deterministic, five checks; exhaustive where the scope is exhaustive),
  wired into `run_all.py`, with a frozen copy and verbatim expected output
  in the chapter directory.
- Every theorem in the chapter is elementary *by design*: the release's
  content is the calculus as a published, falsifiable package — the exact
  biconditional forms, the exact debt constant, and the no-equivariant-
  selector statement — with the program-facing applications explicitly
  `cited`, not claimed.

## Scope fences carried in this release

- The chapter forbids **derived, symmetry-respecting** selection; it does
  not assert selection cannot occur. The residual is stated in FCT-27.
- Which purposes any physical system runs, and what counts as a lawful
  completion for nature, are named open, not implied.

## Archive

Tagging this release triggers the Zenodo webhook; the version DOI is
recorded in [`papers/03-identifiability-and-debt/RELEASE.md`](papers/03-identifiability-and-debt/RELEASE.md)
and CITATION.cff once minted. Concept DOI for all versions:
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591).
