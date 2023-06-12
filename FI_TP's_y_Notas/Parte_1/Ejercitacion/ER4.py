#Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
def cuenta_de_mail(string):
    patron = "[a-zA-Z0-9]@[a-z].com]"
    return bool(re.search(patron, string))

print(cuenta_de_mail("julietasolw1@gmail123.com"))

import re
def validar_email(mail):
    return bool(re.search('^\w+[.-_]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?', mail))



