#!/bin/python3

with open("mi nombre.txt", "a") as mi_arch:
    mi_arch.write("Julieta Wolfsohn")

#Armar un script que lea el archivo 'mi_arch.txt' y me arme otro archivo 'nuevo_arch.txt' con los primeros 5 caracteres del archivo que hicimos 
"""
with open("un_archivo.txt", "r") as mi_arch:
    with open ("nuevo_archivo.txt", "a") as nuevo:
        nuevo.write(mi_arch.readline(5))
"""

texto_leido = open("un_archivo.txt", "r").read()
texto_para_escribir = texto_leido[0:6]
           
with open("nuevo_archivo.txt", "a") as mi_arch:
    mi_arch.write(texto_para_escribir)

