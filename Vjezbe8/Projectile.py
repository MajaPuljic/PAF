from math import *
import numpy as np
import matplotlib.pyplot as plt

class Projectile:

    def __init__(self):
        
        self.xlista = []
        self.ylista = []
        self.tlista = [0]
        self.vx = []
        self.vy = []
        self.g = -9.81

        self.ax = []
        self.ay = []

    def set_initial_conditions(self,v0,theta,x0,y0,m,rho,Cd,A,dt = 0.01):

        kut = (theta/180)*np.pi
        self.dt = dt
        self.xlista.append(x0)
        self.ylista.append(y0)
        self.vx.append(v0*np.cos(kut))
        self.vy.append(v0*np.sin(kut))
        self.m = m
        self.rho = rho
        self.Cd = Cd
        self.A = A

    def reset(self):

        self.__init__()

    def axRK(self,v):

        return -np.sign(v)*(self.rho*self.Cd*self.A)/(2*self.m) * v**2

    def ayRK(self,v):

        return self.g -np.sign(v)*(self.rho*self.Cd*self.A)/(2*self.m)*v**2

    def __move(self):
        self.ax.append(-np.sign(self.vx[-1])*(self.rho*self.Cd*self.A)/(2*self.m) * self.vx[-1]**2)
        self.ay.append(self.g-np.sign(self.vy[-1])*(self.rho*self.Cd*self.A)/(2*self.m)*(self.vy[-1])**2)
        self.vy.append(self.vy[-1] + self.ay[-1]*self.dt)
        self.ylista.append(self.ylista[-1] + self.vy[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.ax[-1]*self.dt)
        self.xlista.append(self.xlista[-1] + self.vx[0]*self.dt)
        self.tlista.append(self.tlista[-1] + self.dt)


    def __moveRK (self):

        k1vx = self.axRK (self.vx[-1])* self.dt
        k1x = self.vx[-1] * self.dt
        k2vx = self.axRK(self.vx[-1] + k1vx/2) * self.dt
        k2x = (self.vx[-1] + (k1vx/2)) * self.dt
        k3vx = self.axRK(self.vx[-1] + k2vx/2) * self.dt
        k3x = (self.vx[-1] + (k2vx/2)) * self.dt
        k4vx = self.axRK(self.vx[-1] + k3vx) * self.dt
        k4x = (self.vx[-1] + k3vx) * self.dt

        k1vy = self.ayRK(self.vy[-1]) * self.dt
        k1y = self.vy[-1] * self.dt
        k2vy = self.ayRK(self.vy[-1] + k1vy/2) * self.dt
        k2y = (self.vy[-1] + (k1vy/2)) * self.dt
        k3vy = self.ayRK(self.vy[-1] + k2vy/2) * self.dt
        k3y = (self.vy[-1] + (k2vy/2)) * self.dt
        k4vy = self.ayRK(self.vy[-1] + k3vy) * self.dt
        k4y = (self.vy[-1] + k3vy) * self.dt

        self.vy.append(self.vy[-1] + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6)
        self.vx.append(self.vx[-1] + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6)
        self.ylista.append(self.ylista[-1] + (k1y + 2*k2y + 2*k3y + k4y)/6)
        self.xlista.append(self.xlista[-1] + (k1x + 2*k2x + 2*k3x + k4x)/6)


    def plot_trajectory(self):
        while self.ylista[-1] >=0:
            self.__move()

    def plot_trajectoryRK(self):
        while self.ylista[-1] >=0:
            self.__moveRK()
    
    def range(self):

        while self.ylista[-1] >=0:
            self.__moveRK()

        D = (self.xlista[-1] -self.xlista[0])

        return D
    


