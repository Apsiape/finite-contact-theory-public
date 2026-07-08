# Release Scripts

This directory contains small public-release hygiene scripts.

Run the release audit from the repository root:

```powershell
python scripts\release_audit.py
```

The audit is not a substitute for human review. It checks repeatable release
conditions: required files, citation and rights metadata, shipped verification,
private-path leaks, internal-process codenames, stale hold-status language,
obvious overclaim phrases, local Markdown links, and Git whitespace errors.
