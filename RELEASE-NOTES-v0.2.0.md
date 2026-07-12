# Release Notes — v0.2.0

**Finite Contact Theory v0.2: Behavior-Conditioned Contextual Capacity and an
Exact Strict Preparation Gap.**

Second public release; the first chapter shipped under the
[EVOLUTION.md](EVOLUTION.md) charter and the
[chapter directory convention](papers/README.md).

## The release ceiling

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack — from one-use contact to counting, to one-receiver gluing, to
> rational Born weights, to the CHSH/Pell boundary, to a carrier grammar grown
> from one-use contact, to a behavior-conditioned contextual capacity with an
> exact strict preparation gap — under which the quantum boundary is a floor
> theorem at **binary-Bell finite-carrier scope**, the preparation gap is an
> exact theorem at **KCBS-pentagon scope**, and every unearned generalization
> is left open by name.

The v0.1 ceiling remains quoted, unchanged, in the frozen v0.1 paper and
release notes.

## What is new

- **Chapter 2**:
  [papers/02-behavior-conditioned-capacity/](papers/02-behavior-conditioned-capacity/paper.md)
  — written in standard quantum-foundations language. The object: the least
  operator-norm capacity any sharp quantum model must carry to reproduce a
  fixed contextuality behavior, and the strict gap between that and what the
  behavior spends.
- **The centerpiece is hand-checkable**: an explicit rational pentagon
  behavior whose every sharp realization, in every finite dimension, has
  capacity strictly above `beta` — proved end to end in exact rational
  arithmetic by a stdlib-only script now in the shipped suite
  (`verification/scripts/exact_gap_certificate.py`).
- Claim rows **FCT-21 through FCT-25**; theorem rows **T-14 through T-17**;
  results ledger
  [FCT-22-exact-gap-certificate-RESULTS.md](verification/results/FCT-22-exact-gap-certificate-RESULTS.md).
- The **novelty posture is graded and honest**: INTERNAL-BLIND evidence class
  (four repository-barred adversarial literature lenses, published queries,
  named nearest precedents, published residual risks) — not external review,
  and the paper says so.
- The **evolution/governance layer**: EVOLUTION.md, the reusable
  [release checklist](docs/release-checklist.md), and the chapter freeze
  rules (added since v0.1.0, first exercised by this release).

## Corrections carried in this release

The chapter's section 5 publishes five corrections from the research arc,
including one found *by* the shipped certificate itself (the Hermitian
uniqueness claim was false; the corrected proof route ships). No previously
published v0.1 claim is affected.

## Release gate

The [release checklist](docs/release-checklist.md) was completed for this
release: scope freeze (ceiling identical in README, chapter paper, claim
register, and these notes); claim and theorem rows complete with labels,
scopes, evidence classes, and residuals; corrections filed; the full shipped
suite passing from a clean clone (`run_all.py`, six scripts); rights-clean
new content (all chapter text and the certificate script are original to the
program); metadata updated; links audited (`scripts/release_audit.py`).

## DOIs

- Concept DOI (always latest):
  [10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591)
- Version DOI (v0.2.0): minted by Zenodo at the GitHub release and recorded
  here, in `CITATION.cff`, and in the chapter's `RELEASE.md` in the
  post-mint commit.

## Citation

Until the version DOI is minted, cite the concept DOI with the version tag:

> Douglas, S. (2026). *Finite Contact Theory v0.2: Behavior-Conditioned
> Contextual Capacity and an Exact Strict Preparation Gap* (v0.2.0). Zenodo.
> https://doi.org/10.5281/zenodo.21253591
