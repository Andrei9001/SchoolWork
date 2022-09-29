import os
import os.path
import random

#Globālie mainīgie=============================
dir = os.getcwd()
zodiaks = ["Mežāzis", "Ūdensvīrs", "Zivis", "Auns", "Vērsis", "Dvīņi", "Vēzis", "Lauva", "Jaunava", "Svari", "Skorpions", "Strēlnieks"]
path0 = "\slinkais_astrologs\ teikumi.txt"
dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
apgalv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
apg1 = []   #   1. horoskopa teksts
sk =[]
ref = []
diap = [1,20,22,41,44,63]
riki = 0
garums =[0,2]
parbaude =[] #  temp
#Funkcijas======================================
def teikums(x, y, z):
    while len(sk) < z:  #nejausi izvelas liniju
        num = random.randint(x,y)
        if num in parbaude:   #parbauda
            continue
        else: 
            parbaude.append(num)
            sk.append(num)  #pievieno izlieototo sarakstam
            apg1.append(lasit[num])
            teikums(diap[2], diap[3], ref[2])
    
    

#Darbības========================================
path = dir+path0.replace(" ","")
with open(path, "r") as f:
    lasit = f.readlines()


#for later?
'''with open(path, 'r') as f:
    for i, rinda in enumerate(f):
        if i in apgalv:
            Divd.append(rinda.strip())
        elif i > 10:
            break
print(Divd)'''

for j in range(20):
    ref.append(len(ref)*2)
#   ref=[0,2,4,6,8,10]




    

for m in zodiaks:
    riki=random.randint(0,1)
    treici=random.choice(garums)
    print(m)
    if treici == 0:
        teikums(diap[0], diap[1], ref[2])
        teikums(diap[2], diap[3], ref[3])
    elif treici == 2:
        teikums(diap[0], diap[1], ref[3])
        teikums(diap[2], diap[3], ref[4])
    if riki == 1: teikums(diap[4],diap[5],7+treici)
    print(apg1,"\n")
    sk.clear()
    apg1.clear()
    print(parbaude)