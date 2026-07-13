# Chapter 7 — Claim Snapshot (as of the v0.7.0 release tag)

This file freezes the claim-register rows this chapter rests on, exactly as
they stand at the release tag. The *live* view — including any later
promotion, demotion, or withdrawal — is the
[public claim register](../../docs/public-claim-register.md). If the two ever
differ, the register is current and this snapshot is historical; that is by
design.

| ID | Short name | Status | Scope | Evidence state |
|---|---|---|---|---|
| FCT-42 | The two-axis public stack (index claim) | `PROGRAM / INDEX` | Exactly FCT-01..41 / T-01..32 as labeled | `shipped` (by reference to the full suite) |
| FCT-43 | The forced/received schema | `PROGRAM / SCHEMA` | Shipped instances named; generalization cited | `shipped` instances + `cited` schema |
| FCT-44 | The no-selector recurrence | `PROGRAM / SCHEMA` | T-19 shipped; recurrence across shipped rows checkable; reading cited | `shipped` instances + `cited` schema |

Full row text, verbatim from the register at the tag, follows.

---

## FCT-42 - The Two-Axis Public Stack

Status: `PROGRAM / INDEX`
Scope: the public repository at the v0.7.0 tag — claim rows FCT-01..FCT-41,
theorem rows T-01..T-32, organized as a quantum-facing axis (chapters 1–2)
and a finite-epistemics axis (chapters 3–6).
Evidence state: `shipped` by reference — the full `run_all.py` suite
(ten scripts) passes on a clean clone.

Public statement:

The published program is exactly its rows: each is runnable or cited as
labeled, each carries its own scope and residuals, and the chapter-7 map
adds no claim beyond the organization itself. Falsified by any row failing
its shipped check or misstating its scope.

Evidence:

- shipped: the entire verification suite; the release audit.

Checks / controls:

- `run_all.py` (chapters 1–6 scripts) and `release_audit.py` both pass at
  the tag.

Residuals:

- the map's architecture commentary (how the axes meet) is exposition, not
  a claim row.

## FCT-43 - The Forced/Received Schema

Status: `PROGRAM / SCHEMA`
Scope: shipped instances named below; the program-level generalization is
cited research posture.
Evidence state: `shipped` instances + `cited` schema.

Public statement:

Across every published chapter, what the finite structure forces is
grammar, signs, order, exact biconditionals, and exact constants of form
(the `ceil(log2 m)` debt, `EC = H + KL + O`, the heap identities, the
helix monodromy); what it never forces is a selection — which alternative,
which origin, which magnitude. Shipped instances: T-18/T-19, T-23, T-26.
The generalization — that this forced/received split is the deep structure
of physical law — is a schema, not a shipped theorem, and carries this
label precisely so it cannot be read above its evidence.

Evidence:

- shipped: the named theorem rows;
- cited: the private program's forced/received boundary corpus.

Checks / controls:

- each named instance has its own shipped check.

Residuals:

- no criterion is shipped for classifying an arbitrary new structure as
  forced or received; the schema earns rows only through new scoped
  theorems.

## FCT-44 - The No-Selector Recurrence

Status: `PROGRAM / SCHEMA`
Scope: T-19 shipped; its recurrence across shipped rows checkable; the
program-level reading cited.
Evidence state: `shipped` instances + `cited` schema.

Public statement:

One obstruction arrives at every level examined: a symmetry-respecting
rule cannot select a point of a symmetric fiber (T-19). Any actual
selection — an origin of time (T-26), an actual alternative, a unit or
scale (cited) — must be received, and its record costs at least
`ceil(log2 m)` bits, refined by the second law of asking (T-23) and run
forward as the ledger arrow (T-28). The reading of selection as the single
received residue of physics is cited posture, labeled as such.

Evidence:

- shipped: T-19, T-23, T-26, T-28;
- cited: the private no-selector corpus (multiple independent arrivals).

Checks / controls:

- the shipped instances are machine-checked; the recurrence is checkable
  by reading the rows together.

Residuals:

- "every level examined" is bounded by the published chapters; new levels
  must earn their own rows.
