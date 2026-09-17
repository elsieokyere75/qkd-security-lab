
# BB84 QBER Comparison

## Objective

Compare the sifted-key quantum bit error rate (QBER) in an
ideal BB84 simulation with and without an intercept-resend attack.

## Method

Run 10,000 transmissions in each scenario:

1. No Eve and no noise.
2. Eve intercepts every state, measures in a random basis,
   and resends a replacement state.

Calculate QBER as the number of mismatched sifted bits
divided by the total number of sifted bits.

## Observed results

| Scenario | QBER |
| --- | ---: |
| No Eve, no noise | 0.00% |
| Eve intercepts and resends | 25.50% |

The ideal intercept-resend model predicts an average sifted-key
QBER of 25%. Individual simulation results vary randomly.

## Interpretation

Basis sifting discards positions where Alice and Bob chose
different bases. QBER measures disagreements in the positions
they keep.

Errors can indicate disturbance, but QBER alone cannot establish
that Eve is present. Real-world noise can also produce errors.

This is an educational simulation, not a physical QKD system
or a complete security analysis.