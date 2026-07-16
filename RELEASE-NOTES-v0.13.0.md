# Release Notes — v0.13.0

**A governance and prior-art release. No new scientific claim; the live
release ceiling is unchanged from v0.12.**

This release acts on an independent read of the public repository. It
hardens the program's novelty discipline where it had a gap, confronts the
quantum-optics prior art that Chapters 10–12 build on, and aligns the
front-page framing with the live ceiling. Every theorem, claim row, and
shipped script is unchanged; what changes is what is cited, how the novelty
of Chapters 10–12 is graded, and one governance gate.

## What changed

**Added:**

- `docs/related-work-linear-optics.md` — a prior-art companion note that
  applies the Chapter-2 blind novelty protocol, retroactively, to the
  multiphoton-interference / partial-distinguishability / real-vs-complex
  literature that Chapters 10–12 enter. It records a 15-reference must-cite
  list (Tichy, Shchesnovich, de Guise, Tillmann, Menssen, Brod–Galvão,
  Seron–Novo–Cerf, Bapat–Sunder, Drury, Dittel, Renou, McKague, and others),
  grades each Chapter 10–12 result **recovery / sharpening / plausibly-new**
  against them, and identifies the surviving citable contributions (the
  specific closed forms and, most of all, the `n=5` count-region geometry).
- Correction **C-18** — logs that Chapters 10–12 shipped without a
  related-work section because the novelty protocol was not rerun on the
  quantum-optics pivot; records the retroactive fix and the regrade.
- Release-checklist **§2a (novelty protocol gate)** — any chapter entering a
  literature not previously swept must rerun the four-lens blind search and
  name nearest precedents before tagging.
- `RELEASE-NOTES-v0.13.0.md` (this file).

**Changed:**

- `README.md` — the front-page headline is realigned from "Reality, rebuilt"
  to the accurate framing ("a finite reconstruction program … grow the
  machinery of physics … run every proof"), matching the live ceiling; a
  "Recoveries, honestly named" paragraph now points to the Chapter-10–12
  prior-art note; the status section states v0.13.0 as a governance release
  with the ceiling unchanged.
- `docs/public-claim-register.md` — **FCT-45** gains an explicit
  starting-datum disclosure: the public forcing chain of Chapter 8 begins at
  the *retained interface*; why exactly the three quarter-turns are retained
  (the floor-level chirality/selection upstream) is `cited` from the private
  corpus, not shipped. This names the program's deepest current corpus
  dependency in the register itself.
- `CITATION.cff`, `.zenodo.json`, `CHANGELOG.md` — refreshed to v0.13.0.

**Not changed:** every chapter directory (all frozen), every claim row's
proof status, all seventeen shipped scripts, and the v0.12 live ceiling
(verbatim in the README, the claim register, the Chapter-12 paper, and the
v0.12.0 notes).

## Release gate (checklist, this release)

- **Scope freeze** — ceiling unchanged; stated identically where required;
  everything beyond it still held open by name. ✔
- **Claim register** — no new/changed claim rows except the FCT-45 residual
  disclosure (weakest-accurate label preserved; no ID reused, none deleted). ✔
- **Theorem bank** — no new theorem rows. ✔
- **Corrections** — C-18 filed for the novelty-protocol gap; no chapter
  frozen text altered (the regrade is a novelty grade, not a theorem
  withdrawal), and the affected chapters are pointed to from C-18 and the
  companion note. ✔
- **Verification** — no new shipped script; `run_all.py` (seventeen scripts)
  still passes on a clean clone. ✔
- **Chapter** — N/A (no new chapter this release). ✔
- **Rights** — all new text is rights-clean; no private drafts or raw notes
  included; the private corpus is *named*, not copied. ✔
- **Metadata** — CHANGELOG, CITATION.cff, `.zenodo.json`, and this notes
  file updated. ✔
- **Clean-clone audit** — `scripts/release_audit.py` passes (required files,
  canonical ceilings verbatim, overclaim scan, links, shipped verification,
  whitespace). ✔
- **Novelty protocol (§2a)** — this release *is* the retroactive application
  of the gate to Chapters 10–12. ✔

## Why this is a release, not a patch

The prior-art confrontation is genuine scholarship: it moves large parts of
Chapters 10–12 from implicitly-novel to explicitly-recovery, supplies the
citations a referee in photonic quantum information would require, and
narrows the program's real contribution in that line to a short, honest
list. Making that record citable — and installing the gate that prevents the
gap from recurring — is exactly the kind of correction the program treats as
progress.
