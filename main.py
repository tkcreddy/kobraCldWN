# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from logpkg.log_kcld import LogKCld,log_to_file
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
    read_config = rc('/Users/krishnareddy/PycharmProjects/kobraCld/config/config.json')
    kafka_config = read_config.kakfa_config
    #print(kafka_config['bootstrap_servers'])
    producer=Producer(kafka_config['bootstrap_servers'],kafka_config['topic'])



if __name__ == '__main__':
    print_hi("Krishna")
