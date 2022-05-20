import Projectile as pct
import numpy as np

pct1 = pct.Projectile()
pct1.set_initial_conditions(5,60,0,0,0.4,0,0,0)
pct1.range()
pct1.plot_trajectory()
pct1.reset()

pct2 = pct.Projectile()
pct2.set_initial_conditions(5,60,0,0,0.04,0,0,0)
pct2.range()
pct2.plot_trajectory()
pct2.reset()

pct3 = pct.Projectile()
pct3.set_initial_conditions(5,60,0,0,0.03,0,0,0)
pct3.range()
pct3.plot_trajectory()
pct3.reset()

pct4 = pct.Projectile()
pct4.set_initial_conditions(5,60,0,0,0.02,0,0,0)
pct4.range()
pct4.plot_trajectory()
pct4.reset()

print("Za ∆t <= 0.03 Euler-ova metoda daje dovoljno precizno numeričko rješenje koje na x − y grafu nema naznake ne-fizikalnog gibanja.")

