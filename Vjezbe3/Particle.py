import matplotlib.pyplot as plt
import numpy as np

class particle:

    def __init__(self):
        
        self.xlista = []
        self.ylista = []
        self.vx = []
        self.vy = []
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
        self.ylista.append(self.ylista[-1] + self.ylista[-1]*self.dt)
        self.vx.append(self.vx[-1] + self.g*self.dt)
        self.xlista.append(self.xlista[-1] + self.xlista[-1]*self.dt)

    def range(self):

        while True:
            self.__move()

            if self.ylista[-1] <= 0:
                 break

        D = (self.xlista[-1] - self.xlista[0])

        return D

    def plot_trajectory(self):

        plt.plot(self.xlista,self.ylista)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")

        plt.show()




    



    

