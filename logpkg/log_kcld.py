import logging
import functools
from utils.ReadConfig import ReadConfig as rc
from utils.singleton import Singleton

class _LogKCld(object):


    read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
    logging_config = read_config.logging_config
    #name="my_app"
    log_file = logging_config['file_path']
    log_level = logging_config['level']
    def __init__(self,name="kcld", log_file=log_file, level=log_level):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler
        self.console_handler = logging.StreamHandler()
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

        # File handler (optional)
        if log_file:
            self.file_handler = logging.FileHandler(log_file)
            self.file_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.file_handler)
        print(f"initialized once")
        #return logger
    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)

def log_to_file(logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Log function call details
                logger.info(f"Calling function: {func.__name__}")
                logger.info(f"Arguments: {args}, {kwargs}")

                # Execute the original function
                result = func(*args, **kwargs)

                # Log the return value
                logger.info(f"Function returned: {func.__name__} {result}")

                return result
            except Exception as e:
                # Log any exceptions that occur during function execution
                logger.error(f"Error in function {func.__name__}: {str(e)}")
                raise

        return wrapper
    return decorator

class LogKCld(_LogKCld,metaclass=Singleton):
    pass
#Example usage
# if __name__ == "__main__":
#
#     # Set up a logger named "my_app"
#     logger = LogKCld()
#     #logger = setup_logger("my_app", log_file="../app.log")
#
#     # Apply the logpkg decorator to a function
#     @log_to_file(logger)
#     def add_numbers(a, b):
#         return a + b
#
#     # Call the decorated function
#     result = add_numbers(3, 5)
#     logger.info(f"Final result: {result}")
