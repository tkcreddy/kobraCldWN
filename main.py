# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
from utils.kafka.producer_kafka import Producer
#from utils.kafka.consumer_kafka import AsyncKafkaConsumer
from logpkg.log_kcld import LogKCld,log_to_file
logger=LogKCld()
#logger = setup_logger("my_app", log_file="app.log")
#from utils.kafka.producer_kafka import *
#from utils.kafka.
@log_to_file(logger)
def print_hi(name) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


async def main():
    from utils.ReadConfig import ReadConfig as rc
    from utils.CommandConfig import CommandConfig as cc
    read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
    kafka_config = read_config.kakfa_config
    command_config=cc('/Users/krishnareddy/PycharmProjects/kobraCld/config/commands.json')
    system_config_info=command_config.system_config_info
    #print(kafka_config['bootstrap_servers'])

    # This is producer from server side sending  the  client to run a  command and return the results
    #Producer sends to Host_topic(topic) for now
    producer=Producer(kafka_config['bootstrap_servers'],kafka_config['topic'])

    # This is consumer that  receives the command output from the client.
    #consumer = AsyncKafkaConsumer(kafka_config['bootstrap_servers'], kafka_config['group_id'], kafka_config['command_output_topic'])
    #print(system_config_info)
    producer.send(system_config_info)
    #await consumer.consume_messages()






if __name__ == '__main__':
    print_hi("Krishna")
    asyncio.run(main())
