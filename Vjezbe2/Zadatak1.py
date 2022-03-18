import numpy as np 
import math
import matplotlib.pyplot as plt

t = np.linspace(0,10,100)
dt = 0.01 


def jednoliko_gibanje (F,m):
    a = F/m
    v = 0
    x = 0
    
    v_lista = []
    x_lista = []

    for i in range(100):
        v = v + a*dt
        x = x + v*dt 

        v_lista.append(v)
        x_lista.append(x)


    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(t, x_lista)
    axs[0, 0].set_title("x-t graf")
    axs[0,0].set_xlabel('$t | [s]$')
    axs[0,0].set_ylabel('$x | [m]$')

    axs[0, 1].plot(t, v_lista)
    axs[0, 1].set_title('v-t graf')
    axs[0,1].set_xlabel('$t | [s]$')
    axs[0,1].set_ylabel('$v | [m/s]$')

    axs[1, 0].plot(t, np.repeat(a,100))
    axs[1, 0].set_title('a-t graf')
    axs[1,0].set_xlabel('$t | [s]$')
    axs[1,0].set_ylabel('$a | [m/s^2]$')

    plt.show()

jednoliko_gibanje(10,3)



