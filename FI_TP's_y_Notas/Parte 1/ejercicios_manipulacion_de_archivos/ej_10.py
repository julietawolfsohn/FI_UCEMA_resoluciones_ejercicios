#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

#!/bin/python3

import glob, os, sys

def juntar_archivos_txt(carpeta):
    path_carpeta = os.path.dirname(carpeta)
    carpeta_destino = os.path.join(path_carpeta, "Resultado")
    if not os.path.exists(carpeta_destino):
        os.mkdir(carpeta_destino)
    nombre_archivo = "resultado.txt"
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
    with open(ruta_archivo, "w") as archivo_resultado:
        for archivo in glob.glob(os.path.join(path_carpeta, "*.txt")):
            with open(archivo, "r") as archivo_lectura:
                archivo_resultado.write(archivo_lectura.read())


print(juntar_archivos_txt("practica_MANIPULACION_ARCHIVOS"))