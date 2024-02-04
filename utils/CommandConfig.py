import json
from utils.singleton import Singleton
#from logpkg.log_decorator import setup_logger,log_to_file
#logger = setup_logger("my_app", log_file="app.log")
class _CommandConfig:
    file_path='/Users/krishnareddy/PycharmProjects/kobraCld/config/commands.json'
    def __init__(self, file_path=file_path):
        # if file_path is None:
        #     file_path = "../../config/config.json"
        self.file_path = file_path
        self._config_data = None
        self.load_config()

    def load_config(self):
        with open(self.file_path, 'r') as file:
            self._config_data = json.load(file)

    @property
    def os_system_cmd(self):
        return self._config_data['OS_System_Cmd']

class CommandConfig(_CommandConfig, metaclass=Singleton):
    pass

