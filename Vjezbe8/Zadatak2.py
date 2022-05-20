from cProfile import label
import Projectile as pct
import numpy as np
import matplotlib.pyplot as plt

pct1 = pct.Projectile()
pct1.set_initial_conditions(10,60,0,0,10,1.225,0.47,1)
pct1.plot_trajectory()

pct2 = pct.Projectile()
pct2.set_initial_conditions(10,60,0,0,10,1.225,0,1)
pct2.plot_trajectoryRK()

plt.plot(pct1.xlista,pct1.ylista, 'r')
plt.plot(pct2.xlista,pct2.ylista, 'g')
plt.legend(["s otporom zraka","bez otpora zraka"], loc = "upper left")
plt.show()

