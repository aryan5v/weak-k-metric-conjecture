#!/usr/bin/env python3
"""Exact k=2 certification via integer programming (HiGHS), independent of
every construction. Requires scipy (NOT in requirements.txt; install it
manually to run this optional script):

    pip install scipy
    python scripts/certify_k2_ilp.py

For each instance it solves min sum s_w subject to
    sum_w |d(x,w) - d(y,w)| s_w >= 2   for every unordered pair {x, y},
and re-validates the returned set against the original distance definition.
Results are recorded in experiments/results/k2_exact_boundary.json.
"""
import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.weak_k_metric import distance, selected_vertices, verify_original_definition


def exact_wdim2_ilp(n: int, m: int) -> tuple[int, list]:
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp

    verts = [(i, j) for i in range(n) for j in range(m)]
    a = []
    for x, y in combinations(verts, 2):
        a.append([abs(distance(x, v) - distance(y, v)) for v in verts])
    mat = np.array(a, dtype=float)
    res = milp(
        c=np.ones(len(verts)),
        constraints=LinearConstraint(mat, 2.0, np.inf),
        integrality=np.ones(len(verts)),
        bounds=Bounds(0, 1),
        options={"time_limit": 1800},
    )
    if res.status != 0:
        raise RuntimeError((n, m, res.message))
    chosen = [verts[t] for t in range(len(verts)) if res.x[t] > 0.5]
    matrix = [[0] * m for _ in range(n)]
    for i, j in chosen:
        matrix[i][j] = 1
    ok, witness = verify_original_definition(n, m, 2, matrix)
    if not ok:
        raise AssertionError(("returned set invalid", n, m, witness))
    return len(chosen), chosen


CASES = (
    [(3, m) for m in range(3, 8)]
    + [(4, m) for m in range(4, 9)]
    + [(5, m) for m in range(5, 12)]
    + [(6, m) for m in range(7, 13)]
    + [(7, m) for m in range(7, 14)]
)


def main() -> None:
    out = []
    for n, m in CASES:
        value, chosen = exact_wdim2_ilp(n, m)
        out.append({"n": n, "m": m, "exact_wdim2": value, "equals_m": value == m})
        print(f"n={n} m={m}: wdim_2={value} ({'= m' if value == m else '> m'})",
              flush=True)
    path = Path(__file__).resolve().parents[1] / "experiments" / "results" / "k2_ilp_rerun.json"
    path.write_text(json.dumps(out, indent=2))
    print("wrote", path)


if __name__ == "__main__":
    main()
