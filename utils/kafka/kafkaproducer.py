from kafka import KafkaProducer
from utils.singleton import Singleton


class Producer(metaclass=Singleton):

    __connection = None

    def __init__(self):
        self.__connection = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                          value_serializer=lambda x: x.encode('utf-8'))

    def produce_business(self, data):
        self.__connection.send('raw-business', value=data)