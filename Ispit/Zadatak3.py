import VertikalniHitac as VH
import matplotlib.pyplot as plt

tijelo = VH.Projektil(10,10)
h,v,t = tijelo.liste()

plt.plot(t,h)
plt.xlabel("t(s)")
plt.ylabel("h(m)")
plt.title("h - t graf")
plt.show()

plt.plot(t,v)
plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.title("v - t graf")
plt.show()


