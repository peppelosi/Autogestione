from ast import Try
import socket
import time
import datetime
import requests

from socket_connection import get_socket
from utils import getConfig
from main_working import get_RFID_list
from configparser import ConfigParser



def main(config: ConfigParser):

    port = int(config['TEST_PARAMETERS']['port'])
    ip_reader = str(config['TEST_PARAMETERS']['list'])
    n_tags = int(config['TEST_PARAMETERS']['n_tags'])
    time_max = int(config['TEST_PARAMETERS']['time_max'])

    while(True):
        print(get_RFID_list(get_socket(ip_reader, port), time_max))
        





if __name__ == '__main__':
    config = getConfig()
    main(config)
