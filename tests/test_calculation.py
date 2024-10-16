"""
Test for calculation.py.
"""
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import Command

class MockCommand(Command):
    """
    Test the MockCommand class.
    """
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b

def test_create_calculation():
    """
    Test calculations.
    """
    a = Decimal('2')
    b = Decimal('3')
    command = MockCommand()

    calculation = Calculation.create(a, b, command)

    assert calculation.a == a
    assert calculation.b == b
    assert calculation.command == command

def test_perform_calculation():
    """
    Test results.
    """
    a = Decimal('4')
    b = Decimal('5')
    command = MockCommand()

    calculation = Calculation(a, b, command)
    result = calculation.perform()

    assert result == a + b

def test_repr_calculation():
    """
    Test repr.
    """
    a = Decimal('6')
    b = Decimal('7')
    command = MockCommand()

    calculation = Calculation(a, b, command)
    repr_str = repr(calculation)

    assert f"Calculation({a}, {b}, MockCommand)" == repr_str
