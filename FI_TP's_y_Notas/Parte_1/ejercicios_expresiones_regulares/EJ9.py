#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

import re

def entre_guiones(string):
    return re.findall(r"-(.*?)-",string)

string = "Hoy estuvimos trabajando con re -regular expression-en Python - con VSCode-"
print(entre_guiones(string))

#search/find --> devuelven solo lo que pediste
#findall --> devuelve una lista
#. --> significa cualquier tipo de caracter
