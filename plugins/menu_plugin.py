# plugins/menu_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin

class MenuPlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        print("Available Commands:")
        print("add - Addition")
        print("subtract - Subtraction")
        print("multiply - Multiplication")
        print("divide - Division")
        return 0  # Return 0 or any value, as it won't affect the result
