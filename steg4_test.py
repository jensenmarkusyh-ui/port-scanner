"""
Network Scanner Project
Students: [Oscar, Pontus, Markus, Rajan, Jakub]
Date: [2025-10-20]
"""

import socket
import time

open_ports = []
portname = {
    22: "SSH (OpenSSH 8.2)",
    80: "HTTP (nginx)",
    443: "HTTPS",
}

def render_bar(percent: float, width: int = 10) -> str:
    """Returnerar en grafisk progressbar med 'width' rutor."""
    filled = int(percent / 100 * width)
    empty = width - filled
    return "[" + "█" * filled + "░" * empty + "]"

def print_scan_progress(scanned: int, total: int, open_count: int, width: int = 10):
    """Skriver ut hur stor del av skanningen som är klar och antal öppna portar."""
    percent = (scanned / total) * 100 if total > 0 else 0
    bar = render_bar(percent, width)
    print(f"Skannar... {bar} {int(percent)}% ({open_count} öppna)", end="\r", flush=True)

# --- Programstart ---
print("Nätverksskanner v1.0")
print("====================")

target = input("Vilken IP-adress/hostname vill du skanna -> ")
print("Mellan vilka portar vill du skanna")
port1 = int(input("Port1 - "))
port2 = int(input("Port2 - "))

# Rensa skärmen (gör bara radbrytningar)
print("\n" * 50)
print("Nätverksskanner v1.0")
print("====================")
print("Mål: " + target)
print(f"Portintervall: {port1} - {port2}")
print("Time out: 0,5 sekund\n")
input("Tryck Enter för att börja skanna...\n")
print(f"Skannar\nMål: {target}\n")

print("Resultat:")
print("---------")

# --- Starta tidsmätning ---
start_time = time.time()

total_ports = port2 - port1 + 1
scanned = 0

# Visa initial progress
print_scan_progress(scanned, total_ports, len(open_ports))

# --- Portskanning ---
for port in range(port1, port2 + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    sock.close()

    scanned += 1
    if result == 0:
        name = portname.get(port, "Okänd tjänst")
        open_ports.append((port, name))
        print()  # ny rad så progress inte skrivs över
        print(f"Port {port}: Open - {name}")
    print_scan_progress(scanned, total_ports, len(open_ports))

# --- Stoppa tidsmätning ---
end_time = time.time()
elapsed = end_time - start_time

# --- Slutlig utskrift ---
print("\n\nSkanning klar!")
print(f"Tidsåtgång: {elapsed:.2f} sekunder")

if open_ports:
    print("\nÖppna portar:")
    for port, name in open_ports:
        print(f" - Port {port}: {name}")
else:
    print("\nInga öppna portar hittades.")

# --- Spara resultat i loggfil (append-läge, alla körningar sparas) ---
with open("scan_results.txt", "a", encoding="utf-8") as file:
    file.write("=== Nätverksskanner Logg ===\n")
    file.write(f"Tid: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    file.write(f"Mål: {target}\n")
    file.write(f"Portintervall: {port1}-{port2}\n")
    file.write(f"Totalt portar: {total_ports}\n")
    file.write(f"Tidsåtgång: {elapsed:.2f} sekunder\n")
    file.write(f"Antal öppna portar: {len(open_ports)}\n")
    file.write("=============================\n")

    if open_ports:
        file.write("Öppna portar:\n")
        for port, name in open_ports:
            file.write(f" - Port {port}: {name}\n")
    else:
        file.write("Inga öppna portar hittades.\n")

    file.write("\n")  # tom rad mellan olika körningar

print(f"\nResultatet har sparats i 'scan_results.txt'.")
