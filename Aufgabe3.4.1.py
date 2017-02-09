from random import randint

def zaehle(wuerfe):
    """Diese Funktion fragt die haeufigkeit ab, die der Wuerfel geworfen werden soll
    und erzeugt pro wurf eine Zufaellige Zahl zwischen von 1 bis 6. Wurf und Zahl
    werden dann in einem Dictionary abgelegt."""
    wuerfe = range(1,wuerfe+1)
    dic = {}
    zahl = 0

    for x in wuerfe:
        zahl = randint(1,6)
        dic[x] = zahl

    print(dic)

#     print(dic)
#
zaehle(int(input()))
