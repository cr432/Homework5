# __init__.py
from decimal import Decimal
from calculator.operations import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, MenuCommand  # Import the MenuCommand
from calculator.calculations import Calculations  # Manages history of calculations
from calculator.calculation import Calculation  # Represents a single calculation

# Definition of the Calculator class
class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, command) -> Decimal:
        """Create and perform a calculation, then return the result."""
        # Create a Calculation object using the static create method, passing in operands and the operation
        calculation = Calculation.create(a, b, command)
        # Add the calculation to the history managed by the Calculations class
        Calculations.add_calculation(calculation)
        # Perform the calculation and return the result
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, AddCommand())

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, SubtractCommand())

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, MultiplyCommand())

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, DivideCommand())

    @staticmethod
    def menu(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, MenuCommand())
