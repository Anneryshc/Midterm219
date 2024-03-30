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
                # Warning message for negative numbers
                print("Warning: Performing addition with negative numbers.")
                logging.warning("Performing addition with negative numbers.")
            
            # Log the start of addition operation
            print("Performing addition...")
            logging.info("Performing addition...")
            
            result = num1 + num2
            
            # Log the result of addition
            print(f"The addition of {num1} and {num2} is : {result}")
            logging.info(f"The addition of {num1} and {num2} is : {result}")
            
            return result  # Return the result of addition
            
        except ValueError:
            # Log error for invalid input
            print("Error: Please enter valid numbers.")
            logging.error("Invalid input: Please enter valid numbers.")

if __name__ == "__main__":
    Addition().execute()

