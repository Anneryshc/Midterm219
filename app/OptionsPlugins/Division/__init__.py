import sys
import logging
from app.CommandLogging import Command


class DivisionCommand(Command):
    """
    A command to perform division of two numbers.
    """

    def execute(self):
        """
        Executes the division command.
        """
        try:
            logging.info("Starting division operation")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            logging.info(f"User input: {num1}, {num2}")

            if num2 == 0:
                warning_msg = "Warning: Division by zero can lead to unexpected results."
                logging.warning(warning_msg)
                print(warning_msg)
                return None  # Salir del método si el segundo número es cero

            result = num1 / num2
            logging.info(f"Division result: {result}")
            print(f"The division of {num1} and {num2} is : {result}")
            logging.info("Division operation completed successfully")
            
            return result  # Devolver el resultado de la división

        except ValueError:
            error_msg = "error: Please enter valid numbers."
            logging.error(error_msg)
            print(error_msg)
            return None

if __name__ == "__main__":
    DivisionCommand().execute()
    