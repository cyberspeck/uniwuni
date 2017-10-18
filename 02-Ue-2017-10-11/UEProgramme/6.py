#! /usr/bin/python

from time import *
import sys

# Rudimentäres Beispiel 2
def get_bytes(interface):
  fp=open("/proc/net/dev","r")
  data=fp.readlines()

  fp.close()
  for z in data:
    if z.find(interface)!=-1:
      r=z.split(':')
      return int(r[1].split()[0])

# ------------------------------------
print sys.argv

interface=sys.argv[1]
b_start=get_bytes(interface)
print b_start
if not b_start:
  print "schlecht"
  sys.exit(0)

while 1:
    print 0.2*(get_bytes(interface)-b_start),"bytes/s"
    b_start=get_bytes(interface)
    sleep(5)


