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
        self.is_running = True
        self.user_input = None
        
        logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(console_handler)

        try:
            load_dotenv() 
        except Exception as e:
            self.logger.error(f"Error loading environment variables: {e}")

        self.data_directory = os.getenv('DATA_DIR', 'data')
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

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
                self.history = pd.concat([self.history, pd.DataFrame({'Operation': [user_input], 'Result': [result]})], ignore_index=True)  # Actualiza el historial con el resultado
                self.logger.info(f"Operation: {user_input}, Result: {result}")

if __name__ == "__main__":
    app = App()
    app.start()

