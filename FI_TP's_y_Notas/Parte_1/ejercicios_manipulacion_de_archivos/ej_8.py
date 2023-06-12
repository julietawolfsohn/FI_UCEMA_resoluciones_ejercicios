#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

#!/bin/python3

import glob, os, sys

def sumar_documentos(documento1, documento2, archivo_a_sumar):
    with open(documento1, "r") as doc1, open(documento2, "r") as doc2, open(archivo_a_sumar, "a") as salida:
        contenido1 = doc1.read()
        contenido2 = doc2.read()
        salida.write(contenido1 + contenido2)

def sumar_info(doc1, doc2, doc3):
    with open(doc1, "r") as arch1, open(doc2, "r") as arch2, open(doc3, "r+") as arch3:
        arch3.write(arch1.read() + arch2.read())

sumar_documentos("ejemplo.txt", "ejemplo_modificado(ej6).txt", "ejemplo_modificado.txt")