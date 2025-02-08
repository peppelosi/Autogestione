from asyncio.windows_events import NULL
import socket
import time


from configparser import ConfigParser
from webbrowser import open_new
from logger import tags_inspector_log as log
from utils import getConfig



def get_socket(ip, port):  # socket creation

    s = NULL

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

    except TimeoutError:

        log.error("\n\t\t\t\t\tNo connection")

    finally:

        return s



def get_RFID_list(s):

    tag_list = ''
    message = '[0A0000]'  # request data from reader

    try:
        s.send(message.encode())
        tag_list = s.recv(1024).decode()  # reading list

        message = '[9A0000]'  # stack data erase
        s.send(message.encode())

    except ConnectionError:

        log.error('Connection failed!')

    finally:

        s.close()
        tag_list = tag_list.replace("]", "] ").split(
            " ")  # string manipulation

        # string manipulation: last tag_list element is an empty element
        return tag_list[:len(tag_list)-1]



def order_list(RFID_list):

    i=0
    Tags = ["","","","",""]
    Tags_2 = Tags

    for tag in RFID_list:
        Tags[i] = tag[len(tag)-5:len(tag)-3]

        try:

            Tags_2[i] = int(Tags[i])

        except ValueError:

            log.error("Value error")
            print("Value error")
            return Tags
        
        finally:

            i+=1

    Tags = ["","","","",""]

    for i in range(len(RFID_list)):
        Tags[Tags_2[i]-1] = Tags_2[i]
    
    return Tags


def list_in_file(list_file, f):
    
    f.write(str(time.asctime()))
    for el in list_file:
        f.write("\t"+str(el))
    f.write("\n")
    

def check(ip, port):
    
    i = 1
    tot_errors = 0
    error = False
    round_time = int(config['RUN_PARAMETERS']['round_time'])
    sleep_time = int(config['RUN_PARAMETERS']['sleep_time'])

    f = open("file_indagine.txt", "a")
    f.write("\n\n\tStart. Time: " + str(sleep_time) + "\n")
    

    print('Reading tags: ')
    log.info('Prova di misurazione\n')
    while(i <= round_time):

        s = get_socket(ip, port)
        if s != NULL:
            Rfid = get_RFID_list(s)

            
            if len(Rfid) != 0:

                # control of all elements, expect summary element
                for tag in Rfid[:len(Rfid)-1]:
                    if len(tag) != 12:
                        error = True
                
                # control for incorrect rilevation in the summary element
                if ']' not in Rfid[len(Rfid)-1] or len(Rfid[len(Rfid)-1]) != 6:
                    error = True
                    list_in_file(order_list(Rfid[:len(Rfid)]), f)
                else:
                    log.info('\n\t\t\t\t\tMisuration ' + str(i) + ':\t' + str(Rfid))
                    list_in_file(order_list(Rfid[:len(Rfid)-1]), f)
            else:

                log.error('empty read')
                error = True

            if(error):

                log.error('\n\t\t\t\t\tMisuration ' + str(i) + ':\t' + str(Rfid))
                tot_errors += 1
            

        i += 1
        time.sleep(sleep_time)
        error = False

    log.info('\n\t\t\t\t\tMisurazione terminata. Errors: ' + str(tot_errors) + '\n\n\n\n')
    f.close()



def main(config: ConfigParser):

    port = int(config['SOCKET']['port'])
    ip_reader = str(config['AERIALS']['list'])
    check(ip_reader, port)



if __name__ == '__main__':
    config = getConfig()
    main(config)
