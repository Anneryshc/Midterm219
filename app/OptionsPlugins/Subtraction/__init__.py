import sys
import logging
from app.CommandLogging import Command

class SubtractionCommand(Command):
    """
    A command class to perform subtraction operation.
    """

    def execute(self):
        """
        Executes the subtraction command.
        """
        try:
            num1 = float(input("Enter the first number: "))  # Prompt user to enter the first number
            num2 = float(input("Enter the second number: "))  # Prompt user to enter the second number
            
            # Log the start of subtraction operation
            print("Performing subtraction...")
            logging.info("Performing subtraction...")
            
            result = num1 - num2  # Perform the subtraction
            
            # Log the result of the subtraction
            print(f"The subtraction of {num1} and {num2} is : {result}")
            logging.info(f"The subtraction of {num1} and {num2} is : {result}")
            
            return result  # Return the result of the subtraction
            
        except ValueError:
            # Log error for invalid input
            print("Error: Please enter valid numbers.")
            logging.error("Error: Please enter valid numbers.")
