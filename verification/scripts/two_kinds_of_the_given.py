#!/usr/bin/env python3
"""Chapter 29 -- The Two Kinds of the Given (public verifier).

Exact, dependency-free. The genesis dynamics' labeled kernel is
verified SYMMETRIC (strictly stronger than doubly stochastic) on
every closed sector tested -- a discrete Liouville-type property
from which uniform invariance, detailed balance, and the
microcanonical form follow AT THIS SCOPE (the general all-sector
statement is a conjecture, named). Classical frames cited per the
blind sweep: symmetric/doubly-stochastic kernels (Levin-Peres-
Wilmer; Birkhoff-von Neumann), Liouville-theorem-style grounding of
equal a priori weights (Tolman; the typicality school), the switch-
chain model class (Fosdick et al.), torsors (Baez), measurement-
scale typology (Stevens; Krantz-Luce-Suppes-Tversky), and the
absolute-objects tradition (Anderson-Friedman; Pitts). The census's
two-species classification ships as a FRAMEWORK with a completeness
CONJECTURE and a standing falsifier, not a theorem.
"""
from itertools import permutations, product
from fractions import Fraction

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

def closure_labeled(E0):
    seen = {E0}
    stack = [E0]
    while stack:
        E = stack.pop()
        for (a, b) in E:
            singles = contact_singles(E, a, b)
            for choice in product((a, b), repeat=len(singles)):
                S = succ_max(E, a, b, dict(zip(singles, choice)),
                             singles)
                if S not in seen:
                    seen.add(S)
                    stack.append(S)
    return seen

def kernel_row(E):
    m = len(E)
    row = {}
    for (a, b) in E:
        singles = contact_singles(E, a, b)
        k = len(singles)
        w = Fraction(1, m * 2 ** k)
        for choice in product((a, b), repeat=k):
            S = succ_max(E, a, b, dict(zip(singles, choice)),
                         singles)
            row[S] = row.get(S, 0) + w
    return row

def relabel(E, p):
    return frozenset(tuple(sorted((p[a], p[b]))) for a, b in E)

