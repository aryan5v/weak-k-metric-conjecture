"""Utilities for Conjecture 6.1 on K_n square K_m.

The verifier uses the original definition of weak k-resolution.
"""
from __future__ import annotations

from itertools import combinations
from typing import Iterable

Vertex = tuple[int, int]
Matrix = list[list[int]]


def distance(u: Vertex, v: Vertex) -> int:
    """Graph distance in K_n square K_m = two-coordinate Hamming distance."""
    return int(u[0] != v[0]) + int(u[1] != v[1])


def cyclic_candidate(n: int, m: int, k: int) -> Matrix:
    """Construct the candidate set attaining Conjecture 6.1.

    Preconditions: n >= 3, m >= n+1, 3 <= k <= 2n.
    """
    if n < 3:
        raise ValueError("n must be >= 3")
    if m < n + 1:
        raise ValueError("m must be >= n+1")
    if not (3 <= k <= 2 * n):
        raise ValueError("k must satisfy 3 <= k <= 2n")

    r = (k + 1) // 2
    a = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        for t in range(r):
            a[(j + t) % n][j] = 1

    if k % 2 == 1:
        # Column n exists because m >= n+1 and duplicates the cyclic pattern
        # of column 0. Removing this cell creates the unique (r-1)-column.
        assert a[0][n] == 1
        a[0][n] = 0

    return a


def selected_vertices(a: Matrix) -> list[Vertex]:
    return [
        (i, j)
        for i, row in enumerate(a)
        for j, bit in enumerate(row)
        if bit
    ]


def row_sums(a: Matrix) -> list[int]:
    return [sum(row) for row in a]


def column_sums(a: Matrix) -> list[int]:
    if not a:
        return []
    return [sum(a[i][j] for i in range(len(a))) for j in range(len(a[0]))]


def delta_s(x: Vertex, y: Vertex, s: Iterable[Vertex]) -> int:
    return sum(abs(distance(x, w) - distance(y, w)) for w in s)


def verify_original_definition(n: int, m: int, k: int, a: Matrix) -> tuple[bool, tuple | None]:
    """Check every unordered vertex pair using the original definition."""
    s = selected_vertices(a)
    verts = [(i, j) for i in range(n) for j in range(m)]
    for x, y in combinations(verts, 2):
        val = delta_s(x, y, s)
        if val < k:
            return False, (x, y, val)
    return True, None


def conjectured_value(m: int, k: int) -> int:
    r = (k + 1) // 2
    return m * r - (1 if k % 2 else 0)


def nonaligned_matrix_delta(a: Matrix, x: Vertex, y: Vertex) -> int:
    """Closed-form Delta_S for a non-aligned pair, useful for auditing."""
    i, j = x
    ip, jp = y
    if i == ip or j == jp:
        raise ValueError("pair must be non-aligned")
    g = row_sums(a)
    h = column_sums(a)
    return h[j] + h[jp] + g[i] + g[ip] - 2 * a[i][jp] - 2 * a[ip][j]
