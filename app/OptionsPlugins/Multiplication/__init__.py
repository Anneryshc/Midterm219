import sys
import logging
from app.CommandLogging import Command

class MultiplicationCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Registro de la operación de multiplicación iniciada
            print("Performing multiplication...")
            logging.info("Performing multiplication...")
            
            result = num1 * num2
            
            # Registro del resultado de la multiplicación
            print(f"The multiplication of {num1} and {num2} is : {result}")
            logging.info(f"The multiplication of {num1} and {num2} is : {result}")
            
        except ValueError:
            # Registro de error en caso de entrada no válida
            print("Error: Please enter valid numbers.")
            logging.error("Error: Please enter valid numbers.")

# Llama a la función para ejecutarla directamente al importar el módulo
if __name__ == "__main__":
    MultiplicationCommand().execute()
