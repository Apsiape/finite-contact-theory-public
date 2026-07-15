# Chapter 12 — Freeze Record

| Field | Value |
|---|---|
| Chapter | 12 — The Exact Quantum Count Regions and the Limits of Counting |
| Release tag | `v0.12.0` |
| Concept DOI | [10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591) |
| Version DOI (v0.12.0) | pending mint (recorded here in the tagging commit) |
| Chapter deposit DOI | none yet (optional; see `../README.md`) |
| Freeze date | 2026-07-15 |
| Claim rows | FCT-63 (n=3 complete region + negative-Gram boundary); FCT-64 (n=4 9-simplex + central insufficiency + six laws); FCT-65 (n=5 emergent qubit + rebit-blindness + K₅); FCT-66 (single-source ℝ/ℂ/ℍ no-go); FCT-67 (sequential closure + registered conjugation witness). FCT-61/FCT-62 residuals cross-referenced (Ch11 inequality = the n=3 boundary; FCT-61 protocol reduces to tritter counts). |
| Theorem rows | T-47 (n=3/4 exact regions); T-48 (n=5 emergent qubit + rebit-blindness); T-49 (single-source ℝ/ℂ/ℍ counting no-go); T-50 (sequential closure exposes σ_y + the conjugation gap) |
| Shipped verification | `verification/count_regions.py` (frozen copy here, live copy in `/verification/scripts/`) |

Standalone quantum-information mathematics (no theory buy-in) that also upgrades
Chapters 10–11: the negative-Gram inequality is *the* complete boundary of
quantum three-photon tritter statistics. The region theorems are proof-backed
and independently reproduced; the conjugation-witness is a **registered,
experiment-open** protocol with a precisely named target model class — not a
performed experiment and not a claim about nature.

Freeze rule: after tagging, this directory does not change except to fill the
version-DOI and (if minted) chapter-deposit-DOI rows above in the tagging commit
itself. Corrections affecting this chapter are filed in
[`../../docs/correction-ledger.md`](../../docs/correction-ledger.md) and noted
in later release notes.
