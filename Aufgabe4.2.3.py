from random import randint

def CPUraet(n):
    userN = n
    unterG = 1
    oberG = 100
    cpuN = 0
    feedback = ""
    versuche = 0
    while cpuN != userN:
        cpuN = randint(unterG, oberG)
        feedback = input("{0}? : ".format(cpuN).lower())
        if feedback == "r":
            versuche += 1
            break
        elif feedback == "g":
            oberG = (cpuN-1)
            versuche += 1
        elif feedback == "k":
            unterG = (cpuN+1)
            versuche += 1
    print("Nur {0} Versuche!".format(versuche))

CPUraet(int(input()))
