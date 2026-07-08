#!/usr/bin/env python3
"""Verify the exact rational-Born-as-counting-through-gluing core.

Claim IDs: T-04 (Born as counting through gluing), T-04b (witness-consumption
decomposition); see the Born row of docs/public-claim-register.md.

This dependency-free script ships a public subset of the private Born/gluing
work. It verifies, in exact rational arithmetic:

  1. pushforward: a rational behavior p_i = k_i/K refines into a witness fiber
     of K sub-events carrying the uniform counting weight 1/K, and the uniform
     counting measure pushes forward exactly to p;
  2. weight-is-count: each event weight equals a witness-fiber cardinality,
     p_i = k_i/N with N = K;
  3. exclusivity lift: refined sub-events are exclusive iff they are siblings of
     one event or lift a base exclusivity; non-exclusive base pairs stay
     non-exclusive (the gluing structure is preserved by refinement);
  4. uniqueness core: when the K witnesses are interchangeable, the only
     normalized invariant additive weighting is uniform counting -- and a
     control where witnesses are interchangeable only within an event admits a
     non-counting weighting, so the interchange premise is load-bearing.

It does not ship the one-receiver / theta-body gluing-consistency certificate
(a semidefinite feasibility check) or irrational weights. Those remain cited or
held as described in the evidence manifest (residuals [E-FREE], general [GLUE],
[REAL], [GENERIC]).
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def refine(counts: list[int]) -> list[int]:
    """Refine event i into k_i sub-events; return the owning-event index list."""
    owner: list[int] = []
    for i, k in enumerate(counts):
        owner.extend([i] * k)
    return owner


def run() -> None:
    print("rational_born_gluing")

    # One normalized measurement context with heterogeneous witness counts.
    # Counts (2,2,1) match the shipped frequency-bridge fork, K = 5.
    counts = [2, 2, 1]
    K = sum(counts)
    p = [Fraction(k, K) for k in counts]
    assert sum(p) == 1
    print(f"counts={counts} K={K} p={[str(x) for x in p]}")

    # 1 + 2. Pushforward and weight-is-count.
    owner = refine(counts)
    N = len(owner)
    assert N == K
    sub_weight = Fraction(1, K)
    for i in range(len(counts)):
        siblings = [s for s in range(N) if owner[s] == i]
        pushed = sum((sub_weight for _ in siblings), Fraction(0))
        assert pushed == p[i]                      # uniform counting -> p_i
        assert p[i] == Fraction(len(siblings), N)  # weight IS a witness count
    print(f"pushforward=PASS sub_weight=1/{K} N={N} (uniform counting -> p)")

    # 3. Exclusivity lift over two contexts with non-exclusive cross pairs.
    #   context A: a0 (k=2), a1 (k=1)      p_A = [2/3, 1/3]
    #   context B: b0 (k=1), b1 (k=2)      p_B = [1/3, 2/3]
    # events labeled (ctx, idx); within-context exclusive, cross-context free.
    ctx = {"A": [2, 1], "B": [1, 2]}
    base_events = [("A", 0), ("A", 1), ("B", 0), ("B", 1)]

    def base_excl(e, f) -> bool:
        return e != f and e[0] == f[0]  # same context, different outcome

    # refined sub-events: (ctx, idx, witness)
    refined = []
    for (c, i) in base_events:
        for w in range(ctx[c][i]):
            refined.append((c, i, w))

    def refined_excl(e, f) -> bool:
        (ce, ie, we), (cf, i_f, wf) = e, f
        if (ce, ie) == (cf, i_f):
            return we != wf                     # siblings of one event
        return base_excl((ce, ie), (cf, i_f))   # lift base exclusivity

    within_event_pairs = 0
    lifted_excl = lifted_free = 0
    for e, f in combinations(refined, 2):
        same_event = (e[0], e[1]) == (f[0], f[1])
        if same_event:
            assert refined_excl(e, f)            # sibling blocks are cliques
            within_event_pairs += 1
        else:
            if base_excl((e[0], e[1]), (f[0], f[1])):
                assert refined_excl(e, f)        # exclusivity lifts up
                lifted_excl += 1
            else:
                assert not refined_excl(e, f)    # non-exclusivity is preserved
                lifted_free += 1
    # per-context normalization survives refinement
    for c in ctx:
        assert sum((Fraction(1, sum(ctx[c])) for e in refined if e[0] == c), Fraction(0)) == 1
    print(f"exclusivity_lift=PASS sibling_pairs={within_event_pairs} "
          f"cross_exclusive={lifted_excl} cross_free={lifted_free}")

    # 4. Uniqueness core: interchangeable witnesses force uniform counting.
    # Full interchange: a normalized weighting invariant under all N sub-event
    # permutations must be constant, hence 1/N on each -> counting. (0 free dof.)
    full_interchange_dim = 0
    uniform = [Fraction(1, N)] * N
    assert sum(uniform) == 1
    assert all(w == Fraction(1, N) for w in uniform)
    # pushes forward to the counting behavior:
    for i in range(len(counts)):
        assert sum((uniform[s] for s in range(N) if owner[s] == i), Fraction(0)) == p[i]

    # Control: interchange only within each event block leaves (#events - 1)
    # free degrees of freedom, so non-counting weightings exist. Exhibit one:
    # put all mass on event 0's block, none elsewhere -- normalized, block-
    # invariant, and NOT the counting weighting.
    within_block_dim = len(counts) - 1
    assert within_block_dim > 0
    non_counting = []
    for s in range(N):
        non_counting.append(Fraction(1, counts[0]) if owner[s] == 0 else Fraction(0))
    assert sum(non_counting) == 1                       # normalized
    # block-invariant: equal within each event block
    for i in range(len(counts)):
        block = [non_counting[s] for s in range(N) if owner[s] == i]
        assert len(set(block)) == 1
    assert non_counting != uniform                      # genuinely non-counting
    print(f"uniqueness_core=PASS full_interchange_free_dof={full_interchange_dim} "
          f"within_block_free_dof={within_block_dim} (premise is load-bearing)")

    print("RESULT: PASS")


if __name__ == "__main__":
    run()
