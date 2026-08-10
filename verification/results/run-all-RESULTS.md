# Shipped Verification Runner — RESULTS

Status: FAST PATH PASS
Script: `verification/scripts/run_all.py`
Command: `python verification/scripts/run_all.py --fast`
Date run: 2026-08-07
Environment: Windows / Python 3.13
Dependencies: Python standard library only
Observed runtime: 8 seconds

## Included scripts

The curated path ran 12 representative scripts:

- `no_jam_open_rule.py`
- `rational_born_gluing.py`
- `chsh_pell_boundary.py`
- `exact_gap_certificate.py`
- `nonexact_return_reconstruction.py`
- `negative_gram_holonomy.py`
- `mixed_state_exclusion.py`
- `rf_boundary.py`
- `causal_ceiling_family.py`
- `admission_forks.py`
- `spine_forks.py`
- `born_price.py`

## Results

All 12 scripts exited zero. Stable ending:

```text
ALL SHIPPED VERIFICATION: PASS  (12 scripts, 8s)
```

Verdict: FAST PATH PASS.

## Residuals

- This record covers the curated fast path, not all 80 result scripts.
- A full-suite PASS is not inferred from this run.
- Run `python verification/scripts/run_all.py` for complete shipped
  verification; use `--serial` only when one-at-a-time diagnostics are needed.
- Repository hygiene is a separate gate: `python scripts/release_audit.py`.
