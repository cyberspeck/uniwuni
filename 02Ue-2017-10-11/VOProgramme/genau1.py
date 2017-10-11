# -*- coding: utf-8 -*-

""" Berechnet b**2 - 4*a*c (quadratische Gleichung)
    mit der Genauigkeit von 3 ... 8 Stellen
    für die Werte a=1.22, b=3.34, c=2.28
    Obwohl die Werte a,b,c nur auf 3 Stellen angegeben sind, erält man das
    "genaue" Resultat erst bei 6 Stellen Genauigkeit.
"""
from decimal import *
print __doc__

getcontext().prec = 3

b=Decimal("3.34")
a=Decimal("1.22")
c=Decimal("2.28")


for p in range(3,9):
   getcontext().prec = p
   print "Genauigkeit: %d Stellen" % p
   print "b=%s, a=%s, c=%s" % (b,a,c)
   print "b**2 - 4*a*c = ",
   print "%s - %s = " % (b**2,4*a*c),
   print b**2-4*a*c
   print

