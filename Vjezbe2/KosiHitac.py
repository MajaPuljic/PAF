from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from math import *

def xy_putanja (v0,theta,y_pocetni):

    kut = theta*np.pi/180

    vx = np.cos(kut)*v0
    vy = np.sin(kut)*v0

    x = 0
    y = y_pocetni

    dt = 0.01
    a = -9.81

    x_lista = []
    y_lista = []

    while True:
        x = x + vx*dt
        vy = vy + a*dt
        y = y + vy*dt

        if y <=0:
            break

        y_lista.append(y)
        x_lista.append(x)

    plt.plot(x_lista,y_lista)
    plt.xlabel('$x | [m]$')
    plt.ylabel('$y | [m]$')
    plt.title("xy_putanja")

    plt.show()

def max_h (v0,theta,y_pocetni):

    kut = theta*np.pi/180
    vy = np.sin(kut)*v0

    y = y_pocetni

    dt = 0.01
    a = -9.81

    while True:

        vy = vy + a*dt

        if vy <= 0:
            break

        y = y + vy*dt

    return y

def domet (v0,theta,y_pocetni):

    kut = theta*np.pi/180

    vx = np.cos(kut)*v0
    vy = np.sin(kut)*v0

    x = 0
    y = y_pocetni

    dt = 0.01
    a = -9.81

    while True:
        x = x + vx*dt
        vy = vy + a*dt
        y = y + vy*dt

        if y <=0:
            break
    
    return x

def max_v (v0,theta,y_pocetni):

    kut = theta*np.pi/180

    vx = np.cos(kut)*v0
    vy = np.sin(kut)*v0

    x = 0
    y = y_pocetni

    dt = 0.01
    a = -9.81

    while True:

        x = x + vx*dt
        vy = vy + a*dt
        y = y + vy*dt

        if y <=0:
            break
    
    vmax = sqrt(vx**2 + vy**2)
    return vmax

def meta(x_meta,y_meta,r,v0,theta,y_pocetni):

    kut = theta*np.pi/180

    vx = np.cos(kut)*v0
    vy = np.sin(kut)*v0

    x = 0
    y = y_pocetni

    dt = 0.01
    a = -9.81

    d_pocetna = sqrt((x_meta)**2 + (y_meta - y_pocetni)**2)

    x_lista = []
    y_lista = []

    score = False
    
    while True:
        x = x + vx*dt
        vy = vy + a*dt
        y = y + vy*dt

        if y <=0:
            break

        y_lista.append(y)
        x_lista.append(x)
        d_konacna = sqrt((x_meta - x)**2 + (y_meta - y)**2)

        if d_konacna <= r:
            score = True
            break
        else:
            if d_konacna - r < d_pocetna:
                d_pocetna = d_konacna - r

    if score:
        print("Projektil je pogodio metu")
    
    else:
        print("Projektil nije pogodio metu,\n najmanja udaljenost od mete bila je: {}m".format(d_pocetna))


    theta = np.linspace(0, 2*np.pi, 1000)
    X = r * np.cos(theta) + x_meta
    Y = r* np.sin(theta) + y_meta

    fig = plt.figure(figsize=(5,5), dpi=200)
    ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
    ax.set_aspect('equal')
    plt.rcParams.update({'font.size': 6})
    plt.axis('equal')
    ax.plot(x_meta, y_meta, 'b*')
    ax.plot(X,Y,'r')
    ax.set_xlabel('X os')
    ax.set_ylabel('Y os')
    ax.grid()

    plt.plot(x_lista,y_lista)

    plt.show()











    

    