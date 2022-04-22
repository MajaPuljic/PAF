import calculus as c
import matplotlib.pyplot as plt

listx1,listy1 = c.deriviranje(c.trigonometrijska,-5,5,0.1,2)
listx2,listy2 = c.deriviranje(c.kubna,-5,5,0.1,2)
plt.plot(listx1,listy1,"*")
plt.plot(listx2,listy2,".")
plt.show()