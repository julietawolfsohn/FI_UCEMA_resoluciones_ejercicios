#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

import os, sys, re, glob

def lineas_sin_letra(archivo, letra):
    contador = 0
    with open(archivo, "r") as miarch:
        for linea in miarch.readlines():
            if not linea.startswith(letra):
                contador += 1
    return contador

print(lineas_sin_letra("ej1.txt", "a"))