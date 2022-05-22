import ProjectileKK as pct
import numpy as np
import matplotlib.pyplot as plt

pct1 = pct.Projectile()
pct1.set_initial_conditions(10,60,0,0,10,1.225,izbor ="kocka",a=0.8)
pct1.plot_trajectoryRK()

pct2 = pct.Projectile()
pct2.set_initial_conditions(10,60,0,0,10,1.225,izbor ="kugla",r=0.45)
pct2.plot_trajectoryRK()

plt.plot(pct1.xlista,pct1.ylista,'r')
plt.plot(pct2.xlista,pct2.ylista,'g')
plt.grid()
plt.legend(["kocka","kugla"], loc = "upper left")
plt.show()
