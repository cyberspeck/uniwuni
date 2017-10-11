a=2.
b=1.
c=4e-165
d=2e-165
# Null division erst bei 2e-165 (double)
print "c**2=",c**2

print "(a*c+b*d)/(c**2+d**2)=",(a*c+b*d)/(c**2+d**2)
print "(a+b*(d/c))/(c+d*(d/c))=",(a+b*(d/c))/(c+d*(d/c))
0.5
c1=complex(a,b)
c2=complex(c,d)
print "c1/c2=",c1/c2

