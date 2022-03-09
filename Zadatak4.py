import numpy as np
import math

x1,y1 = [int(x) for x in input("Unesite x1 i y1: ").split()]
x2,y2 = [int(x) for x in input("Unesite x2 i y2: ").split()]

def koeficjent():
    a = round((y2 - y1) / (x2 -x1),2)
    return a

def isjecak (k): 
    b = round((y1 - (k*x1)),2)
    return b

print ("Jednadžba pravca je y = {}x + {}".format (koeficjent(),isjecak(koeficjent())))