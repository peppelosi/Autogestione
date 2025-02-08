import socket
import requests

from logger import tags_inspector_log as log



def get_socket(ip, port):  # socket creation

    s = None

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))

    except TimeoutError:
        log.error("\n\t\t\t\t\tNo connection")
        x = requests.post('http://www.poggiolevante.net/autogestione/update.php', {'conn': '0'})

    finally:
        return s
