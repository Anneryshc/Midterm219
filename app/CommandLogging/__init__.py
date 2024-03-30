from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract base class representing a command.
    """
    @abstractmethod
    def execute(self):
        """
        Abstract method to execute the command.
        """
        pass

class CommandHandler:
    """
    Singleton class to handle commands.
    """

    _instance = None  # Class variable to store the singleton instance

    def __new__(cls):
        """
        Create a new instance if it doesn't exist.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.commands = {}  # Dictionary to store registered commands
        return cls._instance

    def register_command(self, command_name: str, command: Command):
        """
        Register a new command.

        Args:
            command_name (str): Name of the command.
            command (Command): Instance of the command.
        """
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """
        Execute a registered command.

        Args:
            command_name (str): Name of the command to execute.

        Returns:
            Result of the executed command.
        """
        try:
            return self.commands[command_name].execute()  # Return the result of the executed command
        except KeyError:
            print(f"No such command: {command_name}")
            return None

    def get_available_commands(self):
        """
        Get a list of available commands.

        Returns:
            List of available command names.
        """
        return list(self.commands.keys())
