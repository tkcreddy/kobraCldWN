import json
#from logpkg.log_decorator import setup_logger,log_to_file
#logger = setup_logger("my_app", log_file="app.log")
class CommandConfig:
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
    def system_config_info(self):
        return self._config_data['system_configuration']


