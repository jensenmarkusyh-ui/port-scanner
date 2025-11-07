"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-21]
"""

import socket 

target = "scanme.nmap.org" # #Skannar adressen
port1 = 20 # #Söker genom portarna 20-100
port2 = 100

portname = {
    22: "SSH", # Portnamnen som skannas 
    80: "HTTP",
    443: "HTTPS",   
}

print("Skannar " + (target) + "...") # Visar att den skannar portarna

for port in range(port1, port2 + 1): # Looper igenom port 20,21,...
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # skapar en socket för att ansluta till IPV4 med AF_INET, Sock stream socket används för TCP protokoll

    sock.settimeout(0.3)  # Timmeout för skanning av alla portar på 0,3 sekunder

    result = sock.connect_ex((target, port)) # Försöker göra en TCP-anslutning till (target,port) och returnerar en sifferkod i stället för att kasta undantag.
    
    if result == 0:
        name = portname.get(port)
        if name:
            print("Port " + str(port) + ": Open - " + name) # Om resultatet är 0 ör porten öppen
        else:
            print("Port " + str(port) + ": Open") # Om resultatet är 0 ör porten öppen
    else:
        print("Port " + str(port) + ": Closed") # Om resultatet är något annat än 0 så är porten closed