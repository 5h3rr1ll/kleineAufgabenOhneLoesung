def Teiler(n):
    x = range(2, n)
    for i in x:
        if n % i == 0:
            print(i)

Teiler(int(input("Die Teiler welcher Zahl möchtest du wissen? ")))
