"""
    TCP Server Socket Programming
    Author:Sabelo Mtetwa
    08 November 2021
"""

""" 
    socket forms basis to all network communications in Python
    Allows us to create sockets within the program
"""
from socket import *

""" 
    Either a string with server IP address (e.g., 128.138.32.126) or
    server hostname (e.g., cis.poly.edu) - an automatic DNS lookup will happen to get the IP address"""
server_name = '127.0.0.1'

""" Server Port Number """
server_port = 12000

""" 
    Create server socket
    1st argument: address family -> AF_INET = IPv4
    2nd argument: socekt type -> SOCK_STREAM = TCP socket
"""
server_socket = socket(AF_INET, SOCK_STREAM)

""" Assigns the port number to the server socket """
server_socket.bind((server_name, server_port))

""" Listens for TCP connection, argument 1 means max of 1 queued connection """
server_socket.listen(1)

print('The server is ready to receive')

""" Waits to receive a packet """
while True:
    """ Creates a new socket in the server when a client is connected """
    connection_socket, address = server_socket.accept()

    """ Gets data from the client throught the server socket """
    message = server_socket.recvfrom(2048)

    """ Converts message from byte to string and capitalize chatracters """
    modifiedMessage = message.decode().upper()

    """
        Converts message to byte
        Sends to the client - through the connection socket
    """
    connection_socket.send(modifiedMessage.encode())

    """ CLose the connection socket for this client """
    connection_socket.close()
