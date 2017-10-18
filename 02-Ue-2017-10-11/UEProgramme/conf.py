#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

CONF={'anz':{'max':3000,'min':1,'typ':int}, 
   'start':{'max':300,'min':4,'typ':float},
   'ende':{'max':3000,'min':4,'typ':float}
   }
KEYS=CONF.keys()
MESSUNG=[]

#print sys.argv
fp=open(sys.argv[1],"r")
lines=fp.readlines()
fp.close()

for l in lines:
#     print l
     if l.strip()[0]=='#': continue
     t1=l.split("=")
     t=[x.strip() for x in t1]
     print t
     if t[0] in KEYS:
        #print t[0]
        v=CONF[t[0]]['typ'](t[1])
        print v
        if v>CONF[t[0]]['max']:
	   print t[0],"zu gross"
	   sys.exit(0)  
     else:
       print t[0],"nicht gefunden"
       sys.exit(0)
