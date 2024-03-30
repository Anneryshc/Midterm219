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
            
            # Logging the multiplication operation start
            print("Performing multiplication...")
            logging.info("Performing multiplication...")
            
            result = num1 * num2
            
            # Logging the result of multiplication
            print(f"The multiplication of {num1} and {num2} is : {result}")
            logging.info(f"The multiplication of {num1} and {num2} is : {result}")
            
            return result  # Returning the result of multiplication
            
        except ValueError:
            # Logging error in case of invalid input
            print("Error: Please enter valid numbers.")
            logging.error("Error: Please enter valid numbers.")

if __name__ == "__main__":
    MultiplicationCommand().execute()

