# commands.py
from decimal import Decimal
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        pass

class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b

class SubtractCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a - b

class MultiplyCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b

class DivideCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Error: Division by zero.")

class MenuCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        print("Available Commands:")
        print("add - Addition")
        print("subtract - Subtraction")
        print("multiply - Multiplication")
        print("divide - Division")
        return 0  # Return 0 or any value, as it won't affect the result
