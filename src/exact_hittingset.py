"""Independent exact verifier via weighted pair-witness constraints.

This module intentionally does NOT reuse the candidate construction. For each
unordered vertex pair {x,y}, it computes separate masks for vertices whose
distance-difference contribution is one or two. A weak k-resolving set S must
have total witness weight at least k for every pair. The exact optimizer then
searches subsets by cardinality.

This is exponential and intended only for small certification instances.
"""
from __future__ import annotations

from itertools import combinations

Vertex = tuple[int, int]
WeightedWitness = tuple[int, int]


def distance(u: Vertex, v: Vertex) -> int:
    return int(u[0] != v[0]) + int(u[1] != v[1])


def witness_masks(n: int, m: int) -> tuple[list[Vertex], list[WeightedWitness]]:
    verts = [(i, j) for i in range(n) for j in range(m)]
    masks: list[WeightedWitness] = []
    for x, y in combinations(verts, 2):
        unit_mask = 0
        double_mask = 0
        for idx, w in enumerate(verts):
            contribution = abs(distance(x, w) - distance(y, w))
            if contribution == 1:
                unit_mask |= 1 << idx
            elif contribution == 2:
                double_mask |= 1 << idx
        masks.append((unit_mask, double_mask))
    return verts, masks


def is_weak_k_resolving_mask(
    selected_mask: int, masks: list[WeightedWitness], k: int
) -> bool:
    return all(
        (selected_mask & unit_mask).bit_count()
        + 2 * (selected_mask & double_mask).bit_count()
        >= k
        for unit_mask, double_mask in masks
    )


def exact_wdim_hittingset(n: int, m: int, k: int) -> tuple[int, int]:
    """Return exact optimum and one selected bit-mask for tiny instances."""
    verts, masks = witness_masks(n, m)
    N = len(verts)
    indices = range(N)
    for size in range(N + 1):
        for chosen in combinations(indices, size):
            selected = 0
            for idx in chosen:
                selected |= 1 << idx
            if is_weak_k_resolving_mask(selected, masks, k):
                return size, selected
    raise RuntimeError("no weak k-resolving set found")


def mask_to_matrix(mask: int, n: int, m: int) -> list[list[int]]:
    a = [[0] * m for _ in range(n)]
    idx = 0
    for i in range(n):
        for j in range(m):
            a[i][j] = int(bool(mask & (1 << idx)))
            idx += 1
    return a
