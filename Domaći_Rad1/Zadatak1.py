import Particle as prt
import numpy as np
import matplotlib.pyplot as plt

p3 = prt.particle()
p3.set_initial_conditions(5,60,0,0,0.001)
#p3.plot_trajectory()
print("Ukupno vrijeme je: ",p3.total_time())
print("Domet: ",p3.range())
print("Maksimalna brzina je: ",p3.max_speed())
p3.reset()