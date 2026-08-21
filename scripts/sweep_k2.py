#!/usr/bin/env python3
"""Sweep the k=2 transversal construction against the original definition.

Covers the whole proved regime m >= 2n-2 on a bounded grid, emphasizing the
seam m in {2n-2, 2n-1, 2n}. Supporting evidence only; the proof in
K2_RESOLUTION.md uses no computation.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.weak_k2 import row_sums, transversal_candidate
from src.weak_k_metric import verify_original_definition


def main() -> None:
    checked = 0
    for n in range(3, 9):
        for m in range(2 * n - 2, min(3 * n, 26)):
            a = transversal_candidate(n, m)
            if sum(row_sums(a)) != m:
                raise AssertionError((n, m, "wrong size"))
            ok, witness = verify_original_definition(n, m, 2, a)
            if not ok:
                raise AssertionError((n, m, witness))
            checked += 1
    print(f"verified {checked} k=2 parameter pairs (m >= 2n-2) against the "
          "original definition")


if __name__ == "__main__":
    main()
