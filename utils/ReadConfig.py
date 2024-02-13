import json
from utils.singleton import Singleton
import os
#from logpkg.log_decorator import setup_logger,log_to_file
#logger = setup_logger("my_app", log_file="app.log")
class _ReadConfig:

    def __init__(self,base_dir=None):
        """
        Initialize the ReadConfig object.

        :param base_dir: The base directory to use for the configuration file. Defaults to 'config/' if not provided.
        """
        if base_dir != None:
            self.base_dir=base_dir
        else:
            self.base_dir='config/'
        self.file_path = os.path.join(self.base_dir, 'config.json')
        self._config_data = None
        self.load_config()
        print(f"Initializing ReadConfig once {self.file_path}")
    @property
    def set_config_dir(self):
        """

        This method sets the configuration directory.

        :param self: This is a reference to the current object.
        :return: Returns the base directory where the configuration files are located.

        """
        return self.base_dir
    def load_config(self):
        """
        Load configuration data from a file.

        :return: None
        """
        try:
            with open(self.file_path, 'r') as file:
                self._config_data = json.load(file)
        except Exception as e:
            print(f"file open error {e}")

    @property
    def logging_config(self):
        """
        Retrieves the logging configuration data.

        :return: The logging configuration data.
        """
        return self._config_data['logging']

    @property
    def kafka_config(self):
        """
        Retrieves the Kafka configuration from the _config_data dictionary.

        :return: The Kafka configuration.
        """
        return self._config_data['kafka']

    @property
    def kafka_ssl(self):
        """
        :return: The SSL configuration for Kafka
        """
        return self.kafka_config['ssl_config']

    @property
    def encryption_config(self):
        """
        Retrieves the encryption configuration data.

        :return: The encryption config data.
        """
        return self._config_data['encryption']

class ReadConfig(_ReadConfig,metaclass=Singleton):
    """
    ReadConfig Class
    ================

    This class is a singleton that provides functionality to read configuration data.

    """
    pass
