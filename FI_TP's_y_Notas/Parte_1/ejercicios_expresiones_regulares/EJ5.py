#Escribí un programa que diga si un string empieza con un número específico.
#VER COMO HACERLO
def empieza_con_num(string, numero):
    return string.startswith(numero)
    
print(empieza_con_num("0juli", "2"))


import re
def empieza_con_numero(string, numero):
    patron = "^" + str(numero)
    if re.search(patron, string) is not None:
        return "Emipieza con el numero"
    else:
        return "No empieza"
    
print(empieza_con_numero("5juli", "5"))

#me devuelve un bool
def numero_especifico(string, numero):
    return bool(re.search("^" + str(numero), string))

print(numero_especifico("45julijuli", "5"))