"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket 
import sys

open_ports = []
portname = {
    22: "SSH (OpenSSH 8.2)", 
    80: "HTTP (nginx)",
    443: "HTTPS",   
}

print("Nätverksskanner v1.0")
print("====================")

target = input("Vilken ip-address/hostname vill du skanna -> ")
print("Mellan vilka portar vill du skanna")
port1 = int(input("Port1 - "))
port2 = int(input("Port2 - "))

total_ports = port2 - port1 + 1
scanned = 0

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Nätverksskanner v1.0")
print("====================")
print("Mål: " + target)
print(f"Portintervall: {port1} - {port2}")
print("Time out: 0,5 sekund\n")
input("Tryck Enter för att börja scanna...\n")
print(f"Skannar port {port1}/{port2}")
print("Mål: " + target + "\n")

print("Resultat:")
print("---------")
for port in range(port1, port2 + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))

    
    if result == 0:
                name = portname.get(port, "Okänd/tjänst")
                print(f"Port {port}: Open - {name}")
                open_ports.append(port) 

    scanned += 1
    percent = int(scanned / total_ports * 100)
    sys.stdout.write(f"\r {percent}% ")
    sys.stdout.flush()

print("\n\nSkanning färdig.\n")

if open_ports:
    print("Öppnade portar:")
    for p in open_ports:
        print(f"- Port {p}: {portname.get(p, 'Okänd/tjänst')}")
else:
    print("Inga öppna portar hittades.")