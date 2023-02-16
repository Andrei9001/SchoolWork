from datetime import datetime
import csv
import pandas as pd

class Rekins:
    
    #Izveidos un aprēķinās kastītes vēlamos rēķinus
    def __init__(self,name,text,size,price,sum,total):
        self.name = name
        self.text = text
        self.size = size
        self.price = price
        self.wage = 15
        self.tax = 21
        self.rekina_summa = sum
        self.total = total
    def order(self):
        self.name = str(input("Jūsu vārds: "))
        self.text =  str(input("Ko jūs vēlētos iegravēt: "))
        self.size = input('Kastītes izmērs atdalīts ar komatu milimetros (a*h*b): ').split(',')
        self.price = float(input('kokmateriāla cena EUR/m^2: '))

    def izdrukat(self):
        print("{}\nPasūtītājs   {}\nTeksts    {}\nPlatums     {}\nAugstums    {}\nDziļums     {}\nKokmateriāla cena    {} EURO\nDarba izmaksas      {}\nPVN     {}".format(kas.laiks(),self.name,self.text,self.size[0],self.size[1],self.size[2],self.price,self.wage,self.tax))
        for i in self.rekina_summa:
            print('{}.kaste: {}'.format(self.rekina_summa.index(i)+1,round(i,2)))
        print('Rēķins: {}'.format(self.total))
    
    def aprekins(self):
        produkta_cena = len(self.text)*1.2+(int(self.size[0])/100*int(self.size[1])/100*int(self.size[2])/100)/3*self.price
        pvn_summa = (produkta_cena + self.wage)*self.tax/100
        self.rekina_summa.append((produkta_cena+self.wage)+pvn_summa)
        for i in self.rekina_summa:
            self.total =+ i
        self.total = round(self.total,2)

    def laiks(self):
        time = datetime.now()
        return time.strftime("%d.%m.%Y, %H:%M:%S")
    def datums(self):
        time = datetime.now()
        return time.strftime("%d.%m.%Y")

    def cheque(self):
        with open ('cheque.csv','w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(["Vards","Teksts","Platums","Augstums","Dzilums","Kokmateriala cena","Rekina summa","Darba izmaksas","PVN",kas.datums()])
            csv_writer.writerow([self.name,self.text,self.size[0],self.size[1],self.size[2],self.price,self.total,self.wage,self.tax])

kas = Rekins("Andrejs","Hi! My name is...","200,200,200",10,[],0)

kas.aprekins()
kas.cheque()
kas.izdrukat()

#while True:choice = 