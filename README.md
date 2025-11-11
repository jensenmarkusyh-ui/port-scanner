# Network Scanner

## Group Members
- Oscar 
- Markus 
- Pontus 
- Rajan 
- Jakub 


## Description

Söker efter portar på en ip-adress, den visar om portarna är öppna eller stängda samt visar bannern på portarna. Den sätter även en timeout beroende på hastighetsval. Skriver ut resultat med färgkoder och emojis.  


## Usage
Python network_scanner.py
Kör scriptet i terminalen(> py .\network scanner.py)
Välj ip-address/hostname som du vill och har lov att skanna t.ex (scanme.nmap.org)
Tryck enter för att välja sitt portintervall
Port 1 = Från första porten t.ex 1
Port 2 = Till sista porten t.ex 80
Välj sedan hastighet - Snabb, Mellan, Långsam
Tryck Enter för att börja skanna!



## Features
- Söka portar på en egen vlad ip-adress/hostname.
- Ändra hastighet på sökningar (Snabb, Mellan, långsamt)
- Färgad utdata, printar ut data i olika färger för att lättare visualisera.


## Testing


Vi började med att testa scanna port 1-80 på sidan scanme.nmap.org för att se om vi kunde scanna ip-adressen samt portarna, vilket vi kunde göra och fick svar om portarna var öppna eller stängda. 
Nästa test vi gjorde var att testa scanna en icke giltig adress som t.ex 111.111.111.111 så visar den att alla portar  är stängda vilket inte är korrekt för att man bör inte kunna scanna en icke giltig ip-adress. 

Vi testade att scanna portar på scanme.nmap.org med olika hastigheter vilket fungerade som det skulle.

### Testchecklista:

[ ] Testa på scanme.nmap.org\
När vi kör scanme.nmap.org på portarna 20 till 80 så visar den att port 22 & 80 är öppna. Port 22 är SSH och Port 80 är HTTP. Det blir även samma resultat när man skriver in IP-adressen till scanme.nmap.org.
(45.33.32.156)

[ ] Testa med giltiga och ogiltiga IP-adresser\
När man skriver en giltig IP-adress så skannar den igenom portarna som man har givit. Skriver man en felaktig IP-adress så kommer den be användaren skriva in en ny ip address

[ ] Testa med ogiltiga portintervall\
När man skriver en ogiltig port så kommer det felmeddelande som säger att man måste använda ett tal mellan 1-65535 och så får användaren skriva in en gång till. 

[ ] Testa felhantering (vad händer om internet är frånkopplat?)\
Nätverk skanningen fungerar inte om man inte är uppkopplad till nätverket.

[ ] Testa med olika timeout-värden\
Vi har 3 olika timeout alternativ. Snabb, mellan och långsam. Om man skriver in ett felt värde så kommer det upp ett felmeddelande och skanningen körs inte.



## Known Limitations
- Nätverk skanningen fungerar inte om man inte är uppkopplad till nätverket. 
- När man skriver att första porten i portintervallen är större än den andra craschar scripten 
- Om man skriver in en ip address med som inte leder någon stans men ändå är uppbyggd på rätt sätt, t.ex 189.192.1.1 så kommer scripten köras men visa att alla portar är stängda 
 



## What We Learned
Vi har förbättrat våra kunskaper att jobba som en grupp genom bra samt tydlig kommunikation, utdelade arbetsuppgifter och allmän grund förståelse av Python. Men även hur en port scanner fungerar



