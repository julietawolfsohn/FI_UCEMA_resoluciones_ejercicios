#Escribí un programa que separe y devuelva los caracteres númericos de un string

# \D --> caracter no numerico

import re

def extraer_numeros(string):
    resultado = re.split("\D+", string)
    for elemento in resultado:
        print(elemento)

print(extraer_numeros("Hola mundo"))

#si hago "Hola Mundo".split(" ") --> me va a dar una lista ["Hola", "Mundo"]
