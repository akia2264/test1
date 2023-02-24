#!/usr/bin/env python3
import cgi

def calculer():
    form = cgi.FieldStorage()
    nombre1 = form.getvalue('nombre1')
    nombre2 = form.getvalue('nombre2')
    
    if not nombre1 or not nombre2:
        return "Veuillez fournir deux nombres valides."
    
    try:
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)
    except ValueError:
        return "Veuillez fournir deux nombres valides."
    
    resultat = nombre1 * nombre2
    return str(resultat)

print("Content-Type: text/html")
print("")
resultat = calculer()
print(resultat)
