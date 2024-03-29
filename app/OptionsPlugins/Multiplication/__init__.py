import sys
import logging
from app.CommandLogging import Command

class MultiplicationCommand(Command):
    """
    A command to perform multiplication of two numbers.
    """

    def execute(self):
        """
        Executes the multiplication command.
        """
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
            
            return result  # Devolver el resultado de la multiplicación
            
        except ValueError:
            # Registro de error en caso de entrada no válida
            print("Error: Please enter valid numbers.")
            logging.error("Error: Please enter valid numbers.")

if __name__ == "__main__":
    MultiplicationCommand().execute()

