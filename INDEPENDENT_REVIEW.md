# Independent adversarial referee report

**Referee: Kimi K3 model** (independent AI reviewer, isolated worktree, scratch
implementations — no reuse of this repository's `src/` code).

## Verdict

**VALID PROOF**

The referee audited the proof of Conjecture 6.1 at pinned commit `a68accd`
in a detached worktree. Scratch checks were written independently and did not
reuse the repository's `src/` implementations. No repository files were
modified during the audit.

## Obligation table

| # | Item | Verdict |
|---|---|---|
| 1 | Cartesian-product distance and equations (1), (2), and (3) | PASS |
| 2 | Equation (4), `Delta >= 2k-4 >= k`, for every non-aligned pair and `k>=4` | PASS |
| 3 | Even and odd bounded-integer lower bounds, including all stated boundaries | PASS |
| 4 | Cyclic construction for arbitrary `m`, including exact first-block row counts | PASS |
| 5 | Presence and deletion of `(0,n)`, unique deficient column, and retained row bound | PASS |
| 6 | Standalone `k=3` argument and explicit search for `Delta<3` | PASS; true non-aligned minimum is 4 |
| 7 | Exact match between the theorem statement and Conjecture 6.1 | PASS; checked against arXiv:2505.19642 |

## Independent mathematical findings

### Distance identities

The referee re-derived all three identities from

$$d((a,b),(i,j))=\mathbf{1}_{a\ne i}+\mathbf{1}_{b\ne j}.$$

For non-aligned pairs, the endpoint contributions are two, the two cross
vertices contribute zero, and the remaining vertices in exactly one incident
layer contribute one. This gives equation (3) exactly.

### Non-aligned reduction

For $k\ge4$, the aligned premises give

$$\Delta_S\ge(h_j+h_{j'})+(g_i+g_{i'})-4\ge2k-4\ge k.$$

The referee also produced a $3\times4$ matrix showing that this general reduction
is false for $k=3$, confirming that the proof's separate $k=3$ treatment is
necessary.

### Lower bound

Both extremal arguments were rechecked algebraically. The cap $h_j\le n$ cannot
invalidate the lower bound because removing a constraint can only decrease the
relaxed minimum, while the construction attains the claimed value within the
cap. Exhaustive bounded-vector enumeration found the expected minimizers:

- $(r,\dots,r)$ for even $k=2r$;
- permutations of $(r-1,r,\dots,r)$ for odd $k=2r-1$.

This included $m=n+1$, $k=3$, $k=2n-1$, and $k=2n$.

### Construction and deletion

The referee confirmed that column $j$ consists of rows $\{j,\dots,j+r-1\}$ modulo
$n$, and that a complete residue block of $n$ columns contains every row exactly
$r$ times. Column $n$ duplicates column zero, contains $(0,n)$, and its deletion
leaves row zero's $r$ entries among the first $n$ columns untouched.

### The $k=3$ case

After deletion, the column-pair contribution is at least three and the row-pair
contribution at least four. Equation (3) therefore gives

$$\Delta_S\ge3+4-4=3.$$

No non-aligned value below three was found; the actual minimum is four. Same-row
pairs can be tight at three, as required.

## Independent computation

Computational evidence was used only as an adversarial check, not as part of
the proof. The referee reported:

- exhaustive formula verification for every subset of $K_3\square K_3$,
  $K_2\square K_3$, and $K_2\square K_2$;
- 4,000 random subset checks on $4\times5$ and $5\times8$ instances;
- direct construction checks on 616 parameter triples with $3\le n\le9$, plus
  large-$m$ spot checks;
- bounded-column enumeration on 84 instances;
- independent bitmask enumeration and HiGHS ILP certification on the priority
  boundary instances;
- 70 larger ILP certifications, each revalidated against the raw distance
  definition.

Every result agreed with the theorem.

## Suspected gaps investigated and dismissed

- missing or misweighted endpoint terms in equation (3);
- tightness of equation (4) at $k=4$;
- incorrect optimization direction in the lower bound;
- a loophole caused by $h_j\le n$;
- cyclic degeneracy at $r=n$ or for large $m$;
- failure of the $(0,n)$ deletion;
- incompatible simultaneous minima in the $k=3$ estimate;
- drift between the theorem, conjecture, and source definition.

No logical gap or concrete counterexample was found.

## Final assessment

The referee concluded that the proof is self-contained and valid. The only
comments were cosmetic presentation points, not mathematical defects. Commit
`f7d289d` subsequently added tests but did not change the audited proof.
