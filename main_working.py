import socket
import time
import datetime
import requests

from configparser import ConfigParser
from webbrowser import open_new
from utils import getConfig
from logger import tags_inspector_log as log
from socket_connection import get_socket
from checker import count_tag



def get_RFID_list(s, time_max):

    tag_list = ''
    s.settimeout(60*time_max)

    try:
        tag_list = s.recv(1024).decode()  # reading list

    except ConnectionError:
        log.error('Connection failed!')

    finally:
        s.close()
        return tag_list




def get_tag_info(n_tags):

    all_times = []
    presence = []

    first_asctime = str(time.asctime())

    for j in range(n_tags):
        all_times.append(first_asctime)
        presence.append(False)

    return [presence, all_times]
        


def get_tag(ip, port, time_max):

    s = get_socket(ip, port)

    if s != None:
        Rfid = get_RFID_list(s, time_max)
        
        if len(Rfid) != 12:
            log.error('\n\t\t\t\t\tMisuration :\t' + str(Rfid))
            tag = -1
                    
        else:
            x = requests.post('http://www.poggiolevante.net/autogestione/update.php', {'conn': '1'})
            tag = Rfid[7:9]
            log.info('\n\t\t\t\t\tMisuration :\t' + str(tag))
            
        
    return int(tag)



def main(config: ConfigParser):

    port = int(config['SOCKET']['port'])
    ip_reader = str(config['AERIALS']['list'])
    n_tags = int(config['RUN_PARAMETERS']['n_tags'])
    time_max = int(config['RUN_PARAMETERS']['time_max'])
    x = requests.post('http://www.poggiolevante.net/autogestione/update.php', {'start': '1'})

    [presence, all_times] = get_tag_info(n_tags)

    log.info('Prova di misurazione\n')

    while(True):
        tag = get_tag(ip_reader, port, time_max)
        [presence, all_times] = count_tag(tag, str(time.asctime()), all_times, presence, time_max)



if __name__ == '__main__':
    config = getConfig()
    main(config)
