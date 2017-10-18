from decimal import *
import sys
"""Berechnet x**2-y**2 sowie (x+y)*(x-y)
   mit Genauigkeiten von 3 - 8 Stellen und
   fuer float nach IEEE 754. Ergebnis bit-genau gleich mit double in C
"""
getcontext().prec = 3
# x=1.04, y=1.02
# x=1.004, y=1.002
# 1.04 0.94
# 1.04 0.93
x=Decimal(sys.argv[1])
y=Decimal(sys.argv[2])

for p in range(3,9):
   getcontext().prec = p
   print "Genauigkeit: %d Stellen" % p
   print "x=%s, y=%s" % (x,y)
   print "x^2=",x**2," y^2=",y**2,"x^2-y^2 =",(x**2-y**2)
   print "(x-y)=",x-y,"(x+y)= ",x+y,"(x-y)*(x+y)=",(x-y)*(x+y)
   print

x=float(sys.argv[1])
y=float(sys.argv[2])
print "Double (IEEE 754)"
print "x=%s, y=%s" % (x,y)
print "x^2=",x**2," y^2=",y**2,"x^2-y^2 = %19.17f" % (x**2-y**2)
print "(x-y)= %19.17f (x+y)= %19.17f x+y,= %19.17f" % (x-y,x+y,(x-y)*(x+y))
print

