import numpy as np
import matplotlib.pyplot as plt
import math

x1,y1 = [int(x) for x in input("Unesite x1 i y1: ").split()]
krug_x,krug_y = [int(x) for x in input("Unesite x i y koordinatu kruga: ").split()]

r = int(input("Unesite radijus kruga: "))
if r < 0:
    r = int(input("Unesite radijus kruga: "))
else:
    None
ime = input("Unesite ime grafa: ")
ispis = int(input("Unesite 1 ako zelite da se kruznica ispise na ekranu, a \n 2 ako ju zelite spremit u obliku PDFa: "))
def zadatak6 ():
    
    theta = np.linspace(0, 2*np.pi, 1000)
    x = r * np.cos(theta) + x1
    y = r* np.sin(theta) + y1
    d = math.sqrt((x1 - krug_x)**2 + (y1 - krug_y)**2)
    d2 = abs(d - r)

    
    if d < r:
        polozaj = "Tocka se nalazi unutar kruznice"
    elif d > r:
        polozaj = "Tocka se nalazi van kruznice"
    else:
        polozaj = "Tocka se nalazi na kruznici"

    
    fig = plt.figure(figsize=(5,5), dpi=200)
    ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
    ax.set_aspect('equal')
    plt.rcParams.update({'font.size': 6})
    plt.axis('equal')
    ax.plot(x1, y1, 'r*')
    ax.plot(krug_x, krug_y, 'b*')
    ax.plot(x, y, 'r')
    ax.set_xlabel('X os')
    ax.set_ylabel('Y os')
    ax.set_title(ime)
    ax.grid()

    ax.legend(['{}'.format(polozaj)+'\n'+'Točka A udaljena je od kružnce za'+'\n'+'{}.'.format(d2), 'Središte kružnice ', 'Kružnica.'], loc = 'best')

    if ispis == 1:
        kruznica = plt.show()
    elif ispis == 2:
        kruznica = plt.savefig(ime)
    else:
        kruznica = False
    
    return kruznica

zadatak6()

    

    
    

