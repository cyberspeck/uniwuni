# Iteration durch mehrere Listen mit zip
l=[1,2,3,'wert',3.14,(0,1)]
l1=[7,2,3,'wert',3.14,(0,1),{'edv':5,'mathe':5}]
l2=[9,2,3,'wert',3.14,(0,1),{'edv':5,'mathe':5}]

for a, b, c in zip(l,l1,l2):
   print a,b,c
