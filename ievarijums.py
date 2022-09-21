from turtle import Turtle, Screen

#formula ievārijumam
def ievarijums(cena, prop, nauda):
    x = prop*(nauda/cena); y = x+(nauda/cena)
    x = str(round(x, 3)); y = str(round(y, 3))
    print("Nepieciešams {} kg augļu vai ogu priekš {} kg ievārijuma ".format(x,y))
    t = Turtle()
    screen = Screen()
    screen.setup(width=558, height=558)
    screen.bgpic("iev.gif")
    t.write("Nepieciešams {} kg augļu vai ogu priekš {} kg ievārijuma ".format(x,y), font=FONT)


    screen.exitonclick()

#globālie mainīgie
auo = 0
cuk = 0
izv = 0
nauda = 0
ALIGN= "right"
FONT = ("Courier", 5, "bold")

#intervija
print("Cik saldu plānots taisīt? \nĻoti saldu? \nVidēji saldu? \nNepārāk saldu?")
izv = int(input("Atbildi ievadi šeit: ")) +1
nauda = float(input("Ievadiet plānoto budžetu: "))
cuk = float(input("Ievadiet cukura cenu EURO/kg: "))

#lai aprēķinātu ievārījumu
ievarijums(cuk, izv, nauda)