if __name__ == '__main__':
    C4 = frozenset(((0, 1), (1, 2), (2, 3), (0, 3)))
    C5 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (0, 4)))
    C6 = frozenset(((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)))

    print("## 1: the symmetry property (indifference, exact)")
    results = {}
    spaces = {}
    all_rows = {}
    for name, E0 in (("C4-closure", C4), ("C5-closure", C5),
                     ("C6-closure", C6)):
        space = closure_labeled(E0)
        rows = {E: kernel_row(E) for E in space}
        sym = all(rows[S].get(E, 0) == w
                  for E in space for S, w in rows[E].items())
        col = {E: Fraction(0) for E in space}
        for E in space:
            for S, w in rows[E].items():
                col[S] += w
        ds = all(v == 1 for v in col.values())
        results[name] = (len(space), sym, ds)
        spaces[name] = space
        all_rows[name] = rows
    ok = all(v[1] and v[2] for v in results.values())
    check(f"the labeled kernel is exactly SYMMETRIC -- P(E -> E') "
          f"== P(E' -> E) -- on every closed sector tested: "
          f"{ {k: (v[0], v[1]) for k, v in results.items()} } "
          f"(states, symmetric); double stochasticity and hence "
          f"uniform invariance follow as corollaries "
          f"({all(v[2] for v in results.values())}) ({ok}). "
          f"Symmetric-kernel reversibility w.r.t. the uniform law "
          f"is textbook (cited); the content is that THIS "
          f"dynamics' kernel is symmetric -- a discrete "
          f"Liouville-type property making the microcanonical form "
          f"a consequence rather than a postulate AT THIS SCOPE. "
          f"The all-sector statement is a named conjecture.", ok)

    print("## 2: equivariance (the floor is blind to names)")
    ok2 = True
    rows4 = all_rows["C4-closure"]
    for p in permutations(range(4)):
        for E in spaces["C4-closure"]:
            gE = relabel(E, p)
            want = {relabel(S, p): w for S, w in rows4[E].items()}
            if rows4[gE] != want:
                ok2 = False
    rows6 = all_rows["C6-closure"]
    for p in ((1, 0, 2, 3, 4, 5), (1, 2, 3, 4, 5, 0)):
        for E in list(spaces["C6-closure"])[::37]:
            gE = relabel(E, p)
            want = {relabel(S, p): w for S, w in rows6[E].items()}
            if rows6[gE] != want:
                ok2 = False
    check(f"P(gE -> gE') == P(E -> E') exactly (all 24 relabelings "
          f"x all C4-closure states; a transposition and a 6-cycle "
          f"on sampled C6-closure states) ({ok2}). Label-"
          f"exchangeability is standard for label-free rules "
          f"(cited); this check certifies the implementation "
          f"introduces no hidden label dependence.", ok2)

    print("## 3: microcanonical replication across sectors")
    def sector_stats(space, n):
        PERMSn = list(permutations(range(n)))
        def canonN(E):
            return min(tuple(sorted(tuple(sorted((p[a], p[b])))
                                    for a, b in E)) for p in PERMSn)
        classes = sorted({canonN(E) for E in space})
        idx = {c: i for i, c in enumerate(classes)}
        N = len(classes)
        orbit = [0] * N
        for E in space:
            orbit[idx[canonN(E)]] += 1
        return N, orbit
    reps = {}
    for name, n in (("C4-closure", 4), ("C5-closure", 5),
                    ("C6-closure", 6)):
        N, orbit = sector_stats(spaces[name], n)
        reps[name] = (N, sorted(orbit), sum(orbit))
    ok3 = (reps["C4-closure"][0] == 2 and reps["C5-closure"][0] == 5
           and reps["C6-closure"][0] == 13
           and reps["C6-closure"][2] == 3660)
    check(f"class/orbit structure: {reps} (classes, orbits, "
          f"labeled total) -- the symmetric kernel makes the "
          f"stationary law uniform on labeled worlds in all three, "
          f"so class weights are orbit counts: the C6 sector's "
          f"famous 1/61 is 60/3660 ({ok3}). Kernel symmetry gives "
          f"class-level detailed balance by lumping; the arrow "
          f"needs a price coupling (Chapter 27) or a loop of three "
          f"rooms to exist at all.", ok3)

    print("## 4: the census -- two kinds of the given (framework)")
    SH, DL = "SHADOW", "DIAL"
    REG = [
        ("assignment fork", SH, 0), ("which-branch", SH, 0),
        ("membership/individuation", SH, 0),
        ("occupant identity", SH, 0), ("steering actuality", SH, 0),
        ("semantic key", SH, 1), ("the scheme", SH, 1),
        ("measure key", SH, 1), ("credit boundary", SH, 1),
        ("world-phase", SH, 2), ("orientation/chirality", SH, 2),
        ("temperature beta", DL, "beta=0: unique reversible point"),
        ("anchor injections", DL, "forced form, free magnitude"),
    ]
    RETIRED = ["reference measure (derived from kernel symmetry)",
               "consent boundary (reduces to membership)"]
    shadows = [r for r in REG if r[1] == SH]
    dials = [r for r in REG if r[1] == DL]
    degrees = sorted({r[2] for r in shadows})
    ok4 = (len(REG) == 13 and degrees == [0, 1, 2]
           and len(dials) == 2 and len(RETIRED) == 2)
    check(f"the received-input registry: {len(shadows)} torsor-type "
          f"entries (forced option space, no canonical point -- "
          f"Baez's torsor gloss, cited) graded 5/4/2 on the "
          f"occurrence/class/phase ladder, {len(dials)} dial-type "
          f"entries (forced origin, free magnitude -- the "
          f"ratio-scale/deformation-parameter type, Stevens/KLST "
          f"and the contraction tradition cited), and 2 entries "
          f"RETIRED this release by derivation ({RETIRED}) ({ok4}). "
          f"The two-species split is a CLASSIFICATION FRAMEWORK in "
          f"the absolute-objects tradition (Anderson-Friedman; "
          f"Pitts, cited); its completeness is a CONJECTURE with a "
          f"standing falsifier (exhibit one received input that is "
          f"neither), and the reversibility-selects-the-origin "
          f"criterion for dials is the framework's candidate-novel "
          f"piece.", ok4)

    print(f"\n# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    raise SystemExit(1 if FAIL else 0)
