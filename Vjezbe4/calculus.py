from math import *
from re import A

def three_step (f,x,h):

    derivacija = (f(x+h) - f(x-h))/(2*h)

    return derivacija

def two_step (f,x,h):

    derivacija = (f(x+h) - f(x-h))/h

    return derivacija

def deriviranje (f,donja_granica,gornja_granica,h, izbor = 3):
    xlista = []
    ylista = []

    i = donja_granica
    while i <= gornja_granica:
        xlista.append(i)
        i+=h
    if izbor == 2:
        for el in xlista:
            derivacija = two_step(f,el,h)
            ylista.append(derivacija)
    elif izbor == 3:
        for el in xlista:
            derivacija = three_step(f,el,h)
            ylista.append(derivacija)
    return xlista,ylista

def kubna (x):
    return 3*x**3 - x**2 + 4*x + 2

def trigonometrijska(x):
    return sin(x) + 2*cos(2*x)









