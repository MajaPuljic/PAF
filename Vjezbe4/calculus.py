from math import *
import numpy as np
from re import A

def derivacija_u_tocki(f,x,h = 0.01,metoda = 3):
    if metoda == 3:
        der = (f(x+h) - f(x -h))/(2*h)
    else:
        der = (f(x +h)-f(x))/h   
    return der

def derivacija(f,d,g,h = 0.01,metoda = 3):
    x = np.arange(d,g,h)
    y = []
    for i in x:
        y.append(derivacija_u_tocki(f,i,h,metoda))
    return (x,y)

def integracija_pravokutna(f,d,g,N):
    donjaMeda = 0
    gornjaMeda = 0
    dx = abs(g-d)/N
    for i in range (0,N):
        donjaMeda += f(i*dx) * dx
        gornjaMeda += f((i+1)*dx) * dx
    return gornjaMeda,donjaMeda       

def integracija_trapez(f,d,g,N):
    integral = 0
    dx = abs(g-d)/N
    for i in range(0,N):
        integral += f(i*dx) + f((i+1)*dx)
    return (integral*dx)/2










