
# BB84 Quantum Key Distribution Protocol

## 1. Purpose

BB84 is a quantum key distribution (QKD) protocol that allows Alice and Bob to establish shared secret key material. It uses quantum states to make certain forms of eavesdropping detectable.

The protocol requires both a quantum channel and an authenticated classical channel. The classical channel may be public, but Alice and Bob must be able to verify the authenticity of its messages.

## 2. Encoding bits into quantum states

Alice independently chooses a random classical bit and a random basis for each transmission.

| Bit | Z basis (computational) | X basis (diagonal) |
| --- | --- | --- |
| 0 | \(|0\rangle\) | \(|+\rangle\) |
| 1 | \(|1\rangle\) | \(|-\rangle\) |

The diagonal states are:

\[
|+\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}
\]

\[
|-\rangle = \frac{|0\rangle - |1\rangle}{\sqrt{2}}
\]

Alice prepares the corresponding states and sends them to Bob.

## 3. Bob's measurements

Bob independently chooses either the Z or X basis for each received qubit.

In an ideal channel without interference:

- If Bob chooses Alice's basis, he recovers her encoded bit.
- If Bob chooses the other basis, his result is random, with equal probabilities for 0 and 1.

Bob records his chosen bases and measurement outcomes.

## 4. Basis reconciliation and sifting

After transmission, Alice and Bob announce their basis choices over the authenticated classical channel. They do not announce all their encoded bits.

They keep the positions where their bases match and discard the others. This is called basis sifting.

### Worked example

| Position | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Alice's bit | 1 | 0 | 1 | 0 | 1 | 1 |
| Alice's basis | Z | X | Z | X | X | Z |
| Bob's basis | Z | Z | Z | X | Z | X |
| Keep? | Yes | No | Yes | Yes | No | No |

The matching positions are 1, 3, and 4.

Alice's sifted key is `110`. In the ideal channel without interference, Bob's sifted key is also `110`.

This is an illustrative sifted key, not a final secure key.

## 5. Expected sifting rate

If Alice and Bob choose Z and X independently with equal probability, their bases match in two of four equally likely combinations:

- Z and Z
- X and X

Therefore:

\[
P(\text{basis match}) = \frac{1}{2}
\]

For 200 transmitted qubits, approximately 100 positions are expected to survive basis sifting. The actual number varies because basis choices are random.

## 6. Why authentication matters

Alice and Bob must authenticate their classical messages. Without authentication, Eve could impersonate Bob to Alice and Alice to Bob, potentially establishing separate keys with each party.

Authentication protects the origin and integrity of classical communication. It does not require keeping the announced bases secret.

## 7. Sifting is not the end of BB84

A sifted key is not automatically a final secret key. A more complete QKD workflow includes:

1. Estimating the quantum bit error rate (QBER), potentially by revealing and discarding a sample of sifted bits.
2. Reconciling remaining discrepancies between Alice's and Bob's data.
3. Accounting for information disclosed during reconciliation and information potentially held by Eve.
4. Applying privacy amplification to derive a shorter key.
5. Aborting when the security conditions are not met.

Our educational simulator will introduce these stages progressively. It will not constitute a full security proof or production QKD implementation.

## 8. Day 2 learning outcomes

I can now explain how Alice prepares BB84 states, how Bob measures them, why matching bases are retained, and why approximately half of transmitted positions survive sifting. I also understand that authenticated classical communication is necessary to prevent impersonation.