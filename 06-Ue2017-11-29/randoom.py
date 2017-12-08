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



# https://en.wikipedia.org/wiki/RANDU
a1 = 65539
c1 = 3
m1 = np.power(2, 16)

seed = 42
Hansi = randoom(a1, c1, m1, seed)
Hansi.rand()
Hansi.uni01()

# http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_rand.aspx
a2 = 16807
c2 = 0
m2 = 2147483647

Miller = randoom(a2, c2, m2, seed)
