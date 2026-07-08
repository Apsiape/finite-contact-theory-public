# Shipped Verification Subset - RESULTS

Status: PASS  
Script: `verification/scripts/run_all.py`  
Command: `python verification/scripts/run_all.py`  
Date run: 2026-07-07  
Environment: Windows, Python 3.13.12  
Dependencies: Python standard library only  
Expected runtime: under 30 seconds  
Observed runtime: 0.2722391 seconds

## Included Scripts

- `verification/scripts/no_jam_open_rule.py`
- `verification/scripts/frequency_bridge_exchangeable.py`
- `verification/scripts/rational_born_gluing.py`
- `verification/scripts/chsh_pell_boundary.py`
- `verification/scripts/native_lift_binary_bell.py`

## Results

Stable ending:

```text
ALL SHIPPED VERIFICATION: PASS
```

Verdict: PASS.

## Residuals

This is a small public verification subset. It does not replace the locked
private research corpus. Larger solver-heavy, long-run, or scope-sensitive
artifacts remain `cited` or `held` in `verification/evidence-manifest.md`.
