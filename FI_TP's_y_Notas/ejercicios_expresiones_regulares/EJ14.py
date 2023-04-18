#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

import re
def remplazar(string):
    patron = "[\s\t]"
    return re.sub(patron, ";", string)

print(remplazar("que divertido  que es eso"))