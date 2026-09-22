# Key Reconciliation and Hashing Demonstrations

## Objective

Explore two concepts used during QKD key processing:
identifying disagreements between sifted keys and
transforming a bit sequence with a hash function.

## Mismatch detection

`src/key_reconciliation.py` compares Alice's and Bob's
complete bit lists and returns the indexes where they differ.

Example:

Alice: 1 0 1 1 0 1 0 0
Bob:   1 0 1 0 0 1 0 0

The function returns `[3]`, identifying the fourth bit.

This is a local comparison exercise, not a QKD error-correction
protocol. In a real QKD exchange, Alice and Bob must not reveal
their complete secret keys to each other over a public channel.

## Hashing demonstration

`src/privacy_amplification.py` computes a SHA-256 digest of
a bit sequence. Identical inputs produce identical digests.

This demonstrates deterministic hashing, not secure QKD
privacy amplification. Hashing alone does not establish that
Eve's information has been reduced sufficiently.

A real privacy-amplification procedure requires an appropriate
hashing construction, an output length chosen using a security
analysis, and accounting for information revealed during
reconciliation.

## Test results

All 26 project tests passed.

## Limitations

Neither exercise implements a complete QKD key-processing
protocol or establishes a secure final key.