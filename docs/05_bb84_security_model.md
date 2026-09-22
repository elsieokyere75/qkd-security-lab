
# BB84 Security Model

## What the simulator demonstrates

The educational simulator models ideal BB84 measurement
probabilities, basis sifting, and an intercept-resend attack.

Without Eve or noise, the sifted-key QBER is 0%.
With Eve intercepting and resending every state, the expected
sifted-key QBER is 25%.

## What QBER tells us

QBER measures the fraction of compared sifted bits that differ.

An elevated QBER indicates errors, but it does not identify
their cause. Eavesdropping, channel noise, and equipment
imperfections can all introduce errors.

## Why authentication matters

Alice and Bob must authenticate their classical messages,
including the messages used for basis comparison.

Without authentication, Eve could impersonate Bob to Alice
and Alice to Bob. Low QBER on those separate connections
would not establish that Alice and Bob share a key with
each other.

## Why a sifted key is not a final key

A complete QKD protocol also needs parameter estimation,
error correction, privacy amplification, and a security
analysis appropriate to its assumptions and implementation.

This project does not yet implement those steps or establish
a secure final key.

## Error correction and privacy amplification

Error correction helps Alice and Bob reconcile differences
between their sifted keys. They exchange authenticated
classical information to identify and correct errors.

That exchange can reveal some information about the key
to Eve, so matching keys alone are not enough.

Privacy amplification uses an appropriate method, such as
universal hashing, to produce a shorter key while reducing
Eve's potential information about it.

The amount of shortening depends on the security analysis,
including the estimated information available to Eve and
information leaked during error correction.