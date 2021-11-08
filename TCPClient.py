"""
    TCP Client Socket Programming
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
    Create client socket
    1st argument: address family -> AF_INET = IPv4
    2nd argument: socekt type -> SOCK_STREAM = TCP socket
"""
client_socket = socket(AF_INET, SOCK_STREAM)

""" Initiate (establishes) a TCP connection with the server """
client_socket.connect((server_name, server_port))

""" Message to send through the socket """
message = input('Input lowercase sentences: ')

""" Convert message from string type to byte type """
byte_message = message.encode()

""" 
    send sends the message to the TCP connection through the socket
"""
client_socket.send(byte_message)

"""
    incomming packet's data (from server) is stored in modified_message
"""
modified_message = client_socket.recvfrom(1024)

""" Converts the message from byte to string and displays it"""
print(modified_message.decode())

""" Closes the socket and the program terminates """
client_socket.close()