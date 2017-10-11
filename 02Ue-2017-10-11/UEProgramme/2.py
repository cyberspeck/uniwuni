#! /usr/bin/python
# -*- coding: utf-8 -*-
# Die erste Zeile (Kommentar # gefolgt von !)
# bestimmt den Interpreter von dem die nachfolgenden
# Anweisungen interpretiert werden sollen
# In unserem Fall der python-Interpreter
# Linux: Das Programm kann direkt von der Kommanozeile aufgerufen werden
#        "chmod u+x Dateiname" vorher nicht vergessen! 

# Weitere komplexere Datentypen
# Listen
# Eine Liste ist eine geordnete Ansammlung von Objekten beliebigen Datentyps
# Sie werden durch [...] begenzt und können durch einen Index angesprochen werden.
# Unterschied zu Feld (Array) in anderen Programmiersprachen
l=[2,1.4,"Text",[1,2,3]]
print l

# for-Schleifen
# Schleifen und Listen stehen in einer Beziehung
# Man spricht auch von iterierbaren Objekten (iterables)
# Die Anweisungen der for-Schleife sind eingerückt!
print "For-Schleife 1:"
for e in l: # e durchläuft der Reihe nach alle Elemente del Liste l
    print e
# Mit hilfe der range-Funktion kann ein Index generiert
# werden, um z.B. eine Schleife mittels Index zu durchlaufen
# wie z.B. in C oder Fortran
print "For-Schleife range:"
for i in range(len(l)):
   print i,l[i]  
print "l[3][2]=",l[3][2]
# Für Listen-Objekte gibt es bereit viele vordefinierte
# Methoden um mit ihnen bequem arbeiten können
# Siehe z.B. pydoc list

# Strings -> Zeichenketten
# Eine Zeichenkette wird entweder durch einfache (') oder
# doppelte (") Anführungszeichen eingeschlossen. Nicht mischen!
s='irgend was'
s="irgend was"
s="Das ist ein einfaches Anführungszeichen (')"
s='Das ist ein doppeltes Anführungszeichen (")'

print "Strings:"
s="    qwertzui        \n"
# Strings können inder sogenannten slice-schreibweise
# bearbeitet werden.
# s[a:b] vom Index a bis zum Index b
# Dabei kann entweder a oder b weggelassen werden.
# Wird a weggelassen, so ist der erste Index (a=0)
# Wird b weggelassen, so ist b der letzte Index
# Negative Indizes werden vom Ende weggezählt
# s[-1] ist das letzte Zeichen, s[-2] das vorletzte.
#
# Das alles gilt auch für Listen !!!
# 
a=s[5:-5]
print s,a
print s[:9]
print s[9:]
#print s
print "strip:",s.strip()
# Für strings gibt es viele Funktionen, die den Umgang erleichtern
# Siehe z.B. pydoc list
#
# z.B. die strip-Methode entfernt whitespace oder andere 
# Zeichen vom Anfang und Ende einer Zeichenkette
# a="   Eine Zeile meines Texts   \n"
# a.strip() ->  "Eine Zeile meines Texts"
# z.B. die split-Methode spaltet eine Zeichenkette nach Trennzeichen auf
# "1,2,3,4".split(",") -> ["1","2","3","4"] (Liste)

s=" 3.5    4.6  1  7.5e12\n"
print "Zwischenschritt:",(s.strip()).split()
fz=[float(z) for z in s.strip().split()]
# Ergebnis: Liste von flaot-Zahlen
# " 3.5    4.6  1  7.5e12\n".strip(): Entferne jeden "white space" vorne und hinten
# -> "3.5    4.6  1  7.5e12".split() -> splitte nach Leerzeichen
# -> ["3.5", "4.6", "1", "7.5e12"]
# -> float(z) verwandle die Zeichenkette in eine float-Zahl
# -> [3.5, 4.6, 1, 7.5e12]
print fz

# Alternative Möglickeit: Suksessives Erweitern einer Liste
# l.append(x)
# Hängt das Objekt x an die Liste l an
fz=[]
for e in s.strip().split():
   print fz
   fz.append(float(e))

print fz






