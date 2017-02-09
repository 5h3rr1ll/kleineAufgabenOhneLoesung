#ImportError: No module named "daten"
# from daten import A, B
#
# a = 3
# b = 5

from random import randint

a = randint(0,10)
b = randint(0,10)

if a > b:
    print("A hat den Wert %d und ist die groessere Zahl." % a)
elif a == b:
    print("Beide Zahlen sind gleich gross.")
else:
    print("B hat den Wert %d und ist die groessere Zahl." % b)
