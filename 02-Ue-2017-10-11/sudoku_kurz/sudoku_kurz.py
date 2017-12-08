#-*- coding: utf-8 -*-
import random
import sys
import os

print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print ('+++++++++++++++++++++ Sudokulöser  1.0 +++++++++++++++++++++')
print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print ('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print("\nWelches Sudoku soll geöffnet werden?")
dateiname = input()
print("\n", dateiname, " wird geöfnnet.")
sudoku_file = open(dateiname, "r")
print ("Datei ", sudoku_file.name, " wurde im ", sudoku_file.mode, " mode geöffnet.")
sudoku_input = sudoku_file.read()
print(sudoku_input)
feld = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]],[[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
zeile = []
for currentline in sudoku_input:
    zeile.append(currentline)
#print (str.split(zeile[160]))          #Tut allerletztes Besetzte stelle in zeile ausgeben
missingnumbers = 81

for y in range(0,9):
#    print("\n", end="")
    for x in range(0,9):
        feld[x][y][0]= str.split(zeile[x * 2 + 18 * y])
        feld[x][y][0] = ''.join(feld[x][y][0])
        #print(x, y)
        #print(feld)
        feld[x][y][0] = int(feld[x][y][0])
#        print(feld[x][y][0], " ", end="")
        if feld[x][y][0] != 0:
            missingnumbers = missingnumbers -1
            z = 9
            while (z > 0):
                del feld[x][y][z]
                z = z -1

print("Anzahl der fehlenden Stellen: ", missingnumbers)
#Druckt das Gesamte verbleibene Array aus:
'''
print("Anzahl der fehlenden Stellen: ", missingnumbers)
print("\n")
for y in range(0,9):
    print("\n", end="")
    for x in range(0,9):
        print(feld[x][y], " ", end="")
'''
iterations = 0
fehlerstelle = 100
while (missingnumbers > 0):
    iterations = iterations + 1
    print("Durchgang Nummer ", iterations)

    #Zeilencheck
    for y in range(0,9):
        for x1 in range(0,9):
            if feld[x1][y][0] != 0:
                c = feld[x1][y][0]
    #            print("Gefunden! (", x1 , "/", y, ") =", feld[x1][y][0])
                for x2 in range(0,9):
    #                print("x1 = ", x1)
    #                print("x2 = ", x2)
    #                print("y  = ", y)
                    if (c in feld[x2][y]) and (x1 != x2) and (len(feld[x2][y]) > 1) and (c != 0):                 #feld[x1][y] is type int
                        feld[x2][y].remove(c)                             #feld[x2][y] is type list
    if (iterations == fehlerstelle):
        print("\nAfter Zeilencheck")
        for y in range(0, 9):
            print("\n", end="")
            for x in range(0, 9):
                print(feld[x][y], " ", end="")
    #Spaltencheck
    for x in range(0,9):
        for y1 in range(0,9):
            if feld[x][y1][0] != 0:
                c = feld[x][y1][0]
    #            print("Gefunden! (", x1 , "/", y, ") =", feld[x1][y][0])
                for y2 in range(0,9):
    #                print("x1 = ", x1)
    #                print("x2 = ", x2)
    #                print("y  = ", y)
                    if (c in feld[x][y2]) and (y1 != y2) and (len(feld[x][y2]) > 1) and (c != 0):                 #feld[x1][y] is type int
                        feld[x][y2].remove(c)                             #feld[x2][y] is type list
    if (iterations == fehlerstelle):
        print("\nAfter Spaltencheck")
        for y in range(0, 9):
            print("\n", end="")
            for x in range(0, 9):
                print(feld[x][y], " ", end="")
    #Bereichcheck
    for a in [0,3,6]:
        for b in [0,3,6]:
            for x1 in range(0,3):
                for y1 in range(0,3):
                    if feld[a+x1][b+y1][0] != 0:
                        c = feld[x1][y1][0]
                        for x2 in range(0,3):
                            for y2 in range(0,3):
                                if (c in feld[x2][y2]) and (x1 != x2) and (y1 != y2) and (c != 0) and (len(feld[x2][y2]) > 1):
                                    feld[x2][y2].remove(c)
    if (iterations == fehlerstelle):
        print("\nAfter Bereichscheck")
        for y in range(0, 9):
            print("\n", end="")
            for x in range(0, 9):
                print(feld[x][y], " ", end="")
    #Fertige Zahlen um den 0 bereinigen
    for x in range(0,9):
        for y in range(0,9):
            if len(feld[x][y]) == 2:
                feld[x][y].remove(0)
                missingnumbers = missingnumbers -1
    print("\nAnzahl der fehlenden Stellen: ", missingnumbers)
    #Zeilenweise single option
    for i in range(1,10):
        for y in range(0,9):
            icounter = 0
            for x in range(0,9):
                if i in feld[x][y]:
                    icounter = icounter + 1
                    last_x = x
                    last_y = y
            if icounter == 1:
                #print("Singleoption Zeile hat was gefunden (", last_x, "/", y, ")")
                for k in range(0,10):
                    if (k in feld[last_x][y]) and (k != i) and (len(feld[last_x][y]) > 1):
                        feld[last_x][y].remove(k)
    if (iterations == fehlerstelle):
        print("\nAfter Zeilen Single Option")
        for y in range(0, 9):
            print("\n", end="")
            for x in range(0, 9):
                print(feld[x][y], " ", end="")
    #Spaltenweise single option
    for i in range(1,10):
        for x in range(0,9):
            icounter = 0
            for y in range(0,9):
                if i in feld[x][y]:
                    icounter = icounter + 1
                    last_x = x
                    last_y = y
            if icounter == 1:
                #print("Singleoption Spalte hat was gefunden (", x, "/", last_y, ")")
                for k in range(0,10):
                    if (k in feld[x][last_y]) and (k != i) and (len(feld[x][last_y]) > 1):
                        feld[x][last_y].remove(k)
    if (iterations == fehlerstelle):
        print("\nAfter Spalten Single Option")
        for y in range(0, 9):
            print("\n", end="")
            for x in range(0, 9):
                print(feld[x][y], " ", end="")
    #Bereichsweise Single Option
    for i in range(1,10):
        for a in [0,3,6]:
            for b in [0,3,6]:
                icounter = 0
                for x in range(0,3):
                    for y in range(0,3):
                        if i in feld[x+a][y+b]:
                            icounter = icounter +1
                            last_x = x+a
                            last_y = y+b
                if icounter == 1:
                 #   print("Singleoption Bereich hat was gefunden (", last_x, "/", last_y, ")")
                    for k in range(0,10):
                        if (k in feld[last_x][last_y]) and (k != i) and (len(feld[last_x][last_y]) > 1):
                            feld[last_x][last_y].remove(k)
    if (iterations == fehlerstelle):
        print("\nAfter Bereich Single Option")
        for y in range(0, 9):
            print("\n", end="")
            for x in range(0, 9):
                print(feld[x][y], " ", end="")
    missingnumbers = 0
    for x in range(0,9):
        for y in range(0,9):
            c = feld[x][y][0]
            if c == 0:
                missingnumbers = missingnumbers +1
    print("\nAnzahl der fehlenden Stellen: ", missingnumbers)
print("\n")
for y in range(0,9):
    print("\n", end="")
    for x in range(0,9):
        print(feld[x][y], " ", end="")