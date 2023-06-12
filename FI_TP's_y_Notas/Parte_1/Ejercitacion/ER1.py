#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re
#1
def caracter_permitido(string):
    patron = ".+[a-zA-Z0-9]"
    if re.search(patron, string):
        return "Hay un carcater permitido"
    else:
        return "No lo hay"

print(caracter_permitido("!!!==="))

#2
import re
def caracteres_permitidos(string):
    return bool(re.search('[a-zA-Z0-9]',string))

print(caracteres_permitidos("Julieta"))