import re, os, glob

# Movernos a la carpeta Datos
# Obtener los nombres de los archivos .txt
# Abrir cada txt y leerlo con read()
# Buscar y guardar los mails en cada .txt
# Movernos a la carpeta inicial
# Crear la carpeta Resultados
# Movernos a la carpeta Resultados
# Crear el archivo mails.txt
# Escribir la información de los mails en ese archivo

def mails(carpeta_entrada, carpeta_salida, archivo_salida):
    os.chdir(carpeta_entrada)
    txts = glob.glob("*.txt")
    lista_mails = []
    for txt in txts:
        with open(txt, "r") as texto:
            mi_archivo = texto.read()
            lista_mails += re.findall(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}", mi_archivo)
            # lista_mails = lista_mails + re.findall(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}")

    os.chdir("../../")
    os.mkdir(carpeta_salida)
    os.chdir(carpeta_salida)
    with open(archivo_salida, "a") as salida:
        for mail in lista_mails:
            salida.write(mail + "\n")

# ejecutando el procedimiento:
mails("Datos/Enero", "Resultados", "mails.txt")


# Nombres de personas que tengan un apellido que empiece con H:
#"\w{2,12}\sH\w{1,15}"
#"[a-zA-Z]{2,12}\sH[a-zA-Z]{1,15}"
