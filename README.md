# Calculator App
Welcome to the Calculator App repository! This calculator is a command-line application built in Python that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. It also provides a menu option to display available commands.

# Design Patterns Implementation
We have employed several design patterns to ensure a clean and modular codebase:

Command Pattern: We use the Command pattern to encapsulate each operation as a command object, allowing us to decouple the invoker (user input) from the receiver (operation execution).
Singleton Pattern: The CommandHandler class utilizes the Singleton pattern to ensure that only one instance exists to handle all commands efficiently.
You can explore the implementation of these design patterns in our code:

[Command Pattern ](https://github.com/Anneryshc/Midterm219/tree/main/app/OptionsPlugins)
[Singleton Pattern](https://github.com/Anneryshc/Midterm219/blob/main/app/CommandLogging/__init__.py)

 note :all menu options the user can enter being part of commands pattern

# Environment Variables Usage
We leverage environment variables for configuration settings, such as specifying the data directory location. This enhances flexibility and allows users to customize their environment easily. You can view how we utilize environment variables in our code here.
, DATA_DIR is the environment variable that controls the location of the data directory in your application. You can set this variable in your runtime environment to customize the location of the data directory to your needs.

[Environment Variables](https://github.com/Anneryshc/Midterm219/blob/main/app/__init__.py)

# Logging
Logging plays a crucial role in our application for tracking events, debugging, and error handling. We use Python's built-in logging module to log various events throughout the application's lifecycle. This ensures transparency and facilitates troubleshooting. You can find our logging implementation here.

# Note : you can find logging throughout the program

# Exception Handling
We utilize try/catch blocks to handle exceptions gracefully, following both the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches:

LBYL: We anticipate potential errors, such as invalid user input, and validate inputs before performing operations to prevent exceptions.
EAFP: We catch exceptions that may occur during operation execution and handle them appropriately, displaying informative error messages to the user.
You can see how we implement exception handling in our code to illustrate LBYL and EAFP approaches here.

[Exception Handling ](https://github.com/Anneryshc/Midterm219/tree/main/app/OptionsPlugins)


# Video Demonstration
Check out our video demonstration showcasing the Calculator App's key features and functionalities! Learn how to use the app effectively and explore its capabilities.

[Link to video](https://drive.google.com/file/d/1CoZIoT2SEkL6FoVOGiyP5Izzfu9ON0Mo/view?usp=sharing)

# GitHub Actions
We have integrated GitHub Actions into our workflow to automate testing. Our code undergoes rigorous testing on GitHub Actions, ensuring its reliability and robustness. All tests must pass before any changes are merged into the main branch.

# Pytest,pylint and cov passed

[Pytest](./imagestest/pytest.png)
[coverage](./imagestest/cov1.png)
[Pylint](./imagestest/pylint1.png)

# Usage:
1- Clone this repository to your local machine.
2- Navigate to the project directory.
3- Run python main.py to start the calculator.
4- Follow the on-screen instructions to perform the desired operations.

Feel free to explore our repository, run the application locally, and contribute to its enhancement. We welcome your feedback and contributions!

Enjoy your Python calculator!