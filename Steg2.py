"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-21]
"""

import socket # Importerar socket biblioteket

target = "scanme.nmap.org" #Skannar adressen
port1 = 20 
port2 = 100 #Söker genom portarna 20-100
print("Skannar " + (target) + "...") #Skriver ut att skanningen startar

for port in range(port1, port2 + 1):  #Looper igenom port 20,21,...
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #skapar en socket för att ansluta till IPV4 med AF_INET, Sock stream socket används för TCP protokoll

    sock.settimeout(0.3) #timmeout för skanning av alla portar på 0,3 sekunder

    result = sock.connect_ex((target, port)) # Försöker göra en TCP-anslutning till (target,port) och returnerar en sifferkod i stället för att kasta undantag.
    
    if result == 0:
        print("Port " + str(port) + ": Open") #Om resultatet är 0 ör porten öppen
    else:
        print("Port " + str(port) + ": Closed") #Om inte så är porten stängd eller inte tillgänglig.


