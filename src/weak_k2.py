"""The k=2 regime of K_n square K_m.

For k=2 the column-pair inequality h_j + h_j' >= 2 forces |S| >= m
(Lemma 1 of K2_RESOLUTION.md), and equality forces a transversal:
exactly one landmark per column, S = {(f(j), j)}. This module builds the
extremal transversals and checks the weak-2 transversal criterion

    (R1)  g_i + g_i' >= 2   for all distinct rows i, i';
    (R2)  g_i + g_i' >= 4   for all distinct rows i, i' in the image of f;

which by Lemma 3 is *equivalent* to S_f being weak 2-resolving.

The theorem proved in K2_RESOLUTION.md: for n >= 3,

    wdim_2(K_n square K_m) = m   iff   m >= 2n-2,

and wdim_2 >= m + 1 for 3 <= m <= 2n-3.
"""
from __future__ import annotations

Matrix = list[list[int]]


def transversal_matrix(n: int, m: int, f: list[int]) -> Matrix:
    """Incidence matrix of {(f(j), j) : 0 <= j < m}."""
    if len(f) != m or any(not 0 <= r < n for r in f):
        raise ValueError("f must map columns {0..m-1} into rows {0..n-1}")
    a = [[0] * m for _ in range(n)]
    for j, i in enumerate(f):
        a[i][j] = 1
    return a


def diagonal_f(n: int, m: int) -> list[int]:
    """The plain diagonal f(j) = j mod n (valid regime: m >= 2n)."""
    return [j % n for j in range(m)]


def transversal_candidate(n: int, m: int) -> Matrix:
    """Extremal weak-2-resolving transversal of size m, for m >= 2n-2.

    Regimes (Lemma 4 of K2_RESOLUTION.md):
      m = 2n-2: row sums (0, 2, ..., 2);
      m = 2n-1: row sums (0, 3, 2, ..., 2);
      m >= 2n:  diagonal, every row sum >= 2.
    """
    if n < 3:
        raise ValueError("n must be >= 3")
    if m < 2 * n - 2:
        raise ValueError("no weak-2-resolving transversal exists for m <= 2n-3")
    if m == 2 * n - 2:
        f = [(j % (n - 1)) + 1 for j in range(m)]
    elif m == 2 * n - 1:
        f = [(j % (n - 1)) + 1 for j in range(m - 1)] + [1]
    else:
        f = diagonal_f(n, m)
    return transversal_matrix(n, m, f)


def row_sums(a: Matrix) -> list[int]:
    return [sum(row) for row in a]


def column_sums(a: Matrix) -> list[int]:
    if not a:
        return []
    return [sum(a[i][j] for i in range(len(a))) for j in range(len(a[0]))]


def is_transversal(a: Matrix) -> bool:
    return all(v == 1 for v in column_sums(a))


def transversal_criterion(a: Matrix) -> bool:
    """Check (R1) and (R2) for a transversal incidence matrix.

    By Lemma 3 this is equivalent to the set being weak 2-resolving.
    """
    if not is_transversal(a):
        raise ValueError("criterion applies to transversals only")
    n = len(a)
    g = row_sums(a)
    image = [i for i in range(n) if g[i] > 0]
    r1 = all(g[i] + g[ip] >= 2 for i in range(n) for ip in range(i + 1, n))
    r2 = all(
        g[i] + g[ip] >= 4
        for x, i in enumerate(image)
        for ip in image[x + 1 :]
    )
    return r1 and r2
