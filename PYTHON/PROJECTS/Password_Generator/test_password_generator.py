import string

import pytest
from password_generator import PasswordGenerator


def test_password_length():
    generator = PasswordGenerator(
        length=12,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True
    )

    password = generator.generate()

    assert len(password) == 12

def test_uppercase():
    generator = PasswordGenerator(
        length=12,
        use_uppercase=True,
        use_lowercase=False,
        use_numbers=False,
        use_symbols=False
    )

    password = generator.generate()

    assert any(character.isupper() for character in password)

def test_lowercase():
    generator = PasswordGenerator(
        length=12,
        use_uppercase=False,
        use_lowercase=True,
        use_numbers=False,
        use_symbols=False
    )

    password = generator.generate()

    assert any(character.islower() for character in password)

def test_numbers():
    generator = PasswordGenerator(
        length=12,
        use_uppercase=False,
        use_lowercase=False,
        use_numbers=True,
        use_symbols=False
    )

    password = generator.generate()

    assert any(character.isdigit() for character in password)



def test_symbols():
    generator = PasswordGenerator(
        length=12,
        use_uppercase=False,
        use_lowercase=False,
        use_numbers=False,
        use_symbols=True
    )

    password = generator.generate()

    assert any(character in string.punctuation for character in password)

def test_no_character_types():
    generator = PasswordGenerator(
        length=12,
        use_uppercase=False,
        use_lowercase=False,
        use_numbers=False,
        use_symbols=False
    )

    with pytest.raises(ValueError):
        generator.generate()

def test_password_too_short():
    generator = PasswordGenerator(
        length=3,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True
    )

    with pytest.raises(ValueError):
        generator.generate()