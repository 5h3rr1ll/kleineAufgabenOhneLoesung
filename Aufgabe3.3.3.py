from daten import Hauptstaedte

def spiegeln(dic):
    Bundeslaender = {}
    for key, value in dic.items():
        # print(key)
        # print(value)
        Bundeslaender[value]=key
    print(Bundeslaender)

spiegeln(Hauptstaedte)
