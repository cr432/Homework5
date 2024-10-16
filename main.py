import os
import importlib
import inspect
from decimal import Decimal, InvalidOperation
from typing import Dict, Type
from plugins.plugin_interface import CommandPlugin

class Calculator:
    def __init__(self):
        self.plugins: Dict[str, Type[CommandPlugin]] = self.load_plugins()

    def load_plugins(self) -> Dict[str, Type[CommandPlugin]]:
        plugins = {}
        plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        for filename in os.listdir(plugin_dir):
            if filename.endswith('_plugin.py'):
                module_name = f'plugins.{filename[:-3]}'
                module = importlib.import_module(module_name)
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, CommandPlugin) and obj != CommandPlugin:
                        plugin_name = name.lower().replace('plugin', '')
                        plugins[plugin_name] = obj
        return plugins

    def execute_command(self, command: str, a: Decimal, b: Decimal) -> Decimal:
        if command not in self.plugins:
            raise ValueError(f"Unknown command: {command}")
        return self.plugins[command]().execute(a, b)

    def display_menu(self):
        print("\nAvailable commands:")
        commands = ", ".join(self.plugins.keys())
        print(commands)
        print("\nType 'menu' to see this list again, or 'exit' to quit.")

def get_decimal_input(prompt: str) -> Decimal:
    while True:
        try:
            return Decimal(input(prompt))
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")

def main():
    calculator = Calculator()
    
    print("Welcome to the Calculator!")
    calculator.display_menu()
    
    while True:
        command = input("\nEnter command: ").lower().strip()
        
        if command == 'exit':
            print("Goodbye!")
            break
        
        if command == 'menu':
            calculator.display_menu()
            continue
        
        if command not in calculator.plugins:
            print(f"Unknown command: {command}")
            calculator.display_menu()
            continue
        
        try:
            a = get_decimal_input("Enter first number: ")
            b = get_decimal_input("Enter second number: ")
            
            result = calculator.execute_command(command, a, b)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()