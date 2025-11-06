"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket 
import time

max_banner = 15

print("\033[32mNätverksskanner v1.0\033[0m")
print("====================")

target = input("Vilken ip-address/hostname vill du skanna -> \n")
print("Mellan vilka portar vill du skanna")
port1 = int(input("Port1 - "))
port2 = int(input("Port2 - "))
speed = input("Välj hastighet (snabb / mellan / långsam): ").strip().lower()

if speed == "snabb":
    timeout = 0.5
elif speed == "mellan":
    timeout = 1
elif speed == "långsam":
    timeout = 2
else:
    print("\n🔴 Ogiltigt val, standardvärde används (1 sekund). 🔴")
    timeout = 1

    time.sleep(3)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("\033[32mNätverksskanner v1.0\033[0m")
print("====================")
print("Mål: " + target)
print(f"Portintervall: {port1} - {port2}")
print(f"Time out: {timeout} sek\n")
input("Tryck Enter för att börja scanna...\n")
print(f"Skannar port {port1} till {port2}")

probes = {
    80: b"HEAD / HTTP/1.0\r\n\r\n",
    443: b"HEAD / HTTPS/1.0\r\n\r\n",
}

print("Resultat:")
print("---------")

for port in range(port1, port2 + 1):
   
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)              
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"🟢 Port {port}: \033[32mOpen\033[0m")
            payload = probes.get(port, b"\r")
            try:
                sock.sendall(payload)
            except Exception:
                pass

            try:
                banner = sock.recv(4096).decode(errors="ignore").strip()
                if banner:
                    if len(banner) > max_banner:
                        banner = banner[:max_banner]
                    print("  Banner:", banner)
                else:
                    print("  Banner: (ingen mottagen)")
            except socket.timeout:
                print("  Banner: (timeout — inget svar)")
            except Exception:
                print("  Banner: (kunde inte läsa)")

        else:
             print(f"🔴 Port {port}: \033[31mClose\033[0m")
sock.close()