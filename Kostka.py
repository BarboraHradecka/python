#!/usr/bin/env python3

import random

 
class Kostka:
    def __init__(self, pocet_sten=6):
        self.__pocetSten = pocet_sten
    
    def hod(self):
        return random.randint(1,self.__pocetSten)

    def getpocetSten(self):
        return self.__pocetSten
    def setpocetSten(self, pocet_sten):
        if pocet_sten > 0:
            self.__pocetSten = pocet_sten
        else:
            print(f'Pocet sten musi byt > 0, ponechavam: {self.__pocetSten}')

k1 = Kostka(6)
print(k1.hod())

k2 = Kostka(-12)
print(k2.getpocetSten)

print(k1.getpocetSten())
k1.setpocetSten(995)
print(k1.hod())

