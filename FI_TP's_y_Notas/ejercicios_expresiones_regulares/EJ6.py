#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
#(PORQUE NO FUNCIONA?)
import re
def lista_string(frase):
    if re.search("[a, b]", frase):
        return "Estan en la frase"
    else:
        return "No estan en la frase"

print(lista_string("juli comio"))

import re
def string_en_frase(frase):
    return bool(re.search("[a, m]", frase))
frase="budin"
print (string_en_frase(frase))