import matplotlib.pyplot as plt
import numpy as np
from math import *

class HarmonicOscilator:

    def __init__(self):

        self.t = []
        self.x = []
        self.v = []
        self.a = []

    def set_initial_conditions(self,m,k,dt,v0,x0):

        self.dt = dt
        self.m = m
        self.k = k
        self.t.append(0)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(-(self.k/self.m)*x0)
        

    def reset(self):

        self.__init__()

    def __move(self):

        self.t.append(self.t[-1] + self.dt)
        self.a.append((-self.k/self.m)*self.x[-1])
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.x.append(self.x[-1] + self.v[-1]*self.dt)

    def oscillate(self,t_uk):
        
        while self.t[-1]< t_uk:
            self.__move()


    def plot(self):
    
        fig, axs = plt.subplots(2, 2)

        axs[0, 0].plot(self.t,self.x,)
        axs[0, 0].set_title("x-t graf")
        axs[0,0].set_xlabel('$t | [s]$')
        axs[0,0].set_ylabel('$x | [m]$')

        axs[0, 1].plot(self.t,self.v)
        axs[0, 1].set_title('v-t graf')
        axs[0,1].set_xlabel('$t | [s]$')
        axs[0,1].set_ylabel('$v | [m/s]$')

        axs[1, 0].plot(self.t,self.a)
        axs[1, 0].set_title('a-t graf')
        axs[1,0].set_xlabel('$t | [s]$')
        axs[1,0].set_ylabel('$a | [m / s2]$')

        plt.show()

    def liste(self):
         return self.x,self.t

    def period(self):
        period = 0
        for i in range(1,len(self.x)):
            if self.x[i] >= self.x[0]:
                break

            period += self.dt
        
        return period

    def period_analiticki(self):
        period = 2 * np.pi * sqrt(self.m / self.k)

        return period








    


        


