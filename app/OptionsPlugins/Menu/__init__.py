import os
import sys
import logging  # Agregar logging
from app.CommandLogging import CommandHandler
from app.CommandLogging import Command

class MenuCommand(Command):
    def execute(self):
        show_menu()

def show_menu():
    command_handler = CommandHandler()

    # Obtener la lista de carpetas en la carpeta 'plugins'
    plugin_folders = [folder for folder in os.listdir('app/OptionsPlugins') if os.path.isdir(os.path.join('app/OptionsPlugins', folder))]

    # Registrar el encabezado "Available commands:"
    logging.info("Available commands:")

    # Escribir los comandos del menú en sys.stdout
    for plugin_folder in plugin_folders:
        # Ignorar el directorio __pycache__ dentro de la carpeta menu
        if plugin_folder != "__pycache__":
            command = f" - {plugin_folder}"
            sys.stdout.write(command + '\n')
            logging.info(command)