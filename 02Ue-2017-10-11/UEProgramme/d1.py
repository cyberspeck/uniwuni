# Definiert ein dictionary:
# key: string oder int -> Value
# Schlüssel - > Wert: Kann alles sein
# Wie Wörterbuch
d={'a':1234, 'b':[1,4,'ert'], 'zz':'Text'}

# Auf die einzelnen Werte wird zugegriffen
# in dem man den key in eckigen Klammern angibt
d['f']={}

# Iteration durch ein dictionary mit keys()
for k in d.keys():
    print k,"->",d[k]print d['a']

#d['b']=7
print d
print d['b'][1]

# Iteration durch ein dictionary mit iteritems
for k, v in d.iteritems():
    print k,v

