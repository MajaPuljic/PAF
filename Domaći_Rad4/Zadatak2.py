import ProjectileKK2 as pct
import numpy as np
import matplotlib.pyplot as plt
from math import*

#Kodu treba 4 do 5 minuta da se izvrsi do kraja
print("Nultocke grafa su kutevi potrebni za pogodit metu, ako graf nema nultocaka zadana brzina je premala!")
xm = 20
ym = 0
rm = 1

pct1 = pct.Projectile()
pct1.set_initial_conditions(20,3,0,0.01,0,izbor="/",r=0.45)
pct1.angle_range(xm,ym,rm)
pct2 = pct.Projectile()
pct2.set_initial_conditions(20,3,0,0.01,0,12.1796,izbor="/",r=0.45)
pct2.plot_trajectoryRK()

pct3 = pct.Projectile()
pct3.set_initial_conditions(20,3,0,0.01,0,77.7,izbor="/",r=0.45)
pct3.plot_trajectoryRK()

print("Meta se nalazi u T({},{})".format(xm,ym))
plt.plot(pct2.xlista,pct2.ylista,'r')
plt.plot(pct3.xlista,pct3.ylista,'g')
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.legend(["kut od 12.1796°","kut od 77.7°"], loc = "upper left")
plt.grid()
plt.show()
