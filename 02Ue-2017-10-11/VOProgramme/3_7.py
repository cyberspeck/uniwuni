# -*- coding: utf-8 -*-

from decimal import *
import sys

""" Dezimalzahl mit veränderlicher Genaugkeit
    3./7. mit variabler Genauigkeit
"""
q=Decimal(3)/Decimal(7)
dp=getcontext().prec
print "Genauigkeit:",dp,"Stellen"
print "q = 3./7. = %30.28f" % q

for p in range(3,dp+5):
   getcontext().prec = p
   print "{0:2d}".format(p),"Stellen: q == 3./7.",
   
   if q == Decimal(3)/Decimal(7): print "  gleich",
   else: print "ungleich",
   print q,"==",Decimal(3)/Decimal(7)

