import pkgutil
import importlib
import logging
import pandas as pd
from app.CommandLogging import CommandHandler, Command
from app.OptionsPlugins.Menu import MenuCommand
from dotenv import load_dotenv
import os

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.is_running = True  # Eliminado el punto y coma
        self.user_input = None  # Eliminado el punto y coma
        
        # Configurar loggings
        logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        # Configurar un manejador adicional para mostrar mensajes de nivel INFO en la consola
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(console_handler)

        # Cargar variables de entorno desde el archivo .env
        try:
            load_dotenv() 
        except Exception as e:
            self.logger.error(f"Error loading environment variables: {e}")

        # Obtener la ruta de la carpeta de datos desde la variable de entorno
        self.data_directory = os.getenv('DATA_DIR')
        if self.data_directory is None:
            self.logger.error("Error: DATA_DIR variable de entorno no configurada.")
            raise ValueError("DATA_DIR variable de entorno no configurada.")
        
        # Crear o cargar el archivo de historial de cálculos con Pandas
        self.history_file = os.path.join(self.data_directory, 'calc_history.csv')
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)
        else:
            self.history = pd.DataFrame(columns=['Operation', 'Result'])
            self.history.to_csv(self.history_file, index=False)

    def load_plugins(self):
        plugins_package = 'app.OptionsPlugins'
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
        self.command_handler.register_command('Menu', MenuCommand())

    def start(self):
        self.load_plugins()
        print("Type 'exit' to exit, For more information write 'Menu'")
        while self.is_running:
            if self.user_input is not None:
                user_input = self.user_input
                self.user_input = None
            else:
                user_input = input(">>> ").strip()
                self.logger.info(f"User input: {user_input}")
            if user_input == 'exit':
                self.logger.info("Exiting...")
                self.history.to_csv(self.history_file, index=False)
                raise SystemExit
            else:
                result = self.command_handler.execute_command(user_input)
                self.history = pd.concat([self.history, pd.DataFrame({'Operation': [user_input], 'Result': [result]})], ignore_index=True)

if __name__ == "__main__":
    app = App()
    app.start()
