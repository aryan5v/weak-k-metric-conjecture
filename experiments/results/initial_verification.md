# Initial verification

Date: 2026-08-20

A direct Python verifier was used to test the cyclic construction against the **original distance-sum definition** of weak `k`-resolution.

Initial private scratch run checked:

- `3 <= n <= 8`;
- `n+1 <= m <= min(n+5, 11)`;
- every `3 <= k <= 2n`.

No failure was found, and every constructed set had exactly the cardinality predicted by Conjecture 6.1.

The committed sweep script extends this reproducibly. These checks are adversarial validation only; the proof must stand independently of them.
