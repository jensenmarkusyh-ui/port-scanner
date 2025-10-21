"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket 

target = "scanme.nmap.org"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((target, port))

if result == 0:
        print("Port " + str(port) + " is open")
else:
        print("Port " + str(port) + " is closed")
sock.close()