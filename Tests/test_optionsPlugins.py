"""
Test de comandos.
"""
from io import StringIO
import logging
import pytest
from app.OptionsPlugins.Addition import Addition
from app.OptionsPlugins.Subtraction import SubtractionCommand
from app.OptionsPlugins.Multiplication import MultiplicationCommand
from app.OptionsPlugins.Division import DivisionCommand
from app.OptionsPlugins.Menu import show_menu


@pytest.fixture
def mock_input(monkeypatch):
    """Fixture para la entrada de usuario simulada."""
    user_input = StringIO()
    monkeypatch.setattr('sys.stdin', user_input)
    return user_input

def test_app_menu_command(capsys, caplog):
    """Test para verificar el menú de la aplicación."""
    # Configure the logger
    caplog.set_level(logging.INFO)

    # Execute the show_menu() function
    show_menu()

    # Capture output and logs
    captured = capsys.readouterr()
    logs = caplog.text

   # Check if the output and logs contain the expected commands
    assert "Available commands:" in logs
    assert " - Addition" in captured.out
    assert " - Division" in captured.out
    assert " - exit" in captured.out
    assert " - Menu" in captured.out
    assert " - Multiplication" in captured.out
    assert " - Subtraction" in captured.out

def test_addition_command(capfd, monkeypatch):
    """Test for the addition command."""
    # We simulate that the user enters two numbers
    inputs = iter(['5', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # We execute the addition command
    Addition().execute()

    # We capture the output of the application
    captured = capfd.readouterr()

    # We check if the addition was performed correctly and the result was printed
    assert "The addition of 5.0 and 7.0 is : 12.0\n" in captured.out, "The addition was not done correctly"

def test_addition_command_negative_numbers(capfd, monkeypatch):
    """Test for the addition command with negative numbers."""
    # We simulate that the user enters two negative numbers
    inputs = iter(['-5', '-7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # We execute the addition command
    Addition().execute()

    # We capture the output of the application
    captured = capfd.readouterr()

    # We check if the addition was performed correctly and the result was printed
    assert "The addition of -5.0 and -7.0 is : -12.0\n" in captured.out, "The addition of negative numbers was not done correctly"


def test_subtraction_command_valid_input(capfd, monkeypatch):
    """Test for the subtraction command with valid input."""
    # We simulate that the user enters two numbers
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # We execute the subtraction command
    SubtractionCommand().execute()

    # We capture the output of the application
    captured = capfd.readouterr()

    # Expected subtraction message, including the result
    expected_output = "The subtraction of 5.0 and 3.0 is : 2.0"

    # We check if the subtraction was performed correctly and the result was printed
    assert expected_output in captured.out, f"Se esperaba '{expected_output}', pero se obtuvo '{captured.out}'"

def test_subtraction_command_invalid_input(capfd, monkeypatch, caplog):
    """Test for subtraction command with invalid input."""
    # Configure the logger
    caplog.set_level(logging.ERROR)

    # We simulate that the user enters invalid entries
    inputs = iter(['invalid', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # We execute the subtraction command
    SubtractionCommand().execute()

    # We capture the logger logs
    logs = caplog.text

    # We check if the expected error message was generated
    assert "Error: Please enter valid numbers." in logs

def test_division_command_valid_input(capfd, monkeypatch, mock_input, caplog):
    """Test for the division command with valid input."""
    # We simulate that the user enters two valid numbers
    mock_input.write('6\n3\n')
    mock_input.seek(0)

    # We execute the division command
    DivisionCommand().execute()

   # We capture the output of the application
    captured = capfd.readouterr()

    # Verificamos si la división se realizó correctamente y el resultado se imprimió
    assert "The division of 6.0 and 3.0 is : 2.0" in captured.out

def test_division_command_invalid_input(capfd, monkeypatch, mock_input, caplog):
    """Test for division command with invalid input."""
    # Configure the logger
    caplog.set_level(logging.ERROR)

    # We simulate the user entering an invalid entry followed by a valid number
    mock_input.write('invalid\n3\n')
    mock_input.seek(0)

    # We execute the division command
    DivisionCommand().execute()

    # We capture the logger logs
    logs = caplog.text

  # We check if the expected error message was generated
    assert "Please enter valid numbers." in logs
    expected_message = "Please enter valid numbers."
    assert expected_message in logs

def test_multiplication_command(capfd, monkeypatch):
    """Test for the multiplication command."""
    # We simulate that the user enters two numbers
    inputs = iter(['5', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # We execute the multiplication command
    MultiplicationCommand().execute()

    # We capture the output of the application
    captured = capfd.readouterr()

    # We check if the multiplication was performed correctly and the result was printed
    assert "The multiplication of 5.0 and 7.0 is : 35.0\n" in captured.out, "The multiplication was not done correctly"

def test_multiplication_command_invalid_input(capfd, monkeypatch, caplog):
    """Test para el comando de multiplicación con entrada inválida."""
    # Configure the logger
    caplog.set_level(logging.ERROR)

    # We simulate the user entering an invalid value followed by a valid number
    inputs = iter(['invalid', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # We execute the multiplication command
    MultiplicationCommand().execute()

    # We capture the logger logs
    logs = caplog.text

   # We check if the expected error message was generated
    assert "Error: Please enter valid numbers." in logs
