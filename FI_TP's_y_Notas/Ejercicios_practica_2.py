#EJ 1
#Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control" y le agregue el string "revisado" y le quite el elemento "control".

#!/usr/bin/env/python3

lista = ["mora", "control", "juli"]

def palabra (lista):
    if "control" in lista:
        lista.remove("control")
        lista.append("revisado")
    return lista
    
print(palabra(lista))

#EJ 2 
#Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.

def elemento (lista2):
    lista2.pop(0)
    return lista2
lista2= ["atun", "lapiz", "cuaderno", "papel"]
print (elemento(lista2))

#EJ 3 
def ejercicio3(lista3, palabra):
    if palabra in lista3:
        return lista3.index(palabra)

lista3= ["salmon", "arroz", "alga", "panizado"]

print(ejercicio3(lista3, "salmon"))

