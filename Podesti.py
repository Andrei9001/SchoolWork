import math
# 1 podests = 6 fin + 12 parls + 8 sts
# standrata izmēri x=300mm y=200mm z=126mm    | 60000mm^2 * 6 priekš viena standrta = 360000 mm^2 = 0.36m^2
Ssk = 0
d = 0
def trying(x):
    try:
        x = float(x)
    except:
        print("Ievadītā vērtība nav pieļaujama. Mēģiniet vēlreiz")

while True:
    print("pasūtījuma specifika: \n 1. Standarta izmērs \n 2. Pēc pasūtījuma \n 3. Aprēķināt nepieciešamos materiālus atlasei")
    izv = (input("Veicamā darbība (Nr): "))
    trying(izv)
    izv = float(izv)

    if izv <= 3 : #parbauda vai izvele ir korekta
        if izv == 1 : #Standrta uzskaite
            print("Standarta izmēri ir 300mm x 200mm x 126mm")
            print("Ievadiet 0 lai atgrieztos iepriekšējā izvēlnē")
            sk = int(input("Ievadiet skaitu cik taisīt: "))
            if sk == 0: continue
            Ssk += sk * 0.36
            d += sk
        #   pĒc pasūtījuma parametru ievade
        elif izv == 2 :
            #print("Ievadiet 0 jebkurā laukā lai atgrieztos iepriekšējā izvēlnē")
            merv = input("Ievadiet mērvienību - mm, cm vai m: ")
            a = float(input("Ievadiet platumu: "))
            b = float(input("Ievadiet dziļumu:"))
            h = float(input("Ievadiet augstumu:"))
            sk = int(input("Cik šādas kastes taisīt? "))
            #if merv or a or b or h or sk == 0: 
                #print ("Atgriežamies atpakļ bez pieskaites..."); continue
            d += sk

            if merv == "mm": #  Aprēķini
                Ssk += (a * b * math.ceil(h//21) * sk)*0.000001 #Lai iegutu laukumu no mm metros
            elif merv == "cm":
                Ssk += (a * b * math.ceil(h//2.1) * sk)*0.0001 #Lai iegutu laukumu no cm metros
            elif merv == "m":
                Ssk += (a * b * math.ceil(h//0.021) * sk) #Lai iegutu laukumu metros
                
        elif izv == 3 :
            break

    elif izv >= 3 :
        print("Ievadītā vērtība nav pieļaujama. Mēģiniet vēlreiz")
        continue

Ssk = round(Ssk, 3)
msl = d * 12
st = d * 8
print("Dotajai produkcijai vajadzēs {} m^2 ar finieiri \n {} malu stiprinājuma līstes un {} stūra stiprinājumus".format(Ssk, msl, st))