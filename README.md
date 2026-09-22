
# QKD Security Lab

## Overview

QKD Security Lab is a self-directed educational project exploring the foundations and security of quantum key distribution (QKD), with a focus on the BB84 protocol.

The project combines written study, Python simulations, experiments, and tests. It examines ideal BB84 measurement probabilities, basis sifting, an intercept-resend attack, quantum bit error rate (QBER), and the role of authenticated classical communication.

It also includes introductory exercises on key comparison and hashing, plus a conceptual architecture connecting QKD, post-quantum cryptography (PQC), and public key infrastructure (PKI).

**This is an educational simulation, not a physical QKD implementation or a security-validated protocol.**

## Objectives

- Understand the quantum principles underlying BB84.
- Simulate ideal BB84 measurement and basis sifting.
- Model an intercept-resend eavesdropping attack.
- Compare sifted-key QBER with and without Eve.
- Study QKD security assumptions and authentication requirements.
- Explore key reconciliation and hashing through limited educational exercises.
- Examine the complementary roles of QKD, PQC, and PKI.

## Project Roadmap

| Day | Topic | Status |
| --- | --- | --- |
| 1 | Quantum foundations for QKD | Completed |
| 2 | BB84 protocol and mathematics | Completed |
| 3 | Ideal BB84 simulation and testing | Completed |
| 4 | Intercept-resend attack | Completed |
| 5 | QBER comparison and experiments | Completed |
| 6 | Security model and adversary assumptions | Completed |
| 7 | Key comparison and hashing demonstrations | Completed |
| 8 | Authentication and PKI concepts | Completed |
| 9 | Conceptual QKD, PQC, and PKI architecture | Completed |
| 10 | Repository review and final documentation | In progress |

## Implemented Work

### BB84 simulation

`src/bb84.py` models ideal measurement outcomes and basis sifting. It also includes an intercept-resend model in which Eve measures each intercepted state in a randomly selected basis and resends a replacement.

### QBER experiments

`src/qber_experiment.py` compares sifted-key error rates with and without Eve.

In one run of 10,000 transmissions per scenario, the observed results were:

| Scenario | Observed sifted-key QBER |
| --- | ---: |
| No Eve and no noise | 0.00% |
| Eve intercepts and resends every state | 25.50% |

The ideal intercept-resend model predicts an average sifted-key QBER of 25%. Results vary between runs because the simulation uses randomness. Errors indicate disturbance but do not, by themselves, prove that Eve is present.

### Key comparison and hashing

`src/key_reconciliation.py` identifies mismatched positions by comparing two complete bit lists locally. It **does not implement a QKD error-correction protocol**.

`src/privacy_amplification.py` demonstrates deterministic SHA-256 hashing. Despite its filename, it **does not implement or establish secure QKD privacy amplification**.

### Authentication demonstration

`src/authentication_demo.py` demonstrates HMAC challenge-response using a shared secret. It does not implement certificates, digital signatures, TLS, or authentication of the BB84 simulator's classical messages.

### Architecture model

`src/architecture_model.py` describes proposed QKD, PQC, and PKI components and flags a configuration where QKD is enabled without an authenticated classical channel. It records design assumptions; it does not validate a deployed system.

## Run the Project

From the repository root, with Python and pytest installed:

```powershell
python -m pip install pytest
python -m src.bb84
python -m src.qber_experiment
python -m pytest -q
```

At the end of Day 9, the test suite contained **33 passing tests**.

## Documentation

| File | Topic |
| --- | --- |
| `docs/01_quantum_foundations.md` | Quantum foundations |
| `docs/02_bb84_protocol.md` | BB84 protocol |
| `docs/03_intercept_resend_attack.md` | Intercept-resend attack |
| `docs/04_qber_comparison.md` | QBER experiment |
| `docs/05_bb84_security_model.md` | Security assumptions and key processing |
| `docs/06_key_reconciliation_and_hashing.md` | Key comparison and hashing limitations |
| `docs/07_qkd_authentication_and_pki.md` | Authentication and PKI |
| `docs/08_qkd_pqc_pki_architecture.md` | Conceptual QKD, PQC, and PKI design |

## Scope and Limitations

This repository samples ideal BB84 measurement probabilities using classical Python code. It does not simulate physical qubits or quantum hardware.

It does not implement a complete QKD protocol, secure error correction, security-parameter-based privacy amplification, or an authenticated classical channel for BB84. It does not establish a secure final key or provide a formal security proof.

The QKD, PQC, and PKI architecture is a conceptual proposal, not an implemented hybrid cryptographic protocol.

## Related Research Interests

- Quantum cryptography and QKD
- Post-quantum cryptography
- Cryptographic protocol security
- PKI and digital identity
- Quantum-safe infrastructure and crypto-agility
```

