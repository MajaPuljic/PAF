from cProfile import label
import harmonic_oscillator as HO
import matplotlib.pyplot as plt
import numpy as np

HO1 = HO.HarmonicOscilator()
HO1.set_initial_conditions(0.1,8,0.01,0,1)
HO1.oscillate(3)
HO1.plot()

#NUMERICKI

fig= plt.figure(figsize=(20,10))

H02 = HO.HarmonicOscilator()
H02.set_initial_conditions(0.1,8,0.001,0,1)
H02.oscillate(3)
x2,t2 = H02.liste()
plt.scatter(t2,x2,s=0.5,label='dt=0.001')
H02.reset()

H03 = HO.HarmonicOscilator()
H03.set_initial_conditions(0.1,8,0.01,0,1)
H03.oscillate(3)
x3,t3 = H03.liste()
plt.scatter(t3,x3,s=5,label='dt=0.01')
H03.reset()

H04 = HO.HarmonicOscilator()
H04.set_initial_conditions(0.1,8,0.05,0,1)
H04.oscillate(3)
x4,t4 = H04.liste()
plt.scatter(t4,x4,s=5,label='dt=0.05')
H04.reset()

#ANALITICKI
tA = np.arange(0,3,0.001)
omega = np.sqrt(8/0.1)
phi = np.pi/2
xA = 1*np.sin(omega*tA+phi)
plt.plot(tA,xA,c='red',label='analiticki')

plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('Harmonic oscillator')
plt.legend(loc="lower right")
plt.show()