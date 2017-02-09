from random import randint, choice
#eine Liste der WochenTage
Wochentage = ["Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

def gradzahl(Tage):
    gradzahl = randint(10,20)
    #die Differenz,l die der folge Tag haben darf in einer Liste festhalten
    differenz = [-2, 2]
    print("Am Montag werden es",gradzahl,"°C.")
    for x in Tage:
        #choice, ist ein methode aus der Library random. choice waehlt zufaellig
        #einen Wert aus einer Liste. Als Argument kann also auch NUR eine Liste
        #Liste übergeben werden, in Form einer Liste! z.B. [x,y]
        gradzahl += choice(differenz)
        #hier schummel ich, da die Aufgabe sagt, das der Wert zwischen 10 und 20
        #sein soll. Mit der if-Abfrage stelle ich sicher dass die Temeperatur
        #stets min 10 und höchsten 20 Grad sind.
        # if gradzahl < 10:
        #     gradzahl = 10
        # elif gradzahl > 20:
        #     gradzahl = 20
        print("Am",x,"werden es",gradzahl,"°C.")

gradzahl(Wochentage)
