import logging
import time
from logpkg.log_kcld import LogKCld, log_to_file
from kafka.producer import KafkaProducer
import json
from faker import Faker
from utils.ReadConfig import ReadConfig as rc
from utils.singleton import Singleton
fake = Faker()
logger = LogKCld()


def get_faker_data():
    return {"name": fake.name(),
            "address": fake.address(),
            "by": fake.year()}


@log_to_file(logger)
def json_serializer(data):
    """
    :param data: The data to be serialized into a JSON formatted string.
    :return: The JSON formatted string representation of the data.
    """
    return json.dumps(data).encode("utf-8")


class Producer:

    @log_to_file(logger)
    def __init__(self, bootstrapserver, topic,**kwargs)->None:
        """
        Constructor method for initializing the object.

        :param bootstrapserver: The address of the bootstrap server.
        :type bootstrapserver: str
        :param topic: The name of the Kafka topic.
        :type topic: str
        :param kwargs: Additional keyword arguments to be passed to KafkaProducer.
        :type kwargs: dict

        :raises Exception: Exception is raised if an error occurs during initialization.
        """
        self.bootstrap_servers = [bootstrapserver]
        self.topic = topic
        try:
            self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,**kwargs)
        except Exception as err:
            logging.error(f"Exception in {err}")
            raise

    @log_to_file(logger)
    def send(self, data)->any:
        """
        Sends the given data to the Kafka topic.

        :param data: The data to be sent.
        :type data: Any
        """
        try:
            self.producer.send(self.topic,json_serializer(data))
            print(f"sending data {data}")
        except Exception as err:
            logging.error(f"Exception in {err}")
            raise

    @log_to_file(logger)
    def flush(self)->None:
        """
        Flushes the producer.

        :return: None
        """
        try:
            self.producer.flush()
        except Exception as err:
            logging.error(f"Exception in {err}")
            raise


