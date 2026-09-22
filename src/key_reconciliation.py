"""Educational tools for comparing sifted keys."""


def mismatched_positions(
    alice_key: list[int],
    bob_key: list[int],
) -> list[int]:
    """Return the indexes where Alice's and Bob's bits differ."""
    if len(alice_key) != len(bob_key):
        raise ValueError("Keys must have equal lengths")

    return [
        index
        for index, (alice_bit, bob_bit) in enumerate(
            zip(alice_key, bob_key)
        )
        if alice_bit != bob_bit
    ]