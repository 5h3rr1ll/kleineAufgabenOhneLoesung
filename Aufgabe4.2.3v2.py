from random import randint

def CPUraet(n):
    userN = n
    unterG = 1
    oberG = 100
    cpuN = 0
    feedback = ""
    versuche = 0
    cpuN = randint(unterG, oberG)
    differenz = 0
    while cpuN != userN:
        cpuN = cpuN
        feedback = input("{0}? : ".format(cpuN).lower())
        if feedback == "r":
            versuche += 1
            break
        elif feedback == "g":
            oberG = (cpuN-1)
            versuche += 1
            cpuN = (cpuN/2)
        elif feedback == "k":
            unterG = (cpuN+1)
            versuche += 1
            cpuN = (cpuN/2)
    print("Nur {0} Versuche!".format(versuche))

CPUraet(int(input()))
