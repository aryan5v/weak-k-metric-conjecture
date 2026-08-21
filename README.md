# Weak k-Metric Dimension of Rectangular Hamming Graphs — Conjecture 6.1 Resolved

This repository contains a complete, self-contained proof of Conjecture 6.1 from:

> E. Fernández, S. Klavžar, D. Kuziak, M. Muñoz-Márquez, I. G. Yero,
> **On the weak k-metric dimension of Hamming graphs**, *Discrete Optimization* 60 (2026), 100945.
> DOI: [10.1016/j.disopt.2026.100945](https://doi.org/10.1016/j.disopt.2026.100945) · arXiv:[2505.19642](https://arxiv.org/abs/2505.19642)

## Result

For all $n \ge 3$, $m \ge n+1$, and $3 \le k \le 2n$:

$$\mathrm{wdim}_k(K_n\square K_m)=
\begin{cases}
m\lceil k/2\rceil,&k\text{ even},\\[2mm]
m\lceil k/2\rceil-1,&k\text{ odd}.
\end{cases}$$

The proof uses only the Cartesian-product distance definition — no ILP
formulation, no reliance on the paper's Proposition 4.1, and no computation.

## Read this

- **[`SOLUTION.md`](SOLUTION.md)** — problem statement, result, and full proof (start here)
- **[`INDEPENDENT_REVIEW.md`](INDEPENDENT_REVIEW.md)** — independent adversarial referee audit (Kimi K3 model): verdict **VALID PROOF**

The proof has also passed internal algebraic, boundary, and exact-computation
audits. It has not yet undergone formal journal peer review.

## Repository layout

| Path | Purpose |
|---|---|
| `SOLUTION.md` | Problem, solution, and complete proof |
| `INDEPENDENT_REVIEW.md` | Independent referee report (Kimi K3 model) |
| `src/weak_k_metric.py` | Cyclic construction + direct verifier from graph distances |
| `src/exact_hittingset.py` | Independent exact weighted-witness verifier |
| `src/bruteforce.py` | Tiny-instance subset-enumeration reference optimum |
| `tests/` | Proof-lemma, construction, and exact-optimum regression tests |
| `scripts/sweep_verify.py` | Parameter sweep against the original definition |
| `experiments/results/` | Machine-readable baselines |
| `references/references.bib` | Bibliography |

The three verification code paths are deliberately independent of each other;
they support but are not part of the proof.

## Running the verification

Requirements: Python 3.10+, `pytest`. No commercial solver needed.

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q                       # 9 tests
python scripts/sweep_verify.py  # verifies 324 parameter triples
```

CI runs both checks on every push and pull request.

## Citation

See `references/references.bib`.
