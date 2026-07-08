# DOI Release Roadmap

Status: working roadmap for the first public DOI release.

This roadmap defines what must be finished before this repository is worthy of
a public tag and DOI snapshot. The target is not to publish every private
research artifact. The target is to publish a clean, scoped, citable public artifact:

> Finite Contact Theory v0.1 is a finite reconstruction program with a public
> axiom spine, theorem index, claim register, correction ledger, and evidence
> posture. It contains a scoped theorem stack through the binary-Bell native
> carrier lift, while leaving the general quantum selector, q >= 3 extensions,
> cross-site interlocking, gravity sourcing, and nature-facing predictions open.

## Release Decision

The first DOI release now targets a **small shipped verification subset plus
cited private evidence**. This means:

- a dependency-free public script subset verifies a few clean core claims;
- larger private research ledgers remain cited, historical, or held;
- no README language claims that the shipped subset reproduces every private
  research artifact;
- the evidence manifest separates `shipped`, `cited`, `historical`, and `held`.

## Current State

Already in place:

- public repository scaffold;
- conservative rights posture;
- citation metadata;
- README with scoped theory horizon;
- status labels, including `MEASURED`;
- public claim register release-draft ledger;
- correction ledger first pass;
- mathematical core draft;
- theorem-bank draft with proof-sketch stubs and dependency graph;
- hold register;
- verification evidence manifest;
- v0.1 technical-note draft;

Not yet release-ready:

- claim rows are now release-draft prose but need final human review;
- theorem rows have first proof sketches and a dependency graph, but still need
  source-polishing;
- private evidence paths need stable citation posture;
- first paper/monograph has release links and needs final human polish;
- a small shipped verification subset is admitted;
- links and source references have not had a clean-clone audit;
- `CITATION.cff` and release metadata are set for the tagged DOI release.

## Must Finish Before Any DOI

### 1. Freeze The v0.1 Scope

Define the release in one paragraph and keep all docs aligned to it.

Required decisions:

- release title;
- v0.1 claim ceiling;
- which claims are backed by shipped scripts versus cited private evidence;
- whether the first paper is a short paper, long paper, or monograph-style
  technical note;
- exact rights posture for text, scripts, and figures.

Exit condition:

- README, paper abstract, claim register, and release checklist all state the
  same release ceiling.

### 2. Finalize Claim Register Release Rows

`docs/public-claim-register.md` is now a release-draft ledger. It still needs a
final human review before DOI tagging.

Required work:

- confirm FCT-01 through FCT-20 release prose;
- ensure every row has label, scope, public statement, evidence state, source,
  controls or reason controls do not apply, and residuals;
- demote or remove rows that cannot carry a public source after final review;
- check every private-only claim is held, cited, or historical.

Exit condition:

- every public claim maps to either `docs/theorem-bank.md`,
  `docs/correction-ledger.md`, or `docs/roadmap.md`.

### 3. Harden The Theorem Bank

`docs/theorem-bank.md` should be the mathematical table of contents for the
release.

Required work:

- polish proof-sketch stubs for T-01 through T-13;
- separate theorem, measured result, recovery, model-scope result, and frontier
  target;
- replace private shorthand with public source language;
- identify which rows are cited-only and which have public artifacts;
- keep the compact dependency graph aligned with claim-register revisions.

Exit condition:

- a technically minded reader can see the theorem stack without reading the
  private repository.

### 4. Finish The Public Mathematical Core

`docs/mathematical-core.md` should become the clean formal spine.

Required work:

- define the primitive symbols and words used in the release;
- define trace class, witness fiber, reception/gluing, aperture, carrier, and
  completion in public prose;
- include the reconstruction ladder;
- state the exact scope fences;
- add a "do not read this as" subsection.

Exit condition:

- the first paper can cite this document as the release's formal vocabulary.

### 5. Write The First Paper

`papers/finite-contact-theory-v0.1.md` is now a real technical-note draft with
release links. It still needs final human polish before DOI tagging.

Recommended structure:

