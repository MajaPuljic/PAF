import numpy as np
import matplotlib.pyplot as plt

def kosi_hitac(v0,theta):

    kut = theta*np.pi/180

    vx = np.cos(kut)*v0
    vy = np.sin(kut)*v0

    x = 0
    y = 0

    dt = 0.01
    a = -9.81

    vx_lista = []
    x_lista = []
    vy_lista = []
    y_lista = []
    t = []

    for i in range(100):
        vx_lista.append(vx)
        x = x + vx*dt
        x_lista.append(x)

        vy = vy + a*dt
        vy_lista.append(vy)
        y = y + vy*dt
        y_lista.append(y)

        t.append(i*dt)

        

    fig, axs = plt.subplots(2, 2)

    axs[0, 0].plot(x_lista, y_lista)
    axs[0, 0].set_title("x-y graf")
    axs[0,0].set_xlabel('$x | [m]$')
    axs[0,0].set_ylabel('$y | [m]$')

    axs[0, 1].plot(t, x_lista)
    axs[0, 1].set_title('x-t graf')
    axs[0,1].set_xlabel('$t | [s]$')
    axs[0,1].set_ylabel('$x | [m]$')

    axs[1, 0].plot(t, y_lista)
    axs[1, 0].set_title('y-t graf')
    axs[1,0].set_xlabel('$t | [s]$')
    axs[1,0].set_ylabel('$y | [m]$')

    plt.title("Kosi hitac")

    plt.show()

kosi_hitac(5,40)

