# Verification Scripts

This directory contains the live shipped verification scripts for the public
theory. The scripts use Python's standard library and exact arithmetic unless a
script states a narrower numerical role in its own header.

Run the curated 12-script path for quick confidence:

```powershell
python verification\scripts\run_all.py --fast
```

Run all 80 result scripts only when a complete validation is actually needed:

```powershell
python verification\scripts\run_all.py
```

Add `--serial` to either command for deterministic one-at-a-time execution.
The default is parallel execution with at most eight workers and one progress
line per script.

`run_all.py` is intentionally independent of `scripts/release_audit.py`.
Repository hygiene does not imply mathematical verification, and mathematical
verification does not imply that the public wording, links, metadata, or scope
fences are clean.

The authoritative inventory is the `SCRIPTS` list in `run_all.py` and the
evidence classification in `verification/evidence-manifest.md`. Material not
admitted to the public evidence package remains outside this runner.
