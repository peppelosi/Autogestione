import socket

from configparser import ConfigParser

from utils import getConfig


def runServer(config: ConfigParser):
    """
    Main function

    Parameters:
      config (ConfigParser): Description of arg1
    """
    # mocked data to send
    data_to_send = "[7400000201][7300000001][7400000101][0301]"

    # Define IP address and port number
    ipAddress = config['TEST_SERVER']['ip_address']
    portNumber = int(config['TEST_SERVER']['port_number'])

    # Create a UDP socket
    udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the UDP socket to the IP address and the port number
    udpSvr.bind((ipAddress, portNumber))

    # Receive datagrams from clients forever
    bufferSize = int(config['TEST_SERVER']['buffer_size'])

    # Receive incoming datagrams
    while(True):
        udpClientData = udpSvr.recvfrom(bufferSize)

        # Datagram from client
        datagramFromClient = udpClientData[0]

        # Datagram from server
        datagramSourceAddress = udpClientData[1]

        # print data received from the client
        print(udpClientData)

        # send data to the client
        udpSvr.sendto(data_to_send.encode(), datagramSourceAddress)

if __name__ == '__main__':
    config = getConfig()
    runServer(config)
