import sys
import logging
from app.CommandLogging import Command

class SubtractionCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Registro de la operación de resta iniciada
            print("Performing subtraction...")
            logging.info("Performing subtraction...")
            
            result = num1 - num2
            
            # Registro del resultado de la resta
            print(f"The subtraction of {num1} and {num2} is : {result}")
            logging.info(f"The subtraction of {num1} and {num2} is : {result}")
            
            return result  # Devolver el resultado de la resta
            
        except ValueError:
            # Registro de error en caso de entrada no válida
            print("Error: Please enter valid numbers.")
            logging.error("Error: Please enter valid numbers.")
