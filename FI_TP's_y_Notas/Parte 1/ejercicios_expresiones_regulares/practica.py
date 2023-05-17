#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
import re
def obtener_substrings(string):
    patron = (".\w[@&]$")
    return re.findall(patron, string)
    
print(obtener_substrings("@julilamas123&"))

def get_substr(string):
    return re.findall("[@|&](.*?)[@|&]", string)


#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

import re
def reemplazar_caracteres(string):
    patron = r"\W+"
    return re.sub(patron, "_", string, 2)

print(reemplazar_caracteres("juli  #?123"))

#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

import re 
def palabras_unidas(string):
    patron = r"\s"
    return re.findall(patron, string)

print(palabras_unidas("juli_wolfsohn"))


#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

import re 
def string_con_caracteristicas(string):
    patron = ".[\sa-zA-Z0-9]$"
    if re.search(patron, string) is not None:
        return "encontro"
    else:
        return "no encontro" 


print(string_con_caracteristicas("Juli la 1"))
print(string_con_caracteristicas("Juli_gana!"))
print(string_con_caracteristicas("Juli gana"))


