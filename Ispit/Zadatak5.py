import VertikalniHitac as VH
import numpy as np
import matplotlib.pyplot as plt

k = 1.5

tijeloAR = VH.Projektil(10,10)
max_hAR = tijeloAR.max_hAR(k)
t_ukAR = tijeloAR.t_ukAR(k)

tijelo = VH.Projektil(10,10)
max_h = tijelo.max_h()
t_uk = tijelo.t_uk()

print("Za Δt = 0.01 sa otporom zraka maksimalna visina objekta je: {} m, bez otpora zraka je:{}m \n,a ukupno vrijeme sa otporom zraka je: {}s,bez otpora zraka je:{}s".format(max_hAR,max_h,t_ukAR,t_uk ))

tijeloAR2 = VH.Projektil(10,10,0.05)
max_hAR2 = tijeloAR2.max_hAR(k)
t_ukAR2 = tijeloAR2.t_ukAR(k)

tijelo2 = VH.Projektil(10,10)
max_h2 = tijelo2.max_h()
t_uk2 = tijelo2.t_uk()

print("Za Δt = 0.05 sa otporom zraka maksimalna visina objekta je: {} m, bez otpora zraka je:{}m \n,a ukupno vrijeme sa otporom zraka je: {}s,bez otpora zraka je:{}s".format(max_hAR2,max_h2,t_ukAR2,t_uk2 ))

tijeloAR3 = VH.Projektil(10,10,0.1)
max_hAR3 = tijeloAR3.max_hAR(k)
t_ukAR3 = tijeloAR3.t_ukAR(k)

tijelo3 = VH.Projektil(10,10)
max_h3 = tijelo3.max_h()
t_uk3 = tijelo3.t_uk()

print("Za Δt = 0.10 sa otporom zraka maksimalna visina objekta je: {} m, bez otpora zraka je:{}m \n,a ukupno vrijeme sa otporom zraka je: {}s,bez otpora zraka je:{}s".format(max_hAR3,max_h3,t_ukAR3,t_uk3 ))