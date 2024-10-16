# calculation.py
from decimal import Decimal
from calculator.operations import Command  # Assuming you have a commands module

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, command: Command):
        self.a = a
        self.b = b
        self.command = command

    @staticmethod    
    def create(a: Decimal, b: Decimal, command: Command):
        return Calculation(a, b, command)

    def perform(self) -> Decimal:
        """Perform the stored calculation and return the result."""
        return self.command.execute(self.a, self.b)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.command.__class__.__name__})"
