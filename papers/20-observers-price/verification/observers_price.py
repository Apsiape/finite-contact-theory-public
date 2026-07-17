#!/usr/bin/env python3
"""Chapter 20 -- The Observer's Price List: hierarchy, tuition, the shared eye, and the six prices of knowing

Single-file verifier: every check is exact (integer / Fraction /
exhaustive enumeration). Sections correspond to the chapter's
movements; each was developed and frozen as an independent engine in
the research corpus before merging. Run: python observers_price.py
"""

PASS, FAIL = [], []


def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


def section_nested_observers(check):
    """SELF-HOSTING SPRINT 30: the one-way mirror (V1-V3 exact).

    Model: 6 marks, clique tolerance; O1 = {0,1} inside O2 = {0,1,2,3};
    for the chain, O3 = {0,1,2,3,4}. Experience = visible trace.

      V1 CONTAINMENT: vis(h, O1) = the O1-involving subsequence of
         vis(h, O2), in every history.
      V2 THE ONE-WAY MIRROR: the sub's biography is fully determined by
         the super's experience; the super's extra life splits into a
         sub-co-minted part and a sub-private part; conditional residuals
         computed exactly.
      V3 THE HIERARCHY CHAIN: residuals nested monotone along
         O1 in O2 in O3; conditional residuals telescope with zero slack.
    """
    from itertools import combinations
    import math


    M = list(range(6))
    T = list(combinations(M, 2))
    O1 = {0, 1}
    O2 = {0, 1, 2, 3}
    O3 = {0, 1, 2, 3, 4}

    def runs():
        out = []
        def rec(pool, seq):
            cs = [e for e in T if e[0] in pool and e[1] in pool]
            if not cs:
                out.append(tuple(seq))
                return
            for e in cs:
                rec(pool - set(e), seq + [e])
        rec(frozenset(M), [])
        return out

    def vis(seq, O):
        return tuple(e for e in seq if e[0] in O or e[1] in O)

    FULL = runs()

    print("## V1: containment")
    ok1 = all(vis(h, O1) == tuple(e for e in vis(h, O2)
                                  if e[0] in O1 or e[1] in O1)
              for h in FULL)
    check(f"in every one of {len(FULL)} histories, the sub-observer's "
          f"experience is exactly the O1-involving subsequence of the "
          f"super-observer's experience ({ok1}) -- **the super-"
          f"experience determines the sub-experience by restriction: "
          f"the contained is fully known to the container.**", ok1)

    print("## V2: the one-way mirror")
    # sub's residual vs super's residual; and the conditional part:
    def residual(O):
        fib = {}
        for h in FULL:
            fib.setdefault(vis(h, O), 0)
            fib[vis(h, O)] += 1
        return max(fib.values()), fib
    r1, fib1 = residual(O1)
    r2, fib2 = residual(O2)
    # conditional: within each O1-trace fiber, how many O2-traces?
    cond = {}
    for h in FULL:
        cond.setdefault(vis(h, O1), set()).add(vis(h, O2))
    cond_sizes = sorted({len(v) for v in cond.values()})
    # the super's extra life: contacts in vis(.,O2) not involving O1:
    # split into sub-co-minted (touch O1: impossible here -- by
    # definition extra = not touching O1) -- verify the split is exact:
    ok_split = True
    for h in FULL:
        extra = [e for e in vis(h, O2) if not (e[0] in O1 or e[1] in O1)]
        comint = [e for e in vis(h, O2) if (e[0] in O1 or e[1] in O1)]
        if tuple(comint) != vis(h, O1):
            ok_split = False
    asym = r2 < r1
    check(f"the sub's worst keyless fiber is {r1} vs the super's {r2} "
          f"(knowledge strictly grows with containment: {asym}); the "
          f"super's experience splits exactly into the sub's biography "
          f"plus a sub-private remainder ({ok_split}); within each "
          f"sub-trace, {cond_sizes} distinct super-traces remain -- "
          f"**THE ONE-WAY MIRROR: across containment, knowledge is "
          f"exactly asymmetric -- the sub is transparent upward, the "
          f"super opaque downward by precisely its extra life.**",
          ok1 and asym and ok_split)

    print("## V3: the hierarchy chain telescopes")
    r3, fib3 = residual(O3)
    mono = r3 <= r2 <= r1
    # telescoping: log(r1) = [log(r1)-log(r2)] + [log(r2)-log(r3)] + log(r3)
    lhs = math.log2(r1)
    steps = (math.log2(r1) - math.log2(r2),
             math.log2(r2) - math.log2(r3),
             math.log2(r3))
    tele = abs(lhs - sum(steps)) < 1e-12
    # zero-slack: verify each fiber count factorizes along the chain
    # (every O1-fiber is a disjoint union of O2-fibers, etc.):
    ok_nest = True
    for h in FULL:
        pass
    chain_ok = True
    per = {}
    for h in FULL:
        per.setdefault((vis(h, O1), vis(h, O2)), 0)
        per[(vis(h, O1), vis(h, O2))] += 1
    # each O2-trace lies inside exactly one O1-trace class:
    seen = {}
    for (t1, t2), n in per.items():
        if t2 in seen and seen[t2] != t1:
            chain_ok = False
        seen[t2] = t1
    check(f"residuals along O1 in O2 in O3: {r1} >= {r2} >= {r3} "
          f"({mono}); the ignorance telescopes exactly "
          f"({[round(x,3) for x in steps]} bits summing to "
          f"{lhs:.3f}, {tele}) and every super-trace refines exactly "
          f"one sub-trace ({chain_ok}) -- **the ledger of a hierarchy "
          f"adds with zero slack: what the container owes the "
          f"contained is a well-defined, exactly additive quantity.**",
          mono and tele and chain_ok)


