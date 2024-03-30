"""
This module contains unit tests for the CommandHandler class.
"""

from app.CommandLogging import CommandHandler, Command


class MockCommand(Command):
    """
    A mock command class to simulate the execution of a command.
    """

    # pylint: disable=too-few-public-methods
    def execute(self):
        """
        Executes the mock command and returns a success message.
        """
        return "Mock Command Executed"


def test_register_and_execute_command():
    """
    Tests the registration and execution of a mock command.
    """
    handler = CommandHandler()
    handler.register_command("mock", MockCommand())
    result = handler.execute_command("mock")
    assert result == "Mock Command Executed"


def test_execute_nonexistent_command():
    """
    Tests the execution of a nonexistent command.
    """
    handler = CommandHandler()
    result = handler.execute_command("nonexistent")
    assert result is None