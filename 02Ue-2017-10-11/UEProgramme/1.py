# -*- coding: utf-8 -*-
# Die erste Zeile bestimmt das "encoding" des Zeichensatzes
# (in unserem Fall UTF8). Wichtig bei Kommentaren und Textausgabe
# Wird sie weggelassen dürfen in Kommentaren und Textvariablen
# nur ASCII-Zeichen verwendet werden (keine Umlaute!)
#
# 1. Programm
# Die Einrückung spielt eine wesentliche Rolle in python
# und muss penibel eingehalten werden.
# Aufruf des Programms von der Kommandozeile:
# python Dateiname
#
# Variablen werden einfach zugewiesen
# Ein Datentyp wird vorher nicht deklariert,
# er ergibt sich aus dem Typ des r-Werts
# integer (keine Längenbeschränkung)
a=5   # Zuweisung
i=int("6")
i=int(5)

# float -> double
f=5.
g=5E0

# String (Zeichenkette)
b="12345" 

#Ausgabe auf stdout - Bildschirm
print "Ergebnis:",a,b,i,f,g

# Bedingte Anweisung
# Keine Klammern, endet mit Doppelpunkt
# Die Einrückung definiert den if-Block
if i==5:
    print "i ist 5"
    g=99.
elif i==4:
    print "Ich bin 4"
else:
    print "nicht 5 und auch nicht 4"

print g
# Variablen-Typen können beliebig im Programmablauf geändert werden
b=3.2
print "b=",b

