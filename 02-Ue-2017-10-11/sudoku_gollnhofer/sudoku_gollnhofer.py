from copy import deepcopy
input=open("sudoku_schwer916.txt", "r")
list=[]
oldlist=[]
einsneun=[1,2,3,4,5,6,7,8,9]
i=0
z=0
for int in input:		
	list.append(int.split())
	i=i+1

#del list[7]
#del list[3]
oldlist=deepcopy(list)
for z in range(9):
	for s in range(9):
		if oldlist[z][s]=="0":
			oldlist[z][s]="."

for i in range(0,9):		
	for j in range(0,9):
		if list[i][j] == "0":
			list[i][j]=[1,2,3,4,5,6,7,8,9]

block=[]	
			
for z in range(0,7,3):	#block befuellen, BZW liste wird eindimensional, aber blockweise
	
	for s in range(0,7,3):
		for blockZ in range(z,z+3):
			for blockS in range(s,s+3):
				#b=list[blockZ][blockS]
				block.append(list[blockZ][blockS][:])
input.close()

"""
Bis hierher nur Befuellen von list und block
Jetzt kommen Definitionen:
"""
def BlockAktl():

	block=[]	
			
	for z in range(0,7,3):	#List auf block schreiben
	
		for s in range(0,7,3):
			for blockZ in range(z,z+3):
				for blockS in range(s,s+3):
					block.append(list[blockZ][blockS])
"""
def ListAktl():
	list=[]
	for liob in range(0,81,9)
		for z in range(i,i+2)
			for s in range(i,i+2)
					list[z][s]=block[i]
					i=i+1
l[0][0]=block[0]
list 01=block[1]
list10=block[3]
"""

def ZeilenStreichen():
	for z in range(9):			#Checken der Zeilen
		for s in range(9):
			if len(list[z][s]) == 1:  #Wenn die Zahl schon fix ist continue
					continue
			for zi in range(len(list[z][s])):     #zi fuer Position der Ziffer in den unsicheren Listen
					a=list[z][s][zi]
					for it in range(9):			  #it iteriert die Spalten durch
							if len(list[z][it]) > 1:   #Wenn das Feld noch nicht fix ist continue
								continue
							b=list[z][it][0]
							c=float(b)
							if a == c: 					
								list[z][s][zi]=0
def SpaltenStreichen():			#Analog zu ZeilenStreichen
	for s in range(9):			  #s fuer Zeile
		for z in range(9):		  #z fuer Spalte
			if len(list[z][s]) == 1:  #Wenn die Zahl schon fix ist continue
				continue
			for zi in range(len(list[z][s])):     #zi fuer Position der Ziffer in den unsicheren Listen
				a=list[z][s][zi]
				for it in range(0,9):			  #it iteriert die Zeilen durch
						if len(list[it][s]) > 1:   #Wenn das Feld noch nicht fix ist continue
							continue
						b=list[it][s][0]
						c=float(b)
						if a == c: 					
							list[z][s][zi]=0
def BlockStreichen():						#BlockStreichen
	for liob in range(0,81,9):			#liob ist linkes oberes Feld der Bloecke
		for blockiter in range(liob, liob+9):   
			if len(block[blockiter])==1:		
				continue
			for ititer in range(len(block[blockiter])): 	
				a=block[blockiter][ititer]	
				for bit in range(liob, liob+9):
					if len(block[bit])>1:
						continue
					#if len(block[bit])==1:
					#	if block[bit] is not int:
					#		block[bit]=str(block[bit][0])
							#print ("Sicher Zahl im Block ", bit, block[bit][0])
					b=block[bit][0]
					c=float(b)
					
					if c==a:
						block[blockiter][ititer]=0
