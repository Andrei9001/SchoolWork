import matplotlib.pyplot as plt
import numpy as np
import random
class Function:
    def __init__(self,color):
        self.color = color
    def linijas(self):
        y_points = np.array(np.random.randint(100, size=(10)))
        y_points2=np.array(np.random.randint(100,size=(10)))
        plt.plot(y_points,'o-')
        plt.plot(y_points2, '+:{}'.format(random.choice(self.color)))
        plt.grid()
        plt.show()

    def grfiks(self):
        for i in range(10):
            coo = []
            for j in range(2):
                coo.append(np.random.randint(1,50))
            set.append(coo)
        likne=np.array(set)
        x,y = likne.T
        plt.plot(x,y,'{}'.format(random.choice(self.color)))
        plt.grid()
        plt.show()

    def kvadratF(self):
        a = int(input('Ievadiet a vērtību: '))
        b = int(input('Ievadiet b vērtību: '))
        c = int(input('Ievadiet c vērtību: '))
        virs = round((-1*b)/(2*a))
        for i in range(virs-20,virs+21):
            x.append(i)
            y.append(a*i**2+b*i+c)
        plt.plot(x,y,'{}'.format(random.choice(self.color)))
        plt.grid()
        plt.show()





#======variables=========
x = []
y = []
set = []
color = ['r','g','k','y','c','m']


graph = Function(color)

graph.grfiks()
graph.linijas()
graph.kvadratF()
#linijas(set)
