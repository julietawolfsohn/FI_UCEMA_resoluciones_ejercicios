#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos. --> esta bien

import re
def cambiar_primeros_caracteres(string):
    patron = r"\W+"
    return re.sub(patron, "_", string, 2)

print(cambiar_primeros_caracteres("Hola 015?? Juli"))
