import sys
import logging
from app.CommandLogging import Command


class DivisionCommand(Command):
    def execute(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if num2 == 0:
                warning_msg = "Warning: Division by zero can lead to unexpected results."
                logging.warning(warning_msg)
                print(warning_msg)
                return  # Salir del método si el segundo número es cero

            result = num1 / num2
            print(f"The division of {num1} and {num2} is : {result}")
        except ValueError:
            error_msg="error: Please enter valid numbers."
            logging.error(error_msg)
            print(error_msg)