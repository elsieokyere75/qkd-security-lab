import pytest

from src.key_reconciliation import mismatched_positions


def test_finds_one_mismatch():
    alice = [1, 0, 1, 1, 0, 1, 0, 0]
    bob = [1, 0, 1, 0, 0, 1, 0, 0]

    assert mismatched_positions(alice, bob) == [3]


def test_finds_multiple_mismatches():
    assert mismatched_positions([0, 1, 0, 1], [1, 1, 1, 1]) == [0, 2]


def test_matching_keys_have_no_mismatches():
    assert mismatched_positions([1, 0, 1], [1, 0, 1]) == []


def test_rejects_unequal_key_lengths():
    with pytest.raises(ValueError):
        mismatched_positions([1, 0], [1])