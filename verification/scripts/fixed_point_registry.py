#!/usr/bin/env python3
"""Chapter 56: the fixed point and the five receipts (exact).

Standard library only. Three groups:
  X1  The Beth model pair re-checked (the cell-admission fork's witness).
  X2  The received-input registry: exactly five entries, each matched to its
      long-standing program face; no sixth entry.
  X3  The routing-departure witness: the loop-instrument values on the
      regrouped process tensors, computed exactly by cycle counting on the
      wiring diagrams -- aligned terms give 1, cross terms give d^2 = 4, the
      causally separable mixture averages to 5/2.
"""
from fractions import Fraction as F

fails = []
def check(label, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" {detail}" if detail else ""))
    if not ok:
        fails.append(label)

# ---- X1: Beth pair (compact re-check) ----
Stage = {"a", "w"}; Lawful = {"a", "w"}; AARG = {"a"}; Real = {"a"}
def lawful(Adm):
    return AARG <= Adm and Real <= Adm and Adm <= (Stage & Lawful)
check("X1 Beth pair: two lawful expansions over one reduct disagree on admissibility",
      lawful({"a"}) and lawful({"a", "w"}) and {"a"} != {"a", "w"})

# ---- X2: the registry ----
REGISTRY = {
    "hereditary world orientation": "one received arrow (retention direction)",
    "polarization/chirality": "a received point of the polarization sphere",
    "world-phase": "the conserved closure-class receipt",
    "genealogy policy": "carry-or-collapse of coherence receipts",
    "absolute physical scale": "the calibration anchor",
}
check("X2a exactly five received world inputs", len(REGISTRY) == 5)
check("X2b no balancing entry (BMS resolved into the genealogy tower)",
      not any("balanc" in k for k in REGISTRY))
check("X2c provenance and closure hypotheses are not world inputs",
      not any(k.startswith(("RIA", "H_C")) for k in REGISTRY))

# ---- X3: loop-instrument values by exact cycle counting ----
# Wiring model: ports live in row and column copies. Every process/instrument
# component is a set of weighted wires (perfect-matching edges) on the port
# copies; the contraction value is (prod of weights) * d^(#closed cycles).
d = 2

def loop_value(process_wires, preps):
    """process_wires: list of frozensets of port-copy names forming the union
    matching (each port-copy appears exactly twice across the full list);
    preps: number of 1/d normalization weights. Value = d^cycles / d^preps."""
    # build adjacency: each port-copy node has exactly two incident wires
    from collections import defaultdict
    adj = defaultdict(list)
    for idx, wire in enumerate(process_wires):
        a, b = tuple(wire)
        adj[a].append((idx, b))
        adj[b].append((idx, a))
    seen_wires = set()
    cycles = 0
    for start in list(adj):
        if all(i in seen_wires for i, _ in adj[start]):
            continue
        # walk the cycle
        node = start
        first_unused = next(i for i, _ in adj[node] if i not in seen_wires)
        wire_idx = first_unused
        while True:
            seen_wires.add(wire_idx)
            nxt = next(b for i, b in adj[node] if i == wire_idx)
            node = nxt
            unused = [i for i, _ in adj[node] if i not in seen_wires]
            if not unused:
                cycles += 1
                break
            wire_idx = unused[0]
    return F(d) ** cycles / F(d) ** preps

def W_wires(order, tag):
    """Process wires for W^{A<B} (order='AB') or W^{B<A} (order='BA'),
    on parties tagged by `tag` (e.g. '' or 'p' for the primed copy).
    Components (row r / column c copies):
      prep at earlier-party input: wire (X_I.r -- X_I.c), weight 1/d (counted via preps)
      channel earlier-out -> later-in: wires (E_O.r -- L_I.r), (E_O.c -- L_I.c)
      identity at later-party output: wire (L_O.r -- L_O.c)
    """
    A, B = ("A" + tag, "B" + tag)
    E_, L_ = (A, B) if order == "AB" else (B, A)
    return [
        frozenset({f"{E_}_I.r", f"{E_}_I.c"}),
        frozenset({f"{E_}_O.r", f"{L_}_I.r"}),
        frozenset({f"{E_}_O.c", f"{L_}_I.c"}),
        frozenset({f"{L_}_O.r", f"{L_}_O.c"}),
    ]

def loop_instrument_wires():
    """The regrouped loop instrument: Alice holds (A, A'), Bob holds (B, B').
    Alice wires A_I -> A'_O and A'_I -> A_O; Bob wires B_I -> B'_O and
    B'_I -> B_O. Each identity wire contributes row and column edges."""
    out = []
    for src, dst in [("A_I", "Ap_O"), ("Ap_I", "A_O"), ("B_I", "Bp_O"), ("Bp_I", "B_O")]:
        out.append(frozenset({f"{src}.r", f"{dst}.r"}))
        out.append(frozenset({f"{src}.c", f"{dst}.c"}))
    return out

def value(order1, order2):
    wires = W_wires(order1, "") + W_wires(order2, "p") + loop_instrument_wires()
    return loop_value(wires, preps=2)   # one prep per process factor

v_ab_ab = value("AB", "AB")
v_ba_ba = value("BA", "BA")
v_ab_ba = value("AB", "BA")
v_ba_ab = value("BA", "AB")
check("X3a aligned terms give 1", v_ab_ab == 1 and v_ba_ba == 1, f"({v_ab_ab}, {v_ba_ba})")
check("X3b cross terms give d^2 = 4 (the double causal loop)", v_ab_ba == 4 and v_ba_ab == 4,
      f"({v_ab_ba}, {v_ba_ab})")
avg = (v_ab_ab + v_ab_ba + v_ba_ab + v_ba_ba) / 4
check("X3c the separable mixture's self-tensor evaluates to 5/2 (invalid as a process)",
      avg == F(5, 2), f"(= {avg})")

print(f"fixed_point_registry: {'ALL PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}")
raise SystemExit(0 if not fails else 1)
