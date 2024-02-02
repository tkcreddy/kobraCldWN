import multiprocessing
from logpkg.log_kcld import LogKCld,log_to_file
import subprocess
from utils.os import OsSystemCmd,OsCustomCmd
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
        if msg_json:
            first_key = list(msg_json.keys())[0]
            print(f"key is {first_key}")

            if first_key == "OS_System_Cmd":
                OsSystemCmd(msg_json[first_key])
            elif first_key == "OS_Metrics_Cmd":
                action2(json_data[first_key])
            elif first_key == "OS_Custom_cmd":
                action

            elif first_key == "Container_Cmd":
                action3(json_data[first_key])
            else:
                pass
        else:
            print("Error: Empty JSON data")
        #print(f"command is {msg_json['get_cpu_info']}")
        # command=msg_json['get_cpu_info']
        # command="ls"
        # result=os.cpu_count()
        result = {}
        result['hostname'] = os.uname()
        try:
            # Execute the OS command
            result['cpu_count'] = os.cpu_count()
            result['Total_memory'] = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
            # result = subprocess.run(command, shell=True, check=True, capture_output=True)
            # print('Command executed successfully. Output:', result.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print('Error executing command:', e)
        print(f"Command output is {result}")
        return result