
import pytest

from src.qber_experiment import qber


def test_qber_no_errors():
    assert qber([0, 1, 1, 0], [0, 1, 1, 0]) == 0.0


def test_qber_one_error_in_four_bits():
    assert qber([0, 1, 1, 0], [0, 1, 0, 0]) == 0.25


def test_qber_all_bits_differ():
    assert qber([0, 1, 1, 0], [1, 0, 0, 1]) == 1.0


def test_qber_rejects_unequal_lengths():
    with pytest.raises(ValueError):
        qber([0, 1], [0])


def test_qber_rejects_empty_keys():
    with pytest.raises(ValueError):
        qber([], [])