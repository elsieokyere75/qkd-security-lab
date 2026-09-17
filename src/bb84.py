
"""Educational simulation of ideal BB84 measurement and basis sifting."""

import secrets


def random_bits(count: int) -> list[int]:
    """Generate count random classical bits."""
    if count < 0:
        raise ValueError("count must not be negative")

    return [secrets.randbelow(2) for _ in range(count)]


def random_bases(count: int) -> list[str]:
    """Generate independent random Z/X basis choices."""
    if count < 0:
        raise ValueError("count must not be negative")

    return ["Z" if secrets.randbelow(2) == 0 else "X"
            for _ in range(count)]


def measure(
    alice_bit: int,
    alice_basis: str,
    bob_basis: str,
) -> int:
    """Model an ideal BB84 measurement outcome."""
    if alice_bit not in (0, 1):
        raise ValueError("alice_bit must be 0 or 1")

    if alice_basis not in ("Z", "X") or bob_basis not in ("Z", "X"):
        raise ValueError("bases must be Z or X")

    if alice_basis == bob_basis:
        return alice_bit

    # Measuring in the incompatible basis gives a random result.
    return secrets.randbelow(2)


def sift_keys(
    alice_bits: list[int],
    alice_bases: list[str],
    bob_bits: list[int],
    bob_bases: list[str],
) -> tuple[list[int], list[int]]:
    """Keep only positions where Alice's and Bob's bases match."""
    lengths = {
        len(alice_bits),
        len(alice_bases),
        len(bob_bits),
        len(bob_bases),
    }

    if len(lengths) != 1:
        raise ValueError("All input lists must have equal lengths")

    alice_key = []
    bob_key = []

    for a_bit, a_basis, b_bit, b_basis in zip(
        alice_bits, alice_bases, bob_bits, bob_bases
    ):
        if a_basis == b_basis:
            alice_key.append(a_bit)
            bob_key.append(b_bit)

    return alice_key, bob_key


def simulate_bb84(count: int) -> tuple[list[int], list[int]]:
    """Run ideal BB84 transmission and basis sifting."""
    alice_bits = random_bits(count)
    alice_bases = random_bases(count)
    bob_bases = random_bases(count)

    bob_bits = [
        measure(bit, a_basis, b_basis)
        for bit, a_basis, b_basis in zip(
            alice_bits, alice_bases, bob_bases
        )
    ]

    return sift_keys(
        alice_bits, alice_bases, bob_bits, bob_bases
    )


if __name__ == "__main__":
    alice_key, bob_key = simulate_bb84(20)

    print("Alice's sifted key:", alice_key)
    print("Bob's sifted key:  ", bob_key)
    print("Matching positions:", len(alice_key))