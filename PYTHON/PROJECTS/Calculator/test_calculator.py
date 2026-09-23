import pytest

from PYTHON.PROJECTS.Calculator.calculator import Calculator


def test_add():
    calculator = Calculator(10, 5)
    assert calculator.add() == 15


def test_subtract():
    calculator = Calculator(10, 5)
    assert calculator.subtract() == 5


def test_multiply():
    calculator = Calculator(10, 5)
    assert calculator.multiply() == 50


def test_power():
    calculator = Calculator(2, 3)
    assert calculator.power() == 8


def test_divide():
    calculator = Calculator(10, 5)
    assert calculator.divide() == 2


def test_divide_by_zero():
    calculator = Calculator(10, 0)

    with pytest.raises(ZeroDivisionError):
        calculator.divide()


def test_negative_numbers():
    calculator = Calculator(-10, -5)

    assert calculator.add() == -15
    assert calculator.subtract() == -5
    assert calculator.multiply() == 50


def test_decimal_numbers():
    calculator = Calculator(10.5, 2.5)

    assert calculator.add() == 13
    assert calculator.subtract() == 8
    assert calculator.multiply() == 26.25
    assert calculator.divide() == pytest.approx(4.2)