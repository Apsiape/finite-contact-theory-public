# Chapter 17 — claim snapshot (as of the v0.17.0 release tag)

Five claim-register rows; live view in
[`docs/public-claim-register.md`](../../docs/public-claim-register.md).

## FCT-85 — The Price Field on the Atlas

- Status: `THEOREM / MODEL-SCOPE`
- Statement: ledger flow types the atlas cells — 00 PAID (settlement is
  a bought quotient; coagulation pays its whole state space), 10 FLAT,
  01 CREDIT, 11 MIXED: on the relocation model E = 2T over L = A₄,
  contact acts are permutations (history free) and the law quotient has
  maxfiber exactly 2 — the price of lawfulness is 1 bit, the retained
  central bit; the registration promotion is a 1-bit ledger
  transaction. The marks cell is the only floor whose ledger balances
  internally.
- Evidence: shipped — `mint_and_bill.py` §A.

## FCT-86 — The Funding Identity: Forced Fork, Mint = Bill

- Status: `THEOREM / MODEL-SCOPE` (lemma KNOWN-VARIANT: persistence/
  diamond, Winskel et al., cited; identity KNOWN: Mazurkiewicz/
  Cartier–Foata + Kahn–Kim, cited — the axiom-demotion and the
  accounting reading are the claims)
- Statement: all minted distinction is consumption-choice distinction;
  deterministic multi-step one-use floors do not exist (exhaustive:
  4752 floors — the fork-staging half of the central law is a theorem
  at model scope; the no-selector half remains the named postulate);
  admissible orderings per content class = the order-forgetting
  quotient's fiber exactly (mint = bill, class by class).
- Evidence: shipped — `mint_and_bill.py` §B.

## FCT-87 — The Cut Flow-Typed; the Debt Calculus Unified

- Status: `THEOREM / MODEL-SCOPE` (flow-typing PLAUSIBLY-NEW per blind
  sweep; two-part-code frame cited)
- Statement: the present is expensive because it is minted (exact
  reachable counts); paid cells erase their present at terminals, flat
  cells never grow one — the Cut is the signature of the mint. On the
  rivals, in Chapter 3's own vocabulary: order bits are future-inert
  for contact protocols (re-deriving Chapter 13's readability-of-order
  axiom as necessary); T-19's receipt bound = the ledger price of the
  floor's choice-to-outcome map, cell by cell; future-completeness =
  the mint is closed. The epistemic pillars are generic in form,
  flow-typed in bite.
- Evidence: shipped — `mint_and_bill.py` §C–D.

## FCT-88 — The Three-Column Cut: Constants as Registrations

- Status: `THEOREM / MODEL-SCOPE` (definition PLAUSIBLY-NEW per sweep;
  informal ancestors cited: Gell-Mann, Wheeler, Smolin, Weinberg,
  Müller)
- Statement: a constant is a fork-registration the law action inherits
  — underived (no equivariant selector at rule level), O(1)-readable
  from every window, paid once and replicated free (R = 1 vs decaying
  R for present bits). Law = derivable O(1) | constant = underived
  O(1) | present = underived Θ(N). Dissolves constants-omnipresence.
  Honesty note: the present-bit replication decay is established as a
  separation, not exhibited as a gradient, in the shipped model.
- Evidence: shipped — `mint_and_bill.py` §E.

## FCT-89 — The Two Bills

- Status: `MEASURED / MODEL-SCOPE / RECOVERY-VARIANT` (numeric
  discovery grade, labeled; organizing restatement of Hatano–Sasa /
  Speck–Seifert + Maroney + Kolchinsky–Wolpert, all cited; claimed
  sliver: the combinatorial merge price as the excess floor)
- Statement: a driven floor's steady-state dissipation is housekeeping
  (exploration; zero contraction; price-orthogonal); the ledger price
  floors the excess (erasure) bill only (Landauer face); the corners
  tune independently. The ledger prices selection and only selection.
- Evidence: shipped — `mint_and_bill.py` §F (labeled grade).
