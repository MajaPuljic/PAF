import Particle as prt

p1 = prt.particle()
p1.set_initial_conditions(5,45,0,3,0.01)
p1.range()
p1.plot_trajectory()
p1.reset()