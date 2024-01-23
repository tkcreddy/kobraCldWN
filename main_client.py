# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import multiprocessing
from utils.kafka.producer_kafka import Producer
from utils.kafka.consumer_kafka import Consumer
from logpkg.log_kcld import LogKCld,log_to_file
import subprocess
from utils.os.OsCommandExecution import OsCommandExecution
import json
import os


stop_event = multiprocessing.Event()
logger=LogKCld()

#logger = setup_logger("my_app", log_file="app.log")
#from utils.kafka.producer_kafka import *
#from utils.kafka.
@log_to_file(logger)
def print_hi(name) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def main():
    from utils.ReadConfig import ReadConfig as rc
    from utils.CommandConfig import CommandConfig as cc
    read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
    kafka_config = read_config.kakfa_config


    consumer = Consumer(kafka_config['bootstrap_servers'], kafka_config['group_id'], kafka_config['topic'])
    #print(system_config_info)
    #producer.send(system_config_info)
    msg_json=''

    consumer.consumer.subscribe(kafka_config['topic'])
    while not stop_event.is_set():
        for msg in consumer.consumer:
            msg_json=json.loads(msg.value.decode('utf-8'))
            print(f"this is the message from async {msg_json}")
            print(f"command is {msg_json['get_cpu_info']}")
            #command=msg_json['get_cpu_info']
            #command="ls"
            #result=os.cpu_count()
            result={}
            result['hostname'] = os.uname()
            try:
                # Execute the OS command
                result['cpu_count']=os.cpu_count()
                result['Total_memory']=os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
                #result = subprocess.run(command, shell=True, check=True, capture_output=True)
                #print('Command executed successfully. Output:', result.stdout.decode('utf-8'))
            except subprocess.CalledProcessError as e:
                print('Error executing command:', e)
            print(f"Command output is {result}")
            if stop_event.is_set():
                break
    consumer.consumer.close()

    producer = Producer(kafka_config['bootstrap_servers'], kafka_config['command_output_topic'])




if __name__ == '__main__':
    main()
