import math
import random

#Globālie mainīgie
dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
d = 0

with open('teikumi.txt', 'r') as f:
    lines = f.readlines()



def nedelas_horoskopi():
    return



'''for i in dienas:
    print(dienas[d])
    d += 1'''
    

for i in range(100): 
    print((lines[d].strip()))
    d +=1


