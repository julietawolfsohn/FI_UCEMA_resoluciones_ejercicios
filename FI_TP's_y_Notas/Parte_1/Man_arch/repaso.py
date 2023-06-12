import re, os, glob

"""glob"""
textos = glob.glob("*.txt") #lleva entre comillas algo que vos estas queriendo buscar

# * -- siganifica cualquier cosa
# "*" -- devolveme una lista de todo lo que hay en la lista
# "*.txt" -- guarda en una lista todos los archivos que terminan con .txt
# DEVUELVE LA LISTA DE LOS NOMBRES

"""os"""
os.mkdir("Documentos/Parcial1")
#es para crear carpetas

os.chdir("Documentos/Parcial1")
# para moverme a una carpeta, no a un archivo
os.chdir("../..") # para volver 2 carpetas para atras

#abrir archivos y leerlos

with open(archivo, "modo") as variable:
    
    # archivo = ruta a la cual quiero seguir/abrir
    
#forma 1
with open("Documentos/Parcial1/ejercicio1.txt", "r") as entrada:
    pass

#forma 2 - MEJOR FORMA
os.chdir("Documentos/Parcial1") #movernos en carpetas
with open("ejercicio1.txt", "r") as entrada: #leer los archivos
    mi_archivo = entrada.read()
    entrada.readline()
    entrada.readlines() #me gusrada todo el archivo en una lista donde cada elemnto va a ser una linea 
    
    pass

with open("ejercicio2.txt", "w") as entrada: # si no existe, lo crea, si existe lo sobreescribe (te borra lo que hay y te agrega lo nuevo)
    pass
    
with open("ejercicio3.txt", "a") as entrada: # si ya existe agrega cosas, y si no existe lo crea
    pass                                     #GENERALMENTE CONVIENE USAR ESTO
    