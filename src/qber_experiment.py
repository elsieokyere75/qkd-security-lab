
"""Compare ideal BB84 QBER with and without intercept-resend."""

from src.bb84 import simulate_bb84, simulate_intercept_resend


def qber(alice_key: list[int], bob_key: list[int]) -> float:
    """Calculate the fraction of mismatched sifted bits."""
    if len(alice_key) != len(bob_key):
        raise ValueError("Keys must have equal lengths")
    if not alice_key:
        raise ValueError("Cannot calculate QBER for empty keys")

    errors = sum(
        alice_bit != bob_bit
        for alice_bit, bob_bit in zip(alice_key, bob_key)
    )
    return errors / len(alice_key)


if __name__ == "__main__":
    transmissions = 10_000

    alice_key, bob_key = simulate_bb84(transmissions)
    no_eve_qber = qber(alice_key, bob_key)
    eve_qber = simulate_intercept_resend(transmissions)

    print(f"No Eve QBER:   {no_eve_qber:.2%}")
    print(f"With Eve QBER: {eve_qber:.2%}")