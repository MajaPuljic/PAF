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

def E2(t):
    E2 = np.array([0,0,0])
    return E2

def B2(t):
    Bz = t/10
    B2 = np.array([0,0,Bz])
    return B2

v02 = np.array([0.1,0.1,0.1])
q2 = -1
m2 = 1

p1 = prt.Particle(E1,B1,v01,q1,m1)
p1.plot_trajectoryRK(0.01,10)
xlist1, ylist1, zlist1 = p1.liste()


p2 = prt.Particle(E2,B2,v02,q2,m2)
p2.plot_trajectoryRK(0.01,10)
xlist2, ylist2, zlist2 = p2.liste()


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(xlist1, ylist1, zlist1, c="blue", label="electron ( B = const. )")
ax.plot3D(xlist2, ylist2, zlist2, c="red", label="electron ( B = f(t) )")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()



def E3(t):
    E3 = np.array([0,0,0])
    return E3

def B3(t):
    Bz = t/10
    B3 = np.array([0,0,Bz])
    return B3

v03 = np.array([0.1,0.1,0.1])
q3 = -1
m3 = 1

def E4(t):
    E4 = np.array([0,0,0])
    return E4

def B4(t):
    Bz = t/10
    B4 = np.array([0,0,Bz])
    return B4

v04 = np.array([0.1,0.1,0.1])
q4 = 1
m4 = 1

p3 = prt.Particle(E3,B3,v03,q3,m3)
p3.plot_trajectoryRK(0.01,10)
xlist3, ylist3, zlist3 = p3.liste()


p4 = prt.Particle(E4,B4,v04,q4,m4)
p4.plot_trajectoryRK(0.01,10)
xlist4, ylist4, zlist4 = p4.liste()


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(xlist3, ylist3, zlist3, c="orange", label="electron")
ax.plot3D(xlist4, ylist4, zlist4, c="green", label="positron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.view_init(30,30)
plt.legend()
plt.show()