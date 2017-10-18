# -*- coding: utf-8 -*-
from decimal import *

import sys
""" Berechnet die Fläche eines Dreiecks nach der Heronschen Flächenformel
    Einmal nach der Standardformel und das andere Mal nach einer Umformung,
    die das numerische Verhalten verbessert.
"""
# 9.0 4.53 4.53
# 9.0 4.56 4.56
# 11.1 5.55 5.56
def heron_simple(a,b,c):
    print a+b+c
    s=(a+b+c)/Decimal(2)
    print s
    return (s*(s-a)*(s-b)*(s-c)).sqrt()

def heron_prec(a,b,c):
    return( (a+(b+c))*(c-(a-b))*(c+(a-b))*(a+(b-c))  ).sqrt()/4

getcontext().prec = 3

a=Decimal(sys.argv[1])
b=Decimal(sys.argv[2])
c=Decimal(sys.argv[3])

for p in range(3,9):
   getcontext().prec = p
   print "Genauigkeit: %d Stellen" % p
   print "a=%s, b=%s, c=%s" % (a,b,c)
   s=s=(a+b+c)/Decimal(2)
   print a+b+c,s
   print "A(normal)=%s" % ((s*(s-a)*(s-b)*(s-c)).sqrt())
   print "A(besser)=%s" % (((a+(b+c))*(c-(a-b))*(c+(a-b))*(a+(b-c))).sqrt()/Decimal(4))
   print


