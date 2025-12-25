import pytest

from src.string_utils import count_vowels


def test_count_vowels():
    assert count_vowels("banana") == 3


def test_count_vowels_case_insensitive():
    assert count_vowels("ApPlE") == 2


def test_count_vowels_non_string():
    with pytest.raises(TypeError):
        count_vowels(1234)
