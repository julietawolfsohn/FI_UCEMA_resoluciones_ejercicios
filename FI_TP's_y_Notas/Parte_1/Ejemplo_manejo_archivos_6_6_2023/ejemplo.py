import re, os, glob

# archivos tienen extensión: .txt, .dat, .py, .csv
# carpetas no tienen extensión

# glob
textos = glob.glob("*.txt") # guarda en una lista todos los archivos que terminan en .txt
datos = glob.glob("*.dat") # guarda en una lista todos los archivos que terminan en .dat

# os
os.mkdir("Documentos/Parcial1")
os.chdir("Documentos/Parcial1")

# hacen cosas

os.chdir("../..")


# Abrir archivos
with open(archivo, "modo") as variable:
    pass

#forma 1
with open("Documentos/Parcial1/ejercicio1.txt", "r") as entrada:
    mi_archivo = entrada.read()
    entrada.readline()
    lineas = entrada.readlines()

    for linea in entrada:
        print(linea)
        
    pass

with open("Documentos/Parcial1/ejercicio2.txt", "w") as entrada:
    pass

with open("Documentos/Parcial1/ejercicio3.txt", "a") as entrada:
    pass

#forma 2
os.chdir("Documentos/Parcial1")
with open("ejercicio1.txt", "r") as entrada:
    pass

with open("ejercicio2.txt", "w") as entrada: # si no existe ejercicio2.txt, lo crea. Si existe, lo sobreescribe.
    pass

with open("ejercicio3.txt", "a") as entrada: # si ya existe ejercicio3.txt, agrega cosas. Si no existe, lo crea.
    pass




