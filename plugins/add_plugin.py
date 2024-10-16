# plugins/add_plugin.py
from decimal import Decimal
from plugins.plugin_interface import CommandPlugin

class AddPlugin(CommandPlugin):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b
