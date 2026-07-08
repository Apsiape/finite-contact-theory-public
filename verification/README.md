# Verification

This directory holds clean verification scripts and result ledgers tied to
public claims.

For the current evidence posture, see
[evidence-manifest.md](evidence-manifest.md).

## Admission Rule

A verification item should include:

- a short claim ID from `docs/public-claim-register.md`;
- exact run instructions;
- expected runtime;
- dependency notes;
- frozen inputs or parameters;
- controls and kill conditions;
- a result ledger that states what passed, failed, or remained open.

## Layout

```text
verification/scripts/
  Runnable scripts.

verification/results/
  Result ledgers, logs, or summarized outputs tied to scripts.

verification/evidence-manifest.md
  Evidence posture for shipped, cited, historical, and held sources.
```

See [verification-standard.md](verification-standard.md) for admission rules.

## Current Packaging Posture

The first release may cite some private verification ledgers before copying
them into this repository. A claim is public-load-bearing only when its evidence
status says one of the following:

- `shipped`: script and result ledger are included here;
- `cited`: private artifact is named, but not yet shipped;
- `historical`: included only as provenance, not as release evidence;
- `held`: not used as public evidence.

Held-material native-lift material now has a small shipped public core plus
cited private evidence. Sliwa-41 rerun artifacts remain `held` unless copied or
precisely cited as imported recovery.
