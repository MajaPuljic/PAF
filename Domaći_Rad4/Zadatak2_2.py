import ProjectileKK2 as pct
import numpy as np
import matplotlib.pyplot as plt
from math import*

#Kodu treba 4 do 5 minuta da se izvrsi do kraja
print("Nultocke grafa su kutevi potrebni za pogodit metu, ako graf nema nultocaka zadana brzina je premala!")
xm = 130
ym = 0
rm = 3

pct1 = pct.Projectile()
pct1.set_initial_conditions(50,0,0,0.1,1.22,izbor="/",r=0.45,Cd=0.1,A=0.01)
pct1.angle_range(xm,ym,rm)

pct2 = pct.Projectile()
pct2.set_initial_conditions(50,0,0,0.1,1.22,28.7262,izbor="/",r=0.45,Cd=0.1,A=0.01,)
pct2.plot_trajectoryRK()

pct3 = pct.Projectile()
pct3.set_initial_conditions(50,0,0,0.1,1.22,54.9504,izbor="/",r=0.45,Cd=0.1,A=0.01)
pct3.plot_trajectoryRK()

print("Meta se nalazi u T({},{})".format(xm,ym))
plt.plot(pct2.xlista,pct2.ylista,'r')
plt.plot(pct3.xlista,pct3.ylista,'g')
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.legend(["kut od 28.7262°","kut od 54.9504°"], loc = "upper left")
plt.grid()
plt.show()