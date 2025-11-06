while True:
    try:
        port1 = int(input("Port1 - "))
        if port1 <= 0:
            print("Ogiltigt, försök igen")
            continue
        break
    except ValueError:
        print("Ogiltigt, försök igen")

while True:
    try:
        port2 = int(input("Port2 - "))
        if port2 <= 0:
            print("Ogiltigt, försök igen")
            continue
        break
    except ValueError:
        print("Ogiltigt, försök igen")

print(f"Du skrev in Port1 = {port1} och Port2 = {port2}")