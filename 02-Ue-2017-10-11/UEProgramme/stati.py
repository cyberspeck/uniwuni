from types import *
import sys
from math import *

class statistic(list):
   """ Statistische Funktionen
   """
   def __init__(self,l):
      """ Konstruktor
      """
      if type(l)==StringType:
         fp=open(l,"r")
	 l=fp.readlines()
	 fp.close()
	 nl=[]
	 for i in l:
	  if i.strip()[0]=='#':continue
	  nl.append(i)
	 l=nl
      elif type(l)!=ListType:
           raise ValueError("l must be a filename or a list")
	    
      list.__init__(self,[float(x) for x in l])
# -----------------------------------------------
   def mean(self):
       mw=sum(self)/len(self)
       s=0.
       for i in self:
          s+=(mw-i)**2
       return mw, sqrt(1./(len(self)-1)*s)
# -----------------------------------------------
   def __add__(self,l):
       if type(l)==ListType:
          return [a+b for a,b in zip(self,l)]
       elif type(l)==FloatType or type(l)==IntType :
          return [a+l for a in self]
       else:
          raise TypeError("Nur Liste oder Zahl erlaubt")
 # -----------------------------------------------
   def __repr__(self):
      s=""
      for i in self:
          s+="%12.5g, " % i
      return s.strip().strip(',')
     
if __name__=='__main__':
  d=statistic([1.1,2.2,3.3,4.4])
  print d,str(d)

  mw=d.mean()
  print "mw:",mw[0],'sigma:',mw[1]

  for i in d:
      print i
      
      
  d1=statistic(['2.13',2,4])
  print d1.mean()

  d2=statistic('a.dat')
  print d2.mean()


  l=[1.1,2.2,3.3,4.4]
  x=statistic(l)
  print d+l

  print d+5

  d2=statistic('a.dat')
  print d2.mean()
#print sys.stdin
