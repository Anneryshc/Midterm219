from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.commands = {}
        return cls._instance

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            return self.commands[command_name].execute()  # Devolver el resultado de la operación ejecutada por el comando
        except KeyError:
            print(f"No such command: {command_name}")
            return None

    def get_available_commands(self):
        return list(self.commands.keys())
