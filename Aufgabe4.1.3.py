from daten import BundeslaenderLst, BundesLandHauptstadt
from random import choice, randint

def RateSpiel():
    anzListeneintreage = len(BundesLandHauptstadt)

    while True:
        zufallsnummer = randint(1,anzListeneintreage-1)
        bundesland = list(BundesLandHauptstadt)[zufallsnummer]
        antwort = input("Wie heisst die Hauptstadt von {0}? ".format(bundesland))
        if antwort == "Ende":
            print("Auf Wiedersehen")
            break
        elif antwort == BundesLandHauptstadt[bundesland]:
            print("Richtig! Wenn Du keine Lust mehr hast, gib einfach das Wort Ende als Antwort ansonsten geht es mit Enter weiter. ")
            continue
        elif antwort != BundesLandHauptstadt[bundesland]:
            print("Das war leider flasch. Versuch es doch nochmal.")
            continue

RateSpiel()
