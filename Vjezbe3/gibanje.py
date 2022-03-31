import Particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.particle()
p1.set_initial_conditions(5,60,0,0,0.01)
print("Domet: ",p1.range())
p1.plot_trajectory()
p1.reset()

xlista = []
ylista = []
D_analiticki = 100 * np.sin(2*np.pi/3)/9.81
dt = list(np.linspace(0.01,1,200))

for i in dt:
    p2 = prt.particle()
    p2.set_initial_conditions(10,60,0,0,i)
    xlista.append(p2.range())
    ylista.append(abs(xlista[-1] - D_analiticki)*100/D_analiticki)
    p2.reset()
    
plt.plot(dt,ylista)
plt.xlabel("dt [s]")
plt.ylabel("greška [%]")
plt.show()