import json
from utils.ReadConfig import ReadConfig as rc
from utils.singleton import Singleton
import os

class _CommandConfig:

    def __init__(self)->None:
        """
        Initialize an instance of the class.

        :param None:
            No parameters required for this method.

        :return:
            This method does not return anything.
        """
        # if file_path is None:
        #     file_path = "../../config/config.json"
        read_confg = rc()
        self.base_dir=read_confg.set_config_dir
        self.file_path = os.path.join(self.base_dir, 'commands.json')
        #self.file_path = file_path
        self._config_data = None
        self.load_config()

    def load_config(self)->any:
        """
        Load configuration data from a specified file.

        :rtype: None
        """
        with open(self.file_path, 'r') as file:
            self._config_data = json.load(file)

    @property
    def os_system_cmd(self)->any:
        """
        Get the OS System Command from the configuration data.

        :return: The OS System Command as specified in the configuration data.
        """
        return self._config_data['OS_System_Cmd']

class CommandConfig(_CommandConfig, metaclass=Singleton):
    """

    :class:`CommandConfig` is a singleton class that extends the `_CommandConfig` base class. This class provides the command configuration for the application.

    This class should not be directly instantiated. Instead, use the `CommandConfig.get_instance()` method to retrieve the singleton instance.

    .. code-block:: python

        from CommandConfig import CommandConfig

        cmd_config = CommandConfig.get_instance()

    Methods:
    ---------

    get_instance()
        Returns the instance of the `CommandConfig` class.

    """
    pass

