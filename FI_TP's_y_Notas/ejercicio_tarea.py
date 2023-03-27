#¡Desafío final! Creá un script swap.py que tome dos nombres de archivo y renombre al primero con el nombre del segundo, y al segundo lo renombre con el nombre del primero. Ejemplo:

import os

file1 = "hola.txt"
file2 = "chau.txt"

os.rename(file1, "temporal")
os.rename(file2, file1)
os.rename("temporal", file2)

#modificar este script para incorprar el nombres de los archivos desde la terminal 