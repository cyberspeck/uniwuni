from decimal import *

import sys
# 365 0.06
def ln_e(x): return (1+x).ln()
def ln_1(x): return x
def ln_2(x): return x*(1+x).ln()/((1+x)-1)

n=20
xs=Decimal(0)
xe=Decimal("0.001")
d=(xe-xs)/n
print "x; ln x   ",
for p in range(3,10): print p,"Stellen",
print
for i in range(1,n+1):
 x=xs+i*d
 print 1+x,
 for p in range(3,10):
   getcontext().prec = p
   try: l2=ln_2(x)
   except: l2="*"
   print ln_e(x), ln_1(x), l2,
 print


