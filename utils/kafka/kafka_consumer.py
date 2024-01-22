import asyncio
from aiokafka import AIOKafkaConsumer
from utils.ReadConfig import ReadConfig as rc
class AsyncKafkaConsumerWithState:
    def __init__(self, bootstrap_servers, group_id, topic):
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.topic = topic
        self.consumer = AIOKafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            auto_offset_reset='earliest',  # You can change this to 'latest' if you want to start from the latest offset
            enable_auto_commit=True,
        )
        self.state = {}

    async def consume_messages(self):
        await self.consumer.start()

        # Consume messages
        try:
            async for msg in self.consumer:
                # Process the received message
                print('Received message: {}'.format(msg.value.decode('utf-8')))

                # Update state (for example, track the last consumed message offset)
                self.state[msg.partition] = msg.offset
        finally:
            await self.consumer.stop()



read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
kafka_config = read_config.kakfa_config
print(kafka_config['bootstrap_servers'])
# Example usage
# bootstrap_servers = 'your_kafka_bootstrap_servers'
# consumer_group_id = 'your_consumer_group_id'
# topic = 'your_kafka_topic'
consumer = AsyncKafkaConsumerWithState(kafka_config['bootstrap_servers'], kafka_config['group_id'], kafka_config['topic'])
asyncio.run(consumer.consume_messages())
print("Consumer state:", consumer.state)

