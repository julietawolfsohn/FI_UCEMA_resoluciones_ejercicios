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
#Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.
def ejercicio3(lista3, palabra):
    if palabra in lista3:
        return lista3.index(palabra)

lista3= ["salmon", "arroz", "alga", "panizado"]

print(ejercicio3(lista3, "salmon"))

#EJ 4 (CHEQUEAR xq me da none)
#Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el elemento de una lista y agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?
def agrego_y_saco(pal1,pal2,comida):
    if comida in pal1:
        pal1.remove(comida)
        pal2.append(comida)
    elif comida in pal2:
        pal2.remove(comida) and pal1.append(comida)

pal1= ["Huevo", "Lechuga", "Tomate"]
pal2= ["Carne", "Pollo", "Pesacdo"]
   
print(agrego_y_saco(pal1,pal2,"Torta"))


#EJ 5 (VER xq me da none)
#Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], la función debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.
def numeros_par_o_impar(numeross):
    for elemento in numeross:   
        if elemento % 2 == 0:
            return lista_final.append(True)
    else:
        return lista_final.append(False)
    
numeross = [2, 45, 108, 12, 7]
lista_final = []
print(numeros_par_o_impar(numeross))

#EJ 6 (VER)
#Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

"""lista4 = ["Lucas", "Juli", "Male"; "Sebi"]

def caracter(lista4, letra):
    if caracter in lista4:
        return letra + "aparece en el diccionario"
    
print(caracter(lista4,"L"))"""

#EJ 7 (hacer cuando haga el 6)
#Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.


#EJ 8 (VER)
#Definir una función que dada una palabra, nos diga si el palíndromo o no.
"""def palindromo_si_no(palabr):

    if palabr.startwith(letra) and palabr.endswith(letra):
        return "es palindromo"
    
print(palindromo_si_no(anana))"""

#EJ 9
#Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.
def productoria(lista_numeros2):
    resultado2 = 1
    for nu in lista_numeros2:
        resultado2 *= nu
    return resultado2
lista_numeros2 = [2,2,2]
print(productoria(lista_numeros2))

#EJ 10 (FALTA HACER)
 