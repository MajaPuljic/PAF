import matplotlib.pyplot as plt
import numpy as np
from math import *
import random 

class particle:

    def __init__(self):
        
        self.xlista = []
        self.ylista = []
        self.vx = []
        self.vy = []
        self.T = [0]
        self.g = -9.81

    def set_initial_conditions(self,v0,theta,x0,y0,dt):

        kut = (theta/180)*np.pi
        self.dt = dt
        self.xlista.append(x0)
        self.ylista.append(y0)
        self.vx.append(v0*np.cos(kut))
        self.vy.append(v0*np.sin(kut))

    def reset(self):

        self.__init__()

    def __move(self):

        self.vy.append(self.vy[-1] + self.g*self.dt)
        self.ylista.append(self.ylista[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + 0*self.dt)
        self.xlista.append(self.xlista[-1] + self.vx[-1]*self.dt)
        self.T.append(self.T[-1] + self.dt)

    def range(self):

        while self.ylista[-1] >= 0.:
            self.__move()
            #print(self.ylista[-1])

        D = (self.xlista[-1] - self.xlista[0])

        return D

    def plot_trajectory(self):

        plt.plot(self.xlista,self.ylista)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")

        plt.show()

    def total_time(self):

        while self.ylista[-1] >= 0.:
            self.__move()
            
        return (self.T[-1])
    
    def max_speed(self):

        while self.ylista[-1] >= 0:
            self.__move()
        
        vmax = self.vy[0]
        
        for i in self.vy:

            if abs(i) > vmax:
                vmax = abs(i)

        return (vmax)

    def D_ovisnost (self,v0):
        domet_lista = []
        kut_lista = np.linspace(0,90)
        for i in kut_lista:
            self.reset()
            self.set_initial_conditions(v0,i,0,0,0.01)
            domet_lista.append(self.range())

        plt.plot(kut_lista,domet_lista)
        plt.xlabel("ǩut [°]")
        plt.ylabel("domet [m]")
        plt.show()

    def T_ovisnost(self,v0):
        vrijeme_lista = []
        kut_lista = np.linspace(0,90)
        for i in kut_lista:
            self.reset()
            self.set_initial_conditions(v0,i,0,0,0.01)
            vrijeme_lista.append(self.total_time())

        plt.plot(kut_lista,vrijeme_lista)
        plt.xlabel("ǩut [°]")
        plt.ylabel("vrijeme [s]")
        plt.show()









         



    
            






        





    



    
