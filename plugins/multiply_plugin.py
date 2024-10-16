# plugins/multiply_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin

class MultiplyPlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a * b
