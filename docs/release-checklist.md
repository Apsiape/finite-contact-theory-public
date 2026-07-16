# Release Checklist

The reusable gate every release must pass before tagging. Copy this list into
the release notes draft and check every item there, so each release carries
its own completed gate. The v0.1-specific version of this gate is preserved as
[`release-roadmap.md`](release-roadmap.md).

Governance context: [`../EVOLUTION.md`](../EVOLUTION.md).

## 1. Scope freeze

- [ ] The release ceiling is stated in one paragraph.
- [ ] README, the chapter paper's abstract, the claim register, and the
      release notes all state the *same* ceiling.
- [ ] Everything beyond the ceiling is held open by name (roadmap or hold
      register).

## 2. Claim register

- [ ] Every new or changed row has: status label, scope, public statement,
      evidence class, source link, controls (or the reason controls do not
      apply), and residuals.
- [ ] Every row carries the weakest accurate label.
- [ ] Every status transition since the last tag is logged in its row with
      date and reason.
- [ ] No row was deleted; no ID was reused.

## 2a. Novelty protocol (prior-art gate)

- [ ] If the chapter enters a literature not swept by an earlier chapter, the
      Chapter-2 four-lens blind novelty search is **rerun** for the new
      subfield before tagging.
- [ ] The nearest published precedents are named in the chapter or in a
      companion related-work note tied to the claim register, and each result
      is graded recovery / sharpening / plausibly-new against them.
- [ ] Any result whose mechanism is standard is labeled recovery, not
      presented as new. (Prompted by C-18: Chapters 10-12 shipped into the
      quantum-optics literature without this gate; the retroactive fix is
      [`related-work-linear-optics.md`](related-work-linear-optics.md).)

## 3. Theorem bank

- [ ] New theorem rows have proof sketches or explicit `cited-only` marks.
- [ ] The dependency graph includes the new rows.
- [ ] Superseded rows point forward instead of being overwritten.

## 4. Corrections

- [ ] Every demotion, withdrawal, or meaning-changing wording fix since the
      last tag has a correction-ledger entry.
- [ ] Corrections affecting a frozen chapter are noted in these release notes
      with a pointer to the chapter.

## 5. Verification

- [ ] `python verification/scripts/run_all.py` passes on a **clean clone** on
      a machine other than the author's working tree.
- [ ] Every new shipped script has a results document under
      `verification/results/`.
- [ ] The evidence manifest is updated: every claim's evidence is classed
      `shipped`, `cited`, `historical`, or `held`.
- [ ] No public wording exceeds what the shipped subset supports.

## 6. Chapter

- [ ] The chapter directory follows the convention in
      [`../papers/README.md`](../papers/README.md) (paper, claims snapshot,
      frozen verification copies, RELEASE.md).
- [ ] The chapter is written against `docs/mathematical-core.md` vocabulary,
      with recovery anchors to standard literature named where they exist.
- [ ] The chapter states its own scope fence and what would falsify or demote
      its claims.

## 7. Rights

- [ ] All new text, figures, data, and scripts are rights-clean.
- [ ] No private working drafts, third-party material without permission, or
      raw notes are included.

## 8. Metadata

- [ ] `CHANGELOG.md` has the release section.
- [ ] `CITATION.cff` matches the new version and release date.
- [ ] `.zenodo.json` title, version, and description match the release.
- [ ] Release notes file exists (`RELEASE-NOTES-vX.Y.Z.md`).

## 9. Clean-clone audit

- [ ] All internal links resolve on a fresh clone.
- [ ] All DOI badges and citation blocks show the correct DOIs.

## 10. Tag and deposit

- [ ] Git tag `vX.Y.Z` created; GitHub release published.
- [ ] Zenodo version DOI minted and resolving.
- [ ] README citation section updated with the new version DOI.
- [ ] If the chapter gets its own Zenodo deposit, its DOI is recorded in the
      chapter's `RELEASE.md` and in the claim rows it carries.

## Zenodo Metadata (added after the v0.3.0–v0.7.0 round)

`.zenodo.json` controls the metadata Zenodo attaches to the deposit minted
from a tag. Without it, Zenodo copies the PREVIOUS version's metadata
(title/version drift — this happened to the v0.3.0–v0.7.0 deposits, whose
Zenodo-displayed titles need a one-time manual edit in the Zenodo UI).
Before tagging: bump `title` and `version` in `.zenodo.json` in the same
commit that bumps CITATION.cff.
