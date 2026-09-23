import pytest
from string_tools import clean_text, word_count


@pytest.fixture
def sample_text():
    return "I love Python"


def test_clean_text(sample_text):
    assert clean_text(sample_text) == "hello"


def test_word_count(sample_text):
    assert word_count(sample_text) == 3