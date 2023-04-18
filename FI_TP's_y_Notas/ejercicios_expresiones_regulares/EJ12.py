#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

"""import re
def reemplazar(ocurrencia):
    patron = "[" ", "_", ":"]"
    return re.sub(patron, "|", ocurrencia)

print(reemplazar("Hola soy_ Juli, como es tu nombre:"))"""


import re
def reemplazar(ocurrencia):
    patron = "[ _:]"
    return re.sub(patron, "|", ocurrencia)

print(reemplazar("Hola soy_ Juli, como es tu nombre:"))

