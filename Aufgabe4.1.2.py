def RechenHilfe():
    zahl1 = int(input("Gibt eine Zahl ein: "))
    operator = input("Waehle eine Rechenart +, -, * oder /: ")
    zahl2 = int(input("Gib eine zweite Zahl ein: "))
    ergebnis = 0
    if operator == "+":
        ergebnis = zahl1+zahl2
    elif operator == "-":
        ergebnis = zahl1-zahl2
    elif operator == "*":
        ergebnis = zahl1*zahl2
    elif operator == "/":
        ergebnis = zahl1/zahl2
    print("Das ergebnis von {0}{1}{2} lautet {3}".format(zahl1, operator, zahl2,ergebnis))

print(RechenHilfe())
