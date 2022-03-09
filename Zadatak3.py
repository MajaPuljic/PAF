import numpy as np
import math

try:
    x1,y1 = [int(x) for x in input("Unesite x1 i y1: ").split()]
    x2,y2 = [int(x) for x in input("Unesite x2 i y2: ").split()]
except:
    print("Unijeli ste string, ponovno pokrenite program")

if x2 != x1:
 a = round((y2 - y1) / (x2 -x1),2)
 b = round((y1 - (a*x1)),2)
 print ("Jednadžba pravca je y = {}x + {}".format (a,b))
else:
    x1,y1 = [int(x) for x in input("Ponovno unesite x1 i y1: ").split()]
    x2,y2 = [int(x) for x in input("Ponovno unesite x2 i y2: ").split()]
    a = round((y2 - y1) / (x2 -x1),2)
    b = round((y1 - (a*x1)),2)
    print ("Jednadžba pravca je y = {}x + {}".format (a,b))