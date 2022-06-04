import harmonic_oscillator as HO
import matplotlib.pyplot as plt
import numpy as np

HO1 = HO.HarmonicOscilator()
HO1.set_initial_conditions(0.1,8,0.01,0,1)
print("Numericki period je: {}".format(HO1.period()))
HO1.reset()

xlista = []
ylista = []
dt = list(np.linspace(0.001,0.25,1000))

for i in dt:
    HO2 = HO.HarmonicOscilator()
    HO2.set_initial_conditions(0.1,8,i,0,1)
    HO2.oscillate(3)
    analiticki = HO2.period_analiticki()
    xlista.append(HO2.period())
    ylista.append(abs(xlista[-1] - analiticki))
    HO2.reset()

plt.plot(dt,ylista)
plt.xlabel("dt [s]")
plt.ylabel("greška [%]")
plt.show()
    