"""
def NullenStreichen():		#Streichen der Nullen in Liste
	z=0
	s=0

	for z in range(9):			
		for s in range(9):
			if len(list[z][s])==1:
				continue
			while 0 in list[z][s]:
				try:	
					list[z][s].remove(0)
					#list[z][s].remove("0")
				except:
					pass
			if len(list[z][s])==1:			#Wenn Zahl sicher: list to string
				list[z][s]=str(list[z][s][0])
				print("nullenstreichen sicher ", z,s, list[z][s][0])
"""
def NullenStreichen():
	z=0
	s=0	
	for i in range(81):
		if len(block[i])==1:
			block[i]=str(block[i][0])
			continue
		while 0 in block[i]:
			try:
				block[i].remove(0)
			except:
				pass
def NurEineZahlZeile():	
	for i in range(1,10):
		for z in range(9):			#zeilen checken ob eine zahl nur einmal vorkommt
			a=0	
			b=0
			for sublist in range(9):
				if len(list[z][sublist])==1:
					continue	
			
				a=a+list[z][sublist].count(i)
			if a==1:
				for j in range(9):
					if len(list[z][j])==1:
						continue	
					b=list[z][j].count(i)
					if b==1: 						
							list[z][j]=str(i)							#einzelne zahlen in der liste werden sicher
def NurEineZahlSpalte():	
		for i in range(1,10):
			for s in range(9):			#spalten checken ob eine zahl nur einmal vorkommt
				a=0	
				b=0
				for z in range(9):
					if len(list[z][s])==1:
						continue	
			
					a=a+list[z][s].count(i)
			if a==1:
				for j in range(9):
					if len(list[j][s])==1:
						continue	
					b=list[j][s].count(i)
					if b==1: 
							list[j][s]=str(i)		#einzelne zahlen in der liste werden sicher
def Frage():  #ist das Sudoku geloest
	count=0
	for z in range(9):
		for s in range(9):
			if len(list[z][s])>1:	
				return (0)			
			if len(list[z][s])==1:
				count=count+1
				if count==81:
					print ("Das Soduku ist geloest!!")
					return (1)
				
			
			
	
		
	return ("solved")
def NurEineZahlBlock():
	for i in range(1,10):
		for liob in range(0,81,9):
			a=0	
			for blockiter in range(liob, liob+9):
				puffer=block[blockiter][0]
				if len(block[blockiter])==1:	
					if str(puffer)==str(i):
						a=a+1				
						continue
					continue
				a=a+block[blockiter].count(i)
			if a==1:
				for j in range(liob, liob+9):
					if len(block[j])==1:
						continue	
					b=block[j].count(i)
					if b==1: 
							block[j]=str(i)		
def BlockToList():
	for i in range(81):
		Block=(i-(i%9))/9
		BlockPos=i-(i-(i%9))
		if Block<3:
			liobz=0
		if Block in range (3,6):
			liobz=3
		if Block in range (6,9):
			liobz=6
		if Block%3==0:
			liobs=0
		if Block%3==1:
			liobs=3
		if Block%3==2:
			liobs=6
		if BlockPos<3:
			list[liobz][liobs+BlockPos]=block[i]
		if BlockPos in range(3,6):
			list[liobz+1][liobs+(BlockPos%3)]=block[i]
		if BlockPos in range(6,9):
			list[liobz+2][liobs+(BlockPos%3)]=block[i]
"""
Start of Program (until here only definitions of functions)
"""
def Durchlauf():
	ZeilenStreichen()
	NullenStreichen()
	SpaltenStreichen()
	NullenStreichen()
	BlockAktl()
	BlockStreichen()
	NullenStreichen()
	BlockToList()
	NullenStreichen()
	NurEineZahlZeile()
	NullenStreichen()
	NurEineZahlSpalte()
	BlockAktl()
	NurEineZahlBlock()
	BlockToList()
for i in range(1000):
	Durchlauf()
	end=Frage()
	if end==1:
		break
print("Die Angabe:")
for i,j in enumerate(oldlist):
	print (i,j)
print("Die Loesung:")
for i,j in enumerate(list):
	print (i,j)
