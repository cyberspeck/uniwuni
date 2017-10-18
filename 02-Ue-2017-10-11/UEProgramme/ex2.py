# Exception
# Bei jedem Fehler wird in python eine "exception" ausgelöst
# " Eine einfache Demo-Funktionen

def Ratio(a,b):
    return a/b

# Durch try ... except statements
# wird auf das Auftreten verschiedener Exception geprüft
try: 
   z=Ratio(5,"abcd")
except ZeroDivisionError:
   print "0-Fehler"
   z=0
except:
  print "anderer Fehler"
  sys.exit(0)

# Tritt keine exception auf wird hier fortgesetzt
print z
# -------

