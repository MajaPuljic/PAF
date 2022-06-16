import solarsystem as uni
import numpy as np

ms = 1.989 * 10**30
vrijeme = 5*365.242 * 24 * 3600
au = 1.496 * 10 **(11)

Sunce = uni.Planet( np.array((0, 0)), np.array((0, 0)),ms)

mz = 5.9742 * 10**24
vzx = - 29783

Zemlja = uni.Planet(np.array((-1. *au,0)), np.array((0,float(vzx))),mz)
sunce_zemlja = uni.Universe(Sunce,Zemlja,vrijeme,360)
sunce_zemlja.plot_trajectory()