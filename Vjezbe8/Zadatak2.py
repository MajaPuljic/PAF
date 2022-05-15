from cProfile import label
import Projectile as pct
import numpy as np
import matplotlib.pyplot as plt

pct1 = pct.Projectile()
pct1.set_initial_conditions(10,45,0,0,0.1,1.22,0.1,0.05)
pct1.plot_trajectory()

pct2 = pct.Projectile()
pct2.set_initial_conditions(10,45,0,0,0.1,1.22,0.1,0.05)
pct2.plot_trajectoryRK()

plt.plot(pct1.xlista,pct1.ylista)
plt.plot(pct2.xlista,pct2.ylista)
plt.show()

