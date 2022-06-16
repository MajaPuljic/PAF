import numpy as np
from math import sqrt 

G = 6.67408 * pow(10,-11)

class Universe:
    def __init__(self):
        self.lista_planeta = []

    def add_planet(self,planet):
        self.lista_planeta.append(planet)

    def __move(self,dt):
        n = len(self.lista_planeta)
        for i in range(n):
            a = np.array([0,0])
            for j in range(n):
                if i != j:
                    a = a + self.lista_planeta[i].gravitational_force_acc(self.lista_planeta[j])
            self.lista_planeta[i].a = a
        for planet in self.lista_planeta:
            planet.v = planet.v + planet.a * dt
            planet.r = planet.r + planet.v * dt
            planet.xlist.append(planet.r[0])
            planet.ylist.append(planet.r[1])

    def evolve(self,T,dt):
        t = 0
        while t < T:
            self.__move(dt)
            t = t + dt

class Planet:
    def __init__(self,name,color,m,r0,v0):
        self.name = name
        self.color = color
        self.m = m
        self.r = r0
        self.v = v0
        self.a = np.array([0,0])
        self.xlist = []
        self.ylist = []

    def __distance(self,other):
        x1 = self.r[0]
        x2 = other.r[0]
        y1 = self.r[1]
        y2 = other.r[1]
        x = x1 - x2
        y = y1 - y2
        d = sqrt(pow(x,2) + pow(y,2))
        return d

    def gravitational_force_acc(self,other):
        distance = self.__distance(other)
        r12 = (self.r - other.r) * (1 / distance)
        a = - ((G * other.m)/(pow(distance,2))) * r12
        return a