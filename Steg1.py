"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket  # Importerar socket biblioteket

target = "scanme.nmap.org" # skannar adressen
port = 80 # skannar port 80 (HTTP)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # skapar en socket för att ansluta till IPV4 med AF_INET, Sock stream socket används för TCP protokoll
result = sock.connect_ex((target, port))

if result == 0:
        print("Port " + str(port) + ": Open") # Om resultatet är 0 är porten öppen
else:
        print("Port " + str(port) + ": Closed") # om inte så är porten stängd eller inte tillgänglig.
sock.close() # stänger socket.


