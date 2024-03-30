import os
import sys
import logging  # Add logging
from app.CommandLogging import CommandHandler
from app.CommandLogging import Command

class MenuCommand(Command):
    def execute(self):
        show_menu()

def show_menu():
    command_handler = CommandHandler()

    # Get the list of folders in the 'plugins' folder
    plugin_folders = [folder for folder in os.listdir('app/OptionsPlugins') if os.path.isdir(os.path.join('app/OptionsPlugins', folder))]

    # Log the header "Available commands:"
    logging.info("Available commands:")

    # Write the menu commands to sys.stdout
    for plugin_folder in plugin_folders:
        # Ignore the __pycache__ directory inside the menu folder
        if plugin_folder != "__pycache__":
            command = f" - {plugin_folder}"
            sys.stdout.write(command + '\n')
            logging.info(command)