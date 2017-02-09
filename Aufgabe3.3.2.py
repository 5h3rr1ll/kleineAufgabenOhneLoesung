from daten import Hauptstaedte

def Stadtstaaten(daten):
    lst = []
    #items() greift auf die einzlenen Schluessel und Werte zu und gibt diese wider.

    for key, value in daten.items():
        if key == value:
            #print("JA!")
            lst.append(key)
    print(lst)
    return lst
Stadtstaaten(Hauptstaedte)
