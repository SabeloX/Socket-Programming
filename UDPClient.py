"""
    UDP Client Socket Programming
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
    2nd argument: socekt type -> SOCK_DGRAM = UDP socket
"""
client_socket = socket(AF_INET, SOCK_DGRAM)

""" Message to send through the socket """
message = input('Input lowercase sentences: ')

""" Convert message from string type to byte type """
byte_message = message.encode()

""" 
    sendto attaches the destination address - (server_name, server_port) to the message
    and sends the packet into the process's socket - client_socket
"""
client_socket.sendto(byte_message, (server_name, server_port))

"""
    incomming packet's data (from server) is stored in modified_message
    the packet's source address is stored in server_address
"""
modified_message, server_address = client_socket.recvfrom(2048)

""" Converts the message from byte to string and displays it"""
print(modified_message.decode())

""" Closes the socket and the program terminates """
client_socket.close()