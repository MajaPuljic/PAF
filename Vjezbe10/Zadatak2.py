import Particle as prt
import matplotlib.pyplot as plt
import numpy as np

def E1(t):
    E1 = np.array([0,0,0])
    return E1

def B1(t):
    B1 = np.array([0,0,1])
    return B1

v01 = np.array([0.1,0.1,0.1])
q1 = -1
m1 = 1

p1 = prt.Particle(E1,B1,v01,q1,m1)
p1.plot_trajectory(0.01,20)
xlist1, ylist1, zlist1 = p1.liste()

def E2(t):
    E4 = np.array([0,0,0])
    return E4

def B2(t):
    Bz = t/10
    B4 = np.array([0,0,1])
    return B4

v02 = np.array([0.1,0.1,0.1])
q2 = -1
m2 = 1

p2 = prt.Particle(E2,B2,v02,q2,m2)
p2.plot_trajectoryRK(0.01,20)
xlist2, ylist2, zlist2 = p2.liste()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(xlist1, ylist1, zlist1, c="blue", label="Euler")
ax.plot3D(xlist2, ylist2, zlist2, c="green", label="Runge-Kutta")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()