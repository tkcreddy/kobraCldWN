import os
import subprocess
from logpkg.log_kcld import LogKCld,log_to_file

logger = LogKCld()


class OsSystemCmd():

    def __init__(self,msg_json):
        self.json_obj=msg_json['Os_System_Cmd']
        self.key=list(self.json_obj.keys())[0]
        self.data:dict = {}


    def cmd_execute(self)->dict:
        cmd=self.json_obj[self.key]
        try:
            self.data[self.key] = subprocess.check_output(cmd).decode('utf-8').replace("\n"," ")
            logger.info(f"data is {self.data}")
        except os.error as e:
            self.data[self.key] = "Error cmd not executed"
            logger.error(f"Error cmd not executed {e}")
        except Exception as e:
            logger.error(f"Command not found {e}")
        return self.data

    def command_execute(self, command):
        count = os.cpu_count()
        data = os.system(command)
        return data
