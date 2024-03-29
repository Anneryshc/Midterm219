import sys
import logging
from app.CommandLogging import Command

class Addition(Command):
    """
    A command to perform addition of two numbers.
    """

    def execute(self):
        """
        Executes the addition command.
        """
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if num1 < 0 or num2 < 0:
                # Registro de advertencia para números negativos
                print("Warning: Performing addition with negative numbers.")
                logging.warning("Performing addition with negative numbers.")
            
            # Registro de la operación de suma iniciada
            print("Performing addition...")
            logging.info("Performing addition...")
            
            result = num1 + num2
            
            # Registro del resultado de la suma
            print(f"The addition of {num1} and {num2} is : {result}")
            logging.info(f"The addition of {num1} and {num2} is : {result}")
            
            return result  # Devolver el resultado de la suma
            
        except ValueError:
            # Registro de error en caso de entrada no válida
            print("Error: Please enter valid numbers.")
            logging.error("Invalid input: Please enter valid numbers.")

if __name__ == "__main__":
    Addition().execute()

