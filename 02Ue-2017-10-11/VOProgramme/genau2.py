from decimal import *

import sys

getcontext().prec = 3

b=Decimal(sys.argv[1])
a=Decimal(sys.argv[2])
c=Decimal(sys.argv[3])

def r1(a,b,c):
    return -b+(b**2-4*a*c).sqrt()

def r2(a,b,c):
    return -b-(b**2-4*a*c).sqrt()

def R1(a,b,c):
    return 2*c/(-b+(b**2-4*a*c).sqrt())

def R2(a,b,c):
    return 2*c/(-b-(b**2-4*a*c).sqrt())

for p in range(3,9):
   getcontext().prec = p
   print "Genauigkeit: %d Stellen" % p
   print "b=%s, a=%s, c=%s" % (b,a,c)
   print "b**2=",b**2," 4*a*c=",4*a*c,"sqrt(b**2-4*a*c) =",(b**2-4*a*c).sqrt()
   print "r1 = ",r1(a,b,c),"r2 = ",r1(a,b,c),"R1 = ",r1(a,b,c),"R2 = ",r1(a,b,c)
   print

