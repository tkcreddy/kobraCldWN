import multiprocessing
from logpkg.log_kcld import LogKCld,log_to_file
import subprocess
from utils.os.OsSystemCmd import OsSystemCmd
from utils.os.OsMetricsCmd import OsMetricsCmd
from utils.os.OsCustomCmd import OsCustomCmd
import json
import jsonpickle
import os
import asyncio
logger=LogKCld()

class MsgProcess():
    def __init__(self,msg:json):
        self.msg=msg
    @log_to_file(logger)
    def msg_process(self)->json:
        msg_json=json.loads(self.msg)
        #msg_json=self.msg
        print(f"this is the message from async {msg_json}")
        try:
            result = {}
            if msg_json:
                first_key = list(msg_json.keys())[0]
                print(f"key is {first_key}")

                if first_key == "Os_System_Cmd":
                    print(f"inside the if for validation {msg_json}")
                    os_system_cmd=OsSystemCmd(msg_json)
                    result=os_system_cmd.cmd_execute()

                elif first_key == "OS_Metrics_Cmd":
                    OsMetricsCmd(msg_json[first_key])
                elif first_key == "OS_Custom_cmd":
                    OsMetricsCmd(msg_json[first_key])

                elif first_key == "Container_Cmd":
                    action3(json_data[first_key])
                else:
                    print(f"passing in {__name__}")
                    pass
            else:
                print("Error: Empty JSON data")

            result['hostname'] = os.uname()
            # Execute the OS command
            result['cpu_count'] = os.cpu_count()
            result['Total_memory'] = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")/(1024*1024*1024)
            # result = subprocess.run(command, shell=True, check=True, capture_output=True)
            # print('Command executed successfully. Output:', result.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print('Error executing command:', e)
        except Exception as e:
            print('Error Executing OS cmd:', e)
        print(f"Command output is {result}")
        return result