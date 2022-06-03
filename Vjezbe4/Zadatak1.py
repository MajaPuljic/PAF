from cProfile import label
import calculus as c
import matplotlib.pyplot as plt
import numpy as np
from math import *

def kubna(x):
    return 5*x**3 -2*x**2 + 2*x -3

print("Vrijednost derivacije u odabranoj točki: ",np.round(c.derivacija_u_tocki(kubna,0,0.01,3),2))

x1,derivacijalista1 = (c.derivacija(kubna,-2,2,0.1,2))
x1_1,derivacijalista1_1 = (c.derivacija(kubna,-2,2,0.001,3))
plt.scatter(x1, derivacijalista1,color="red",s=30, label="Epsilon = 0.1")
plt.plot(x1_1, derivacijalista1_1,'--',label="Epsilon = 0.01")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

def trigonometrijska(x):
    return sin(x)

x2,derivacijalista2 = c.derivacija(trigonometrijska,0,4*pi,0.1)
plt.scatter(x2,derivacijalista2,color="red",s=30,label="Numericki")

#ANALITICKI
def trigonometrijska2(x):
    return cos(x)

x_vrijednosti = np.linspace(0, 4*pi, 1000)
funkcija = []
for i in range(len(x_vrijednosti)):
    funkcija.append(trigonometrijska2(x_vrijednosti[i]))

plt.plot(x_vrijednosti, funkcija,'--',label="Analiticki")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

