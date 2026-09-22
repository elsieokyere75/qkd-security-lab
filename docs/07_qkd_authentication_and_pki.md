# QKD Authentication and PKI

## Objective

Explain why BB84 needs authenticated classical communication
and demonstrate a basic challenge-response check.

## Why authentication matters

Alice and Bob publicly exchange messages during BB84,
including their basis choices. These messages do not need
to be secret, but Alice and Bob must verify who sent them
and that they have not been altered.

Without authentication, Eve could impersonate Bob to Alice
and Alice to Bob. Low QBER on the resulting separate
connections would not prevent this attack.

## Educational HMAC demonstration

`src/authentication_demo.py` generates a random challenge.
A party holding the shared secret computes an HMAC response.
The verifier checks that response using the same secret.

The demonstration produced:

- Correct secret: True
- Wrong secret: False

This illustrates possession of a shared secret. It does not
implement certificates, digital signatures, TLS, or a complete
authenticated QKD protocol.

## Connection to PKI

In certificate-based authentication, a certificate binds an
identity to a public key. A relying party must validate the
certificate and verify that its peer possesses the corresponding
private key.

PKI can support authentication of QKD's classical channel,
but the security of that authentication depends on the
selected protocol, cryptographic algorithms, trust anchors,
and implementation.

## Limitations

This project does not yet authenticate BB84 protocol messages.
The HMAC exercise is separate from the BB84 simulator and
does not establish a secure QKD key.