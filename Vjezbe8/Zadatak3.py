import Projectile as pct
import numpy as np
import matplotlib.pyplot as plt

Cdlista = np.linspace(0,1,100)
dometCD = []

for i in Cdlista:
    p1 = pct.Projectile()
    p1.set_initial_conditions(10,60,0,0,10,1.225,i,0.63)
    dometCD.append(p1.range())

plt.plot(Cdlista,dometCD)
plt.xlabel("Cd")
plt.ylabel("domet[m]")
plt.show()

mlista = np.linspace(1,10,100)
dometm = []

for i in mlista:
    p2 = pct.Projectile()
    p2.set_initial_conditions(10,60,0,0,i,1.225,0.47,0.63,)
    dometm.append(p2.range())

plt.scatter(mlista,dometm, s = 0.9 )
plt.xlabel("m[kg]")
plt.ylabel("domet[m]")
plt.show()
    




