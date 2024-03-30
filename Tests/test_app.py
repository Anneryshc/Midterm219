"""
Test for commands.
"""
import logging
import pytest
from app import App

@pytest.fixture
def app():
    """
    Fixture to instantiate the application.
    """
    return App()

def test_app_start_exit_command(app, monkeypatch, caplog):
    """
    Test to verify that the application starts and exits correctly.
    """
    # Set the logging level to capture logs
    caplog.set_level(logging.INFO)

    # Simulate user input 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    # Execute the application and verify that SystemExit exception is raised
    with pytest.raises(SystemExit):
        app.start()

    # Capture the logs generated during execution
    logs = caplog.text
    # Check if the output and logs contain the expected exit message
    assert "Exiting..." in logs
