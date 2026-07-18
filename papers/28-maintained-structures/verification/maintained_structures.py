#!/usr/bin/env python3
"""Chapter 28 -- Maintained Structures (public verifier).

Exact, exhaustive, dependency-free. A tracked substructure S of a
genesis-floor world, its preservation prices, its control-invariance
under adversarial scheduling, and the copy-construction dichotomy.
Language is deliberately structural (per the blind sweep's audit):
no biological claim is made anywhere in this chapter. Classical
frames cited in-line: context preservation in local graph rewriting
(double-pushout tradition), controlled invariance / safety games
(McNaughton; Zielonka), self-stabilization daemons (Dijkstra;
Dolev), and the constructor-theoretic asymmetry of copy formation
(von Neumann; Deutsch-Marletto). The chapter's own artifacts: the
exact preservation-price law with its unique witness, the exact
autonomy/cooperation dichotomy, and defect concentration.
"""
from itertools import combinations, product
from collections import deque
import math

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

def nb(E, v):
    return {b if a == v else a for a, b in E if v in (a, b)}

def contact_singles(E, a, b):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    return sorted((Na | Nb) - (Na & Nb))

def succ_max(E, a, b, assign, singles):
    Na = nb(E, a) - {b}
    Nb = nb(E, b) - {a}
    cap = Na & Nb
    S = {e for e in E if a not in e and b not in e}
    S.add((min(a, b), max(a, b)))
    for x in cap:
        S.add((min(a, x), max(a, x)))
        S.add((min(b, x), max(b, x)))
    for s in singles:
        S.add((min(assign[s], s), max(assign[s], s)))
    return frozenset(S)

def induced(E, S):
    return frozenset(e for e in E if e[0] in S and e[1] in S)

def interface(E, S):
    return frozenset(e for e in E if (e[0] in S) != (e[1] in S))

WORLDS = {
    "C6": frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
                     (0, 5))),
    "octahedron": frozenset(e for e in combinations(range(6), 2)
                            if e not in ((0, 3), (1, 4), (2, 5))),
    "K6-e": frozenset(e for e in combinations(range(6), 2)
                      if e != (0, 1)),
    "prism": frozenset(((0, 1), (1, 2), (0, 2), (3, 4), (4, 5),
                        (3, 5), (0, 3), (1, 4), (2, 5))),
}

def bodies(E, n=6):
    out = []
    for k in (2, 3, 4):
        for S in combinations(range(n), k):
            Sset = set(S)
            Ein = induced(E, Sset)
            if not Ein and k > 1:
                continue
            seen = {S[0]}
            stack = [S[0]]
            while stack:
                v = stack.pop()
                for x, y in Ein:
                    w = y if x == v else (x if y == v else None)
                    if w is not None and w not in seen:
                        seen.add(w)
                        stack.append(w)
            if seen == Sset:
                out.append(Sset)
    return out

