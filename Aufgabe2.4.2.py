lst = ["Elias", "Julia", "Daniel", "Dominic"]

def sucheD(lst):
    for name in lst:
        if name[0][0] == "D":
            print(name)

sucheD(lst)
