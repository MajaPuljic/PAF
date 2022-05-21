import ProjectileKK2 as pct
import numpy as np
import matplotlib.pyplot as plt

pct1 = pct.Projectile()
pct1.set_initial_conditions(20,3,0,0.01,0,izbor="/",r=0.45)
pct1.plot_trajectoryRK()
plt.plot(pct1.xlista,pct1.ylista,'r')
plt.grid()
plt.show()
pct1.angle_range(20,0,1)
