import pytest


@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]


def test_length(numbers):
    assert len(numbers) == 5


def test_first_number(numbers):
    assert numbers[0] == 1


def test_last_number(numbers):
    assert numbers[-1] == 5