#!/usr/bin/env python3
import cgi

def calculer():
    form = cgi.FieldStorage()
    nombre1 = int(form.getvalue('nombre1'))
    nombre2 = int(form.getvalue('nombre2'))
    resultat = nombre1 * nombre2
    return resultat

print("Content-Type: text/html")
print("")
resultat = calculer()
print(resultat)
