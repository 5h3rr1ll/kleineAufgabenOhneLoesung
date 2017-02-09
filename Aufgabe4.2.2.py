from random import randint

def ZahlRaten():

    zufallszahlpc = randint(1,100)

    while True:
        userZahl = int(input("Rate welche Zahl zwischen 1 und 100 der PC gewaelt hat! "))
        differnz = zufallszahlpc - userZahl
        if differnz > 20:
            print("Viel zu klein")
            continue
        elif differnz < (-20):
            print("Viel zu gross")
            continue
        elif userZahl > zufallszahlpc:
            print("Zu gross")
            continue
        elif userZahl < zufallszahlpc:
            print("Zu klein")
        else:
            print("Herzlichen Glückwunsch!")
            break
ZahlRaten()
