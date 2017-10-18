# -*- coding: utf-8 -*-
# Formatierte Ausgabe von Objekten (Zahlen)
f=3.1415956467
# Zahl wird auf eine intern definierte Anzahl
# von Vor- und Nachkommastellen ausgegeben
print f
# 
i=2345
# Erstellt eine Zeichenkette mit formatierter Ausgabe
# %...f, %...i formatierte Ausgabe von float, int-Zahlen
# Siehe printf in C
# Die Reihenfolge der Formatangabe und der Variablen ist relevant!
s= "pi = %.2f, i=%07d" % (f,i)
print "Formatiert:",s
print "%f (pi)" % f
# format-Methode:
print "format-methode: {:.2f}".format(f)
# Die Ausgabe eines jeden Objekts wird durch {name:format}
# beschrieben. name oder format oder beides können optional
# weggelassen werden, dann werden Vorgabewerte verwendet 
print "Zahl1 {z1:.2f}   Zahl2 {z2:}".format(z2=f,z1=0.5)

# Mutable - veränderbare Objekte
# z.B. Listen
l=[1,5,9,0,"abc"]
print l
# Einzelnes Objekt der Liste l kann beliebig verändert werden
l[4]=8
print l

# Inmutable - unveränderbare Objekte
# z.B. Strings, Tuple

s="Abcdef"
#s[0]="a" # -> Fehler
# Ein String ist ein fest vorgegebenes Objekt und kann nicht
# verändert werden. Anstatt dessen muss eine neues Objekt erstellt werden
s1="a"+s[1:]
print s1
s="Z"+s[1:] # Auch das ist möglich
print s
# Tuple -> ähnlich Liste nur unveränderlich
t=(1,4,"wertz")
print t
t[0]=3.1



