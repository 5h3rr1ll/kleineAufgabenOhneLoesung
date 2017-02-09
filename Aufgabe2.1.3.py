x = int(input("Wie viele Hunde hast du? "))
# if x > 0:
#     print("Wir haben {0} Hunde".format(x))
# else:
#     print("Wir haben keinen Hund")

hund = "Hund"
hunde = "Hunde"

if x == 1:
    x = "einen"
    print("Wir haben {0} Hund.".format(x))
elif x == 2:
    x = "zwei"
    print("Wir haben {0} Hunde.".format(x))
elif x == 3:
    x = "drei"
    print("Wir haben {0} {1}.".format(x, hunde))
else:
    print("Wir haben keinen Hund.")
