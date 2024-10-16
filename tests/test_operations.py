"""
Test for operations.py.
"""
from decimal import Decimal
from calculator.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    """
    Test the AddCommand class.
    """
    add_command = AddCommand()
    result = add_command.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('5')

def test_subtract_command():
    """
    Test the SubtractCommand class.
    """
    subtract_command = SubtractCommand()
    result = subtract_command.execute(Decimal('5'), Decimal('3'))
    assert result == Decimal('2')

def test_multiply_command():
    """
    Test the MultiplyCommand class.
    """
    multiply_command = MultiplyCommand()
    result = multiply_command.execute(Decimal('2'), Decimal('3'))
    assert result == Decimal('6')

def test_divide_command():
    """
    Test the DivideCommand class.
    """
    divide_command = DivideCommand()
    result = divide_command.execute(Decimal('6'), Decimal('2'))
    assert result == Decimal('3')
