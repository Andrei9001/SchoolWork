import math
import random

#Globālie mainīgie
dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
d = 0
apgalv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Divd = []





def nedelas_horoskopi():
    return



with open('teikumi.txt', "r") as f:
    for i, rinda in enumerate(f):
        if i in apgalv:
            Divd.append(rinda.strip())
        elif i > 10:
            break
print(Divd)



