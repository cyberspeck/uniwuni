# Berechne die Flaeche von verschiedenen 2D-Figuren
# Lösung mit Klassen

# Möglichst allgemeine Definition einer Basisklasse
class figure:
# --------------------------------------- 
 # -> Konstruktor heisst in python __init__(self,...)
    def __init__(self,name): 
        # Vorläufig hat die Figur zur Unterscheidung nur einen Namen 
        self.__name=name
        self.Eigenschaft='rund'
# --------------------------------------- 
     def flaeche(self):
         # Eine Methode zur Berechnung der Fläche
         # Da wir noch nicht wissen wie die Figur aussieht
         # Macht diese Methode noch gar nichts
         pass
# --------------------------------------- 
     def wie_heisst_du(self):
         # Noch eine Methode zum Ausgeben des Namens
         print self.__name
# --------------------------------------- 


f=figure("Unbekannt")
f.wie_heisst_du()
print f.flaeche(), f.Eigenschaft



