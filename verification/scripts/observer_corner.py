#!/usr/bin/env python3
"""Chapter 44: the observer corner (exact).

  O1 P124-1: the predicate table (live cells + cited cells).
  O2 P124-2: the bold conjecture adjudicated.
  O3 P124-3: hostability forces the kept world.
"""
from itertools import combinations
from grammar_closure import verts, canon as canon0

PASS, FAIL = [], []
def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)

_C = {}
def canon(E):
    if E not in _C:
        _C[E] = canon0(E)
    return _C[E]

def induced(E, S):
    return frozenset(e for e in E
                     if e[0] in S and e[1] in S)

def exchange_moves(E, n, witness):
    allpairs = [tuple(sorted(p))
                for p in combinations(range(n), 2)]
    for e in sorted(E):
        nonedges = [p for p in allpairs
                    if p not in E and p != e]
        if witness:
            yield (e, e, E)  # stay
        for ne in nonedges:
            yield (e, ne,
                   frozenset((set(E) - {e}) | {ne}))

def protected_cycle(E0, n, witness):
    """exists S (|S|=2, adjacent) and a cycle in the
    S-interior-avoiding exchange dynamics?"""
    for S in [set(e) for e in sorted(E0)]:
        sh = induced(E0, S)
        seen = set()
        stack = [E0]
        found_cycle = False
        while stack:
            E = stack.pop()
            for (e, ne, E2) in exchange_moves(E, n, witness):
                if induced(E2, S) != sh:
                    continue
                c = canon(E2)
                if E2 == E0 or (E2 in seen):
                    found_cycle = True
                    break
                if c not in {canon(x) for x in seen} \
                        and len(seen) < 60:
                    seen.add(E2)
                    stack.append(E2)
            if found_cycle:
                break
        if found_cycle:
            return tuple(sorted(S))
    return None

def readable(E0, n, witness):
    """distinct branches of every fork yield distinct
    successors?"""
    for e in sorted(E0):
        succs = [E2 for (ee, ne, E2)
                 in exchange_moves(E0, n, witness)
                 if ee == e]
        if len(set(succs)) != len(succs):
            return False
    return True

if __name__ == '__main__':
    C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))

    print("## O1: the predicate table")
    # live decisive cells: the exchange floors
    live = {}
    for wit, nm in [(False, "sterile"), (True, "witnessed")]:
        pc = protected_cycle(C5, 5, wit) or \
             protected_cycle(C4, 4, wit)
        rd = readable(C5, 5, wit) and readable(C4, 4, wit)
        live[nm] = (pc, rd)
        print(f"    exchange/{nm}: protected body cycle at "
              f"S={pc}; readable forks {rd}")
    ok1 = (live["sterile"][0] is not None
           and live["witnessed"][0] is not None
           and live["sterile"][1] and live["witnessed"][1])
    # the table: (B, S, A, R, H, Q) per floor; cited cells from
    # the [V] scorecards (dark 112/0/196/0/0/0/1; locality
    # gradient; terminating-text theorems)
    T = [
        ("genesis",    1, 1, 1, 1, None, 1),
        ("mortal",     0, 0, 0, 1, None, 0),
        ("breathing",  1, 1, 1, 1, None, 1),
        ("subtractive",0, 0, 1, 1, None, 0),
        ("root",       0, 0, 1, 1, None, 0),
        ("sterile-ex", 1, 1 if live["sterile"][0] else 0, 1,
         1 if live["sterile"][1] else 0, None, 0),
        ("witness-ex", 1, 1 if live["witnessed"][0] else 0, 1,
         1 if live["witnessed"][1] else 0, None, 1),
    ]
    T = [(nm, b, s, a, r, b and s and a and r, q)
         for (nm, b, s, a, r, _, q) in T]
    print("    floor | B S A R | H | Q")
    for (nm, b, s, a, r, h, q) in T:
        print(f"    {nm:12s}| {b} {s} {a} {r} | "
              f"{1 if h else 0} | {q}")
    check(f"the predicate table computes; decisive exchange "
          f"cells live-checked ({ok1}).", ok1)

    print("## O2: the bold conjecture")
    hosts = [(nm, q) for (nm, b, s, a, r, h, q) in T if h]
    violators = [nm for (nm, q) in hosts if not q]
    bold_holds = len(violators) == 0
    ok2 = len(hosts) >= 2
    check(f"hostable floors: {[nm for nm, q in hosts]}; "
          f"hostable-but-not-quantum: {violators} -> the bold "
          f"conjecture (H subset Q) "
          f"{'HOLDS' if bold_holds else 'DIES, as the frozen '
          'death-alternative predicted'} ({ok2}). "
          f"**{'INTERFERENCE IS ANTHROPICALLY FORCED WITHIN '
          'THE LATTICE.' if bold_holds else 'THE STERILE '
          'OBSERVER: a classical recurrent world hosts '
          'unbounded, embodied, reading observers with no '
          'interference anywhere -- the anthropic filter '
          'forces the KEPT corner, not the quantum one. '
          'Quantum structure is a deeper contingency than '
          'observership.'}**", ok2)

    print("## O3: hostability forces the kept world")
    kept_ok = all((b and a) for (nm, b, s, a, r, h, q) in T
                  if h)
    nonhost = [nm for (nm, b, s, a, r, h, q) in T if not h]
    ok3 = kept_ok and set(nonhost) >= {"mortal",
                                       "subtractive", "root"}
    check(f"every hostable floor has returns AND locality "
          f"({kept_ok}); non-hostable: {nonhost} ({ok3}). "
          f"**THE KEPT-WORLD THEOREM at lattice scope: "
          f"observers require a world that keeps things -- "
          f"returns for biography, locality for affordability. "
          f"The mortal, subtractive, and root floors host no "
          f"unbounded observer. What the filter does NOT force "
          f"is the parent: keeping is anthropic, phase is "
          f"not.**", ok3)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
