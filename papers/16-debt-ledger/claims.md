# Chapter 16 — claim snapshot (as of the v0.16.0 release tag)

Three claim-register rows; live view in
[`docs/public-claim-register.md`](../../docs/public-claim-register.md).

## FCT-82 — The Exchange Rate of Irreversibility

- Status: `THEOREM / MODEL-SCOPE / RECOVERY` (Lecerf 1963 / Bennett 1973
  for the dilation; Maslov–Dueck 2003/04 for the minimal-garbage formula —
  the chapter's own open question converted to a citation by the blind
  sweep)
- Statement: a non-injective act admits no whole-product permutation lift
  on any fixed finite ancilla (counting; slice-correct lifts fail under
  composition), one fresh one-use register per step always suffices, and
  the minimal fresh-register alphabet is exactly maxfiber(f) — so the
  n-fork collapse act prices at exactly log2 n fresh bits. The price is
  submultiplicative under composition; permutation acts keep price 1
  under every respected quotient, while an absorbing-state mortality
  notion is quotient-discontinuous (the act-price sees through it).
- Evidence: shipped — `debt_ledger.py` §1.

## FCT-83 — The Ledger Inequality: Waste Possible, Theft Impossible

- Status: `THEOREM / MODEL-SCOPE / RECOVERY-VARIANT` (entropy/support
  forms are the classical grouping bound, cited; the packaged composition
  form and its waste/theft reading are the packaging)
- Statement: for any history w on a finite state set,
  log2|S| ≤ log2|im w| + Σ price(f_k), exactly — with equality achieved
  by aligned uniform merges and strict waste exhibited (a merge re-paying
  for already-destroyed distinction). Distinction is never destroyed
  unpaid. Entropy form H(f(X)) ≥ H(X) − log2 maxfiber (grouping bound,
  labeled RECOVERY; support form exact-exhaustive).
- Evidence: shipped — `debt_ledger.py` §2.

## FCT-84 — The Refused Debt: Selection Priced by Counting Alone

- Status: `THEOREM / MODEL-SCOPE` (composition claim: pre-probabilistic
  derivation route; nearest thermodynamic prior art Cabello–Gu–Gühne–
  Larsson–Wiesner PRA 94, 052127 (2016), cited and distinguished — their
  result needs probabilities, Landauer, and finite memory; this needs
  none of the three)
- Statement: for the n-fork, the dilation register alphabet, the
  promotion-record alphabet, and the binary-question identification depth
  are one number (n; ceil(log2 n) in binary units): collapse cost = query
  cost = record cost. Exhaustively, every act resolving an n-fork to one
  actual pays maxfiber = n, and partial resolution to k images pays at
  least ceil(n/k). The no-selector law is a refused debt: lawlike
  (injective) evolution is exactly the debt-free sector, and any
  completion that selects books exactly log2 n. The program's recurring
  ceil(log2 n) — selector debt, actualization debt, promotion records,
  garbage registers — is one conserved ledger entry.
- Evidence: shipped — `debt_ledger.py` §2.
