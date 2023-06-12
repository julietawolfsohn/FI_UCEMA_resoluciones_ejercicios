#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
#!/usr/bin/env/python3 
import os, glob, sys


def cant_palabras(nombre_archivo):
   with open(nombre_archivo, "r") as archivo:
      contenido = archivo.read()
      lista = contenido.split()
      return len(lista)

def cuantas_palabras(nombre):
   with open(nombre, "r") as archivo:
      return len(archivo.read().split())
   
print(cant_palabras("ejemplo.txt"))
print(cuantas_palabras("ejemplo.txt"))