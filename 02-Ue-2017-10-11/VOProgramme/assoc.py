from decimal import *

import sys

getcontext().prec = 8
print "Genauigkeit {0:d} Stellen\n".format(getcontext().prec)

u, v, w = Decimal(11111113), Decimal(-11111111), Decimal('7.5111111')

print "(%s +  %s) + %s  = %s" % (u,v,w,(u + v) + w)
print " %s + (%s  + %s) = %s" % (u,v,w,u + (v + w))
print
print "(%s + %s) = %s" % (u,v,u+v)
print "                         %s + %s = %s" % (u+v,w,(u + v) + w)
print "(%s  + %s) = %s hier wird auf 8 Stellen gerundet" % (v,w,(v + w))
print "                           %s + %s = %s" % ((v + w),u,u + (v + w))

print
print

u, v, w = Decimal(20000), Decimal(-6), Decimal('6.0000003')
print "(%s * %s) + (%s * %s) = %s" % (u,v,u,w,(u*v) + (u*w))
print " %s * (%s + %s) = %s" % (u,v,w,u * (v+w))
print

print "                                hier wird auf 8 Stellen gerundet"
print "(%s * %s) + (%s * %s) = %s + %s = %s" % (u,v,u,w,u*v,u*w,(u*v) + (u*w))
print "%s * (%s + %s) = %s * %s = %s" % (u,v,w,u,v+w,u * (v+w))


