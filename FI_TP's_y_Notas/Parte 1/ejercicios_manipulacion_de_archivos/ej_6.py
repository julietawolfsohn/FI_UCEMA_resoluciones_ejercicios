#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

import glob, os, sys

def eliminar_salto_linea(nombre_archivo, nombre_archivo_nuevo):
    with open (nombre_archivo, "r") as entrada, open(nombre_archivo_nuevo, "w") as salida:
        contenido = entrada.read()
        contenido_modificado = contenido.replace("\n", "")
        salida.write(contenido_modificado)

def sacar_saltos (nombre, archivo_nuevo):
    with open (nombre,"p") as entrada, open(archivo_nuevo, "a") as salida:
        salida.write(entrada.read().replace("\n",""))

eliminar_salto_linea("ejemplo modificado.txt", "ejemplo modificado (ejo). txt")