1. Abstract.
2. What is being reconstructed.
3. Axioms and finite-contact posture.
4. Admissibility calculus and claim labels.
5. Counting and reception.
6. Born and gluing at rational scope.
7. CHSH/Pell and native carrier lift at binary-Bell scope.
8. Continuum as admitted completion.
9. Aperture energy/temperature and gravity-facing open work.
10. Correction ledger and killed claims.
11. Open hinges and next work.

Exit condition:

- the paper can stand alone as the v0.1 DOI object.

### 6. Finish The Evidence Package

The initial shipped subset is now:

- no-jam/open fresh-mark core;
- exchangeable finite frequency bridge;
- native binary-Bell carrier identities.

Required remaining work:

- keep `verification/evidence-manifest.md` as the authoritative evidence
  posture;
- ensure all shipped scripts are standard-library or dependency-pinned;
- keep larger private artifacts as `cited`, `held`, or `historical`;
- do not claim clean-clone reproducibility for cited-only private evidence.

Exit condition:

- release checklist accurately describes the shipped subset and cited private
  evidence.

### 7. Public Source Hygiene

Required checks:

- grep for private absolute paths;
- grep for stale hold-status language;
- grep for overclaims such as "all quantum mechanics", "solves gravity",
  "complete theory", or "selects the boundary" without scope, and manually
  confirm that any remaining hits are caveats or forbidden examples;
- check Markdown links;
- ensure every private-source reference is either cited evidence or replaced by
  public text;
- ensure no scratchpads, transcripts, secrets, or raw private notes are present.

Exit condition:

- clean-clone reader sees a coherent public artifact, not a private lab dump.

### 8. Rights, Citation, And Metadata

Required work:

- confirm `LICENSE.md` is the intended conservative release posture;
- update `CITATION.cff` title, abstract, version, release date, and repository;
- decide whether type remains `software` or should be generalized for a theory
  release;
- add release notes for `v0.1.0`;
- decide whether to include a `CHANGELOG.md`.

Exit condition:

- release metadata is ready before the DOI tag.

### 9. Final Audit Pass

Run before tagging:

```text
python scripts\release_audit.py
```

The script runs the shipped verification subset, checks required files,
metadata, private-path leaks, internal-process codenames, stale hold-status
language, obvious overclaim phrases, local Markdown links, and Git whitespace
errors.

Manual spot checks may still use:

```text
git status --short
rg -n -i "scratchpad|appdata|todo" .
rg -n -F "C:\\" .
rg -n -i "all quantum|solves gravity|complete theory|selects.*boundary" . --glob "!docs/release-roadmap.md"
git diff --check
```

If runnable verification is shipped, also run the public verification command
from a clean clone.

Exit condition:

- no stale scope language;
- no accidental private material;
- no promised artifact missing from the tree.

## Nice To Have Before DOI

These improve the release but should not block v0.1 if the core is clean:

- one diagram of the reconstruction ladder;
- one diagram of the public evidence states;
- a concise glossary;
- a short "how to read this repo" page;
- a release-note file;
- one curated runnable script.

## Explicit Non-Blockers

These should not delay the first DOI:

- general quantum selector theorem;
- q >= 3 and more-outcome native lift;
- cross-site interlocking / CHSH weights;
- gravity sourcing;
- observer-lattice re-registration;
- continuum limit of interacting QFT;
- nature-facing prediction package.

They belong in the roadmap as open hinges, not in the release blocker list.

## Recommended Next Work Order

1. Rewrite the paper into a real v0.1 monograph draft.
2. Convert the claim register into release rows.
3. Add proof sketches to the theorem bank.
4. Clean source/evidence references.
5. Run the final public-scope audit.
6. Tag and archive.

The first public release should feel powerful because it is exact, not because
it says too much. Its strongest public shape is:

```text
finite contact -> counting -> gluing -> rational Born -> CHSH/Pell ->
native binary-Bell carrier -> scoped quantum-boundary theorem,
with all unearned generalizations left open by name.
```
