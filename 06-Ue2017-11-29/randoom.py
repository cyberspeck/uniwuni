# -*- coding: utf-8 -*-
""" Randomness Generator von David Blacher, Christopher Gollnhofer, Johannes Kurz """
import string
import numpy as np
import socket, sys

class randoom:
    data = []

    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.data = [seed]

    def rand(self):
        self.data.append( (self.a*self.data[-1] + self.c) % self.m )
        return self.data[-1]

    def uni01(self):
        return float( self.rand() ) / (self.m - 1)

    def uni(self, imax):
        return imax * float( self.rand() ) / (self.m - 1)

    def gnout(self, imax, setnumber):
        A = np.zeros( (setnumber, 3), float )
        for i in range(setnumber):
            A[i] = (self.uni(imax), self.uni(imax), self.uni(imax))
        return A

class monteboy:

    def __init__(self):
        print("I bims")
        return

    def integriermalwas(self, ZUFALL, a=0, b=10, N=10):
        hit = 0
        miss = 0

        educated_guess = np.zeros( (N,2), float )
        for i in range(N):
            educated_guess[i,0] = a+(b-a)*ZUFALL.uni01()
            educated_guess[i,1] = ZUFALL.uni01()*2-1

            if ( np.sin(educated_guess[i,0]) == 0): continue
            if ( educated_guess[i,1] < np.sin(educated_guess[i,0]) ):
                if ( educated_guess[i,1] > 0. ):
                    print("wir liegen drinnen!  sin({})={}, y={}".format(educated_guess[i,0],np.sin(educated_guess[i,0]), educated_guess[i,1]) )
                    hit = hit + 1
                else:
                    print("wir liegen draußen.. sin({})={}, y={}".format(educated_guess[i,0],np.sin(educated_guess[i,0]), educated_guess[i,1]) )
                    miss = miss + 1
            else:
                if ( educated_guess[i,1] < 0. ):
                    print("wir liegen draußen.. sin({})={}, y={}".format(educated_guess[i,0],np.sin(educated_guess[i,0]), educated_guess[i,1]) )
                    miss = miss + 1
                else:
                    print("wir liegen drinnen!  sin({})={}, y={}".format(educated_guess[i,0],np.sin(educated_guess[i,0]), educated_guess[i,1]) )
                    hit = hit + 1

        return (hit, miss)

def funktion(*args, **kwargs):
    return np.sin(args)


# https://en.wikipedia.org/wiki/RANDU
a1 = 65539
c1 = 3
m1 = np.power(2, 16)
seed = 42
Hansi = randoom(a=a1, c=c1, m=m1, seed=seed)

# http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_rand.aspx
a2 = 16807
c2 = 0
m2 = 2147483647
Miller = randoom(a2, c2, m2, seed)


'''
zufall_anzahl = 50000
zufall_gefallen = Miller.gnout(1, zufall_anzahl)
for i in range(zufall_anzahl):
    print("{} {} {}".format(zufall_gefallen[i,0], zufall_gefallen[i,1], zufall_gefallen[i,2]))
'''


carl = monteboy()
a, b = carl.integriermalwas(Miller, a=0, b=np.pi, N=100)
