#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.weak_k_metric import (
    conjectured_value,
    cyclic_candidate,
    selected_vertices,
    verify_original_definition,
)


def main() -> None:
    checked = 0
    for n in range(3, 9):
        for m in range(n + 1, min(n + 7, 15)):
            for k in range(3, 2 * n + 1):
                a = cyclic_candidate(n, m, k)
                size = len(selected_vertices(a))
                target = conjectured_value(m, k)
                if size != target:
                    raise AssertionError((n, m, k, size, target))
                ok, witness = verify_original_definition(n, m, k, a)
                if not ok:
                    raise AssertionError((n, m, k, witness))
                checked += 1
    print(f"verified {checked} parameter triples against the original definition")


if __name__ == "__main__":
    main()
