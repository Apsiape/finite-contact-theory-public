# Chapter 11 — Freeze Record

| Field | Value |
|---|---|
| Chapter | 11 — The Clean Mixed-State Exclusion |
| Release tag | `v0.11.0` |
| Concept DOI | [10.5281/zenodo.21253591](https://doi.org/10.5281/zenodo.21253591) |
| Version DOI (v0.11.0) | [10.5281/zenodo.21368902](https://doi.org/10.5281/zenodo.21368902) |
| Chapter deposit DOI | none yet (optional; see `../README.md`) |
| Freeze date | 2026-07-15 |
| Claim rows | FCT-62 (the clean mixed-state exclusion, unconditional); FCT-61 residual updated (clean-core exclusion closed, apparatus-nuisance layer open) |
| Theorem rows | T-46 (the count witness equals the Gram determinant; `W = (2/9) det G ≥ 0`) |
| Shipped verification | `verification/mixed_state_exclusion.py` (frozen copy here, live copy in `/verification/scripts/`) |

This chapter closes the **clean core** of the open crux Chapter 10 named: no
partially-distinguishable Hilbert model, pure or mixed, can reproduce the
registered negative-Gram count vector, because the gauge-free count witness
`W = (2/9) det G` is nonnegative for every such model. It is an unconditional
theorem, not an empirical discovery. The apparatus-nuisance layer (multiphoton,
detector, transfer-matrix, drift) remains the external experimental gate, and
the Chapter-10 bridge premises are unchanged.

Freeze rule: after tagging, this directory does not change except to fill the
version-DOI and (if minted) chapter-deposit-DOI rows above in the tagging
commit itself. Corrections affecting this chapter are filed in
[`../../docs/correction-ledger.md`](../../docs/correction-ledger.md) and noted
in later release notes.
