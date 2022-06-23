import VertikalniHitac as VH
import numpy as np
import matplotlib.pyplot as plt


v0 = 10

xlista = []
ylista = []
t_uk_analiticki = 2* v0/9.81
dt = list(np.linspace(0.01,1,500))

for i in dt:
    tijelo = VH.Projektil(10,v0,i)
    xlista.append(tijelo.t_uk())
    ylista.append(abs(xlista[-1] - t_uk_analiticki)*100/t_uk_analiticki)
    tijelo.reset()

plt.plot(dt,ylista)
plt.xlabel("dt [s]")
plt.ylabel("greška [%]")
plt.show()