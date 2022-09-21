def trying(x):
    try:
        x = float(x)
    except:
        print("Ievadītā vērtība nav pieļaujama. Mēģiniet vēlreiz")
        



izmaksas = []
summa = 0
# lin    grida   maina

Afton = True
while Afton == True:
    
    #   Linoleja cenas ievade
    lin = input("Seguma cena (EURO)/m^2 uzrakstīta tikai ar cipariem vai ar punktu kā decimāldaļas atdalītāju: ")
    trying(lin)
    
    #   Platības ievade
    grida = input("Ievadiet grīdas platību kvadrātmetros: ")
    trying(grida)

    #   lietotaja parbaude
    print("Jums vajag pārklāt", grida, " m^2 ar", lin, " eiro/m^2 dārgu segumu?")
    maina = input( "ja vai ne? ")
    
    #aprekins un pievienosana sarakstam
    if maina == "ja":
        #Afton = False
        lin = float(lin)
        grida = float(grida)
        cena = lin * grida
        cenas = round(cena, 2)
        izmaksas.append(cenas)
        print("Lai pārklātu doto telpu, segums maksās {} eiro".format(cenas))
        print(izmaksas)
        turp = int(input("Aprēķināt papildus telpām (1) vai summēt izmaksas(2)? "))
        if turp == 1:
            continue
        elif turp == 2:
            break
        

    elif maina == "ne": continue

print("Yayy you made it")
for i in izmaksas:
    summa += i
print("Kopējais grīdas segums izmaksās", summa, "eiro.")
izmaksas.append(summa, Afton)
print(izmaksas)
