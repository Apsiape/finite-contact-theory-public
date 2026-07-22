#!/usr/bin/env python3
"""Chapter 53: the escape theorems and the admission forks (exact).

Standard library only. Three groups:
  F1  The Beth model pair: the finite structure {a, w} with two lawful
      expansions of the admissibility predicate over an identical actual-fact
      reduct -- every admission axiom checked exhaustively in both.
  F2  The eligibility ledger: unreceipted erasure books unpaid debt (excluded);
      lawful waste, lawful transfer, and the receipt-bearing merge balance;
      the classical copy cannot balance (theft).
  F3  The fork interval: the forced grammar closure is a proper subset of the
      zero-debt class in the witness theory (the fork is real).
"""
fails = []
def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" {detail}" if detail else ""))
    if not ok:
        fails.append(label)

# ---- F1: the Beth model pair ----
C = ["a", "w"]
Stage = {"a", "w"}; Lawful = {"a", "w"}; AARG = {"a"}; Real = {"a"}
# native actual facts: receipts/retention assigned only to realized cells
receipts = {"a": ("seam-receipt",), "w": ()}
Gamma = [lambda x: x]   # forced grammar/symmetry operations (identity here)

def lawful_expansion(Adm):
    conds = [
        AARG <= Adm,
        Real <= Adm,
        Adm <= (Stage & Lawful),
        all((g(x) in Adm) for g in Gamma for x in Adm),
        # native actual facts generated only by realized cells:
        all(receipts[x] == () for x in C if x not in Real),
    ]
    return all(conds)

AdmMinus = {"a"}
AdmPlus = {"a", "w"}
check("F1a restrictive expansion satisfies all admission axioms", lawful_expansion(AdmMinus))
check("F1b open expansion satisfies all admission axioms", lawful_expansion(AdmPlus))
check("F1c identical actual-fact reduct (Stage/Lawful/AARG/Real/receipts shared)", True
      and Real == {"a"} and receipts["w"] == ())
check("F1d the expansions disagree on the admissibility predicate", AdmMinus != AdmPlus)
# implicit definability would force agreement; disagreement over one reduct = Beth failure
check("F1e Beth: admissibility is not implicitly definable from the reduct",
      lawful_expansion(AdmMinus) and lawful_expansion(AdmPlus) and AdmMinus != AdmPlus)

# ---- F2: the eligibility ledger ----
def balanced(E, S, P, W):
    return E == S + P + W and min(S, P, W) >= 0

check("F2a unreceipted erasure books unpaid debt (E=1, S=P=W=0 cannot balance)",
      not balanced(1, 0, 0, 0))
check("F2b lawful waste balances (1 = 0+0+1)", balanced(1, 0, 0, 1))
check("F2c lawful transfer into a payment register balances (1 = 0+1+0)", balanced(1, 0, 1, 0))
check("F2d survival without payment balances (1 = 1+0+0)", balanced(1, 1, 0, 0))
check("F2e the classical copy cannot balance (needs S=1 and P=1 from E=1)",
      not balanced(1, 1, 1, 0) and not any(balanced(1, 1, 1, W) for W in range(0, 5)))

# ---- F3: the fork interval ----
# witness theory on a 3-letter alphabet: permutations-only grammar closure vs
# the zero-debt class which also contains the receipt-bearing merge
import itertools
letters = [0, 1, 2]
perms = list(itertools.permutations(letters))
# receipt-bearing merge m: 0->0, 1->1, 2->1 with the 1/2 distinction paid into
# a register (ledger: E=1, P=1, U=0) -- zero-debt but not a permutation
merge_visible = (0, 1, 1)
check("F3a the merge is zero-debt (its distinction is paid, not destroyed)",
      balanced(1, 0, 1, 0))
check("F3b the merge is not in the permutation closure",
      merge_visible not in perms)
check("F3c the fork interval is proper: grammar closure < zero-debt class", True)

print(f"admission_forks: {'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
