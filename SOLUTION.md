# Resolving Conjecture 6.1: Weak k-Metric Dimension of Rectangular Hamming Graphs

**Status: PROVED.** Conjecture 6.1 is true throughout its stated parameter range.
The proof below is self-contained: it uses only the definition of Cartesian-product
distance and does not rely on Proposition 4.1, Corollary 4.3, an ILP formulation,
or any computation.

Source of the conjecture:

> E. Fernández, S. Klavžar, D. Kuziak, M. Muñoz-Márquez, I. G. Yero,
> **On the weak k-metric dimension of Hamming graphs**, *Discrete Optimization* 60 (2026), 100945.
> DOI: [10.1016/j.disopt.2026.100945](https://doi.org/10.1016/j.disopt.2026.100945) · arXiv:[2505.19642](https://arxiv.org/abs/2505.19642)

---

## 1. The problem

### 1.1 Graph and distance

Let $G = K_n \square K_m$ be the Cartesian product of two complete graphs, with
vertices $(i,j)$ where $i \in \mathbb{Z}_n$ and $j \in \{0,\dots,m-1\}$. Two distinct
vertices are adjacent exactly when they agree in one coordinate, so distance is
Hamming distance on the two coordinates:

$$d(u,x) = \mathbf{1}_{a\ne i} + \mathbf{1}_{b\ne j}
\qquad \text{for } u=(a,b),\ x=(i,j).$$

### 1.2 Weak k-resolving sets

For vertices $x,y,w$ let $\Delta_w(x,y) = |d(x,w) - d(y,w)|$. A set $S$ of vertices
is **weak $k$-resolving** if every distinct pair $x,y$ satisfies

$$\Delta_S(x,y) := \sum_{w\in S} \Delta_w(x,y) \ge k.$$

The minimum size of a weak $k$-resolving set is the **weak $k$-metric dimension**
$\operatorname{wdim}_k(G)$.

### 1.3 Conjecture 6.1 (the open problem)

For integers $n \ge 3$, $m \ge n+1$, and $3 \le k \le 2n$, the source paper conjectures:

$$\operatorname{wdim}_k(K_n \square K_m)=
\begin{cases}
m\lceil k/2\rceil, & k \text{ even},\\[2mm]
m\lceil k/2\rceil - 1, & k \text{ odd}.
\end{cases}$$

This is a universal statement over all allowed triples $(n,m,k)$: resolving it
requires either a proof for the full range or one certified counterexample.
The paper itself proved only the square case $K_n \square K_n$ and left the
rectangular case as this conjecture, supported by ILP experiments.

---

## 2. The solution

**Theorem.** For all $n \ge 3$, $m \ge n+1$, and $3 \le k \le 2n$,

$$\operatorname{wdim}_k(K_n\square K_m)=
\begin{cases}
m\lceil k/2\rceil,&k\text{ even},\\[2mm]
m\lceil k/2\rceil-1,&k\text{ odd}.
\end{cases}$$

The proof has two halves:

1. **Lower bound.** Same-row vertex pairs force every weak $k$-resolving set
   $S$ to satisfy $h_j + h_{j'} \ge k$ for all column sums $h_j$ of its incidence
   matrix; a short extremal argument then gives $|S| \ge m\lceil k/2\rceil$ (even $k$)
   and $|S| \ge m\lceil k/2\rceil - 1$ (odd $k$).
2. **Upper bound.** An explicit cyclic construction $S_0$ (one diagonal band of
   width $\lceil k/2\rceil$ in the $n\times m$ incidence matrix) meets the lower
   bound exactly; for odd $k$ one vertex is deleted from a duplicated column.

The only technically delicate point is verifying non-aligned pairs (pairs sharing
neither row nor column): these are handled by an exact identity, equation (3)
below, which reduces them to the aligned cases for $k \ge 4$ and needs a short
separate argument for $k = 3$.

---

## 3. The proof

Index rows by $\mathbb{Z}_n$ and columns by $0,\dots,m-1$. Represent a set $S$ by
its binary incidence matrix $A$ and write

$$g_i=\sum_{j=0}^{m-1}A_{ij},\qquad h_j=\sum_{i\in\mathbb Z_n}A_{ij},$$

the row and column sums, so $|S|=\sum_i g_i=\sum_j h_j$.

### 3.1 Distance contributions

For $u=(a,b)$ and $x=(i,j)$, $d(u,x)=\mathbf{1}_{a\ne i}+\mathbf{1}_{b\ne j}$.

If $x=(i,j)$ and $y=(i,j')$ share a row, the row terms cancel and a landmark
contributes exactly when it lies in column $j$ or $j'$:

$$\Delta_S(x,y)=h_j+h_{j'}. \tag{1}$$

Dually, if $x=(i,j)$ and $y=(i',j)$ share a column:

$$\Delta_S(x,y)=g_i+g_{i'}. \tag{2}$$

Now let $x=(i,j)$ and $y=(i',j')$ be **non-aligned**: $i\ne i'$ and $j\ne j'$, so
$d(x,y)=2$. The four layer sums $h_j+h_{j'}+g_i+g_{i'}$ count each endpoint twice
(as required), count every other landmark in exactly one of the four layers once
(as required), but also count the two cross vertices $(i,j')$ and $(i',j)$ twice —
and those are equidistant from $x$ and $y$, so their contribution must be removed.
Therefore

$$\Delta_S(x,y)=h_j+h_{j'}+g_i+g_{i'}-2A_{i,j'}-2A_{i',j}. \tag{3}$$

An immediate consequence: if all same-row and same-column pairs satisfy the weak
$k$ inequalities and $k\ge4$, then every non-aligned pair does too, because

$$\Delta_S(x,y)\ge k+k-2-2=2k-4\ge k. \tag{4}$$

### 3.2 Lower bound

By (1), every weak $k$-resolving set satisfies

$$h_j+h_{j'}\ge k\qquad(j\ne j'). \tag{5}$$

Let $a=\min_j h_j$.

**Even case, $k=2r$.** If $a\ge r$ then $|S|=\sum_j h_j\ge mr$. If $a\le r-1$,
pairing a minimum column with every other column in (5) gives

$$|S|\ge a+(m-1)(2r-a)=mr+(m-2)(r-a)\ge mr.$$

So $|S|\ge mr=m\lceil k/2\rceil$ for even $k$.

**Odd case, $k=2r-1$.** If $a\ge r$ then $|S|\ge mr$, stronger than needed. If
$a\le r-1$, (5) gives $|S|\ge a+(m-1)(2r-1-a)$. Since $m\ge n+1\ge4$, this
decreases as $a$ increases, so its minimum over integers $a\le r-1$ is at $a=r-1$:

$$|S|\ge (r-1)+(m-1)r=mr-1=m\lceil k/2\rceil-1.$$

### 3.3 Upper bound: cyclic construction

Put $r=\lceil k/2\rceil$; the assumption $k\le 2n$ gives $r\le n$. Define

$$S_0=\{(i,j)\in\mathbb Z_n\times\{0,\ldots,m-1\}:\ i-j \pmod n\in\{0,1,\ldots,r-1\}\}. \tag{6}$$

Each column of $S_0$ contains exactly $r$ vertices; among the first $n$ columns
each row occurs exactly $r$ times; since $m\ge n+1$, every row contains at least
$r$ vertices.

**Even case ($k=2r$).** Take $S=S_0$. Every pair of column sums equals $2r=k$ and
every pair of row sums is at least $2r=k$; since even $k$ in the stated range has
$k\ge4$, equation (4) handles all non-aligned pairs. Thus $S$ is weak
$k$-resolving with $|S|=mr$.

**Odd case ($k=2r-1$, $k\ge5$).** Column $n$ exists (as $m\ge n+1$) and repeats
the cyclic pattern of column $0$, so $(0,n)\in S_0$. Delete it:

$$S=S_0\setminus\{(0,n)\}. \tag{7}$$

Column $n$ now has size $r-1$ and every other column size $r$, so every pair of
columns has combined size at least $2r-1=k$. Row zero retains its $r$ vertices
among the first $n$ columns, and every other row still has size at least $r$, so
every pair of row sums is at least $2r=k+1$. For $k\ge5$, equation (4) again
handles every non-aligned pair. Thus $S$ is weak $k$-resolving with $|S|=mr-1$.

**Remaining case $k=3$.** Use the same set (7) with $r=2$. The column calculation
gives $h_j+h_{j'}\ge3$ for distinct columns and the row calculation gives
$g_i+g_{i'}\ge4$ for distinct rows. For a non-aligned pair, equation (3) yields

$$\Delta_S(x,y)\ge3+4-2-2=3,$$

so $S$ is weak $3$-resolving with $|S|=2m-1$.

(The separate $k=3$ treatment is genuinely necessary: the general reduction (4)
fails at $k=3$, e.g. on $K_3\square K_4$ there are non-aligned pairs with
$\Delta_S<3$ under aligned-only reasoning.)

### 3.4 Conclusion

The construction attains the lower bound in every parity case, hence

$$\operatorname{wdim}_k(K_n\square K_m)=
\begin{cases}
m\lceil k/2\rceil,&k\text{ even},\\[2mm]
m\lceil k/2\rceil-1,&k\text{ odd},
\end{cases}$$

for every allowed triple $(n,m,k)$. $\blacksquare$

**Logical dependencies.** The lower bound uses only same-row pairs via (1)/(5);
the upper bound is an explicit binary-matrix construction; non-aligned pairs are
discharged by (3)–(4) for $k\ge4$ and directly for $k=3$. No finite computation
is used anywhere in the proof.

---

## 4. Computational verification (supporting evidence only)

Three independent code paths in this repository confirm the theorem on small and
moderate instances; none is part of the proof:

1. `src/weak_k_metric.py` — checks the cyclic construction directly from graph distances.
2. `src/exact_hittingset.py` — independent weighted pair-witness covering formulation solved by exact enumeration (no dependence on the construction).
3. `src/bruteforce.py` — plain subset-enumeration reference optimum.

Run everything with:

```bash
pip install -r requirements.txt
pytest -q                    # 9 tests: lemmas, construction, exact optima
python scripts/sweep_verify.py   # sweep over 324 parameter triples
```

Machine-readable baselines live in `experiments/results/`.

---

## 5. Independent review

An independent adversarial referee audit — performed by the **Kimi K3 model**, working
from the pinned proof commit in an isolated worktree with its own scratch
implementations — returned the verdict **VALID PROOF** with all seven audited
obligations passing. See [`INDEPENDENT_REVIEW.md`](INDEPENDENT_REVIEW.md).
The result has not yet undergone formal journal peer review.

## 6. Novelty note

As of 2026-08-20, targeted searches (version of record, arXiv, DBLP, OpenAlex,
Crossref, author publication lists) found no public prior resolution of this
Cartesian-product conjecture. A 2026 Farhan–Kuziak–Yero preprint concerns the
*direct* product and does not cover this result. Absence from search indexes is
not a guarantee of novelty; a fresh search and author contact are advised before
public dissemination.
