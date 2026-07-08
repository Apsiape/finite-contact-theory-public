#!/usr/bin/env python3
"""Verify the open fresh-mark no-jam property on a finite horizon.

Claim IDs: FCT-09, T-01.

This is a public, dependency-free verification subset. It does not reproduce
the full private script. It checks the core finite claim used in the
public release:

  Under the open fresh-mark rule with act-indexed one-use, every reachable
  fragment through depth 7 has at least one legal extension.

Rules:
  - seed: from the empty fragment, create one mark.
  - fresh: add one fresh mark connected to one existing mark.
  - edge: draw any undrawn edge among existing marks.
  - record: record one available closed triangle not already recorded.

The state is a labeled finite fragment (n, edges, records). Each act consumes
one occasion; no act is reused. The fresh channel is uncapped.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations


DEPTH = 7


@dataclass(frozen=True, order=True)
class State:
    n: int
    edges: frozenset[tuple[int, int]]
    records: frozenset[tuple[int, int, int]]


EMPTY = State(0, frozenset(), frozenset())


def edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def triangles(n: int, edges: frozenset[tuple[int, int]]) -> set[tuple[int, int, int]]:
    out: set[tuple[int, int, int]] = set()
    for a, b, c in combinations(range(n), 3):
        if edge(a, b) in edges and edge(a, c) in edges and edge(b, c) in edges:
            out.add((a, b, c))
    return out


def legal_successors(state: State) -> list[State]:
    if state.n == 0:
        return [State(1, frozenset(), frozenset())]

    successors: list[State] = []

    # Fresh channel: add one new mark connected to any old mark.
    new_mark = state.n
    for old in range(state.n):
        new_edges = set(state.edges)
        new_edges.add(edge(old, new_mark))
        successors.append(State(state.n + 1, frozenset(new_edges), state.records))

    # Draw an undrawn edge on existing support.
    for u, v in combinations(range(state.n), 2):
        e = edge(u, v)
        if e not in state.edges:
            new_edges = set(state.edges)
            new_edges.add(e)
            successors.append(State(state.n, frozenset(new_edges), state.records))

    # Record a closed triangle not yet recorded.
    for tri in triangles(state.n, state.edges) - set(state.records):
        new_records = set(state.records)
        new_records.add(tri)
        successors.append(State(state.n, state.edges, frozenset(new_records)))

    return successors


def run() -> None:
    seen: dict[State, int] = {EMPTY: 0}
    q: deque[State] = deque([EMPTY])
    jammed: list[tuple[State, int]] = []

    while q:
        state = q.popleft()
        depth = seen[state]
        successors = legal_successors(state)
        if not successors:
            jammed.append((state, depth))

        if depth == DEPTH:
            continue

        for nxt in successors:
            if nxt not in seen:
                seen[nxt] = depth + 1
                q.append(nxt)

    by_depth = [0] * (DEPTH + 1)
    for d in seen.values():
        if d <= DEPTH:
            by_depth[d] += 1

    print("no_jam_open_rule")
    print(f"depth={DEPTH}")
    print(f"reachable_states={len(seen)}")
    print(f"states_by_depth={by_depth}")
    print(f"jammed_states={len(jammed)}")

    assert not jammed, "open fresh-mark rule produced a jammed fragment"
    print("RESULT: PASS")


if __name__ == "__main__":
    run()
