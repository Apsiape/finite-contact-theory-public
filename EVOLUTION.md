# How This Theory Evolves in Public

This is the governance charter for a living theory. Finite Contact Theory is
not finished, and this repository is designed to say so precisely. This
document defines how new results arrive, how old results are corrected, and
what a reader or citer can rely on as the program grows.

The short version:

> One canonical repository, released in chapters. History is append-only.
> Corrections are public and loud. Identifiers are stable forever. The latest
> tag is the current state of the theory; every earlier tag remains citable
> and unchanged.

## One canonical repository

This repository is the single public home of the program. There will not be
parallel public repositories, and it will not be restarted from scratch.

The reason is evidential, not sentimental: the git history is part of the
scientific record. Preregistration commits that predate result commits,
corrections filed in the open, and claims that died on the record are the
program's strongest credibility assets. A polished fresh repository would
convert that record into an assertion. Anyone skeptical enough to matter is
invited to check the timestamps.

- **Concept DOI** (always resolves to the latest version):
  [10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591)
- **Version DOIs**: one per tagged release, minted via the Zenodo–GitHub
  integration. Each is a frozen snapshot.

## Releases are chapters

The program publishes when a research cluster closes, not on a calendar. Each
release is a *chapter*: a scoped, self-contained addition to the public
theory, with its own paper, claim rows, and shipped verification.

Version numbers carry meaning:

- **MINOR** (`v0.2.0`, `v0.3.0`, ...): a new chapter. New claim-register rows,
  new theorem-bank rows, new shipped verification, a new paper under
  `papers/`.
- **PATCH** (`v0.2.1`, ...): corrections. Demotions, withdrawals, or wording
  fixes that change public meaning, each carried by a correction-ledger
  entry. Typo-level fixes do not require a release.
- **MAJOR** (`v1.0.0`): reserved for a change in the *kind* of release
  ceiling — for example, the first nature-facing prediction package with a
  registered discriminator. Not a prestige bump.

Every release passes the gate in
[`docs/release-checklist.md`](docs/release-checklist.md) before tagging. The
historical roadmap that gated v0.1 is kept at
[`docs/release-roadmap.md`](docs/release-roadmap.md).

## Append-only rules

These rules exist so that a claim, once public, has a traceable life.

1. **Claim-register rows are never deleted.** A claim changes by status
   transition (`EXTENSION` → `THEOREM`, `MEASURED` → `WITHDRAWN`, ...), and
   each transition is logged in the row with a date and a reason. A withdrawn
   claim remains visible with its history.
2. **The correction ledger is append-only.** Demotions, failed probes,
   withdrawals, and wording corrections are added, never edited away. Quiet
   replacement is reserved for typos and formatting that do not change
   meaning (per [`docs/publication-policy.md`](docs/publication-policy.md)).
3. **Identifiers are stable and never reused.** `FCT-xx` claim IDs, `T-xx`
   theorem IDs, and chapter slugs are permanent. A superseded theorem row
   points forward ("superseded by T-yy"); it is not overwritten.
4. **Published chapters are frozen.** After a chapter's release is tagged and
   deposited, its directory under `papers/` does not change. Corrections to a
   frozen chapter live in the correction ledger and in the release notes of
   the next version, which point back to the affected chapter.

## The reader's and citer's contract

- **To cite the program as a whole**, use the concept DOI. It always resolves
  to the latest version.
- **To cite a specific result**, use the version DOI of the release that
  shipped it (and, once chapter deposits exist, the chapter's own DOI). That
  snapshot will never change.
- **Before relying on an older claim**, check its row in
  [`docs/public-claim-register.md`](docs/public-claim-register.md) at the
  latest version. If the claim was demoted or withdrawn since the release you
  read, the row's history and the
  [correction ledger](docs/correction-ledger.md) will say so plainly.
- **A growing correction ledger is not decay.** The kill count is a health
  metric. A public theory that never retracts anything is not being tested.

## The private-to-public pipeline

The working laboratory is private and much larger than this repository. Public
releases are curated exports, and the export rules are strict:

- a claim ships only with a status label, a stated scope, an evidence class,
  named controls (or the reason controls do not apply), and named residuals —
  the intake rules of [`docs/publication-policy.md`](docs/publication-policy.md);
- claims are worded at the scope their audit *earned*, using the weakest
  accurate label in [`docs/status-labels.md`](docs/status-labels.md);
- shipped verification must run from a clean clone with no dependencies
  beyond the Python standard library (or must declare its dependencies in the
  script header), under
  [`verification/verification-standard.md`](verification/verification-standard.md);
- private evidence may be *cited* (the `cited` class in
  [`verification/evidence-manifest.md`](verification/evidence-manifest.md)),
  but public wording must never exceed what the shipped public artifact
  supports;
- material not yet at export scope stays in the
  [hold register](docs/hold-register.md), by name, so the boundary between
  published and held is itself public.

## Where things live as the program grows

One home per artifact kind. No duplicates, no drift.

| Artifact                          | Single home                            |
| --------------------------------- | -------------------------------------- |
| Claims and their status history   | `docs/public-claim-register.md`        |
| Theorems and dependency structure | `docs/theorem-bank.md`                 |
| Corrections and withdrawals       | `docs/correction-ledger.md`            |
| Chapters (papers)                 | `papers/<NN>-<slug>/` (see below)      |
| Live verification scripts         | `verification/scripts/`                |
| Verification results and manifest | `verification/results/`, `verification/evidence-manifest.md` |
| Held material and its gates       | `docs/hold-register.md`                |
| Open hinges and planned releases  | `docs/roadmap.md`                      |
| Release gate                      | `docs/release-checklist.md`            |
| Formal vocabulary                 | `docs/mathematical-core.md`, `docs/glossary.md` |

The chapter directory convention is specified in
[`papers/README.md`](papers/README.md).

## What this document is not

This charter governs *process*, not truth. Passing the release gate does not
strengthen a status label; a DOI is a citable snapshot, not peer review. The
claims are exactly as strong as their labels and scopes say, and no stronger.
