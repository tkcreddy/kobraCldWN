import json
import os
from logpkg.log_kcld import LogKCld,log_to_file
logger=LogKCld()

class OsCustomCmd:

    def __init__(self,cmd):
        self.cmd=cmd


    def command_execute(self):
        count=os.cpu_count()
        data=os.system(self.cmd)
        return data