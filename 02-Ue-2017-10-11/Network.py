from time import *
import sys

fp=open("/proc/net/dev","r")  #Lesen des aktuellen Empfangswerts in Bytes
data=fp.readlines()

fp.close()
em2=data[3].split()
start=em2[1]


while 1:				#Bilden der Differenz der Werte
	fp=open("/proc/net/dev","r")
	data=fp.readlines()

	fp.close()			
	em2=data[3].split()	
	akt=em2[1]
	diff=int(akt)-int(start)
	start=akt
	sleep(1)
	print ("Die Empfangenen Daten in Byte/s: {}".format(diff))




