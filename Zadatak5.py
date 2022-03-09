import numpy as np
import math
import matplotlib.pyplot as plt

x1,y1 = [int(x) for x in input("Unesite x1 i y1: ").split()]
x2,y2 = [int(x) for x in input("Unesite x2 i y2: ").split()]

ime_xosi = input("Unesite naziv x osi: ")
ime_yosi = input("Unesite naziv y osi: ")

if x2 != x1:
 a = round((y2 - y1) / (x2 -x1),2)
 b = round((y1 - (a*x1)),2)
 print ("Jednadžba pravca je y = {}x + {}".format (a,b))
else:
    x1,y1 = [int(x) for x in input("Ponovno unesite x1 i y1: ").split()]
    x2,y2 = [int(x) for x in input("Ponovno unesite x2 i y2: ").split()]
    a = round((y2 - y1) / (x2 -x1),2)
    b = round((y1 - (a*x1)),2)
    print ("Jednadžba pravca je y = {}x + {}".format (a,b))

x_values = np.linspace(x1,x2,100)
y_values = np.linspace(y1,y2,100)

plt.xlabel(ime_xosi)
plt.ylabel(ime_yosi)

izbor1 = input ("Unesite 1 za prikaz grafa,\n Unesite 2 za spremanje grafa u obliku PDFa: ")
izbor = int(izbor1)
ime = input("Unesite ime grafa: ")

if izbor == 1:
    plt.plot(x_values,y_values)
    plt.show()
elif izbor == 2:
    plt.plot(x_values,y_values) 
    plt.savefig(ime)
else:
    print("Ta opcija ne postoji")
