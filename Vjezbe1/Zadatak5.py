import numpy as np
import math
import matplotlib.pyplot as plt


ime_xosi = input("Unesite naziv x osi: ")
ime_yosi = input("Unesite naziv y osi: ")


def pravac(x1,y1,x2,y2):

    a = round((y2 - y1) / (x2 -x1),2)
    b = round((y1 - (a*x1)),2)

    x_values = np.linspace(x1,x2,100)
    y_values = np.linspace(y1,y2,100)

    plt.xlabel(ime_xosi)
    plt.ylabel(ime_yosi)

    izbor1 = input ("Unesite 1 za prikaz grafa,\n Unesite 2 za spremanje grafa u obliku PDFa: ")
    izbor = int(izbor1)
    ime = input("Unesite ime grafa: ")

    if izbor == 1:
        slika = plt.plot(x_values,y_values)
        plt.show()
    elif izbor == 2:
        slika = plt.plot(x_values,y_values) 
        plt.savefig(ime)
    else:
        slika = False
    
    return slika

pravac(2,3,5,6)