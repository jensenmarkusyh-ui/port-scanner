"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket 

print("Nätverksskanner v1.0")
print("====================")

target = input("Vilken ip-address/hostname vill du skanna -> \n")
print("Mellan vilka portar vill du skanna")
port1 = int(input("Port1 - "))
port2 = int(input("Port2 - "))

total_ports = port2 - port1 + 1
scanned = 0

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ")
print("Nätverksskanner v1.0")
print("====================")
print("Mål: " + target)
print(f"Portintervall: {port1} - {port2}")
print("Time out: 0.5 sekund\n")
input("Tryck Enter för att börja scanna...\n")
print(f"Skannar port {port1} till {port2}")
print("Mål: " + target + "\n")

print("Resultat:")
print("---------")

for port in range(port1, port2 + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2.0)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"🟢 Port {port}: Open")
            try:
                # Försök läsa vad servern skickar direkt efter connect
                banner = sock.recv(4096).decode(errors="ignore").strip()
                if banner:
                    print("  Banner:", banner)
                else:
                    print("  Banner: (ingen mottagen)")
            except socket.timeout:
                print("  Banner: (timeout — inget svar)")
            except Exception:
                print("  Banner: (kunde inte läsa)")
        else:
            print(f"🔴 Port {port}: Closed")

sock.close()