from random import randint

def ZahlRaten():

    zufallszahlpc = randint(1,20)

    while True:
        userZahl = int(input("Rate welche Zahl zwischen 1 und 20 der PC gewaelt hat! "))

        if userZahl > zufallszahlpc:
            print("Zu gross")
            continue
        elif userZahl < zufallszahlpc:
            print("Zu klein")
        else:
            print("Herzlichen Glückwunsch!")
            break
ZahlRaten()
