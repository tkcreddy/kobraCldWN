# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import multiprocessing
from utils.kafka.producer_kafka import Producer
from utils.kafka.consumer_kafka import Consumer
from logpkg.log_kcld import LogKCld,log_to_file
from modules.msg_processing.MsgProcessGateway import MsgProcess
import json
from utils.ReadConfig import ReadConfig as rc
import argparse
stop_event = multiprocessing.Event()
logger=LogKCld()


@log_to_file(logger)
def print_hi(name) -> None:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

@log_to_file(logger)
def main():
    parser = argparse.ArgumentParser(description='A Python CLI application')
    parser.add_argument('--configDir', type=str, help='Please specify ConfigDir')
    args = parser.parse_args()
    read_config = rc(args.configDir)
    kafka_config = read_config.kafka_config
    kafka_ssl_info = read_config.kafka_ssl

    try:
        consumer = Consumer(kafka_config['bootstrap_servers'], kafka_config['group_id'], kafka_config['topic'],**kafka_ssl_info)
        msg_json=''
        logger.info(f"successfully connected to consumer")
        consumer.consumer.subscribe(kafka_config['topic'])
        while not stop_event.is_set():
            for msg in consumer.consumer:
                msg_data = json.loads(msg.value.decode('utf-8'))
                logger.info(f"Data is in the consumer {msg_data}")
                process = MsgProcess(json.dumps(msg_data))
                msg_op = process.msg_process()
                # msg_json=json.loads(msg.value.decode('utf-8'))
                logger.info(f"out put to the result {msg_op}")
                if stop_event.is_set():
                    break
    except Exception as e:
        logger.error(f"error in connecting to consumer with error {e}")
        print(f"error in connecting to consumer with error {e}")
        pass

    finally:
        consumer.consumer.close()

    producer = Producer(kafka_config['bootstrap_servers'], kafka_config['command_output_topic'])




if __name__ == '__main__':
    main()
