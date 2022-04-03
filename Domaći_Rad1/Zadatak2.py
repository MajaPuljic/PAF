import Particle as prt
import matplotlib.pyplot as plt
from math import *

p = prt.particle()
p.set_initial_conditions(6,60,0,0,0.01)
p.D_ovisnost(6)
p.T_ovisnost(6)
