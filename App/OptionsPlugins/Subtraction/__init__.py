import sys
import logging
from app.CommandLogging import Command


class SubtractionCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 - num2
            print(f"the subtraction {num1} and {num2} is : {result}")
        except ValueError:
            logging.error("Error: Please enter valid numbers.")

# Llama a la función para ejecutarla directamente al importar el módulo
if __name__ == "__main__":
    SubtractionCommand().execute()