from src.weak_k_metric import (
    column_sums,
    conjectured_value,
    cyclic_candidate,
    delta_s,
    nonaligned_matrix_delta,
    row_sums,
    selected_vertices,
    verify_original_definition,
)


def test_boundary_sweep():
    for n in range(3, 8):
        for m in range(n + 1, n + 5):
            for k in range(3, 2 * n + 1):
                a = cyclic_candidate(n, m, k)
                assert len(selected_vertices(a)) == conjectured_value(m, k)
                ok, witness = verify_original_definition(n, m, k, a)
                assert ok, (n, m, k, witness)


def test_odd_column_profile():
    n, m, k = 5, 9, 7
    a = cyclic_candidate(n, m, k)
    r = (k + 1) // 2
    h = sorted(column_sums(a))
    assert h == [r - 1] + [r] * (m - 1)
    assert min(row_sums(a)) >= r


def test_k3_nonaligned_formula_matches_direct_requirement():
    n, m, k = 4, 5, 3
    a = cyclic_candidate(n, m, k)
    s = selected_vertices(a)
    for i in range(n):
        for ip in range(n):
            if i == ip:
                continue
            for j in range(m):
                for jp in range(m):
                    if j == jp:
                        continue
                    matrix_value = nonaligned_matrix_delta(a, (i, j), (ip, jp))
                    direct_value = delta_s((i, j), (ip, jp), s)
                    assert matrix_value == direct_value
                    assert matrix_value >= 3


def test_k3_boundary_nonaligned_minimum_is_four():
    for n in range(3, 9):
        m, k = n + 1, 3
        a = cyclic_candidate(n, m, k)
        values = [
            nonaligned_matrix_delta(a, (i, j), (ip, jp))
            for i in range(n)
            for ip in range(i + 1, n)
            for j in range(m)
            for jp in range(m)
            if j != jp
        ]
        assert min(values) == 4
