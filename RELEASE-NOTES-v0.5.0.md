# Release Notes — v0.5.0

**Finite Contact Theory v0.5: Becoming Webs — Lawful Time Without
Foundation.**

Fifth public release; the fourth chapter shipped under the
[EVOLUTION.md](EVOLUTION.md) charter and the
[chapter directory convention](papers/README.md).

## The release ceiling

The live (v0.2) release ceiling is **unchanged** — it continues to control
the README and the claim register. Chapter 5 states its own ceiling in its
opening section: four finite theorems that *separate* features of time
usually bundled together, each a possibility or impossibility statement at
finite-model scope, with the program-facing readings cited, not claimed.

## What is new

- **Chapter 5**:
  [papers/05-becoming-webs/](papers/05-becoming-webs/paper.md) — time,
  disassembled into four independent theorems:
  1. **torsor time** — the time fiber is fully lawful with no derivable
     origin (heap axioms exhaustive; translations fixed-point-free); "this
     moment" is a received selection, priced by the v0.3 selector debt;
  2. **the helix** — law-time covers visible-time: a cyclic visible
     dynamics lifts uniquely to an ascending helix whose monodromy is a
     conserved grade step; exact visible periodicity is compatible with
     strictly ascending law-history;
  3. **the arrow without thermodynamics** — a fully reversible visible
     dynamics coupled to a step ledger never returns jointly (exhaustive,
     510 words): an arrow from pure bookkeeping of asking — no
     probabilities, no entropy; undoing a step is another step;
  4. **lawfulness without foundation** — guarded self-reference has unique
     solutions with no base case, and a Möbius-twisted cover has perfect
     local time with no global "now" (untwisted control: two).
- Claim rows **FCT-34 through FCT-37**; theorem rows **T-26 through T-29**;
  results ledger
  [FCT-34-FCT-37-becoming-webs-RESULTS.md](verification/results/FCT-34-FCT-37-becoming-webs-RESULTS.md).
- Shipped verification: `verification/scripts/becoming_webs.py`
  (stdlib-only, fully deterministic — every check exhaustive at its stated
  scope), wired into `run_all.py`, with a frozen copy and verbatim expected
  output in the chapter directory.
- Chapters 3–5 now form a connected public axis: what identification costs
  (v0.3), what asking is and costs (v0.4), and what time-like structure
  those costs already force or forbid (v0.5).

## Scope fences carried in this release

- Possibility/impossibility theorems only: no claim that nature's time is
  a torsor, that its arrow is ledger-bookkeeping, or that simultaneity is
  topologically twisted.
- Continuum time, relativistic structure, and quantitative arrows are not
  touched.

## Archive

Tagging this release triggers the Zenodo webhook; the version DOI is
recorded in [`papers/05-becoming-webs/RELEASE.md`](papers/05-becoming-webs/RELEASE.md)
and CITATION.cff once minted. Concept DOI for all versions:
[10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591).
