# Release Scripts

This directory contains small public-release hygiene scripts.

Run the release audit from the repository root:

```powershell
python scripts\release_audit.py
```

The audit is not a substitute for human review. It checks repeatable release
conditions: required files, citation and rights metadata, private-path leaks,
internal-process codenames, stale hold-status language, obvious overclaim
phrases, local Markdown links, and Git whitespace errors.

Mathematical verification is deliberately separate. Couple a verification path
to the hygiene audit only when that is useful:

```powershell
python scripts\release_audit.py --verification fast
python scripts\release_audit.py --verification full
```

The default audit never launches the full mathematical suite as a side effect.
