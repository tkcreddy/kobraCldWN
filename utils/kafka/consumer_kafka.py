import time
from kafka.consumer import KafkaConsumer
import json
from utils.ReadConfig import ReadConfig as rc


class Consumer():
    def __init__(self, bootstrapserver, topic,group_id):
        self.bootstrap_server = bootstrapserver
        self.topic = topic
        self.group_id = group_id
        self.consumer = KafkaConsumer(self.topic, bootstrap_servers=self.bootstrap_server,auto_offset_reset = 'earliest',group_id=self.group_id)


def main():
    read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
    kafka_config = read_config.kakfa_config
    print(kafka_config['bootstrap_servers'])
    consumer = Consumer(kafka_config['bootstrap_servers'], kafka_config['topic'],kafka_config['group_id'])
    #consumer=KafkaConsumer(kafka_config['topic'],bootstrap_servers=kafka_config['bootstrap_servers'])
    #consumer.subscribe(kafka_config['topic'])
    while True:
        for message in consumer.consumer:
            #message =  value_deserializer=lambda x: json.loads(x.decode('utf-8')
            print(message.value.decode('utf-8'))


if __name__ == "__main__":
    main()
