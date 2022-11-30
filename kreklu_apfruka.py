cena = 0
apdruka = {
    "Teksts": 5,
    "Zīme" : 7,
    "Foto": 20}
FedEx = False

#==============================
def pasuti_tkreklus(x):
    skaits = float(input("cik?"))
    return skaits*apdruka[x]

#===============================
while True:
    skaits = 0
    print("\nPIEEJAMIE APDRUKAS VEIDI: \n1. teksts \n2. zīme \n3. foto")
    app = input("Izvēlieties apdrukas veidu: ")
    if app == "teksts":
        cena += pasuti_tkreklus("Teksts")
    elif app == "zīme":
        cena += pasuti_tkreklus("Zīme")
    elif app == "foto":
        cena += pasuti_tkreklus("Foto")
    elif app == "exit":
        break

piegade = input("Izvēlieties piegādi\nPIEZĪME: ja piegāde nav nepiciešama atstājiet tukšu: ")
if piegade != "" and cena <= 50: FedEx =True

if FedEx == True: cena += 15
elif cena >= 100: cena = cena-(cena/20)





print(cena)