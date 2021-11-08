"""
    UDP Server Socket Programming
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
server_name = 'hostname'

""" Server Port Number """
server_port = 12000

""" 
    Create server socket
    1st argument: address family -> AF_INET = IPv4
    2nd argument: socekt type -> SOCK_DGRAM = UDP socket
"""
server_socket = socket(AF_INET, SOCK_DGRAM)

""" Assigns the port number to the server socket """
server_socket.bind(('127.0.0.1', server_port))

print('The server is ready to receive')

""" Waits to receive a packet """
while True:
    """ Gets data from the client throught the server socket and the client address """
    message, client_address = server_socket.recvfrom(2048)

    """ Converts message from byte to string and capitalize chatracters """
    modifiedMessage = message.decode().upper()

    """
        Converts message to byte
        Attaches the client address to the message
        Sends to the client - through the server socket
    """
    server_socket.sendto(modifiedMessage.encode(), client_address)
