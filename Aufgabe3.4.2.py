from turtle import *
from random import randint

def crazyTurtle(anzahl):
    for x in range(1,anzahl):
        laenge = randint(10,100)
        winkel = randint(10, 170)
        forward(laenge)
        right(winkel)
    done()

crazyTurtle(randint(10,40))
