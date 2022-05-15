import Projectile as pct
import numpy as np
import matplotlib.pyplot as plt

Cdlista = list(np.linspace(0,1,100))
dometCD = []

for i in Cdlista:
    p1 = pct.Projectile()
    p1.set_initial_conditions(10,45,0,0,0.1,1.22,i,0.05)
    dometCD.append(p1.range())

plt.plot(Cdlista,dometCD)
plt.xlabel("Cd")
plt.ylabel("domet[m]")
plt.show()

mlista = list(np.linspace(1,5,100))
dometm = []

for i in mlista:
    p2 = pct.Projectile()
    p2.set_initial_conditions(10,45,0,0,i,1.22,0.1,0.05)
    dometm.append(p2.range())

plt.scatter(mlista,dometm, s = 0.9 )
plt.xlabel("m[kg]")
plt.ylabel("domet[m]")
plt.show()
    




