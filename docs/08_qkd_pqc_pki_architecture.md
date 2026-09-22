
# Proposed QKD, PQC, and PKI Architecture

## Objective

Explore how quantum key distribution, post-quantum
cryptography, and public key infrastructure could
serve complementary roles in a communication system.

This is a conceptual design, not a deployed or
security-validated system.

## Components

### Alice and Bob

The two endpoints that want to establish shared
key material and communicate securely.

### QKD link

An idealized quantum channel carries BB84 states.
An authenticated classical channel supports basis
comparison and other protocol messages.

The QKD process requires parameter estimation,
error correction, privacy amplification, and
appropriate security checks before key material
can be treated as a final key.

### PQC mechanisms

Post-quantum cryptographic mechanisms can support
key establishment and authentication without
requiring a quantum communication channel.

The choice of algorithms, protocols, and how keys
are combined requires a separate security analysis.

### PKI

A certificate infrastructure can bind endpoint
identities to public keys and support certificate
issuance, validation, renewal, and revocation.

Certificates alone do not authenticate a session.
The protocol must also establish that a peer
possesses the corresponding private key.

## Proposed communication flow

1. Alice and Bob validate the identities and
   authentication credentials used by their
   classical communication protocol.
2. They establish an authenticated classical
   channel.
3. They exchange BB84 states over a quantum link
   and perform authenticated basis comparison.
4. They estimate errors and, if the protocol's
   security conditions permit, perform error
   correction and privacy amplification.
5. A separate PQC key-establishment mechanism
   may provide additional shared key material.
6. Any combination of QKD-derived and PQC-derived
   key material must use a carefully specified,
   analyzed key-derivation design.

## Trust assumptions and limitations

- The classical channel must be authenticated.
- Certificate validation and private-key protection
  remain important.
- QKD hardware and channel behavior introduce
  implementation assumptions absent from our
  educational simulator.
- A low QBER alone does not establish a secure key.
- This project does not implement or validate
  a combined QKD-PQC protocol.

  ## Python architecture model

`src/architecture_model.py` describes which components are
included in a proposed design and warns when QKD is enabled
without an authenticated classical channel.

The model does not establish a connection, validate a
certificate, perform PQC key establishment, or generate
a secure QKD key. Its authentication setting records a
design assumption rather than verifying a real channel.

All 33 project tests passed.