"""Escribir un script en el cual debemos movernos a la carpeta Informes y obtener los archivos *.txt que hayan allí. 
Por cada archivo hay que obtener, por un lado, cuántas veces aparece la palabra "estado" y por otro lado la cantidad de líneas. 
Por último, hay que crear una carpeta que se llame Apellidos, donde hay que crear un archivo llamado Lista.txt que contenga en 
cada línea la primer línea de cada archivo .txt obtenidos anteriormente."""

import os, sys, re, glob


os.chdir("Documentos/Informes")
textos = glob.glob("*.txt")

def buscar_palabra(archivo, palabra):
    re.findall("estado", palabra)

os.mkdir("Documentos/Apellidos")


