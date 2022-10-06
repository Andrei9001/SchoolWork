cena = 0
apdruka = {
    "Teksts": 5,
    "Zīme" : 7,
    "Foto": 20}
FedEx = False

#==============================
def pasuti_tkreklus(x):
    skaits = float(input("cik? "))
    return skaits*apdruka[x]

#===============================
while True:
    skaits = 0
    print("\nPIEEJAMIE APDRUKAS VEIDI: \n1. teksts(5$) \n2. zīme(7$) \n3. foto(20$)")
    app = input("Izvēlieties apdrukas veidu: ")
    if app == "exit":
        break
    app = app.capitalize()
    cena += pasuti_tkreklus(app)
    
piegade = input("Izvēlieties piegādi\nPIEZĪME: ja piegāde nav nepiciešama atstājiet tukšu: ")
if piegade != "" and cena <= 50: FedEx =True

if FedEx == True: cena += 15
elif cena >= 100: cena = cena-(cena/20)





print(cena)