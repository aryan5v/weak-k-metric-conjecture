from src.exact_hittingset import (
    exact_wdim_hittingset,
    is_weak_k_resolving_mask,
    mask_to_matrix,
    witness_masks,
)
from src.weak_k_metric import conjectured_value, verify_original_definition


def test_weighted_masks_match_original_definition_exhaustively():
    n, m = 2, 3
    _, masks = witness_masks(n, m)
    for selected_mask in range(1 << (n * m)):
        matrix = mask_to_matrix(selected_mask, n, m)
        for k in range(1, 2 * n + 1):
            weighted = is_weak_k_resolving_mask(selected_mask, masks, k)
            direct, _ = verify_original_definition(n, m, k, matrix)
            assert weighted == direct, (selected_mask, k)


def test_weight_two_endpoint_regression():
    n, m, k = 3, 4, 3
    verts, masks = witness_masks(n, m)
    chosen = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (2, 2)}
    selected_mask = sum(1 << idx for idx, vertex in enumerate(verts) if vertex in chosen)

    assert is_weak_k_resolving_mask(selected_mask, masks, k)
    direct, witness = verify_original_definition(
        n, m, k, mask_to_matrix(selected_mask, n, m)
    )
    assert direct, witness


def test_exact_small_boundary_cases():
    # Smallest rectangular instance in the conjecture.
    n, m = 3, 4
    for k in range(3, 2 * n + 1):
        optimum, _ = exact_wdim_hittingset(n, m, k)
        assert optimum == conjectured_value(m, k)
