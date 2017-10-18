

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
if __name__=='__main__':

 f_dict=[{"bez":"rectangle","obj":rechteck},{"bez":"square","obj":quadrat}]


 s=raw_input("Your figure? ")
 found=None

 for i in f_dict:
     if i['bez']==s:
 	found=1
 	break

 if found:
   r=i['obj']()
   r.wie_heisst_du()
   r.par_eingabe()
   print r.flaeche()
   print r
 else:
   print s, "does not exist"