if __name__ == '__main__':
    print("## 1: locality, the price law, and the unique witness")
    n_cases = 0
    loc_ok = price_ok = grip_ok = unique_ok = True
    for wname, E in WORLDS.items():
        for S in bodies(E):
            shape = induced(E, S)
            iface = interface(E, S)
            for (a, b) in E:
                n_cases += 1
                singles = contact_singles(E, a, b)
                k = len(singles)
                touching = a in S or b in S
                Ssing = [u for u in singles if u in S]
                parent = {u: (a if u in nb(E, a) else b)
                          for u in singles}
                pres = []
                anchor = 0
                for choice in product((a, b), repeat=k):
                    assign = dict(zip(singles, choice))
                    E2 = succ_max(E, a, b, assign, singles)
                    sh = induced(E2, S) == shape
                    if sh:
                        pres.append(assign)
                        if interface(E2, S) == iface:
                            anchor += 1
                    elif not touching:
                        loc_ok = False
                want = 2 ** (k - len(Ssing)) if touching else 2 ** k
                if len(pres) != want:
                    price_ok = False
                if touching:
                    for assign in pres:
                        for u in Ssing:
                            if assign[u] != parent[u]:
                                price_ok = False
                    proj = {tuple(a2[u] for u in Ssing)
                            for a2 in pres}
                    if Ssing and len(proj) != 1:
                        unique_ok = False
                want_anchor = (1 if touching
                               else 2 ** (k - len(Ssing)))
                if anchor != want_anchor:
                    grip_ok = False
    ok = loc_ok and price_ok and grip_ok and unique_ok
    check(f"across {n_cases} (substructure, contact) cases in 4 "
          f"worlds: external contacts never change E[S] (context "
          f"preservation, standard in local rewriting -- cited) "
          f"({loc_ok}); the E[S]-preserving assignments are exactly "
          f"the in-S-singles-stay-with-parent assignments, price = "
          f"|singles in S| bits with the witness UNIQUE on in-S "
          f"singles ({price_ok}, {unique_ok}); preserving E[S] AND "
          f"the labeled interface admits exactly ONE assignment for "
          f"every touching contact (boundary rigidity) ({grip_ok}) "
          f"({ok}). Shape is cheap -- one bit per exposed member -- "
          f"and boundary-fixing is total.", ok)

    print("## 2: control invariance (the autonomy result)")
    BODY = {0, 1, 2}
    SHAPE = frozenset(((0, 1), (1, 2)))
    def body_ok(E):
        return induced(E, BODY) == SHAPE
    def successors(E):
        out = {}
        for (a, b) in E:
            singles = contact_singles(E, a, b)
            Ssing = [u for u in singles if u in BODY]
            Osing = [u for u in singles if u not in BODY]
            touching = a in BODY or b in BODY
            base = {}
            if touching:
                for u in Ssing:
                    base[u] = a if u in nb(E, a) else b
            env_slots = Osing if touching else singles
            succs = []
            for choice in product((a, b), repeat=len(env_slots)):
                assign = dict(base)
                assign.update(dict(zip(env_slots, choice)))
                S2 = succ_max(E, a, b, assign, singles)
                if not body_ok(S2):
                    return None
                succs.append(S2)
            out[(a, b)] = succs
        return out
    W0 = frozenset(((0, 1), (1, 2), (3, 4), (4, 5), (3, 5),
                    (2, 3), (0, 5)))
    seen = {W0}
    stack = [W0]
    trans = {}
    inv_ok = True
    while stack:
        E = stack.pop()
        t = successors(E)
        if t is None:
            inv_ok = False
            break
        trans[E] = t
        for succs in t.values():
            for S2 in succs:
                if S2 not in seen:
                    seen.add(S2)
                    stack.append(S2)
    check(f"over the full reachable shape-locked space "
          f"({len(seen)} states, every contact, every environment "
          f"assignment) the stay-with-parent strategy keeps E[S] "
          f"invariant every time ({inv_ok}). The tracked "
          f"substructure is CONTROL-INVARIANT under any schedule "
          f"and any adversarial outside assignment, steering only "
          f"its own members (safety-game / controlled-invariance "
          f"frame, cited).", inv_ok)

    print("## 3: the copy-construction dichotomy")
    def is_target(E):
        return len(induced(E, {3, 4, 5})) == 2
    safe = {E for E in seen if not is_target(E)}
    changed = True
    while changed:
        changed = False
        drop = []
        for E in safe:
            for c, succs in trans[E].items():
                if not any(S2 in safe for S2 in succs):
                    drop.append(E)
                    break
        if drop:
            for E in drop:
                safe.discard(E)
            changed = True
    n_targets = sum(1 for E in seen if is_target(E))
    total_block = len(safe) == len(seen) - n_targets
    blocked = W0 in safe
    # cooperative reachability (full control), shortest witness:
    dist = {W0: 0}
    q = deque([W0])
    hit_steps = None
    while q:
        E = q.popleft()
        if is_target(E):
            hit_steps = dist[E]
            break
        for (a, b) in E:
            singles = contact_singles(E, a, b)
            for choice in product((a, b), repeat=len(singles)):
                S2 = succ_max(E, a, b, dict(zip(singles, choice)),
                              singles)
                if body_ok(S2) and S2 not in dist:
                    dist[S2] = dist[E] + 1
                    q.append(S2)
    ok = blocked and total_block and hit_steps == 1
    check(f"copy-construction of E[S] in the complement: the "
          f"adversarial-environment safe set contains ALL "
          f"{len(safe)} not-yet-copied states ({total_block}) -- a "
          f"hostile environment can prevent the copy forever from "
          f"everywhere, while the structure itself stays invariant "
          f"({blocked}); with a cooperative environment the copy is "
          f"reachable in {hit_steps} contact ({hit_steps == 1}) "
          f"({ok}). PERSISTENCE IS AUTONOMOUS; COPY-CONSTRUCTION "
          f"REQUIRES ENVIRONMENTAL COOPERATION -- an exact, "
          f"exhaustively-solved instance of the constructor-"
          f"theoretic asymmetry (von Neumann; Deutsch-Marletto, "
          f"cited), with the attractor/safe-set machinery classical "
          f"(cited).", ok)

    print("## 4: preservation cost concentrates at defects")
    def bill(E, S):
        out = []
        for (a, b) in E:
            singles = contact_singles(E, a, b)
            out.append(sum(1 for u in singles if u in S))
        return out
    k6e = WORLDS["K6-e"]
    free_body = {2, 3, 4}
    b_free = bill(k6e, free_body)
    wound_only = all(set(contact_singles(k6e, a, b)) <= {0, 1}
                     for (a, b) in k6e)
    c6_min = min(sum(bill(WORLDS["C6"], set(S)))
                 for S in combinations(range(6), 3)
                 if induced(WORLDS["C6"], set(S)))
    ok = (sum(b_free) == 0 and wound_only and c6_min > 0)
    check(f"in K6-e every contact's singles lie at the missing "
          f"edge's endpoints ({wound_only}), so a triangle avoiding "
          f"the defect has total preservation cost EXACTLY ZERO "
          f"({sum(b_free) == 0}); in the homogeneous C6 no size-3 "
          f"substructure is free (min total cost {c6_min} > 0) "
          f"({ok}). Preservation cost is not bought down by density "
          f"per se -- it CONCENTRATES AT DEFECTS: structures are "
          f"affordable where the world's irregularity is somewhere "
          f"else.", ok)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
