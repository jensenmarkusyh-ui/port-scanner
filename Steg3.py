"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-21]
"""

import socket 

target = "scanme.nmap.org"
port1 = 20
port2 = 100

portname = {
    22: "SSH", 
    80: "HTTP",
    443: "HTTPS",   
}

print("Skannar " + (target) + "...")

for port in range(port1, port2 + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))
    
    if result == 0:
        name = portname.get(port)
        if name:
            print("Port " + str(port) + ": Open - " + name)
        else:
            print("Port " + str(port) + ": Open")
    else:
        print("Port " + str(port) + ": Closed")