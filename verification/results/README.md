# Verification Results

Status: scaffold for public result ledgers.

This directory holds curated result ledgers for public verification scripts. A
ledger should make the result reproducible and interpretable without exposing
private scratch work or large raw output.

Held-material verification is split. Native-lift and scoped binary-Bell
artifacts may be added after public-scope review. General selector,
cross-site, q >= 3, CHSH-weight, and unbanked certificate artifacts remain
`HOLD`.

## Ledger Naming

Use stable, claim-oriented names:

```text
<claim-id>-<short-name>-RESULTS.md
```

If a result is exploratory, limited, or withdrawn, keep that state in the title
or the first status line.

## Required Ledger Fields

Each result ledger should include:

- claim ID and short name;
- status: `PASS`, `FAIL`, `OPEN`, `LIMITED`, `HOLD`, or `WITHDRAWN`;
- script path under `verification/scripts/`;
- exact run command;
- date run;
- expected runtime and observed runtime;
- dependency summary;
- frozen registration;
- controls;
- result summary;
- residuals and caveats;
- post-hoc diagnostics, if any, explicitly labeled;
- reproduction notes for a clean clone.

## Template

```text
# <Short name> - RESULTS

Claim ID:
Status:
Script:
Command:
Date run:
Environment:
Dependencies:
Expected runtime:
Observed runtime:

## Frozen Registration

- Claim under test:
- Inputs and parameters:
- Seeds or enumeration rule:
- Success gate:
- Failure gate:
- Controls:
- Exploratory-only outputs:

## Results

- Registered checks:
- Controls:
- Verdict:

## Residuals

- Scope limits:
- Known caveats:
- Follow-up:

## Reproduction

1. Start from a clean clone.
2. Install the declared dependencies.
3. Run the command above.
4. Compare the stable output labels with this ledger.
```

## Curation Rules

- Summarize results; do not paste full raw logs.
- Keep large tables private unless they are essential and rights-clear.
- Mark failed gates plainly.
- Mark post-hoc explanation as post-hoc.
- Do not include private paths, machine-specific secrets, local usernames,
  hidden services, or credentials.
- Do not include held held material while it remains on `HOLD`.
- Link failures, demotions, and withdrawals to `docs/correction-ledger.md` when
  they affect public claims.

## Current Contents

Admitted public result ledgers:

- `FCT-09-no-jam-open-rule-RESULTS.md`
- `FCT-10-frequency-bridge-exchangeable-RESULTS.md`
- `T-04-rational-born-gluing-RESULTS.md`
- `FCT-16-chsh-pell-boundary-RESULTS.md`
- `FCT-17-FCT-18-native-lift-binary-bell-RESULTS.md`
- `run-all-RESULTS.md`
- `release-audit-RESULTS.md`
