from random import randint

def zaehle(wuerfe):
    """Diese Funktion fragt die haeufigkeit ab, die der Wuerfel geworfen werden soll
    und erzeugt pro wurf eine Zufaellige Zahl zwischen von 1 bis 6. Wurf und Zahl
    werden dann in einem Dictionary abgelegt."""
    #in der Variable wuerfe wird festgehalten wie oft gewuerfelt werden soll.Da
    #da das obere Ende der Range stets minus 1 ist, also eine Range von 1-10 nur
    #1,2,3,4,5,6,7,8,9 abbildert, wurde die Variable mit +1 ergänzt.
    wuerfe = range(1,wuerfe+1)
    #hier wird ein leeres Dictionary erstellt.
    dic = {}
    #dies ist die Variable für die Zahl, die bei jedem Wurf zufaellig erzeugt wird
    zahl = 0
    #Eine Schleife, die sich so haeufig wiederholt, wie gewuerfelt werden soll
    for x in wuerfe:
        #randint steht für RandomInteger (Zufaellige Zahl).randint ist kein Attribut
        # oder aehnliches,sondern Teil des Moduls random. In der Klammer hinter
        #randint wird festgelegt in welchem Bereich die Zufaellige Zahl erzeugt
        #werden soll, wobei zu beachten ist, dass hier die 6 inkludiert ist.
        #also sind folgende Zahlen moeglioch 1,2,3,4,5 und 6!
        zahl = randint(1,6)
        #hier wird das leere Dictionary mit der WurfZahl und der dazugehörigen
        #zufaelligen Zahl ergaenzt
        dic[x] = zahl
    #Am Ende wird das Dictionary gedruckt
    print(dic)

zaehle(int(input()))
