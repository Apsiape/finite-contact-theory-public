# Release Notes: v0.1.0

Title: Finite Contact Theory v0.1: Growing the Bell/CHSH Quantum Boundary from a
Finite One-Use Floor.

Status: release notes for the first public snapshot.

## The Release Ceiling

The whole release ceiling is a single sentence, quoted identically in the
README, the paper, and the claim register:

> Finite Contact Theory is a finite reconstruction program with a scoped
> theorem stack — from one-use contact to counting, to one-receiver gluing, to
> rational Born weights, to the CHSH/Pell boundary, to a carrier grammar grown
> from one-use contact — under which the quantum boundary is a floor theorem at
> **binary-Bell finite-carrier scope**, with every unearned generalization left
> open by name.

## What This Release Is

This release is a scoped public extraction of Finite Contact Theory — the first
published chapter of a long-range reconstruction program. It is designed to be
citable, auditable, and conservative about claim strength: bold about the one
result it proves, explicit about everything it holds open.

The release contains:

- a finite-contact theory spine;
- public status labels and claim discipline;
- a correction ledger;
- a mathematical core;
- a theorem-bank index with proof sketches;
- a v0.1 technical-note draft;
- a small shipped verification subset;
- a roadmap of open hinges.

## Strongest Public Stack

```text
finite contact
  -> witness counting
  -> one-receiver gluing
  -> rational Born weights
  -> CHSH/Pell boundary structure
  -> native binary-Bell carrier lift
  -> scoped quantum-boundary theorem
```

The last line means binary-Bell finite carrier scope. It does not mean all of
quantum mechanics has been derived.

## Shipped Verification

Run:

```powershell
python verification\scripts\run_all.py
```

Current shipped checks:

- `no_jam_open_rule.py`
- `frequency_bridge_exchangeable.py`
- `native_lift_binary_bell.py`

larger private research ledgers remain cited, historical, or held according to
`verification/evidence-manifest.md`.

## Main Open Hinges

- general quantum selector;
- q >= 3 and more-outcome carrier lift;
- cross-site interlocking and CHSH weights;
- gravity sourcing;
- observer-lattice re-registration;
- nature-facing prediction package;
- continuum limit of interacting QFT.

## Rights

Licensed under CC BY-NC-ND 4.0: share with attribution, no commercial use, no
distribution of derivative works. For commercial use or derivatives, contact
the author. See `LICENSE.md`.
