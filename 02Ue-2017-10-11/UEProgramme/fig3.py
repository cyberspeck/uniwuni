

class figure:
 __name=None
# --------------------------------------- 
 def __init__(self,name):
   self.name=name
# --------------------------------------- 
 def flaeche(self): pass
# --------------------------------------- 
 def wie_heisst_du(self): print self.name
# --------------------------------------- 
 def __repr__(self):
    return self.name
 
class quadrat(figure):
 def __init__(self):
    figure.__init__(self,"Quadrat")
    self.a=None
#----------------------------------------------
 def flaeche(self): return self.a*self.a
#----------------------------------------------
 def par_eingabe(self):
     s=raw_input("Seite: ")
     self.a=float(s)
#----------------------------------------------

class rechteck(figure):
 def __init__(self):
    figure.__init__(self,"Rechteck")
    self.l=None
    self.b=None
#----------------------------------------------
 def flaeche(self): return self.l*self.b
#----------------------------------------------
 def par_eingabe(self):
     s=raw_input("Laenge: ")
     self.l=float(s)

     s=raw_input("Breite: ")
     self.b=float(s)
#----------------------------------------------
print rechteck

for i in [quadrat,rechteck]:
  q=i()
  print q
  q.wie_heisst_du()
  q.par_eingabe()
  print "Flaeche:",q.flaeche()


