"""
Network Scanner Project
Students: [Oscar, Pontus, Markus ,Rajan, Jakub]
Date: [D2025-10-20]
"""

import socket # Importerar socket biblioteket
import time # Importerar time biblioteket

max_banner = 15 # Variablen väljer hur många tecken en banner kan skriva ut 

print("\033[32mNätverksskanner v1.0\033[0m") # \033[32m   \033[0m gör att texten blir grön visuelt / Röd färg används även nedanför
print("====================")

while True:
    target = input("Vilken IP-adress/hostname vill du skanna: \n").strip() # Användaren skriver in en IP-adress eller hostname som den vill skanna
    if not target: # om användaren inte skriver in något alls så kommer ett felmeddelande
        print("Ange något, försök igen.") 
        continue
    try:
        real_ip = socket.gethostbyname(target) # Försöker att omvandla hostname till en IP-adress
       
        break # om det lyckas bryter loopen
    except socket.gaierror: # Om det inte lyckas få tag på IP-adressen
        print("Felaktig IP-adress eller hostname, försök igen.") # felmeddelande
        
print("Mellan vilka portar vill du skanna")

while True:
    try:
        port1 = int(input("Port1 - "))  # Skanna port från >
        if 1 <= port1 <= 65535: # kollar så att porten är mellan 1-65535
            break
        else: # om inte så kommer detta felmeddelande
            print("Ange ett nummer mellan 1 och 65535.")
    except ValueError:
        print("Ange ett giltigt nummer.")

while True:
    try:
        port2 = int(input("Port2 - "))  # Skanna port till <
        if 1 <= port2 <= 65535: # kollar så att porten är mellan 1-65535
            break # bryter loopen om det är sant
        else: # om inte så kommer detta felmeddelande
            print("Ange ett nummer mellan 1 och 65535.") 
    except ValueError:
        print("Ange ett giltigt nummer.")
        
speed = input("Välj hastighet (snabb / mellan / långsam): ").strip().lower() # Använder väljer hastighet på hur snabbt skannigen ska skanna

if speed == "snabb": # Hastigheten som omvanldas till satta nummer för att koden senare ska förstå 
    timeout = 0.5
elif speed == "mellan": 
    timeout = 1
elif speed == "långsam":
    timeout = 2
else:
    print("\n🔴 Ogiltigt val, standardvärde används (1 sekund). 🔴") # om användare skriver in fel så väljer programet automatiskt standarden som är på 1 sek
    timeout = 1

    time.sleep(3) # denna väntar i 3 sekunder så användaren hinner läsa fel meddelandet innan den går vidare

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Gör ett stort mellanrum så att det blir en fint och enkelt för användaren att läsa och förstå
print("\033[32mNätverksskanner v1.0\033[0m")
print("====================")
print(f"Mål: {target} ({real_ip})") # Hostnamet och IP-adressen som användaren valde innan
print(f"Portintervall: {port1} - {port2}") # portintervallet som använderen valde innan
print(f"Time out: {timeout} sek\n") # vilken hastighet som kommer köras
input("Tryck Enter för att börja scanna...\n") # Enter för att starta scripten
print(f"Skannar port {port1} till {port2}") #Förloppsindikator

probes = { 
    80: b"HEAD / HTTP/1.0\r\n\r\n", # probes är en lista med portarna som ska testas men själva inte skickar ut en egen banner så som exempelvis SSH gör
    443: b"HEAD / HTTP/1.0\r\n\r\n",
}

print("Resultat:") 
print("---------")

for port in range(port1, port2 + 1): # den kör for loopen på varje port mellan port1 till port2 och även själva port2
   
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # denna skapar en TCP socket
        sock.settimeout(timeout)  #Detta är hastigheten vi har satt innan. så vi inte hänger för länge vid en port, ifall den inte svarar        
        result = sock.connect_ex((target, port)) #Den försöker att ansluta till target och den valda porten.
         # om det finns kontakt med porten så retunerar connect_ex = 0 om anslutningen lyckades, annars ett fel meddelande/felnummer

        if result == 0: # så om svaret blir 0 är den lyckad och då är port = Open
            print(f"🟢 Port {port}: \033[32mOpen\033[0m") # = Port X: Open
            payload = probes.get(port, b"\r") # Den hämtar data som ska skickas till tjänsten på den porten
            #.get(port betyder: om det inte finns något probe i vår lista över så används bara standard-payloaden som porten skickar
            try: 
                sock.sendall(payload) # Försöker skicka payloaden genom socketen
            except Exception: # Om något går fel fångar (Exception) upp det
                pass #  Om något går fel gör pass så att scripten bara fortsätter utan att göra något mer

            try:
                banner = sock.recv(4096).decode(errors="ignore").strip() # läser svaren från bannern, 4096 skickar mer data
                if banner: # om den hittar något 
                    if len(banner) > max_banner: # om bannern är väldigt lång
                        banner = banner[:max_banner] # denna kortar ner bannern till 15 tecken för att inte det ska bli så himla rörigt
                    print("  Banner:", banner) # denna skriver ut bannern fast nu bara första 15 teckenen av bannern 
                else:
                    print("  Banner: (ingen mottagen)")  # men om inget svar kom alls kommer detta meddelandet
            except socket.timeout:
                print("  Banner: (timeout — inget svar)") # Om anslutningen tog för lång tid kommer detta meddelandet 
            except Exception:
                print("  Banner: (kunde inte läsa)") # Om något annat fel hände kommer detta meddelandet

        else:
             print(f"🔴 Port {port}: \033[31mClose\033[0m") # alltså om resultatet inte är 0, är alltså porten Closed
sock.close() # Stänger socket-anslutningen