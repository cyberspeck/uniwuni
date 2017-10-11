import sys
""" Genaugeit (Kommutativgesetz)
    Verwendung: python 1_10.py Zahl
    Zahl: 0.5, 10 Gut
          0.1, 12 Schlecht
"""
a=float(sys.argv[1])

print "a=%f, a*0.1*10. == a:" % a,a*0.1*10.==a
print "a=%f, 0.1*a*10. == a:" % a,0.1*a*10.==a
print "a=%f, 0.1*10.*a == a:" % a,0.1*10.*a==a

print "10*0.1==1.:",10.*0.1==1.