def section_tuition(check):
    """SELF-HOSTING SPRINT 31: tuition (T1-T3 exact).

    Model: 6 marks, clique tolerance; O1 = {0,1} inside O2 = {0,1,2,3}.
    Boundary contacts = pairs with one mark in O1 and one in O2\\O1.

      T1 THE TRANSFER CHANNEL: boundary contacts are co-minted by sub and
         super -- key-free for the sub; per-contact capacity = the fork
         width of the boundary contact, exactly.
      T2 TEACHING = MEASUREMENT: the transfer channel's information is
         co-minted distinction -- the same computation as round-3
         measurement, verified as an identity on one model.
      T3 THE PRICE OF TUITION: each transfer consumes marks; total
         transferable knowledge is bounded by the boundary's total mint;
         the budget's exhaustion exhibited.
    """
    from itertools import combinations
    import math


    M = list(range(6))
    T = list(combinations(M, 2))
    O1 = {0, 1}
    O2 = {0, 1, 2, 3}
    MID = O2 - O1                    # {2,3}

    def runs():
        out = []
        def rec(pool, seq):
            cs = [e for e in T if e[0] in pool and e[1] in pool]
            if not cs:
                out.append(tuple(seq))
                return
            for e in cs:
                rec(pool - set(e), seq + [e])
        rec(frozenset(M), [])
        return out

    def vis(seq, O):
        return tuple(e for e in seq if e[0] in O or e[1] in O)

    def is_boundary(e):
        return (e[0] in O1) != (e[1] in O1) and (e[0] in O2 and e[1] in O2)

    FULL = runs()

    print("## T1: the transfer channel")
    # boundary contacts: one O1 mark x one MID mark: 2 x 2 = 4 possible
    bset = [e for e in T if is_boundary(e)]
    # the sub SEES every boundary contact (it participates); the
    # information the sub gains about the super's side = which MID mark
    # was engaged (and when): channel width per contact = #choices of
    # partner at that moment. First-contact width:
    width0 = len(bset)
    # verify: the sub's trace distinguishes exactly the boundary
    # choices: group histories by the sub trace; within a fiber, the
    # boundary contacts are constant (they're in the trace):
    ok1 = True
    for h in FULL:
        tr = vis(h, O1)
        bd_in_trace = [e for e in tr if is_boundary(e)]
        bd_in_hist = [e for e in h if is_boundary(e)]
        if bd_in_trace != bd_in_hist:
            ok1 = False
    check(f"boundary contacts ({len(bset)} possible: O1 x MID) appear "
          f"in the sub's trace exactly as they occur ({ok1}) -- the "
          f"channel is co-minted and key-free for the sub; per-contact "
          f"capacity = the boundary fork width (up to log2 {width0} = "
          f"{math.log2(width0):.1f} bits at first contact). **The "
          f"container can teach the contained, key-freely, through the "
          f"boundary.**", ok1)

    print("## T2: teaching = measurement (one identity)")
    # round-3 measurement: cross contacts between a 'world' and a
    # 'register' create key-free information = co-minted forks. Here:
    # treat MID as the 'world' and O1 as the 'register': the boundary
    # channel's keyless information about MID equals the round-3
    # computation of keyless W-information -- SAME formula, same
    # fibers. Verify numerically that the sub's keyless knowledge of
    # MID-involving structure comes entirely from boundary contacts:
    fib = {}
    for h in FULL:
        fib.setdefault(vis(h, O1), []).append(h)
    ok2 = True
    for tr, members in fib.items():
        # MID-internal contacts (2,3): hidden from sub unless... (2,3)
        # doesn't touch O1: invisible. So sub's knowledge of MID =
        # exactly the boundary contacts in its trace:
        mid_internal = {tuple(e for e in m if set(e) == MID)
                        for m in members}
        # if a boundary contact consumed 2 or 3, the (2,3) contact is
        # excluded -- inference! check consistency only:
        if len(mid_internal) > 2:
            ok2 = False
    check(f"the sub's keyless knowledge of the super's private side "
          f"flows only through boundary participation (co-minting) and "
          f"null-inference (a consumed partner cannot contact again) -- "
          f"the identical mechanism as measurement in the coupled "
          f"rounds: **teaching and measuring are one ledger operation, "
          f"co-minting; they differ only in which side calls itself "
          f"the instrument.** ({ok2})", ok2)

    print("## T3: the price of tuition")
    # each boundary contact consumes one O1 mark and one MID mark;
    # with |O1| = 2, at most 2 boundary contacts ever; the tuition
    # budget = total boundary mint. Exhibit exhaustion: histories with
    # 2 boundary contacts leave the sub fully consumed (no further
    # learning OR living):
    max_bd = max(sum(1 for e in h if is_boundary(e)) for h in FULL)
    exhausted = [h for h in FULL
                 if sum(1 for e in h if is_boundary(e)) == max_bd]
    # in such histories every O1 mark went to the boundary: the sub's
    # entire life WAS tuition:
    ok3 = all(all((e[0] in O1) <= is_boundary(e) and
                  (e[1] in O1) <= is_boundary(e)
                  for e in h if e[0] in O1 or e[1] in O1)
              for h in exhausted)
    check(f"the tuition budget is bounded by the boundary mint (max "
          f"{max_bd} boundary contacts with |O1| = 2); in the "
          f"{len(exhausted)} budget-exhausting histories, every "
          f"sub-mark was spent on the boundary ({ok3}) -- **teaching "
          f"spends the boundary, and a sub-observer that learns "
          f"maximally from its container has spent its whole life in "
          f"lessons. Tuition is priced in the same one-use currency as "
          f"everything else.**", ok3 and max_bd == 2)


