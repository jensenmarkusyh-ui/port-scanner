import random # Den importerar random in i scriptet så att koden kan slumpmässigt välja ett alternativ i listan nedanför
round = True # Vi använder variabeln round och skriver round = true så att while loopen ska fortsätta tills scriptet kommer till round = false

print("Spelet körs 5 omgångar") #Använder print så att man förstår att spelet kör 5 omgångar i taget.
while round:    # While kollar ifall man är i en loop, det vet vi för round = true. 
    for i in range(5):  # For i in range kollar hur många gånger spelet ska köras som i detta fall är (5) gånger.
        player1 = input("Välj sten, sax eller påse:") # player1 input används så spelaren kan välja mellan de alternativen
        player2 = random.choice(["sten", "sax", "påse"])  # Player2/datorn kommer välja något av alternativen i listan [] slumpmässigt, detta fungerar då vi har satt import random högst upp i koden.
        print("Datorn valde:", player2) # Printar vad player2 valde i listan genom att lägga till ", player2" då visas vad datorn valde slumpmässigt.
        if player1 == player2: # if satsen använder jag ifall det blir lika, så ifall player1 == (är samma som) player2. så går den till stycket under som då är Oavgjort
            print("Oavgjort!")
        elif (player1 == "sten" and player2 == "sax") or (player1 == "sax" and player2 == "påse") or (player1 == "påse" and player2 == "sten"): 
            # elif körs ifall if raden inte var sann, de 3 kombinationerna är där player1 kan vinna mot player2. Jag använder 'or' för att skilja de 3 alternativen.
            print("Du vann rundan!") # Ifall något alternativ i elif satsen va sant så printar den "Du vann rundan!"
        else: #Ifall ingen av if & elif va sanna så hoppar den ner till else satsen.
            print("Du förlorade rundan.") # Ifall ingen av de 3 kombinationerna eller oavgjort va sanna så printar det "Du förlorade rundan". Och betyder då att player2 vann rundan
    if input("Spela igen? (j/n): ") != "j": #Efter for i in range(5) har körts så används if satsen och frågar om man vill spela igen. Jag använder != för ifall man skriver något som inte är lika med 'j' så avslutas spelet och hoppar ner till round = false
        round = False #Detta betyder att rundan/spelet slutar.
    
