#Definir el ´procedimiento que lea los archivos .txt que estan en la carpeta marzo, y copie la primera linea de cada uno en un archivo dentro de la carpeta resultados(debe estar adentro de new)
#new - datos - adentro de los meses(ej marzo) y buscar lo que me pide de esos txt 

#!/usr/bin/env/python3 
import os, glob, sys

def primeras_lineas(path_a_txt, path_resultados, salida):
    os.chdir(path_a_txt)
    textos = glob.glob("*.txt")
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
          primer_linea.append(texto.readline())  
          
    os.chdir("../../") #me estoy moviendo 2 archivos para atras
    os.mkdir(path_resultados) #creo la carpeta de resultados pero todavia no tengo ningun archivo
    os.chdir(path_resultados) #ya me estoy moviendo a esta carpeta
    with open(salida, "a") as final_txt:       #"a" porq le vamso a ir agregando cosas #salida es un parametro 
        for linea in primer_linea:
            final_txt.write(linea)
    
primeras_lineas("datos/marzo", "resultado", "salida.txt")   #solo modifico el argumento (marzo) cuando lo invoco  

"""
  primeras_lineas("../../resultados") #se trata de no hacer esto para qur el usuario no tenga que poner estos movimientos hacia atras de los path 
""" 
    
    #movernos a marzo
    #extraemos los .txt
    #leemos las primeras primeras_lineas
    #hacemos carpeta de salida (resultados)
    #hacer archivo (salida.txt)
    #poner lineas en archivo nuevo
    
    