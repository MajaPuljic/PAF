from math import *
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.1)  
y = np.sin(x)

plt.plot(x,y)
plt.show()

k = np.interp(0,y,x)
print(k)