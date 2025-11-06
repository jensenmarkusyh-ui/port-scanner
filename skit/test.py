import socket

max_banner = 15

print("Nätverksskanner v1.1 — enklare banner-probing")
print("=============================================")

target = input("Vilken ip-address/hostname vill du skanna -> \n")
print("Mellan vilka portar vill du skanna")
port1 = int(input("Port1 - "))
port2 = int(input("Port2 - "))

print("\n")
print("Mål:", target)
print(f"Portintervall: {port1} - {port2}")
print("Time out: 1.0 sekund\n")
input("Tryck Enter för att börja scanna...\n")

# enkla protokoll-prober för vanliga portar (kan utökas)
probes = {
    80: b"HEAD / HTTP/1.0\r\n\r\n",
    443: b"HEAD / HTTPS/1.0\r\n\r\n",
}

print("Resultat:")
print("---------")

for port in range(port1, port2 + 1):
   
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)              
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"🟢 Port {port}: Open")
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
             print(f"🔴 Port {port}: Closed")
sock.close()