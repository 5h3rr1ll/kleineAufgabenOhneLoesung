# x = 1000
#
# natZah = 0
#
# liste = []
#
# while sum(liste) < x:
#     liste.append(natZah)
#     natZah += 1
# else:
#     print(len(liste))
#
# print(natZah)
# print(max(liste))
# print(sum(liste))

def minAnz(Grenze):
    summe = 0
    zaehler = 1
    while summe < Grenze:
        summe += zaehler
        zaehler += 1
    return zaehler

print(minAnz(1000))
