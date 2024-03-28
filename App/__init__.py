import pkgutil
import importlib
import logging
import pandas as pd  # Importar Pandas para la gestión del historial
from app.CommandLogging import CommandHandler
from app.CommandLogging import Command
from app.OptionsPlugins.Menu import MenuCommand
from dotenv import load_dotenv
import os

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.is_running = True
        self.user_input = None  # Inicializar la entrada del usuario

        # Configurar loggings
        logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        # Configurar un manejador adicional para mostrar mensajes de nivel INFO en la consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(console_handler)

        # Crear o cargar el archivo de historial de cálculos con Pandas
        self.history_file = 'calc_history.csv'
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
        else:
            self.history = pd.DataFrame(columns=['Operation', 'Result'])
            self.history.to_csv(self.history_file, index=False)

        # Cargar variables de entorno desde el archivo .env
        load_dotenv()

    def load_plugins(self):
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

        # Registra el comando de menú
        self.command_handler.register_command('menu', MenuCommand())

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit.")
        while self.is_running:
            if self.user_input is not None:
                user_input = self.user_input  # Utilizar la entrada proporcionada
                self.user_input = None  # Restablecer la entrada para la próxima iteración
            else:
                user_input = input(">>> ").strip()
                self.logger.info(f"User input: {user_input}")  # Registro de la acción del usuario
            if user_input == 'exit':
                self.logger.info("Exiting...")
                # Guardar el historial de cálculos antes de salir
                self.history.to_csv(self.history_file, index=False)
                raise SystemExit  # Lanzar excepción SystemExit
            else:
                # Ejecutar el comando y registrar el resultado en el historial
                result = self.command_handler.execute_command(user_input)
                self.history = self.history.append({'Operation': user_input, 'Result': result}, ignore_index=True)

if __name__ == "__main__":
    app = App()
    app.start()