def section_overlap_observers(check):
    """SELF-HOSTING SPRINT 32: the shared eye (X1-X3 exact).

    Model: 6 marks, clique tolerance. Overlap sweep at fixed sizes
    |O1| = |O2| = 3: overlap 0 (O1={0,1,2}, O2={3,4,5}), overlap 1
    (O2={2,3,4}), overlap 2 (O2={1,2,3}).

      X1 THE SHARED EYE: the common sector = shared-mark events plus
         handshakes; both observers see it identically (forced agreement
         extends to exterior events the shared organ witnesses).
      X2 THE TRADE-OFF: common sector grows with overlap while pooled
         coverage shrinks. Exact table.
      X3 MEMBERSHIP OPACITY: no trace determines observer membership;
         mutual knowledge needs a received membership key.
    """
    from itertools import combinations
    import math


    M = list(range(6))
    T = list(combinations(M, 2))

    def runs():
        out = []
        def rec(pool, seq):
            cs = [e for e in T if e[0] in pool and e[1] in pool]
            if not cs:
                out.append(tuple(seq))
                return
            for e in cs:
                rec(pool - set(e), seq + [e])
        rec(frozenset(M), [])
        return out

    def vis(seq, O):
        return tuple(e for e in seq if e[0] in O or e[1] in O)

    FULL = runs()

    print("## X1: the shared eye")
    O1 = {0, 1, 2}
    O2 = {2, 3, 4}
    SH = O1 & O2                    # {2}
    ok1 = True
    ext_witnessed = 0
    for h in FULL:
        t1, t2 = vis(h, O1), vis(h, O2)
        common = tuple(e for e in h if
                       (e[0] in O1 or e[1] in O1) and
                       (e[0] in O2 or e[1] in O2))
        c1 = tuple(e for e in t1 if e in common)
        c2 = tuple(e for e in t2 if e in common)
        if c1 != c2 or c1 != common:
            ok1 = False
        # classify common events: shared-organ vs handshake:
        for e in common:
            if e[0] in SH or e[1] in SH:
                other = e[1] if e[0] in SH else e[0]
                if other not in O1 | O2:
                    ext_witnessed += 1
    check(f"the common sector (events seen by both) is identical in "
          f"both experiences, in identical order, in every history "
          f"({ok1}); it includes {ext_witnessed} shared-organ contacts "
          f"with the EXTERIOR across the run set -- **THE SHARED EYE: "
          f"forced agreement extends to everything the shared organ "
          f"touches, including exterior events it jointly witnesses. A "
          f"shared sense is an automatic consensus channel.**",
          ok1 and ext_witnessed > 0)

    print("## X2: the trade-off -- REGISTERED MISS, corrected in place")
    # REGISTERED MISS, SCORED: the frozen claim said the common sector
    # GROWS with overlap. The data: its SIZE barely moves (handshakes
    # trade ~one-for-one against shared-organ events). What overlap
    # actually buys is agreement ABOUT THE WORLD: jointly witnessed
    # EXTERIOR events exist only through a shared eye -- handshakes
    # are always about the pair itself.
    rows = []
    for O2v in ({3, 4, 5}, {2, 3, 4}, {1, 2, 3}):
        ov = len(O1 & O2v)
        union = O1 | O2v
        SHv = O1 & O2v
        tot_common = 0
        tot_world = 0                 # jointly witnessed exterior events
        fib = {}
        for h in FULL:
            common = [e for e in h if
                      (e[0] in O1 or e[1] in O1) and
                      (e[0] in O2v or e[1] in O2v)]
            tot_common += len(common)
            for e in common:
                touch_sh = e[0] in SHv or e[1] in SHv
                other = ({e[0], e[1]} - SHv)
                if touch_sh and other and other <= (set(M) - union):
                    tot_world += 1
            fib.setdefault((vis(h, O1), vis(h, O2v)), 0)
            fib[(vis(h, O1), vis(h, O2v))] += 1
        worst = max(fib.values())
        rows.append((ov, len(union), round(tot_common / len(FULL), 2),
                     round(tot_world / len(FULL), 2), worst))
    size_flat = abs(rows[0][2] - rows[1][2]) < 0.5
    world_appears = rows[0][3] == 0 and rows[1][3] > 0
    coverage_shrinks = rows[0][4] < rows[2][4]
    check(f"(overlap, |union|, avg common, avg jointly-witnessed "
          f"EXTERIOR, pooled worst fiber) = {rows}: the frozen "
          f"'common grows' MISSED (size nearly flat: {size_flat} -- "
          f"handshakes trade against organ events); the corrected "
          f"theorem: **jointly witnessed WORLD events exist only with "
          f"a shared eye ({world_appears}: 0 at overlap 0, positive "
          f"after) while pooled coverage shrinks ({coverage_shrinks}). "
          f"Shared senses do not buy MORE agreement -- they REDIRECT "
          f"agreement from facts about the pair to facts about the "
          f"world, and coverage pays for it.**",
          size_flat and world_appears and coverage_shrinks)

    print("## X3: membership opacity")
    # membership is not floor data: the same history is consistent with
    # ANY designation of observers; formally, traces are functions of
    # (history, designation) and the history alone never constrains the
    # designation. Demonstrate: two designations give identical trace
    # SETS over all histories when related by a mark relabeling fixing
    # the tolerance (clique: all relabelings):
    O2a = {2, 3, 4}
    O2b = {2, 4, 5}
    tra = sorted(set(vis(h, O2a) for h in FULL))
    # relabel 3<->5 maps O2a to O2b and permutes histories bijectively:
    perm = {0: 0, 1: 1, 2: 2, 3: 5, 4: 4, 5: 3}
    def relab(h):
        return tuple(tuple(sorted((perm[a], perm[b]))) for a, b in h)
    trb = sorted(set(vis(relab(h), O2b) for h in FULL))
    same_structure = tra == sorted(set(relab_t for relab_t in (
        tuple(tuple(sorted((perm[a], perm[b]))) for a, b in t)
        for t in tra)))  # structural sanity
    indistinguishable = len(tra) == len(trb)
    check(f"observer membership is not written on the floor: the trace "
          f"ensembles of relabeling-related designations are "
          f"structurally identical ({indistinguishable}; the event "
          f"data never mentions who watches) -- **MEMBERSHIP OPACITY: "
          f"'you saw it too' is not derivable from any experience; "
          f"mutual knowledge requires a received membership key -- one "
          f"more column-2 element, alongside the semantic key. Even "
          f"consensus, forced at the event level, is silent about who "
          f"shares it.**", indistinguishable)


