"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket 

target = "scanme.nmap.org"
port1 = 20
port2 = 100

print("Nätverksskanner v1.0")
print("====================")
print("Mål: " + target)
print("Portintervall:" + (port1) + (port2))

print("Skannar " + (target) + "...")

for port in range(port1, port2 + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))
    
    if result == 0:
        print("Port " + str(port) + ": Open")
    else:
        print("Port " + str(port) + ": Closed")