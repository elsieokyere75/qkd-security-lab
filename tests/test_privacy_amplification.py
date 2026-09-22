import pytest

from src.privacy_amplification import hash_bits


def test_identical_bits_produce_identical_hashes():
    bits = [1, 0, 1, 1]
    assert hash_bits(bits) == hash_bits(bits)


def test_changed_bits_produce_different_hashes():
    assert hash_bits([1, 0, 1, 1]) != hash_bits([1, 0, 1, 0])


def test_rejects_empty_input():
    with pytest.raises(ValueError):
        hash_bits([])


def test_rejects_non_binary_input():
    with pytest.raises(ValueError):
        hash_bits([1, 2, 0])