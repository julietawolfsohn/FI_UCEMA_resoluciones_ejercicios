#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras

#!/bin/python3

import glob, os, sys

def frecuencia_palabras(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        cantidad_palabras = {}
        for palabra in palabras:
            if palabra in cantidad_palabras:
                cantidad_palabras[palabra] += 1
            else:
                cantidad_palabras[palabra] = 1
        for elemento in cantidad_palabras:
            cantidad_palabras[elemento] /= len(palabras)
        return cantidad_palabras