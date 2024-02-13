class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Create and return an instance of the class if it doesn't exist yet.
        Otherwise, return the existing instance.

        :param cls: The class object.
        :param args: The positional arguments to be passed to the class constructor.
        :param kwargs: The keyword arguments to be passed to the class constructor.
        :return: An instance of the class.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(type(cls), cls).__call__(*args, **kwargs)
        return cls._instances[cls]