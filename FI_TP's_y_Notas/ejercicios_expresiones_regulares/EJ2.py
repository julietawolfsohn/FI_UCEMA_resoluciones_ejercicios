#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
#(no me da bien) - PREGUNTAR    
import re
def caracteres_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9]",string))

print(caracteres_permitidos("Julieta"))


# No me puede dar True si por ejemplo pongo b --> osea seria adentro de los parentesis true pero con el not bool se hace false 

def caracteres_permitidos1 (string1):
    caracteres_ok = "a" "z" "A" "Z" "0" "9"
    return caracteres_ok in string1
print(caracteres_permitidos1("Julieta"))

#si no tiene todo lo que yo le indique te devuelve False
