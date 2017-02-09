def Anzahl_Vokale(w):
    w = w.lower()
    zaehler = 0
    for b in w:
        if b == "a" or b == "e" or b == "i" or b == "o" or b == "u" or b == "ö" or b == "ä" or b == "ü":
            zaehler += 1
    return zaehler

print(Anzahl_Vokale("immer"))

def Viele_Vokale(lst, n):
    for w in lst:
        Anzahl_Vokale(w)
        if Anzahl_Vokale(w) >= n:
            print(w)

WortListe = ["schreibe", "dann", "eine", "funktion", "viele_vokale","die","zwei", "parameter", "hat"]

Viele_Vokale(WortListe, 3)
