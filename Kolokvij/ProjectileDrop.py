from math import *
import numpy as np
import matplotlib.pyplot as plt

class ProjectileDrop:

    def __init__(self,h,vx,dt):
        self.dt = dt
        self.T = [0]
        self.h = h
        self.vx = vx
        self.xlista = [0]
        self.ylista = [h]
        self.vx = [vx]
        self.vy = [0]

        print ("Objekt je uspješno stvoren, početna visina aviona je: {} ".format(h),",a početna brzina je: {}".format(vx))

    def change_height(self,novi_h):

        self.__init__(novi_h,self.vx)
    
    def accelerate (self,a = 0):
        self.vx = self.vx + a
        print("Nova brzina je: {}".format(self.vx))

    def __move(self):

        self.vy.append(self.vy[-1] - 9.81*self.dt)
        self.ylista.append(self.ylista[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + 0*self.dt)
        self.xlista.append(self.xlista[-1] + self.vx[-1]*self.dt)
        self.T.append(self.T[-1] + self.dt)

    def ispustanje(self):

        while self.ylista[-1] >= 0.:
            self.__move()

    def x_y (self):

        plt.plot(self.xlista,self.ylista)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")

        plt.show()

    def vy_t (self):

        plt.plot(self.T,self.vy)
        plt.xlabel("vrijeme [s]")
        plt.ylabel("vy (m/s)")
        plt.show()

    def total_time(self):

        while self.ylista[-1] >= 0.:
            self.__move()
            
        return (self.T[-1])

    def ovisnost_T_dt(self):
        dt_graf = np.repeat(0.001,0.1,100)
        T_graf = [0]
        for i in dt_graf:
            T_graf.append(T_graf[-1] + i)
        plt.plot(dt_graf,self.T)
        plt.xlabel("dt")
        plt.ylabel("T")




        














    
