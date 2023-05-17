#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

import glob, os, sys

def imprimir_ultimas_lineas(nombre_archivo, n_lineas):
    with open(nombre_archivo, "r") as archivo:
        lista_de_lineas = []
        for linea in archivo:
            lista_de_lineas.append(linea)
    return lista_de_lineas[-n_lineas:len(lista_de_lineas)+1]

def ultimas_lineas(nombre, numero):
    with open(nombre, "r") as archivo:
        return archivo.readlines()[-numero:]
    
print(imprimir_ultimas_lineas("ejemplo.txt", 3))   #el txt esta hecho aparte que es donde hay muchas cosas y me lee la info de ahi