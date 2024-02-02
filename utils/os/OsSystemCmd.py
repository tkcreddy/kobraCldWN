import os

from logpkg.log_kcld import LogKCld

logger = LogKCld()


class OsSystemCmd:

    def __init__(self,):
        return

    @staticmethod
    def command_execute(self, command):
        count = os.cpu_count()
        data = os.system(command)
        return data
