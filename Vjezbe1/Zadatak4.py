import numpy as np
import math

def jednadzba_pravca (x1,y1,x2,y2):
    a = round((y2 - y1) / (x2 -x1),2)
    b = round((y1 - (a*x1)),2)

    print ("Jednadžba pravca je y = {0:.2f} x + {1:.2f}".format(a,b))

jednadzba_pravca(2,3,5,6)