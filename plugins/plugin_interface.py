# plugin_interface.py
from decimal import Decimal
from abc import ABC, abstractmethod

class CommandPlugin(ABC):
    @abstractmethod
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        pass
