# Dictionary enthält eine u.a. eine Liste
d={'a':1234, 'b':[1,4,'ert'], 'zz':'Text'}

# Liste enthält u.a. ein Dictionary
l=[1,2,3,'wert',3.14,(0,1),{'edv':5,'mathe':5},d]

# Einfache Iteration durch die Liste
for i in l:
    print i
# Iteration mit enumerate
# Enumerate liefert bei jedem Aufruf 2 Werte: den Index und den Wert 
for i, v in enumerate(l):
    print 'Index',i,"Wert:",v

# Iteration mit range()
for i in range(len(l)):
    print i,l[i]
