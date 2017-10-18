#Aufgabe:
# Die Flaeche von allen Figuren (fuer beliebige Parameter),
# die in diesem Modul vorkommen berechnen
# Am besten mit einer Schleife

from string import *
from math  import *
import sys

# --------------------------------------- 
def Rechteck(a,b):
  return a*b
# --------------------------------------- 
def Quadrat(a):
  return a**2
# --------------------------------------- 
def Kreis(r):
  return r**2*pi
# --------------------------------------- 
def Ellipse(a,b):
  return a*b*pi
# --------------------------------------- 

if __name__=='__main__':
  # Parameterliste
  # Rechteck, Quadrat, ...
  pl=[(2,3),(4,),(2.3,),(2,3),(pi/4,)]
  # Funktionsliste; ja eine Liste kann auch Funktionen enthalten
  fl=[Rechteck,Quadrat,Kreis,Ellipse,sin]

  # Ausgabe der beiden Listen zur Kontrolle
  # Die beiden Listen sollten gleich lang sein
  # und die einzelnen Werte aus der Parameterliste zu den Funktionen
  # aus der Funktionsliste passen
  # Rechteck -> 2. Parameter, Quadrat -> 1 Parameter, ...
  print pl,fl

  # Es gibt nun viele Möglichkeiten, um die Listen durchzugehen
  # und dia Parameter an die jeweilige Funktion zu übergeben
  print "1****"
  for i,f in enumerate(fl):
      print apply(f,pl[i])
      # apply übergibt eine Parameterliste als tuple (2.Parameter)
      # an eine Funktion (1.Parameter)      
     

  print "2****"
  for i,f in enumerate(fl):
     print f(*pl[i])
     # Der Stern vor dem Parameter bedeutet:
     # übergib die gesamte Parameterliste als tuple an die Funktion

  print "3****"
  # Übergabe mit zip und apply
  for f,p in zip(fl,pl):
      print apply(f,p) 

  funk=Rechteck
  print funk(5.6,7.8)
  print Rechteck(5.6,7.8)
 





