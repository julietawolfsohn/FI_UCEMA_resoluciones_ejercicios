#Realizá un programa que validar si una cuenta de mail está escrita correctamente.

#!/usr/bin/env/python3 

import re
def validar_email(mail):
    return bool(re.search('^\w+[.-_]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?', mail))

print(validar_email("julietasolw@gmail.com"))
print(validar_email("mora123..@gmail1.com"))
    
#en vez de poner \w --> se puede poner[a-z][0-9] y los simbolos/caracteres (que ya esta arriba)