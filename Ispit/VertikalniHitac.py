import numpy as np

class Projektil:
    
    def __init__(self,h0,v0,dt = 0.01,g = -9.81):

        self.dt = dt
        self.tlista = [0]
        self.g = g
        self.h = h0
        self.hlista = [h0]
        self.v = v0
        self.vlista = [v0]
        print("Objekt je uspjesno stvoren!")
        print("Pocetna visina je: {} m\nPocetna brzina je: {} m/s".format(self.h,self.v))

    
    def promjena_h0(self,y):

        self.h = y

    def promjena_v0(self,v):

        self.v = v
    
    def __move(self):

        self.v = self.v + self.g*self.dt
        self.h = self.h + self.v * self.dt
        self.hlista.append(self.h)
        self.vlista.append(self.v)
        self.tlista.append(self.tlista[-1] + self.dt)

    def reset(self):
        self.tlista = [0]
        self.hlista = [self.hlista[0]]
        self.vlista = [self.vlista[0]]
        self.dt = self.dt

    def liste (self):

        while self.hlista[-1] > 0:
            self.__move()  

        return self.hlista,self.vlista,self.tlista  

    def max_h(self):

        while self.vlista[-1]>0:
            self.__move()

        hmax = self.hlista[-1]

        return hmax

    def t_uk(self):

        while self.hlista[-1] > 0:
            self.__move()  

        tuk = self.tlista[-1]

        return tuk

    def __moveAR (self,k):
        a = self.g - k*self.v
        self.v = self.v + a * self.dt
        self.h = self.h + self.v * self.dt
        self.hlista.append(self.h)
        self.vlista.append(self.v)
        self.tlista.append(self.tlista[-1] + self.dt)

    def listeAR (self,k):

        while self.hlista[-1] > 0:
            self.__moveAR(k)  

        return self.hlista,self.vlista,self.tlista 

    def max_hAR(self,k):

        while self.vlista[-1]>0:
            self.__moveAR(k)

        hmax = self.hlista[-1]

        return hmax

    def t_ukAR(self,k):

        while self.hlista[-1] > 0:
            self.__moveAR(k)  

        tuk = self.tlista[-1]

        return tuk


    


    
    