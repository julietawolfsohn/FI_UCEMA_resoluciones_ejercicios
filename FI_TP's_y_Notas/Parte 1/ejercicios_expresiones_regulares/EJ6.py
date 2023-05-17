#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

import re
def esta_en_lista(frase):
    lista=["arbol", "fideos"]
    for elemento in lista:
        if elemento in frase is not None:
            return bool (re.findall(elemento, frase))
        
print(esta_en_lista("mora come empanadas"))




















