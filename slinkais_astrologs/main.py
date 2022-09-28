import os
import os.path
import random

#Globālie mainīgie=============================
dir = os.getcwd()
path0 = "\slinkais_astrologs\ teikumi.txt"
dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
apgalv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Divd = []   #delete?
sk =[]
#===============================================


#Darbības
path = dir+path0.replace(" ","")

#for later?
'''with open(path, 'r') as f:
    for i, rinda in enumerate(f):
        if i in apgalv:
            Divd.append(rinda.strip())
        elif i > 10:
            break
print(Divd)'''


while len(sk) < 2:
    num = random.randint(1,20)
    if num in sk:
        continue
    else: 
        sk.append(num)

print(sk)