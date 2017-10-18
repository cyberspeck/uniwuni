import sys

# Auslösen einer exception im Programm
# Das Programm soll beendet werden, wenn
# beiden float-Zahlen, die als Kommanozeilenargumente
# übergeben werden, gleich sind.
z1=float(sys.argv[1])
z2=float(sys.argv[1])
if z1==z2:
   #raise ValueError("Argumente gleich: %s" % sys.argv[1])
   print "Argumente gleich: {}"format(z1)
   sys.exit(0)
#   
print sys.argv
