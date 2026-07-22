# Contributing

This is a solo-maintained research record with a review discipline. It is not a
software project looking for features — it is a theory looking for pressure. The
method here is **adversarial**: a claim earns its place by surviving attempts to
break it, and the correction ledger
([`docs/correction-ledger.md`](docs/correction-ledger.md)) proves that kills are
honored — 24 recorded corrections, several of them self-inflicted, each printed
alongside the result it corrects. Contributions are welcome in that spirit.
Write to **apsiape@gmail.com**.

There are four ways to contribute, roughly in order of how much they are valued.

## 1. Try to kill something (most valued)

The strongest contribution is a **counterexample or a broken step, reported with
a runnable witness.**

- **The two registered experimental bets ship exact kill conditions.** The
  negative-Gram prediction ([Chapter 10](papers/10-negative-gram-holonomy/paper.md),
  [Chapter 11](papers/11-mixed-state-exclusion/paper.md)) reduces at `n = 3` to a
  single raw-count test and lists the conditions that kill the physical claim
  (an admissible PSD fit exists; `Q₃ = 0` not rejected; the effect is drift or
  binning; a standard positive-Hilbert model in the nuisance family reproduces
  it; replication fails). The actuality protocol
  ([Chapter 35](papers/35-actuality-protocol/paper.md)) ships three tables with
  per-candidate kill conditions. Meeting any one of them is a real result.
- **The theorems ship exact verifiers.** Every shipped result line has a
  dependency-free script under
  [`verification/scripts/`](verification/scripts/); the whole suite runs with
  `python verification/scripts/run_all.py` and prints
  `ALL SHIPPED VERIFICATION: PASS`. If a script's arithmetic is wrong, or its
  claim overreaches what it checks, show it — ideally with a minimal script that
  reproduces the discrepancy.

A kill that survives review is filed to the correction ledger **with credit to
you.**

## 2. Build a second engine

Nothing in this program is meant to be load-bearing on one implementation. If
you re-verify any shipped script's claim with **independent code** — a different
language, a different method, a from-scratch reimplementation — that is a
first-class contribution. Propose it by email with (a) which result line you
re-verified, (b) your independent code, and (c) whether it agrees to the exact
values. Agreements and disagreements are both useful.

## 3. Attack an open problem

The open problems are collected in [`OPEN-PROBLEMS.md`](OPEN-PROBLEMS.md), each
with a difficulty tag and honest prerequisites. Several are **framework-free** —
statable and solvable in standard mathematics with no commitment to this
theory's vocabulary (the flagship positivity-margin problem, OP-01, needs zero
buy-in). Solutions, partial results, and sharper statements all count.

## 4. Improve the on-ramp

The theory is dense and the vocabulary is unusual. Reports of glossary gaps,
passages that need plain language, broken links, or unclear "how to read"
paths are genuinely helpful. See [`docs/glossary.md`](docs/glossary.md) and
[`docs/how-to-read.md`](docs/how-to-read.md).

## Ground rules

- **Exact arithmetic is preferred.** Where a result can be stated exactly
  (rationals, closed forms, integer certificates), state it exactly; floating-
  point is for optimization bounds only, and labeled as such.
- **Scope your claims.** Say precisely what you have shown and what you have
  not. The single most common correction in the ledger is an unscoped
  generalization; a narrow claim that holds beats a broad one that doesn't.
- **No priority disputes without the novelty-sweep discipline.** Claims that
  something is (or isn't) new are settled by a repository-barred literature
  sweep (the release-checklist novelty gate), not by assertion. Priority is a
  public *label*, held separate from whether a result is correct or valuable.
- **Corrections are filed to the ledger, with credit.** A failed or narrowed
  claim keeps its record: the original statement, what survived, the current
  status, and the condition to reopen it. Your name travels with the correction
  you contributed.

Corrections are progress here — the kill-count is a health metric, not an
embarrassment. Thank you for pushing on the work.
