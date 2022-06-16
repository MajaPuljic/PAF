import numpy as np
import matplotlib.pyplot as plt

class Planet:

    def __init__(self, d,v,m):
        
        self.m = m
        self.d = [d]
        self.v = [v]
        self.a = []
        self.x = np.array([0,0,0])
        self.xlist = [0]
        self.ylist = [0]

class Universe:

    def __init__(self,sunce,planet,T,dt):

        self.sunce = sunce
        self.planet = planet
        self.T = T
        self.dt = dt
        self.tlista = [0]
        self.G = 6.67408 * 10**(-11)

    def __move(self):

        while self.tlista[-1] < self.T:

            self.sunce.a.append(-self.G*self.planet.m*(self.sunce.d[-1] - self.planet.d[-1]) /(np.linalg.norm(self.sunce.d[-1] - self.planet.d[-1]))**3)
            self.sunce.v.append(self.sunce.v[-1] + self.sunce.a[-1]*self.dt)
            self.sunce.d.append(self.sunce.d[-1] + self.sunce.v[-1]*self.dt)

            self.planet.a.append(-self.G * self.sunce.m * (self.planet.d[-1] - self.sunce.d[-1]) / (np.linalg.norm(self.planet.d[-1] - self.sunce.d[-1]))**3)
            self.planet.v.append(self.planet.v[-1] + self.planet.a[-1] * self.dt)
            self.planet.d.append(self.planet.d[-1] + self.planet.v[-1] * self.dt)

            self.tlista.append(self.tlista[-1] + self.dt) 

        
    def plot_trajectory(self):

            self.__move()

            x_sunce = []
            y_sunce = []
            x_planet = []
            y_planet = []

            for x, y, in zip(self.sunce.d, self.planet.d):
                x_sunce.append(x[0])
                y_sunce.append(x[1])
                x_planet.append(y[0])
                y_planet.append(y[1])

            fix, axs = plt.subplots()
            axs.plot(x_sunce, y_sunce, linewidth=5)
            axs.plot(x_planet, y_planet)
            axs.set_aspect("equal", "box")
        
            plt.show()