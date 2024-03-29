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
    # Configurar el logger
    caplog.set_level(logging.INFO)

    # Ejecutar la función show_menu()
    show_menu()

    # Capturar la salida y los registros
    captured = capsys.readouterr()
    logs = caplog.text

    # Verificar si la salida y los registros contienen los comandos esperados
    assert "Available commands:" in logs
    assert " - Addition" in captured.out
    assert " - Division" in captured.out
    assert " - exit" in captured.out
    assert " - Menu" in captured.out
    assert " - Multiplication" in captured.out
    assert " - Subtraction" in captured.out

def test_addition_command(capfd, monkeypatch):
    """Test para el comando de suma."""
    # Simulamos que el usuario ingresa dos números
    inputs = iter(['5', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de suma
    Addition().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la suma se realizó correctamente y el resultado se imprimió
    assert "The addition of 5.0 and 7.0 is : 12.0\n" in captured.out, "The addition was not done correctly"
    
def test_addition_command_negative_numbers(capfd, monkeypatch):
    """Test para el comando de suma con números negativos."""
    # Simulamos que el usuario ingresa dos números negativos
    inputs = iter(['-5', '-7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de suma
    Addition().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la suma se realizó correctamente y el resultado se imprimió
    assert "The addition of -5.0 and -7.0 is : -12.0\n" in captured.out, "The addition of negative numbers was not done correctly"


def test_subtraction_command_valid_input(capfd, monkeypatch):
    """Test para el comando de resta con entrada válida."""
    # Simulamos que el usuario ingresa dos números
    inputs = iter(['5', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de resta
    SubtractionCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Mensaje de la resta esperado, incluyendo el resultado
    expected_output = "The subtraction of 5.0 and 3.0 is : 2.0"

    # Verificamos si la resta se realizó correctamente y el resultado se imprimió
    assert expected_output in captured.out, f"Se esperaba '{expected_output}', pero se obtuvo '{captured.out}'"

def test_subtraction_command_invalid_input(capfd, monkeypatch, caplog):
    """Test para el comando de resta con entrada inválida."""
    # Configurar el logger
    caplog.set_level(logging.ERROR)

    # Simulamos que el usuario ingresa entradas inválidas
    inputs = iter(['invalid', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de resta
    SubtractionCommand().execute()

    # Capturamos los registros del logger
    logs = caplog.text

    # Verificamos si se generó el mensaje de error esperado
    assert "Error: Please enter valid numbers." in logs
    
def test_division_command_valid_input(capfd, monkeypatch, mock_input, caplog):
    """Test para el comando de división con entrada válida."""
    # Simulamos que el usuario ingresa dos números válidos
    mock_input.write('6\n3\n')
    mock_input.seek(0)

    # Ejecutamos el comando de división
    DivisionCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la división se realizó correctamente y el resultado se imprimió
    assert "The division of 6.0 and 3.0 is : 2.0" in captured.out

def test_division_command_invalid_input(capfd, monkeypatch, mock_input, caplog):
    """Test para el comando de división con entrada inválida."""
    # Configurar el logger
    caplog.set_level(logging.ERROR)

    # Simulamos que el usuario ingresa una entrada inválida seguida de un número válido
    mock_input.write('invalid\n3\n')
    mock_input.seek(0)

    # Ejecutamos el comando de división
    DivisionCommand().execute()

    # Capturamos los registros del logger
    logs = caplog.text

    # Verificamos si se generó el mensaje de error esperado
    assert "Please enter valid numbers." in logs
    expected_message = "Please enter valid numbers."
    assert expected_message in logs

def test_multiplication_command(capfd, monkeypatch):
    """Test para el comando de multiplicación."""
    # Simulamos que el usuario ingresa dos números
    inputs = iter(['5', '7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de multiplicación
    MultiplicationCommand().execute()

    # Capturamos la salida de la aplicación
    captured = capfd.readouterr()

    # Verificamos si la multiplicación se realizó correctamente y el resultado se imprimió
    assert "The multiplication of 5.0 and 7.0 is : 35.0\n" in captured.out, "The multiplication was not done correctly"

def test_multiplication_command_invalid_input(capfd, monkeypatch, caplog):
    """Test para el comando de multiplicación con entrada inválida."""
    # Configurar el logger
    caplog.set_level(logging.ERROR)

    # Simulamos que el usuario ingresa un valor inválido seguido de un número válido
    inputs = iter(['invalid', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ejecutamos el comando de multiplicación
    MultiplicationCommand().execute()

    # Capturamos los registros del logger
    logs = caplog.text

    # Verificamos si se generó el mensaje de error esperado
    assert "Error: Please enter valid numbers." in logs
