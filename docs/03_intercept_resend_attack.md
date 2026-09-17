
# BB84 Intercept-Resend Attack

## Objective

Extend an educational BB84 simulator to model an eavesdropper,
Eve, and observe the errors introduced into the sifted key.

## Attack model

1. Alice prepares a bit using a randomly chosen Z or X basis.
2. Eve intercepts the state and measures it in a random basis.
3. Eve prepares a replacement using her measurement result and basis.
4. Bob measures the replacement in his randomly chosen basis.
5. Alice and Bob retain positions where their bases match.

The simulator samples ideal measurement outcomes. It does not
simulate physical qubits or a complete QKD security protocol.

## Expected QBER

For a sifted position, Eve chooses the wrong basis with
probability 1/2. In that case, Bob obtains the wrong bit with
probability 1/2.

Expected QBER = 1/2 × 1/2 = 1/4 = 25%.

## Experiment

Transmissions: 10,000
Observed sifted-key QBER: 25.78%

The observed result is close to the theoretical expectation.
Individual runs vary because the choices and measurements are random.

## Interpretation

An elevated QBER can reveal disturbance, but it does not by
itself prove that Eve is present. Noise and equipment
imperfections can also produce errors.

A sifted key is not automatically a secure final key.
Practical QKD also requires authenticated classical
communication, parameter estimation, error correction,
privacy amplification, and a suitable security analysis.