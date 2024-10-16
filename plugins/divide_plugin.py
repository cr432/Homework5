# plugins/divide_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin

class DividePlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Error: Division by zero.")
