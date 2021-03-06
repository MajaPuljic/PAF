import universe
import numpy as np
import matplotlib.pyplot as plt 

au = 1.486e11
minute = 60
hour = 60 * minute
day = 24 * hour
year = 365.242 * day

sun = universe.Planet("Sun","yellow",1.989e30, np.array([0,0]), np.array([0,0]))
mercury = universe.Planet("Mercury","orange",3.3e24, np.array([0,0.466*au]), np.array([-47362,0]))
venus = universe.Planet("Venus","red",4.8685e24, np.array([0.723*au,0]), np.array([0,35020]))
earth = universe.Planet("Earth","green",5.9742e24, np.array([-au,0]), np.array([0,-29783]))
mars = universe.Planet("Mars","brown",6.417e23, np.array([0,-1.666*au]), np.array([24007,0]))
comet = universe.Planet("Comet","grey",10e14,np.array([-4.*au, 1.8*au]),np.array([20000., 0.]),)

solar_system = universe.Universe()
solar_system.add_planet(sun)
solar_system.add_planet(mercury)
solar_system.add_planet(venus)
solar_system.add_planet(earth)
solar_system.add_planet(mars)
solar_system.add_planet(comet)

solar_system.evolve(5 * year, hour)

fig = plt.figure(figsize = (8,8))

i = 0
while i <  15 * 24:
    plt.clf()
    plt.plot(sun.xlist, sun.ylist, label = sun.name, color = sun.color, linewidth = 5)
    plt.plot(mercury.xlist, mercury.ylist, label = mercury.name, color = mercury.color)
    plt.plot(venus.xlist, venus.ylist, label = venus.name, color = venus.color)
    plt.plot(earth.xlist, earth.ylist, label = earth.name, color = earth.color)
    plt.plot(mars.xlist, mars.ylist, label = mars.name, color = mars.color)
    plt.plot(comet.xlist, comet.ylist, label = comet.name, color = comet.color)

    j = i * 24

    plt.plot(mercury.xlist[j], mercury.ylist[j], "o", color = mercury.color)
    plt.plot(venus.xlist[j], venus.ylist[j], "o", color = venus.color)
    plt.plot(earth.xlist[j], earth.ylist[j], "o", color = earth.color)
    plt.plot(mars.xlist[j], mars.ylist[j], "o", color = mars.color)
    plt.plot(comet.xlist[j], comet.ylist[j], "o", color = comet.color)
    i = i + 1
    plt.pause(0.01)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Solar System")
plt.legend(loc="upper right")
plt.show()
