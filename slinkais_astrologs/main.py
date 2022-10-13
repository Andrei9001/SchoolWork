import os
import os.path
from queue import Empty
import random
from tkinter import filedialog
from tkinter import *

#Globālie mainīgie=============================
dir = os.getcwd()
zodiaks = ["Mežāzis", "Ūdensvīrs", "Zivis", "Auns", "Vērsis", "Dvīņi", "Vēzis", "Lauva", "Jaunava", "Svari", "Skorpions", "Strēlnieks"]
path0 = "\slinkais_astrologs\ "
path1 = "teikumi.txt"
path2 = "mainframe.txt"
dienas = ["Pirmdiena", "Otrdiena", "Trešdiena", "Ceturtdiena", "Piektdiena", "Sestdiena", "Svētdiena"]
apgalv = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
apg1 = []   #   1. horoskopa teksts
sk =[]
ref = []
diap = [1,50,52,101,103,252]
riki = 0
garums =[0,2]
parbaude =[]
rna = ""
ara = 0

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
            teikums(diap[4], diap[5], ref[2])
def taka():
    tt = "\ "+ str(input("Ievadiet nedēļu: ")) +".txt"
    t = folder_selected + tt.replace(" ","")
    return t
#Darbības========================================

path = dir+path0.replace(" ","")+path1
with open(path, "r") as f:
    lasit = f.readlines()
#   ref=[0,2,4,6,8,10]
for j in range(20): 
    ref.append(len(ref)*2)

#   saglabā mapīti vēlākam
edit = dir+path0.replace(" ","")+path2

with open(edit, "r+")as p:
    zedit = p.readlines()
    if zedit[1] != " ":  #   pārbauda vai ir aizpildita adrese
        folder_selected = zedit[1].replace(" ","")
        t = taka()
        t.replace("\n", "")
    elif zedit[1] == " ":
        root = Tk() #pajautā par mapīti
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        p.write(folder_selected)
        t = taka()

xt = open(t, "w")
tx = open(t, "a")

print(zedit[1])


#   MASTER
for m in zodiaks:
    riki=random.randint(0,1)
    treici=random.choice(garums)
    #print(m)
    if treici == 0:     #   Random garums
        teikums(diap[0], diap[1], ref[2])
        teikums(diap[4], diap[5], ref[3])
    elif treici == 2:
        teikums(diap[0], diap[1], ref[3])
        teikums(diap[4], diap[5], ref[4])
    if riki == 1: teikums(diap[2],diap[3],7+treici)
    for w in apg1:      #   Gramatika
        ara += 1
        #f ara == 1: rna.lower() + ", "
        if ara %2 == 1:
            rna += w.capitalize()
            if ara == len(apg1): rna += "! "
            else: rna += ", "
        elif ara %2 == 0: rna += w + ". "
    dna = rna.replace("\t", " ")
    rdna = dna.replace("\n", "")
    tx.write(m); tx.write("\n"); tx.write(rdna); tx.write("\n\n") # saraksta teksta failā
    #print(rdna,"\n")
    sk.clear()
    apg1.clear()
    rna = ""
    ara = 0

tx.close()

