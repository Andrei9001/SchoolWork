import matplotlib.pyplot as plt
import numpy as np

def linijas(set):
    y_points= set
    print(y_points)
    y_points2=np.array(np.random.randint(100,size=(10)))

    plt.plot(y_points,'o-')
    plt.plot(y_points2, '+:r')
    plt.show()


set = []
for i in range(10):
    coo = []
    for j in range(2):
        coo.append(np.random.randint(1,50))
    set.append(coo)

#y = ax**2+bx+c




linijas(set)
