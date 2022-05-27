import numpy as np
import math
import matplotlib.pyplot as plt


def pravac(x1,y1,x2,y2):

    a = round((y2 - y1) / (x2 -x1),2)
    b = round((y1 - (a*x1)),2)
    dx = x2-x1
    dy = y2-y1

    izbor1 = input ("Unesite 1 za prikaz grafa,\n Unesite 2 za spremanje grafa u obliku PDFa: ")
    izbor = int(izbor1)
    ime = input("Unesite ime grafa: ")

    if izbor == 1:
        slika = plt.plot([x1-2*dx,x2+2*dx], [y1-2*dy,y2+2*dy])
        plt.plot(x1,y1,'r*')
        plt.plot(x2,y2,'r*')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    elif izbor == 2:
        slika = plt.plot([x1-2*dx,x2+2*dx], [y1-2*dy,y2+2*dy])
        plt.plot(x1,y1,'r*')
        plt.plot(x2,y2,'r*') 
        plt.savefig(ime)
    else:
        slika = False
    
    return slika

pravac(2,3,5,6)