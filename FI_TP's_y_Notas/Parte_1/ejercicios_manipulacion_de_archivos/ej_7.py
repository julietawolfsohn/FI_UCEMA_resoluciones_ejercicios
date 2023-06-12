#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

#!/bin/python3

import glob, os, sys

def palabra_mas_larga(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        palabra_larga = ""
        for palabra in palabras:
            if len(palabra) > len(palabra_larga):
                palabra_larga = palabra
        return "La palabra mas larga es ´" + palabra_larga + "´, que tiene " + str(len(palabra_larga)) + " letras." 

def palabra_mas_largaa(nombre):
    with open(nombre, "r") as archivo:
        palabra_larga = ""
        for palabra in archivo.read().split():
            if len(palabra) > len(palabra_larga):
                palabra_larga = palabra
    return "La palabra mas larga es ´" + palabra_larga + "´, que tiene " + str(len(palabra_larga)) + " letras."