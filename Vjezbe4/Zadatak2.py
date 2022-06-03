from cProfile import label
import calculus as c
import matplotlib.pyplot as plt
import numpy as np
import math

def funkcija(x):
    return 2*x**2 +3 

donja1,gornja1 = c.integracija_pravokutna(funkcija,0,1,10)
integral1 = c.integracija_trapez(funkcija,2,7,100)
print("Donja i gornja meda su: {} i {}".format(donja1,gornja1))

donja = []
gornja = []
int_trapez = []
korak = []
xlista = np.arange(50,1000,50)

for N in xlista:
    donjaX, gornjaX = c.integracija_pravokutna(funkcija,0,1,N)
    donja.append(donjaX)
    gornja.append(gornjaX)
    int_trapez.append(c.integracija_trapez(funkcija,0,1,N))
    korak.append(N)

fig = plt.figure(figsize=(20,10))
plt.scatter(korak,gornja,s=10)
plt.scatter(korak,donja,s=10)
plt.scatter(korak,int_trapez,s=10)

#ANALITICKI

plt.plot(11/3)

plt.xlabel("Koraci")
plt.ylabel("Integral")
plt.title("Numericka integracija")
plt.show()