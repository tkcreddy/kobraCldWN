import time
from kafka.producer import KafkaProducer
from kafka.consumer import KafkaConsumer
import json
from faker import Faker
from utils.ReadConfig import ReadConfig as rc
fake=Faker()

def get_faker_data():
    return { "name": fake.name(),
             "address": fake.address(),
             "by":fake.year()}

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

class Producer:
    def __init__(self,bootstrapserver,topic):
        self.bootstrap_servers=[bootstrapserver]
        #KafkaProducer()
        self.topic=topic
        print(bootstrapserver)
        self.producer=KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def send(self,data):
        self.producer.send(self.topic,data)

    def flush(self):
        self.producer.flush()

def main():

    read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
    kafka_config = read_config.kakfa_config
    print(kafka_config['bootstrap_servers'])
    producer=Producer(kafka_config['bootstrap_servers'],kafka_config['topic'])
    while True:
        data = get_faker_data()
        print(data)
        producer.send(json_serializer(data))
        producer.flush()
        time.sleep(3)





if __name__ == "__main__":
    main()
