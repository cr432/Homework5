'''confest.py file'''
from decimal import Decimal
import pytest
from calculator.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand

@pytest.fixture
def a_b_values():
    """Fixture providing example values for the 'a' and 'b' parameters."""
    return Decimal('3'), Decimal('2')  # Example values for a and b

@pytest.fixture
def command_instances():
    """Fixture providing instances of each command class to be tested."""
    return [
        AddCommand(),
        SubtractCommand(),
        MultiplyCommand(),
        DivideCommand(),
        MenuCommand()
    ]

@pytest.mark.parametrize("command_instance", [
    AddCommand(),
    SubtractCommand(),
    MultiplyCommand(),
    DivideCommand(),
    MenuCommand()
])

def test_execute(command_instance, a_b_values):
    """Test the execute method of each command class."""
    result = command_instance.execute(*a_b_values)
    assert isinstance(result, Decimal)
