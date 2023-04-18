#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
#NO TOMA BIEN LOS DOS PRIMEROS CARACTERES -- COMO HAGO?
import re
def cambiar_primeros_caracteres(string):
    patron = "[\W{2}]"
    return re.sub(patron, "__", string)

print(cambiar_primeros_caracteres("Hola 015?? Juli"))
