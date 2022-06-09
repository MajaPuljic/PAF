from math import *
import numpy as np
import matplotlib.pyplot as plt


class BungeeJumper:

    def __init__(self,m,k,Cd,A,rho,l0,h0):
        self.m = m
        self.k = k
        self.Cd = Cd
        self.A = A
        self.rho = rho
        self.l0 = l0
        self.h0 = h0
        self.v = [0]
        self.y = [h0]
        self.a = [-9.81]
        self.t = [0]
        self.dt = 0.01
        self.g = -9.81
        self.Ek = [0]
        self.Ep = [h0 * m * 9.81]
        self.Eel = [0]
        self.Euk = []

    def Fel(self):
        
        d = self.h0 - self.l0

        if d > 0:
            Fel = self.k * d

        else:
            F = 0
        return F

    