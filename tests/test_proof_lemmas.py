from itertools import combinations, product

from src.weak_k_metric import (
    column_sums,
    conjectured_value,
    delta_s,
    nonaligned_matrix_delta,
    row_sums,
    selected_vertices,
)


def test_all_matrix_delta_formulas_exhaustively():
    n, m = 2, 3
    vertices = [(i, j) for i in range(n) for j in range(m)]

    for bits in product((0, 1), repeat=n * m):
        a = [list(bits[i * m : (i + 1) * m]) for i in range(n)]
        s = selected_vertices(a)
        g = row_sums(a)
        h = column_sums(a)

        for x, y in combinations(vertices, 2):
            direct = delta_s(x, y, s)
            i, j = x
            ip, jp = y
            if i == ip:
                assert direct == h[j] + h[jp]
            elif j == jp:
                assert direct == g[i] + g[ip]
            else:
                assert direct == nonaligned_matrix_delta(a, x, y)


def test_bounded_column_extremum_exhaustively():
    n, m = 4, 5
    for k in range(3, 2 * n + 1):
        feasible_sums = [
            sum(profile)
            for profile in product(range(n + 1), repeat=m)
            if all(profile[j] + profile[jp] >= k for j, jp in combinations(range(m), 2))
        ]
        assert min(feasible_sums) == conjectured_value(m, k)
