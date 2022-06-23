import VertikalniHitac as VH
import numpy as np
import matplotlib.pyplot as plt

tijelo = VH.Projektil(0,10)

hmakismalan = tijelo.max_h()
tukupno = tijelo.t_uk()

print("Maksimalna visina objekta je: {} m\n,a ukupno vrijeme je: {}s".format(hmakismalan,tukupno))
