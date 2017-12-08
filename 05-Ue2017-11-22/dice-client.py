# -*- coding: utf-8 -*-
""" StatistikProgramm mit Entropieberechenung, Mittelwert und Standardabweichung und Detektion der ZinkungRandomness Generator von David Blacher, Christopher Gollnhofer, Johannes Kurz """
import string
import numpy as np
import socket, sys


def connect(port, host):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	except(socket.error, msg):
		s = None
	try:
		s.connect((host,port)) # Verbinden
	except(socket.error, msg):
		s.close()
		s = None
	if s is None:
		print('Can not open socket {}'.format(msg))
		sys.exit(1)
	return s

    
wuerfe = 10000000
port = 56700
host = 'localhost'
modi = [0, 1, 2, 3, 4, 5, 6, 71, 10, 11, 12, 13, 80, 20, 21, 22, 23, 100, 90, 70]

if len(sys.argv) != 2:
	print("Usage: {} würfe(int)".format(sys.argv[0]))
	message = "help"
else:
	wuerfe = string.atoi(sys.argv[1])

Ewert = np.zeros(len(modi))
Entropie = np.zeros(len(modi))
Varianz = np.zeros(len(modi))
StdAbw = np.zeros(len(modi))

for z in range(len(modi)):
    
    print ("Würfel Nr: {}".format(modi[z]))
    s = connect(port, host)
    message = "throw {} {}".format(wuerfe, modi[z])
    s.send(message+"\r\n") #\r\n ist der Zeilenumbruch in Windows
    
    # lesen der Antwort
    data = ""
    while 1:
        d= s.recv(9192)
        if len(d) == 0: break
        data += d

    s.close()
    #print('Received:\n {}\n\n'.format(data))
    
    if message == "help": sys.exit(0);
    
    data = data.strip()
    augen = []
    
    for d in data:
        augen.append(int(d))
    # throw enthält alle Würfe als Liste

    eins_sechs=[0,0,0,0,0,0,0]		#[0] ist Zaehler fuer Einser usw. [6] ist Gesamtzeahler
    probs=[]
    for i in range(len(augen)):
    	puffer=int(augen[i])
    	eins_sechs[puffer-1]=eins_sechs[puffer-1]+1  #counter der einzelnen Zahlen
    	eins_sechs[6]=eins_sechs[6]+1				#Gesamtcounter
    for i in range(6):
    	probs.append(float(eins_sechs[i])/eins_sechs[6])  #Berechnugen der rel.Haeufigkeiten in probs
    for i in range(1,7):
    	Ewert[z]=Ewert[z]+i*probs[i-1]		#Erwartungswert
    for i in range(1,7):
        if probs[i-1] != 0:	Entropie[z]=Entropie[z]-np.log2(probs[i-1])*probs[i-1]		#Entropie
    for i in range(1,7):
    	Varianz[z]=Varianz[z]+probs[i-1]*np.power((i-Ewert[z]),2)		#Varianz, Standardabweichung
    	StdAbw[z]=np.sqrt(Varianz[z])
    
    print ("Entropie:{}".format(Entropie[z]))
    print ("Erwartungswert:{}".format(Ewert[z]))
    print ("Varianz:{}".format(Varianz[z]))
    print ("Standardabweichung:{}".format(StdAbw[z]))
    print ("Einzelne Wahrscheinlichkeiten: {}\n".format(probs))

varianz_die = (1./6)*( np.power((3.5-1),2) + np.power((3.5-2),2) +  np.power((3.5-3),2) +  np.power((3.5-4),2) +  np.power((3.5-5),2) +  np.power((3.5-6),2) )
stdabw_die = np.sqrt( varianz_die )
print( "Würfel mit StdAbw am nächsten zu echtem Würfel (1.707825127659933...): {}".format(modi[( np.power( (StdAbw - stdabw_die),2 ) ).argmin()]) )
print( "Würfel mit Erwartungswert am nächsten zu 3.5: {}".format(modi[( np.power( (Ewert - 3.5),2 ) ).argmin()]) )
print( "Würfel mit maximaler Entropie: {}".format(modi[( Entropie ).argmax()]) )


