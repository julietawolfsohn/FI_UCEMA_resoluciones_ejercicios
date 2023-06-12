#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
import glob, os, sys

def salto_de_1inea(nombre_archivo, nombre_archivo_nuevo, letra):
    with open(nombre_archivo, "r") as entrada, open(nombre_archivo_nuevo, "w") as salida:
        contenido = entrada.read ()
        conenido_modificado=contenido.replace(letra, letra + "In")
        salida.write(conenido_modificado)

def reemplazar (nombre, letra, archivo_nuevo):
    with open (nombre,"r") as entrada, open(archivo_nuevo,"a") as salida:
        salida.write(entrada.read().replace(letra, letra + "In"))

("ejemplo modificado.txt" "°")
("ejemplo_nuevamente_modificado.txt")