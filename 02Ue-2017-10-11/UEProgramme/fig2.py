

class figure:
# --------------------------------------- 
 def __init__(self,name):
   self.name=name
# --------------------------------------- 
 def flaeche(self): pass
# --------------------------------------- 
 def wie_heisst_du(self): print self.name
# --------------------------------------- 

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


f=figure("Unbekannt")
f.wie_heisst_du()
print f.flaeche()


q=quadrat()
q.wie_heisst_du()
q.par_eingabe()
print q.flaeche()







