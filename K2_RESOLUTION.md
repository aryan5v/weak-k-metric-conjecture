# The remaining $k=2$ problem: $\mathrm{wdim}_2(K_n \square K_m)$

**Status: RESOLVED, with a stronger conclusion than the source paper's belief.**

Fernández, Klavžar, Kuziak, Muñoz-Márquez, and Yero (*On the weak $k$-metric
dimension of Hamming graphs*, Discrete Optimization 60 (2026), 100945,
arXiv:[2505.19642](https://arxiv.org/abs/2505.19642)) remark after
Conjecture 6.1:

> "we strongly believe that the formula from the conjecture above is also valid
> when $k=2$ and $m \ge 2n$. Notice that when $n = 5$, the formula does not hold
> for $m \in \{6, \dots, 9\}$, and for $n = 6$, the formula does not hold for
> $m \in \{7, \dots, 11\}$."

We prove the belief and locate the **exact** validity threshold, which is
$m = 2n-2$, not $2n$:

**Theorem.** For every $n \ge 3$:

1. $\mathrm{wdim}_2(K_n \square K_m) = m$ for every $m \ge 2n-2$
   (in particular for every $m \ge 2n$, proving the paper's belief);
2. $\mathrm{wdim}_2(K_n \square K_m) \ge m+1$ for every $3 \le m \le 2n-3$,
   so the formula $\mathrm{wdim}_2 = m$ fails there and the threshold $2n-2$
   is sharp;
3. the plain diagonal construction $S = \{(j \bmod n, j)\}$ proves part (1)
   only for $m \ge 2n$; the two seam values $m = 2n-2$ and $m = 2n-1$ need
   exceptional transversals given below.

The proof is self-contained and uses no computation. Computational evidence
(certified exact optima, including a correction of two entries in the paper's
Table 1) is collected separately in §4 and `experiments/results/k2_exact_boundary.json`.

---

## 1. Setup and the three pair identities

Rows are indexed by $\mathbb{Z}_n$, columns by $\{0,\dots,m-1\}$. The distance
in $K_n \square K_m$ is Hamming distance on the two coordinates. For a landmark
set $S$ with binary incidence matrix $A$, write

$$g_i=\sum_{j}A_{ij},\qquad h_j=\sum_{i}A_{ij},\qquad |S|=\sum_i g_i=\sum_j h_j .$$

The following identities are $k$-independent (derived and audited in
`SOLUTION.md`, §3.1; equations (1)–(3) there):

* same-row pair $x=(i,j)$, $y=(i,j')$:
  $$\Delta_S(x,y)=h_j+h_{j'}; \qquad \text{(R)}$$
* same-column pair $x=(i,j)$, $y=(i',j)$:
  $$\Delta_S(x,y)=g_i+g_{i'}; \qquad \text{(C)}$$
* non-aligned pair $x=(i,j)$, $y=(i',j')$ ($i\ne i'$, $j\ne j'$):
  $$\Delta_S(x,y)=h_j+h_{j'}+g_i+g_{i'}-2A_{i,j'}-2A_{i',j}. \qquad \text{(N)}$$

$S$ is weak $2$-resolving iff every distinct pair has $\Delta_S \ge 2$.

---

## 2. Proof

### Lemma 1 (universal lower bound). 
*Let $n \ge 2$ and $m \ge 2$. Every weak $2$-resolving set $S$ of
$K_n \square K_m$ satisfies $|S| \ge m$.*

**Proof.** Fix any row $i$. For distinct columns $j \ne j'$ the pair
$(i,j),(i,j')$ and identity (R) force

$$h_j + h_{j'} \ge 2 \qquad (j \ne j'). \tag{5}$$

Let $a = \min_j h_j$. If $a \ge 1$, then $|S| = \sum_j h_j \ge m$. If $a = 0$,
pick $j_0$ with $h_{j_0} = 0$; (5) gives $h_j \ge 2$ for all $j \ne j_0$, so
$|S| \ge 2(m-1) \ge m$ because $m \ge 2$. $\blacksquare$

### Lemma 2 (equality forces a transversal). 
*Let $m \ge 3$. If $S$ is weak $2$-resolving and $|S| = m$, then $h_j = 1$ for
every column $j$; that is, $S$ contains exactly one vertex per column, hence
$S = \{(f(j), j) : 0 \le j < m\}$ for a unique map
$f : \{0,\dots,m-1\} \to \mathbb{Z}_n$.*

**Proof.** If some $h_{j_0} = 0$, Lemma 1's argument gives
$|S| \ge 2(m-1) > m$ (strict since $m \ge 3$), contradicting $|S| = m$. Hence
$h_j \ge 1$ for all $j$, and $\sum_j h_j = m$ forces $h_j = 1$ for every $j$.
$\blacksquare$

Such a set is called a **transversal**; its row sums are
$g_i = |f^{-1}(i)|$.

### Lemma 3 (the transversal criterion). 
*A transversal $S_f$ is weak $2$-resolving if and only if its row sums satisfy*

$$\text{(R1)}\quad g_i + g_{i'} \ge 2 \ \text{for all distinct rows } i,i';$$
$$\text{(R2)}\quad g_i + g_{i'} \ge 4 \ \text{for all distinct rows } i,i'
\text{ in the image of } f.$$

**Proof.** We check the three pair types.

*Same-row pairs.* $\Delta = h_j + h_{j'} = 2$ identically; no constraint beyond
$h \equiv 1$.

*Same-column pairs.* By (C), $\Delta((i,j),(i',j)) = g_i + g_{i'}$. Every pair
of distinct rows occurs (in every column), so these constraints are exactly
(R1).

*Non-aligned pairs.* For $x=(i,j)$, $y=(i',j')$ with $i\ne i'$, $j\ne j'$,
identity (N) with $h \equiv 1$ reads

$$\Delta_S(x,y) = 2 + g_i + g_{i'} - 2\mathbf{1}[f(j')=i] - 2\mathbf{1}[f(j)=i']. \tag{$\ast$}$$

*Case both indicators $1$.* Then $i = f(j')$ and $i' = f(j)$ are distinct rows
in the image of $f$, and $\Delta = g_i + g_{i'} - 2$, which is $\ge 2$ iff
$g_i + g_{i'} \ge 4$. Conversely, for any two distinct image rows $i, i'$,
choosing $j' \in f^{-1}(i)$ and $j \in f^{-1}(i')$ produces such a pair
($j \ne j'$ automatically since $f(j) = i' \ne i = f(j')$). So this family is
exactly (R2).

*Case exactly one indicator $1$.* $\Delta = 1 + g_i + g_{i'} \ge 2$ holds
because $g_i + g_{i'} \ge 1$; indeed (R1) already gives $\ge 2$.

*Case no indicator $1$.* $\Delta = 2 + g_i + g_{i'} \ge 2$ by (R1).

Since every pair of distinct vertices is of exactly one type, (R1) and (R2)
together are necessary and sufficient. $\blacksquare$

### Lemma 4 (constructions at and above the seam). 
*Let $n \ge 3$ and $m \ge 2n-2$. Then a transversal satisfying (R1) and (R2)
exists; hence $\mathrm{wdim}_2(K_n \square K_m) \le m$.*

**Proof.** Three regimes.

**$m = 2n-2$.** Put $f(j) = (j \bmod (n-1)) + 1$. Since $2n-2 = 2(n-1)$, each
of the rows $1, \dots, n-1$ is hit exactly twice and row $0$ is empty:
$g = (0, 2, \dots, 2)$.
(R1): the only zero row pairs as $0 + 2 = 2$; nonzero rows pair as $2+2 = 4$.
(R2): image rows all have $g_i = 2$, pairwise sums $4$.

**$m = 2n-1$.** Extend the previous map by $f(2n-2) = 1$:
$g = (0, 3, 2, \dots, 2)$.
(R1): $0+2 = 2$. (R2): $3+2 = 5$ and $2+2 = 4$.

**$m \ge 2n$.** The diagonal $f(j) = j \bmod n$. Every row sum is
$\lfloor m/n \rfloor$ or $\lceil m/n \rceil$, hence at least $2$; the image is
all rows, and (R1), (R2) hold with sums $\ge 4$.

In each case $|S| = m$, and Lemma 3 certifies weak $2$-resolution.
$\blacksquare$

*Remark.* The diagonal alone does **not** work at $m = 2n-1$: its row sums are
$(2,\dots,2,1)$, and (R2) fails for the pair of a degree-$2$ row and the
degree-$1$ row. Concretely, at $(n,m) = (3,5)$ the pair $x=(0,2)$,
$y=(2,0)$ has $\Delta_S(x,y) = 1 < 2$ (both cross cells $(0,0),(2,2)$ are
landmarks). So the "one diagonal band" idea is exactly tight at $m = 2n$,
while the *formula* starts one step earlier via the exceptional designs above.

### Lemma 5 (below the seam the formula fails). 
*Let $n \ge 3$ and $3 \le m \le 2n-3$. Then
$\mathrm{wdim}_2(K_n \square K_m) \ge m+1$.*

**Proof.** Suppose a weak $2$-resolving set $S$ with $|S| = m$ exists. Since
$m \ge 3$, Lemma 2 makes $S$ a transversal with row-sum vector $g$,
$\sum_i g_i = m \le 2n-3$, satisfying (R1) and (R2).

*Case 1: some row is empty.* By (R1) there is exactly one empty row and every
other row has $g_i \ge 2$, so $\sum_i g_i \ge 2(n-1) = 2n-2 > m$ —
contradiction.

*Case 2: no empty row.* Then the image of $f$ is all $n$ rows and (R2) applies
to every pair of distinct rows. Two distinct rows of weight $1$ would violate
(R2) ($1+1 = 2 < 4$), so at most one row has $g_i = 1$. If one row has
$g_i = 1$, (R2) forces every other row to have weight $\ge 3$, whence
$\sum_i g_i \ge 1 + 3(n-1) = 3n-2 > 2n-3 \ge m$ (the gap is $n+1 > 0$) —
contradiction. Otherwise all rows have weight $\ge 2$, so
$\sum_i g_i \ge 2n > m$ — contradiction.

Thus no size-$m$ weak $2$-resolving set exists; combined with Lemma 1,
$\mathrm{wdim}_2 \ge m+1$. $\blacksquare$

### Proof of the Theorem

Part (1): Lemma 4 gives $\mathrm{wdim}_2 \le m$ for $m \ge 2n-2$, and Lemma 1
gives $\ge m$ (note $m \ge 2n-2 \ge 4 \ge 2$). Part (2) is Lemma 5. Part (3)
is the remark after Lemma 4. The paper's believed statement
($m \ge 2n \Rightarrow \mathrm{wdim}_2 = m$) is the diagonal regime of
Lemma 4. $\blacksquare$

---

## 3. Remarks on the paper's $k=2$ computations

* The paper's note that the formula fails "for $n=5$, $m \in \{6,\dots,9\}$"
  and "for $n=6$, $m \in \{7,\dots,11\}$" is **not correct** at the two seam
  values: certified exact optima (independent ILP; every returned set
  re-validated from the distance definition) give

  $$\mathrm{wdim}_2(K_5 \square K_8) = 8,\quad \mathrm{wdim}_2(K_5 \square K_9) = 9,\quad
  \mathrm{wdim}_2(K_6 \square K_{10}) = 10,\quad \mathrm{wdim}_2(K_6 \square K_{11}) = 11,$$

  and explicit weak $2$-resolving transversals of size $m$ for these instances
  are recorded in `experiments/results/k2_exact_boundary.json` and re-verified
  by `tests/test_k2.py`. For $n=6$ the note even contradicts the paper's own
  Table 2, which reports $10$ and $11$ at $m = 10, 11$. The paper's Table 1
  ($n=5$) $k=2$ entries $9$ and $10$ at $m = 8, 9$ are overestimates, plausibly
  from the modified ILP formulation the paper uses for $k \in \{2,3\}$.
* Everything the paper reports for $m \le 2n-3$ agrees with our exact
  recomputation: e.g. $\mathrm{wdim}_2(K_5 \square K_6) = 8$,
  $\mathrm{wdim}_2(K_5 \square K_7) = 8$, $\mathrm{wdim}_2(K_6 \square K_7) = 9$.

## 4. Computational evidence (supporting only — no part of the proof)

All evidence below is produced by code paths independent of the construction;
Lemma 1 already proves $\mathrm{wdim}_2 \ge m$, so exhibiting a verified set of
size $m$ certifies optimality.

| Instance | Result | Method |
|---|---|---|
| $(3,3),(3,4),(3,5),(4,5),(4,6),(5,7)$ | exact $\mathrm{wdim}_2$ = 4,4,5,6,6,8 | exhaustive weighted-witness enumeration (`src/exact_hittingset.py`), both directions |
| $n=3..7$, $m$ across the seam and beyond (30 instances) | $\mathrm{wdim}_2 = m$ iff $m \ge 2n-2$ in every instance | exact ILP (`scripts/certify_k2_ilp.py`, HiGHS), sets re-validated |
| transversal criterion (R1)∧(R2) vs. original definition | agree on **all** transversals of $(3,4),(3,5),(4,5),(4,6)$ (5,444 functions) | exhaustive (`tests/test_k2.py`) |
| constructions, $n = 3..10$, $m \in \{2n-2, 2n-1, 2n, 2n+1, 3n\}$ and $m \in \{50,101\}$ | all weak 2-resolving, size $m$ | direct verification (`tests/test_k2.py`, `scripts/sweep_k2.py`) |
| diagonal at $m = 2n-1$, $n = 3..8$ | fails, $\min \Delta = 1$, witness non-aligned | direct verification |
| no valid size-$m$ transversal, $3 \le m \le 2n-3$, $n \le 6$ (bounded) | none exist | exhaustive over transversals (valid by Lemma 2) |

**Observed sub-threshold pattern (unproved conjecture).** In every exact
instance with $n \le m \le 2n-3$ the value matches
$\left\lceil \frac{2(n+m)}{3} \right\rceil$, which contains the square case
$\lceil 4n/3 \rceil$ of the paper's Theorem 1.1. We do **not** prove this here;
it is stated as a conjecture supported by the 30 exact instances above and by
the paper's tables wherever they agree with exact recomputation.

## 5. Reproduce

```bash
pip install -r requirements.txt
pytest tests/test_k2.py -q        # lemma-level and seam-exact tests
python scripts/sweep_k2.py        # construction sweep, m >= 2n-2
pip install scipy                 # optional, only for the ILP certification
python scripts/certify_k2_ilp.py  # independent exact optima via HiGHS
```

## 6. Logical dependencies

* Lemmas 1–5 use only the pair identities (R), (C), (N) of `SOLUTION.md` §3.1,
  which carry over verbatim since they are $k$-independent.
* No citation of the paper's Proposition 4.1/4.2 or Corollary 4.3 is needed
  (those concern $k \ge 3$ reductions; at $k = 2$ everything is handled
  directly).
* No finite computation is used in any proof step; §4 is evidence only.