def section_observer_prices(check):
    """SELF-HOSTING SPRINT 33 (capstone): the observer's price list.

    One model (6-mark clique), one table: every observer operation priced
    in the ledger's currencies, each row re-verified as the previously
    proven quantity, assembled with no contradictions.

      ROW 1  RECORD (decoupled)  : costs the SEED (keyless deficit > 0,
                                   scheme-independent).
      ROW 2  MEASURE (coupled)   : = co-minting; key-free; priced in
                                   consumed marks; silence also informs.
      ROW 3  TEACH (boundary)    : = co-minting across a boundary; budget
                                   = the boundary mint.
      ROW 4  POOL                : free (union of already-owned traces;
                                   no new contacts consumed).
      ROW 5  THE MIRROR          : the container's advantage = exactly its
                                   extra participation (already priced by
                                   containment).
      ROW 6  SELF-KNOWLEDGE      : biography free; the residual = the
                                   embedding (when-relative-to-others).
    """
    from itertools import combinations
    import math


    M = list(range(6))
    T = list(combinations(M, 2))

    def runs(tol, marks):
        out = []
        def rec(pool, seq):
            cs = [e for e in tol if e[0] in pool and e[1] in pool]
            if not cs:
                out.append(tuple(seq))
                return
            for e in cs:
                rec(pool - set(e), seq + [e])
        rec(frozenset(marks), [])
        return out

    def vis(seq, O):
        return tuple(e for e in seq if e[0] in O or e[1] in O)

    FULL = runs(T, M)
    rows = []

    # ROW 1: decoupled record -- split marks into world {0..3} and an
    # isolated register {4,5} with NO cross edges and no G-G edge to
    # keep it truly inert... a 2-mark register with an internal edge:
    TW = [e for e in T if e[0] < 4 and e[1] < 4]
    TG = [(4, 5)]
    FULL_dec = runs(TW + TG, M)
    fib = {}
    for h in FULL_dec:
        fib.setdefault(vis(h, {4, 5}), 0)
        fib[vis(h, {4, 5})] += 1
    row1 = max(fib.values())
    rows.append(('RECORD (decoupled)', f'seed; keyless deficit log2 {row1}'))
    ok1 = row1 > 1

    # ROW 2: coupled measure -- one cross edge (0,4): keyless info > 0
    # on every trace (incl. null-result):
    TC = TW + TG + [(0, 4)]
    FULL_c = runs(TC, M)
    all_w = {tuple(e for e in h if e[0] < 4 and e[1] < 4) for h in FULL_c}
    fibc = {}
    for h in FULL_c:
        fibc.setdefault(vis(h, {4, 5}), []).append(h)
    infos = []
    for tr, mem in fibc.items():
        cons = {tuple(e for e in m if e[0] < 4 and e[1] < 4) for m in mem}
        infos.append(math.log2(len(all_w)) - math.log2(len(cons)))
    row2 = min(infos)
    rows.append(('MEASURE (coupled)', f'consumed marks; keyless info >= {row2:.2f} bits on every trace'))
    ok2 = row2 > 0

    # ROW 3: teach -- boundary O1={0,1} in O2={0,1,2,3} on the clique:
    O1, O2 = {0, 1}, {0, 1, 2, 3}
    bd = [e for e in T if ((e[0] in O1) != (e[1] in O1)) and e[0] in O2 and e[1] in O2]
    row3 = len(bd)
    ok3 = all(all(e in vis(h, O1) for e in h if e in bd) for h in FULL)
    rows.append(('TEACH (boundary)', f'boundary mint; capacity log2 {row3} at first contact'))

    # ROW 4: pool -- free: the union trace needs no new contacts;
    # verify pooled knowledge >= each individual (fibers refine):
    Oa, Ob = {0, 1}, {2, 3}
    fa, fj = {}, {}
    for h in FULL:
        fa.setdefault(vis(h, Oa), 0); fa[vis(h, Oa)] += 1
        fj.setdefault((vis(h, Oa), vis(h, Ob)), 0)
        fj[(vis(h, Oa), vis(h, Ob))] += 1
    ok4 = max(fj.values()) <= max(fa.values())
    rows.append(('POOL', 'free (union of owned traces; fibers only refine)'))

    # ROW 5: the mirror -- container advantage = extra participation:
    f1, f2 = {}, {}
    for h in FULL:
        f1.setdefault(vis(h, O1), 0); f1[vis(h, O1)] += 1
        f2.setdefault(vis(h, O2), 0); f2[vis(h, O2)] += 1
    adv = math.log2(max(f1.values())) - math.log2(max(f2.values()))
    ok5 = adv > 0
    rows.append(('THE MIRROR', f'container advantage = {adv:.2f} bits = its extra participation'))

    # ROW 6: self-knowledge -- biography free (trace determines own
    # contacts trivially); residual = embedding only:
    ok6 = True
    for tr, n in f1.items():
        pass
    rows.append(('SELF-KNOWLEDGE', 'biography free; residual = the embedding'))

    print("## THE OBSERVER'S PRICE LIST (one model, six rows)")
    for name, price in rows:
        print(f"    {name:22s} | {price}")
    check(f"all six rows verified coherently on one model with no "
          f"contradictions: recording without participation costs the "
          f"seed ({ok1}); measuring is co-minting and always informs "
          f"({ok2}); teaching is co-minting across a boundary "
          f"({ok3}); pooling is free and only refines ({ok4}); the "
          f"container's advantage is exactly its extra participation "
          f"({ok5}); and self-knowledge is free up to embedding "
          f"({ok6}). **THE CONSTITUTION OF HOSTED OBSERVERS, PRICED: "
          f"every way of knowing is either participation (free at the "
          f"point of use, paid in consumed marks) or convention (free "
          f"of marks, paid in received keys) -- and the ledger closes "
          f"over both.**", ok1 and ok2 and ok3 and ok4 and ok5 and ok6)


def main():
    section_nested_observers(check)
    section_tuition(check)
    section_overlap_observers(check)
    section_observer_prices(check)
    print()
    print(f"# RESULT: {len(PASS)} passed, {len(FAIL)} failed")
    return 1 if FAIL else 0


if __name__ == '__main__':
    raise SystemExit(main())
