
import pytest

from src.bb84 import (
    measure,
    random_bases,
    random_bits,
    sift_keys,
    simulate_bb84,
)


def test_random_bits():
    bits = random_bits(100)

    assert len(bits) == 100
    assert all(bit in (0, 1) for bit in bits)


def test_random_bases():
    bases = random_bases(100)

    assert len(bases) == 100
    assert all(basis in ("Z", "X") for basis in bases)


@pytest.mark.parametrize(
    "bit,basis",
    [
        (0, "Z"),
        (1, "Z"),
        (0, "X"),
        (1, "X"),
    ],
)
def test_matching_bases(bit, basis):
    assert measure(bit, basis, basis) == bit


def test_sifting():
    alice_bits = [1, 0, 1, 0, 1, 1]
    alice_bases = ["Z", "X", "Z", "X", "X", "Z"]
    bob_bases = ["Z", "Z", "Z", "X", "Z", "X"]

    bob_bits = [1, 1, 1, 0, 0, 0]

    alice_key, bob_key = sift_keys(
        alice_bits,
        alice_bases,
        bob_bits,
        bob_bases,
    )

    assert alice_key == [1, 1, 0]
    assert bob_key == [1, 1, 0]


def test_simulation_produces_matching_sifted_keys():
    alice_key, bob_key = simulate_bb84(1000)

    assert alice_key == bob_key
    assert len(alice_key) <= 1000


def test_invalid_bit():
    with pytest.raises(ValueError):
        measure(2, "Z", "Z")


def test_invalid_basis():
    with pytest.raises(ValueError):
        measure(0, "A", "Z")


def test_negative_count():
    with pytest.raises(ValueError):
        random_bits(-1)