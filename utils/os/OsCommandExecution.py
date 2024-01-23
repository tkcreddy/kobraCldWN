import json
import os
from logpkg.log_kcld import LogKCld,log_to_file
logger=LogKCld()

class OsCommandExecution:

    def __init__(self):
        return

    @staticmethod
    def command_execute(self, command):
        count=os.cpu_count()
        data=os.system(command)
        return data