import numpy as np 
import math
import matplotlib.pyplot as plt

t = np.linspace(0,10,100)
vo = 0
xo = 0

def graf (F,m):
    a = F/m
    v = vo + a*t
    x = xo + v*t + 0.5*a*(t**2)

    fig,axs = plt.subplots(2)
    fig.suptitle ("v t i x t graf")
    grafvt = axs[0].plot(t,v)
    grafxt = axs[1].plot(t,x)
    axs[0].set_xlablel("t/s")
    axs[0].set_ylablel("v/ m/s")
    plt.show()

    return grafvt, grafxt

graf(10,3)



