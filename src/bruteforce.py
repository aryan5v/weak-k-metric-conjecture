"""Tiny-instance exact brute force.

This is deliberately simple and only intended for very small graphs.
"""
from __future__ import annotations

from itertools import combinations

from .weak_k_metric import verify_original_definition


def exact_wdim_bruteforce(n: int, m: int, k: int) -> tuple[int, list[list[int]]]:
    vertices = [(i, j) for i in range(n) for j in range(m)]
    N = len(vertices)

    for size in range(N + 1):
        for idxs in combinations(range(N), size):
            chosen = set(idxs)
            a = [[0] * m for _ in range(n)]
            for idx, (i, j) in enumerate(vertices):
                if idx in chosen:
                    a[i][j] = 1
            ok, _ = verify_original_definition(n, m, k, a)
            if ok:
                return size, a
    raise RuntimeError("no weak k-resolving set found")
