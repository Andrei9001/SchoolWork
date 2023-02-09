from datetime import datetime
import csv

class Rekins:
    
    #Izveidos un aprēķinās kastītes vēlamos rēķinus
    def __init__(self,name,text,size,price,sum):
        self.name = name
        self.text = text
        self.size = size
        self.price = price
        self.wage = 15
        self.tax = 21
        self.rekina_summa = sum

    def order(self):
        self.name = str(input("Jūsu vārds: "))
        self.text =  str(input("Ko jūs vēlētos iegravēt: "))
        self.size = input('Kastītes izmērs atdalīts ar komatu milimetros (a*h*b): ').split(',')
        self.price = float(input('kokmateriāla cena EUR/m^2: '))

    def izdrukat(self):
        print(self.name,'\n',self.text,'\n',self.size,'\n',self.price)
        for i in self.rekina_summa:
            print('{}.kaste: {}'.format(self.rekina_summa.index(i)+1,i))
        for i in self.rekina_summa:
            sum =+ i
        print('Rēķins: {}'.format(round(sum,2)))
    
    def aprekins(self):
        produkta_cena = len(self.text)*1.2+(int(self.size[0])/100*int(self.size[1])/100*int(self.size[2])/100)/3*self.price
        pvn_summa = (produkta_cena + self.wage)*self.tax/100
        self.rekina_summa.append((produkta_cena+self.wage)+pvn_summa)

    def cheque(self):
        with open ('cheque.csv','r') as f:
            csv_writer = csv.reader(f)
            for i in csv_writer:
                print(i)
            #if f[0] == :
                #csv_writer("Vārds,Teksts,Platums,Augstums,Dziļums,Kokmateriāla cena,Rēķina summa,Darba izmaksas,PVN")
kas = Rekins("Andrejs","Hi! My name is...","200,200,200",10,[])

kas.aprekins()
kas.cheque()