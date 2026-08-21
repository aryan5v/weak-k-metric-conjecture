"""Lemma-level tests for the k=2 resolution (K2_RESOLUTION.md).

Layers of evidence:
  * exhaustive equivalence of the transversal criterion (Lemma 3) with the
    original distance definition on every transversal of small instances;
  * the constructions (Lemma 4) verified directly from graph distances over a
    boundary-heavy sweep, including m = 2n-2, 2n-1, 2n and m >> n;
  * the plain diagonal shown to FAIL at m = 2n-1 (Delta = 1 witness), which is
    why the m >= 2n sketch in the literature needs the seam constructions;
  * Lemma 5's non-existence of a size-m set for 3 <= m <= 2n-3, checked
    exhaustively over transversals for small n (valid since |S| = m forces a
    transversal by Lemma 2);
  * exact optima at the seam via the independent weighted-witness enumerator.
"""
from itertools import product

from src.exact_hittingset import exact_wdim_hittingset
from src.weak_k2 import (
    column_sums,
    is_transversal,
    row_sums,
    transversal_candidate,
    transversal_criterion,
    transversal_matrix,
)
from src.weak_k_metric import verify_original_definition


def test_transversal_criterion_matches_direct_definition_exhaustively():
    for n, m in [(3, 4), (3, 5), (4, 5), (4, 6)]:
        for f in product(range(n), repeat=m):
            a = transversal_matrix(n, m, list(f))
            direct, witness = verify_original_definition(n, m, 2, a)
            assert transversal_criterion(a) == direct, (n, m, f, witness)


def test_k2_construction_boundary_sweep():
    for n in range(3, 11):
        for m in {2 * n - 2, 2 * n - 1, 2 * n, 2 * n + 1, 3 * n}:
            a = transversal_candidate(n, m)
            assert sum(row_sums(a)) == m
            assert is_transversal(a)
            assert transversal_criterion(a)
            ok, witness = verify_original_definition(n, m, 2, a)
            assert ok, (n, m, witness)


def test_k2_construction_large_m_spot():
    for n in (3, 5, 8):
        for m in (50, 101):
            a = transversal_candidate(n, m)
            ok, witness = verify_original_definition(n, m, 2, a)
            assert ok, (n, m, witness)


def test_diagonal_fails_at_m_equals_2n_minus_1():
    # The plain diagonal has row sums (2,...,2,1) at m = 2n-1 and is NOT
    # weak 2-resolving: a swap pair involving the degree-1 row has Delta = 1.
    # The formula still holds there via the exceptional (0,3,2,...,2) design.
    for n in range(3, 9):
        m = 2 * n - 1
        a = transversal_matrix(n, m, [j % n for j in range(m)])
        ok, witness = verify_original_definition(n, m, 2, a)
        assert not ok
        x, y, value = witness
        assert value == 1
        assert x[0] != y[0] and x[1] != y[1]  # a non-aligned pair is the killer


def test_no_size_m_transversal_below_seam_exhaustive():
    # Lemma 5: for 3 <= m <= 2n-3 no transversal satisfies the criterion.
    # By Lemma 2 (m >= 3) any size-m weak 2-resolving set is a transversal,
    # so this exhaustively confirms wdim_2 > m in the tested range.
    for n in range(3, 7):
        m_cap = 2 * n - 2 if n <= 5 else 5  # keep the enumeration tractable
        for m in range(3, m_cap):
            for f in product(range(n), repeat=m):
                a = transversal_matrix(n, m, list(f))
                assert not transversal_criterion(a), (n, m, f)


def test_exact_optima_at_the_seam():
    # Independent exact optima (weighted pair-witness enumeration):
    #   m = 2n-3 fails strictly, m = 2n-2 and m = 2n-1 attain m.
    for n, m, expected in [
        (3, 3, 4),
        (3, 4, 4),
        (3, 5, 5),
        (4, 5, 6),
        (4, 6, 6),
        (5, 7, 8),
    ]:
        optimum, _ = exact_wdim_hittingset(n, m, 2)
        assert optimum == expected, (n, m, optimum, expected)


def test_paper_table_discrepancy_sets():
    # Certified refutations of Table 1 (n=5) k=2 entries m=8 -> 9, m=9 -> 10
    # in Fernandez et al.: these directly verified sets attain |S| = m.
    # (Lemma 1 gives wdim_2 >= m for every m >= 2, so these are optimal.)
    for n, m, f in [
        (5, 8, [1, 2, 3, 4, 1, 2, 3, 4]),
        (5, 9, [1, 2, 3, 4, 1, 1, 2, 3, 4]),
        (6, 10, [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]),
        (6, 11, [1, 2, 3, 4, 5, 1, 1, 2, 3, 4, 5]),
    ]:
        a = transversal_matrix(n, m, f)
        assert sum(row_sums(a)) == m
        assert all(v == 1 for v in column_sums(a))
        ok, witness = verify_original_definition(n, m, 2, a)
        assert ok, (n, m, witness)
