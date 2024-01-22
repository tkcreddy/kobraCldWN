import json
#from logpkg.log_decorator import setup_logger,log_to_file
#logger = setup_logger("my_app", log_file="app.log")
class ReadConfig:
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
    def database_config(self):
        return self._config_data['database']

    @property
    def api_config(self):
        return self._config_data['api']

    @property
    def logging_config(self):
        return self._config_data['logging']

    @property
    def kakfa_config(self):
        return self._config_data['kafka']

    @property
    def encryption_config(self):
        return self._config_data['encryption']
if __name__ == "__main__":
    config_path = "../config/config.json"
    read_config = ReadConfig(config_path)

    # Accessing individual configuration values using properties
    db_config = read_config.database_config
    api_config = read_config.api_config
    logging_config = read_config.logging_config
    logger = setup_logger("my_app", log_file=logging_config['file_path'],level=logging_config['level'])
    kafka_config = read_config.kakfa_config
    encryption_config = read_config.encryption_config
    # Example usage
    # print("Database Host:", db_config['host'])
    # print("Database Port:", db_config['port'])
    # print("API Base URL:", api_config['base_url'])
    # print("Logging Level:", logging_config['level'])
    # print("Logging File Path:", logging_config['file_path'])
    logger.info(f"Database Host: {db_config['host']}")
    logger.info(f"Database Port: {db_config['port']}")
    logger.info(f"API Base URL: {api_config['base_url']}")
    logger.info(f"Logging Level:  {logging_config['level']}")
    logger.info(f"Logging File Path: {logging_config['file_path']}")
    logger.info(f"Kafka config: {kafka_config['bootstrap_servers']}")
    logger.info(f"Encryption Key: {encryption_config['key']}")