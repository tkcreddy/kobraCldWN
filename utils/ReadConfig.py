import json
from utils.singleton import Singleton
#from logpkg.log_decorator import setup_logger,log_to_file
#logger = setup_logger("my_app", log_file="app.log")
class _ReadConfig:
    def __init__(self, file_path):
        # if file_path is None:
        #     file_path = "../../config/config.json"
        self.file_path = file_path
        self._config_data = None
        self.load_config()

    def load_config(self):
        with open(self.file_path, 'r') as file:
            self._config_data = json.load(file)

    @property
    def logging_config(self):
        return self._config_data['logging']

    @property
    def kakfa_config(self):
        return self._config_data['kafka']

    @property
    def encryption_config(self):
        return self._config_data['encryption']

class ReadConfig(_ReadConfig,metaclass=Singleton):
        pass
