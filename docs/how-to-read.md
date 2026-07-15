# How To Read This Repository

Status: reader guide (current as of v0.10 — ten chapters).

## Start Here

Read in this order:

1. `README.md` for the public framing.
2. `papers/07-program-map/paper.md` for the whole-program map and the live
   ceiling (then any chapter that pulls you).
3. `papers/finite-contact-theory-v0.1.md` for the v0.1 release narrative.
3. `docs/mathematical-core.md` for the formal vocabulary.
4. `docs/theorem-bank.md` for theorem rows and proof sketches.
5. `docs/public-claim-register.md` for public claim labels and scopes.
6. `docs/correction-ledger.md` for what was killed, demoted, or narrowed.
7. `verification/evidence-manifest.md` for what evidence is shipped, cited,
   historical, or held.

## The Main Rule

Every claim is scoped. If a sentence sounds large, read its status label and
scope before reading it as a general claim.

Example:

```text
The quantum boundary is a floor theorem at binary-Bell finite carrier scope.
```

This does not mean:

```text
All quantum mechanics is derived.
```

## Evidence States

- `shipped`: runnable from this public repository;
- `cited`: locked private artifact or chapter is named but not copied;
- `historical`: provenance, not public-load-bearing;
- `held`: not public evidence yet.

## What To Reproduce First

Run:

```powershell
python verification\scripts\run_all.py
```

This checks the shipped public subset. It does not reproduce the full private
research corpus.

## What Not To Overread

This release does not claim:

- all physics is derived;
- the general quantum selector is solved;
- gravity sourcing is solved;
- the continuum limit of interacting QFT is solved;
- nature-facing predictions are ready for public betting.

It does claim a scoped, auditable reconstruction stack and a public method for
separating theorem, recovery, measurement, model-scope result, open hinge, and
withdrawal.
