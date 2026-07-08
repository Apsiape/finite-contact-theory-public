# Verification Curation Standard

Status: scaffold for public verification admission.

This standard defines what may enter `verification/scripts/` and
`verification/results/` in the public repository. The private repository remains
the working laboratory; this repository admits only curated, scoped, reproducible
verification artifacts tied to public claims.

## Admission States

- `ADMIT`: ready for public release.
- `ADMIT-LIMITED`: public at a stated scope, with named residuals or scale
  limits.
- `HOLD`: do not publish yet. The item may be valid internally, but needs
  sensitivity review, claim scoping, cleanup, or independent reproduction.
- `PRIVATE`: not a candidate for public release in its current form.
- `WITHDRAWN`: failed a gate and should be reflected in
  `docs/correction-ledger.md` if it affected a public claim.

Held-material verification is split. Scoped binary-Bell native-lift
artifacts may be reviewed for admission or citation; general selector,
cross-site interlocking, q >= 3, CHSH-weight, and unbanked certificate artifacts
remain `HOLD` until each has a separate public-scope review and release
decision. The public reconciliation list lives in
`docs/hold-register.md`.

## Public Script Admission

A public verification script must satisfy all of the following:

- It maps to one or more IDs in `docs/public-claim-register.md`.
- It runs from a clean clone using documented commands.
- It has no dependency on private modules, private paths, untracked local files,
  notebooks, hidden services, credentials, paid APIs, or network access.
- It declares its inputs, seeds, constants, parameter ranges, sample sizes, and
  stopping rules in the script header or an adjacent note.
- It separates registered checks from exploratory diagnostics.
- It includes controls or negative cases when the claim would otherwise be
  unfalsifiable.
- It exits nonzero, raises a clear assertion, or prints an unambiguous failure
  state when a registered gate fails.
- It writes only expected local artifacts, or explains why it writes none.
- It avoids large bundled data. If a data fixture is necessary, the fixture must
  be small, public, rights-clear, and checksum-addressed.

Scripts should prefer the Python standard library and exact arithmetic where
reasonable. Third-party packages are allowed only when they are pinned,
rights-compatible, and documented.

## Result Ledger Admission

Every admitted script should have a result ledger in `verification/results/`.
The ledger is a curated record, not a raw log dump. It should contain:

- claim ID and short name;
- script path and exact command;
- date run;
- environment summary, including OS, Python version, and dependency versions;
- frozen registration, including pass/fail thresholds set before the run;
- controls and why they can fail;
- expected runtime and observed runtime;
- result summary with pass, fail, open, or limited-scope labels;
- residuals, caveats, and post-hoc diagnostics clearly marked;
- checksum or commit reference for the script version when available.

Large tables, raw transcripts, exhaustive logs, and scratch notes should stay
private unless a public reviewer needs them and they pass the privacy and
rights checks below. Public ledgers should quote only the minimum output needed
to make the result auditable.

## Frozen Registrations

Frozen registrations are the public guard against moving targets. Before a
script is first used as evidence for a public claim, record:

- the claim being tested;
- the exact inputs and parameters;
- random seeds or seed-generation rule;
- success thresholds;
- failure thresholds and kill conditions;
- controls and null cases;
- what result labels are possible;
- what will count only as exploratory or post-hoc.

If a script is corrected after first run, keep the old result state visible in
the ledger or correction ledger, explain the correction, and rerun with a new
registration block.

## Controls

Controls are required when the result supports an `EXTENSION`, `MODEL-SCOPE`, or
high-load-bearing `THEOREM` claim. A control should be able to fail the intended
interpretation. Examples of acceptable controls include:

- shuffled, randomized, or symmetry-broken inputs;
- known null models;
- deliberately non-counting or non-admissible variants;
- independent implementations of a small case;
- exact enumeration against a stochastic or sampled procedure;
- ablations that remove the proposed mechanism.

Controls that pass too easily should be named as weak controls, not promoted as
decisive evidence.

## Runtime and Scale

Public scripts should be runnable by a reviewer on a commodity laptop unless the
ledger says otherwise. Each script must declare:

- expected wall-clock time;
- expected memory class;
- whether runtime is deterministic or seed-dependent;
- any slow mode, exhaustive mode, or optional stress test;
- a shorter smoke-test command when the full run is long.

Default public targets:

- smoke tests: under 60 seconds;
- standard verification: under 10 minutes;
- extended verification: allowed only with explicit runtime and scale notes.

Long private runs, large exploratory sweeps, and machine-specific performance
claims stay private unless reduced to a public, reproducible subset.

## Dependencies

Dependencies must be public, installable, and minimal. Each admitted item should
state one of:

- standard library only;
- `requirements.txt` or equivalent pinned dependency set;
- exact external tool versions.

No public script may require private packages, credentials, local absolute paths,
closed datasets, hidden environment variables, or undocumented manual steps.
Network access is disallowed for verification unless the claim itself is about a
public network resource and the ledger records date, URL, checksum, and fallback
behavior.

## Reproducibility

A reviewer should be able to reproduce the result from a clean clone by following
the ledger. Reproducibility requires:

- deterministic seeds, exact enumeration, or recorded seed rules;
- platform-sensitive behavior called out explicitly;
- stable output labels that can be compared without reading raw logs;
- all generated public artifacts either ignored, regenerated, or documented;
- no reliance on private repository state.

For stochastic tests, report the registered seed set and the rule for extending
it. Do not silently replace failed seeds after seeing results.

## What Stays Private

The following do not enter the public repository:

- private working drafts, rough drafts, and untriaged notes;
- raw blind-review transcripts unless separately cleared;
- large raw logs and bulk generated tables;
- sensitive private-process details, including held verification;
- private local paths, machine names, credentials, tokens, and hidden services;
- unpublished personal information or third-party confidential material;
- exploratory failures not yet scoped for the correction ledger;
- scripts that depend on private theory files or private helper modules.

Private material may inform a public ledger, but the public artifact must be a
fresh curation with scoped claims, minimal quoted output, and clear residuals.

## Review Checklist

Before admission, confirm:

- claim ID exists or is being added with a status label;
- script command works from a clean clone;
- registration was frozen before the evidence run;
- controls are present or the ledger explains why none are needed;
- runtime and dependencies are declared;
- result labels match the public claim scope;
- sensitive or private material has been removed;
- failures, demotions, or withdrawals are reflected in
  `docs/correction-ledger.md` when applicable.
