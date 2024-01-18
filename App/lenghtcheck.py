aktuellerString = "Dummy Output soll noch <sfhhes kjsiufh <dfi<sf kjld<fi<soi dlj<hfgoei<s hdf<gdusgfzug gfzugrufug"
gewünscheLänge = 50
anfrageanSystem = False

if len(aktuellerString) > gewünscheLänge:
    output = "Die Daten des Outputs sind zu lang. Bitte kürze den Output auf "+ str(gewünscheLänge) + " Zeichen. Behalte dabei alle Informationen bei: +++" + aktuellerString  +"+++"
    anfrageanSystem = True
else:
    output = aktuellerString  
    anfrageanSystem = False

''' Hie müsse weder der call an das LLM hin oder das Ergebnis zurückgegebenwerden basierend auf der Boolean Variable anfrageanSystem '''

print(output)