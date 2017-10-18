# Übergabe von Kommanozeilenargumenten mit sys.argv
import sys

print sys.argv
z=int(sys.argv[3])
s="{:7d} {:x} argv[0]: {}".format(z,z,sys.argv[0])
print s
