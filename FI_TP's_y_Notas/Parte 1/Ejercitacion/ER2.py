#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
#(String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

import re
def extraer_caracteres(string):
    patron = r"-(.*?)-"
    return re.findall(patron, string)

print(extraer_caracteres("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))