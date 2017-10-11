# -*- coding: utf-8 -*-
from decimal import *

import sys
"""Berechnet das Endkapital für n Tage und dem Zinsatz z für 100 WE, die 
   n-mal einbezahlt wurden
   K_app: Kapital mit Umformung (1+x)**n = exp(n*ln(1+x/n))
"""

# 365 0.06
n=Decimal(sys.argv[1])
z=Decimal(sys.argv[2])
print "n=%s, z=%s" % (n,z)
getcontext().prec = 25
e=(((1+z/n)**n)-1)/(z/n) # Ertragsfaktor; Endkapital=Ausgangskapital*e
K_exact=100*e
print "K=",K_exact,e,getcontext().prec,"Stellen"
print"x=z/n"
print "Genauigkeit | K_berechnet | Differenz     | (1+z/n)**n  | e^(n*ln(x)) | e^(n*(x)/n))| K_app     | Differenz"

for p in range(3,20):
   getcontext().prec = p#
   x=z/n
   f=(1+x)**n
   e=(f-1)/x
   K=100*e
   aln=x
   a=(n*(1+x).ln()).exp()
   b=(n*aln).exp()
   K_ap=100*(b-1)/x
   #print "        %2d  |  %s  | %12.5e  | %s | %s" % (p,str(K)[:9].ljust(9),(K_exact-K),str(f)[:11].ljust(11),b)
   #K_approx=
   print "        %2d  |  %s  | %12.5e  | %s | %s | %s | %s | %s |" % (p,str(K)[:9].ljust(9),(K_exact-K),str(f)[:11].ljust(11),\
          str(a)[:11].ljust(11),str(b)[:11].ljust(11),str(K_ap)[:9].ljust(9),str(K_exact-K_ap)[:9].ljust(9))


