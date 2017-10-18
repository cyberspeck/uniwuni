#! /usr/bin/python
#-*- coding: utf-8 -*-

# Importieren von Modulen
#   from math import *
# Die einzelnen Objekte aus dem Modul math
# werden mit dem entsprechenden Namen aufgerufen
# z.B.  a=sqrt(3.13)
# Nachteil: Wenn in verschiedenen Modulen Objekte mit gleichen Namen
#           enthalten sind
# z.B.  a=sqrt(complex(1.,1.))  
# Alternative
#   import math
# Die einzelnen Objekte aus dem Modul math
# werden mit math.Name aufgerufen
# z.B.  a=math.sqrt(3.13)
# Falls grosse Objekte importiert werden müssen uns Speicherplatz knapp ist:
#   from math import sqrt 
# Falls die Module lange komplizierte Namen haben:
#   import mein_verflixt_kompliziertes_modul as mvc 

import math,sys

# Lesen und schreiben auf Dateien
fp=open("a.dat","r")# -> Öffnen der Datei zum Lesen
data=fp.readlines() # -> Einlesen in Liste, jede Zeile ein Element
fp.close()          # -> Schließen der Datei

print data

# Umwandeln des Texts aus der Datei in eine Liste von float-Zahlen
zeilen_liste=[]

for zeile in data:
   #print z
   t=[float(x) for x in zeile.split()]
   zeilen_liste.append(t)
   #print t

print "zeilen_liste=",zeilen_liste
# zeilen_liste ist eine Liste von Zahlen-Listen (2D Array)
# Jede Zeile ist eine Liste von float-Zahlen
# Die gesamte Datei ist eine Liste von Zahlen-Listen

# Schreiben auf eine Datei
out=open("out.dat","w") # -> Öffnen der Datei zum Schreiben
print out
for t in zeilen_liste:                           # -> Iteration durch zeilen_liste
   #print t
   w=math.sqrt(t[1])                             # -> Berechnen der Wurzel des 2.Wertes je Zeile
   s= "{x:7.3f} {y:12.7f}\n".format(x=t[0],y=w)  # -> Ausgabe von x und y auf einen String
   out.write(s)                                  # -> Scheiben auf die Datei
   #out.write("{x:7.3f} {y:12.7f}\n".format(x=t[0],y=math.sqrt(t[1]))  # auch möglich
   #out.write(str(t[0])+"\t"+str(w)+'\n')                              # ebenso

out.close()  # -> Schließen der Datei






