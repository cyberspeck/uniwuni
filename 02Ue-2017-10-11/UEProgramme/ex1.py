# Exception
# Bei jedem Fehler wird in python eine "exception" ausgelöst
# Eine einfache Demo-Funktion
def Ratio(a,b):
    return a/b

# Durch try
# wird auf das Auftreten einer Exception geprüft
try:
    r=ratio("a","B")
except: # wird ausgeführt wenn eine Exception auftritt
    print "Unerlaubte Division"
    r=0
    
# Tritt keine exception auf wird hier fortgesetzt
print r




