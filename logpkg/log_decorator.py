import logging
import functools
def setup_logger(name, log_file=None, level=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

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
                logger.info(f"Function returned: {result}")

                return result
            except Exception as e:
                # Log any exceptions that occur during function execution
                logger.error(f"Error in function {func.__name__}: {str(e)}")
                raise

        return wrapper
    return decorator

#Example usage
if __name__ == "__main__":
    # Set up a logger named "my_app"
    logger = setup_logger("my_app", log_file="../app.log")

    # Apply the logpkg decorator to a function
    @log_to_file(logger)
    def add_numbers(a, b):
        return a + b

    # Call the decorated function
    result = add_numbers(3, 5)
    logger.info(f"Final result: {result}")
