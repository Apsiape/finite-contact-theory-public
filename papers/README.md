# Papers

Chapters are the citable interfaces of the program: each release ships one
scoped, self-contained paper, and the paper's directory is **frozen** once its
release is tagged and deposited. The living state of the theory is the docs
layer (claim register, theorem bank, correction ledger); the chapters are the
snapshots a reader can rest a citation on.

Governance: [`../EVOLUTION.md`](../EVOLUTION.md). Release gate:
[`../docs/release-checklist.md`](../docs/release-checklist.md).

## Published chapters

- `finite-contact-theory-v0.1.md` — **Chapter 1** (v0.1.0): _Growing the
  Bell/CHSH Quantum Boundary from a Finite One-Use Floor_. Version DOI
  [10.5281/zenodo.21253592](https://doi.org/10.5281/zenodo.21253592). This
  chapter predates the directory convention below and is grandfathered as a
  single file; it is frozen like any other chapter.
- [`02-behavior-conditioned-capacity/`](02-behavior-conditioned-capacity/paper.md)
  — **Chapter 2** (v0.2.0): _Behavior-Conditioned Contextual Capacity and an
  Exact Strict Preparation Gap_. The first chapter under the directory
  convention; DOIs recorded in its
  [`RELEASE.md`](02-behavior-conditioned-capacity/RELEASE.md) at tagging.
- [`03-identifiability-and-debt/`](03-identifiability-and-debt/paper.md)
  — **Chapter 3** (v0.3.0): _The Identifiability and Debt Calculus_. DOIs
  recorded in its [`RELEASE.md`](03-identifiability-and-debt/RELEASE.md) at
  tagging.
- [`04-inquiry-calculus/`](04-inquiry-calculus/paper.md)
  — **Chapter 4** (v0.4.0): _Questions as Operators: the Inquiry Calculus
  and a Second Law of Asking_. DOIs recorded in its
  [`RELEASE.md`](04-inquiry-calculus/RELEASE.md) at tagging.
- [`05-becoming-webs/`](05-becoming-webs/paper.md)
  — **Chapter 5** (v0.5.0): _Becoming Webs: Lawful Time Without
  Foundation_. DOIs recorded in its
  [`RELEASE.md`](05-becoming-webs/RELEASE.md) at tagging.
- [`06-measured-floor/`](06-measured-floor/paper.md)
  — **Chapter 6** (v0.6.0): _A Measured Generative Floor: Delayed
  Individuation, Short-Tailed Separation, and Ballistic Counterfactual
  Defects_. DOIs recorded in its
  [`RELEASE.md`](06-measured-floor/RELEASE.md) at tagging.

## Chapter directory convention (v0.2 onward)

Each new chapter lives in its own directory:

```text
papers/<NN>-<slug>/
  paper.md            the chapter narrative (the citable text)
  claims.md           snapshot of the exact claim-register rows the chapter
                      rests on: IDs, labels, scopes, evidence classes, as of
                      the release tag
  verification/       frozen copies of the chapter's shipped scripts and
                      their expected outputs (the live, maintained versions
                      stay in /verification/scripts/)
  RELEASE.md          the freeze record: release tag, version DOI, concept
                      DOI, chapter deposit DOI if one exists, freeze date
```

`<NN>` is the chapter number (`02`, `03`, ...); the slug is permanent and
never reused.

## Freeze rule

After the release that ships a chapter is tagged:

- the chapter directory does not change;
- corrections affecting the chapter are filed in
  [`../docs/correction-ledger.md`](../docs/correction-ledger.md) and noted in
  the next release's notes, which point back to the chapter;
- the claim-register rows named in `claims.md` remain the live view — if a
  row is later promoted, demoted, or withdrawn, the register (not the frozen
  chapter) carries its current status.

A reader who wants "what the chapter said" reads the frozen directory at its
tag. A reader who wants "what the theory currently holds" reads the docs layer
at the latest tag. Both are always available and never in conflict about which
is which.

## Chapter deposits

A chapter may additionally receive its own Zenodo deposit (publication type),
distinct from the repository's software deposit. When it does:

- the chapter deposit DOI is recorded in the chapter's `RELEASE.md`;
- cite the chapter DOI for the result, the concept DOI for the program;
- the deposit contains the frozen chapter directory only — a reader of the
  paper gets the paper and exactly the evidence it rests on, without the full
  program.

## Intake rule

Companion notes and appendices are added only when they are cleanly tied to
the public claim register, per
[`../docs/publication-policy.md`](../docs/publication-policy.md).
