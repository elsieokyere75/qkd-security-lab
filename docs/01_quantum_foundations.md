# Quantum Foundations for Quantum Key Distribution

## 1. Introduction

Quantum Key Distribution (QKD) uses principles of quantum mechanics to allow two parties to establish secret key material while providing a way to detect certain forms of eavesdropping.

Before implementing the BB84 protocol, it is important to understand several basic concepts:

- Classical bits and qubits
- Quantum states
- Measurement bases
- Superposition
- Measurement disturbance
- The no-cloning theorem

These concepts form the foundation for understanding the security intuition behind BB84.

---

## 2. Classical Bits and Qubits

A classical bit exists in one of two definite states:

0 or 1.

A qubit is a quantum system whose state can be represented as a combination, or superposition, of the basis states |0> and |1>.

A general qubit state can be written as:

|psi> = alpha|0> + beta|1>

where alpha and beta are probability amplitudes satisfying:

|alpha|^2 + |beta|^2 = 1

This does not mean that a measurement simply reveals both 0 and 1. When the qubit is measured in a particular basis, a classical measurement outcome is obtained according to the probabilities associated with the quantum state.

---

## 3. Measurement Bases Used in BB84

BB84 uses two measurement bases.

### 3.1 Computational Basis

The computational basis is also called the Z basis.

Its states are:

|0>

|1>

We use the following encoding:

| Bit | Z Basis State |
| --- | --- |
| 0 | |0> |
| 1 | |1> |

### 3.2 Diagonal Basis

The diagonal basis is also called the X basis.

Its states are:

|+>

|->

where:

|+> = (|0> + |1>) / sqrt(2)

|-> = (|0> - |1>) / sqrt(2)

The encoding is:

| Bit | X Basis State |
| --- | --- |
| 0 | |+> |
| 1 | |-> |

Both the Z and X bases describe and measure quantum states. The Z basis should therefore not be confused with a "classical basis."

---

## 4. Measurement

Measurement is central to BB84.

If Alice prepares a qubit using the Z basis and Bob measures it using the Z basis, Bob obtains Alice's encoded bit with certainty in the ideal model.

For example:

Alice prepares |0>.

Bob measures using the Z basis.

Bob obtains 0 with certainty.

Similarly, if Alice prepares |1> and Bob measures using the Z basis, Bob obtains 1 with certainty.

### Measuring Using a Different Basis

Suppose Alice prepares:

|+>

but Bob measures using the Z basis.

Bob's result is random:

P(0) = 1/2

P(1) = 1/2

Therefore, Bob cannot reliably determine Alice's original X-basis bit.

This gives us an important BB84 principle:

> When Alice and Bob use the same basis, Bob obtains the encoded bit in the ideal model. When they use different bases, Bob's measurement outcome is random.

---

## 5. Measurement Disturbance

Suppose an eavesdropper, Eve, intercepts a qubit sent by Alice.

Eve does not know which basis Alice used.

She may therefore choose the wrong basis when measuring the qubit.

For example:

1. Alice prepares a qubit using the X basis.
2. Eve intercepts the qubit.
3. Eve measures it using the Z basis.
4. Eve obtains a random measurement result.
5. The measurement changes the state available for subsequent processing.
6. Eve sends a state corresponding to her result to Bob.

Because Eve may have measured using the wrong basis, her intervention can introduce errors into the communication.

Alice and Bob can estimate these errors by comparing a sample of their measurement results.

This is one of the ideas behind using the Quantum Bit Error Rate (QBER) to detect abnormal disturbance in a QKD system.

---

## 6. The No-Cloning Theorem

The no-cloning theorem states that an arbitrary unknown quantum state cannot be perfectly copied.

This is important for QKD.

Eve cannot simply intercept an unknown qubit, make a perfect copy of it, keep the copy, and forward another perfect copy to Bob.

If Eve instead measures the qubit to obtain information, she must choose a measurement basis.

Because she does not know Alice's basis in advance, choosing the wrong basis can disturb the state and introduce detectable errors.

The combination of measurement disturbance and the inability to perfectly clone an unknown quantum state contributes to the security principles behind QKD.

---

## 7. Connection to BB84

BB84 uses these quantum properties to establish secret key material between two parties traditionally called Alice and Bob.

The basic idea is:

1. Alice randomly chooses classical bits.
2. Alice randomly chooses Z or X bases.
3. Alice prepares quantum states according to those bits and bases.
4. Bob randomly chooses bases in which to measure the received states.
5. Alice and Bob publicly compare their basis choices.
6. They keep results for positions where their bases matched.
7. They estimate the error rate using part of their data.
8. An unexpectedly high error rate may indicate excessive noise or possible eavesdropping.

Later stages of a complete QKD protocol also require authenticated classical communication, error correction, privacy amplification, and appropriate security analysis.

---

## 8. Key Lessons

From this first stage of the project:

- A classical bit has a definite value of 0 or 1.
- A qubit can exist in a superposition of basis states.
- BB84 uses the Z and X bases.
- Measuring in the correct basis gives the expected encoded bit in the ideal model.
- Measuring in an incompatible basis produces a random result.
- Measuring a quantum system can disturb its state.
- An arbitrary unknown quantum state cannot be perfectly cloned.
- Eavesdropping can therefore introduce errors that Alice and Bob may detect.

These concepts provide the foundation for implementing and analyzing the BB84 protocol.