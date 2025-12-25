import pytest

from src.calculator import multiply_positive_numbers


def test_multiply_positive_numbers():
    assert multiply_positive_numbers(2, 3) == 6


def test_multiply_negative_numbers():
    with pytest.raises(ValueError):
        multiply_positive_numbers(-2, 3)


def test_multiply_non_numbers():
    with pytest.raises(TypeError):
        multiply_positive_numbers("a", 3)
