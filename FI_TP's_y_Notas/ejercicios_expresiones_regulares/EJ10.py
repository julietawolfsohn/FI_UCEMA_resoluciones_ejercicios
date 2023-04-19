#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &


import re
def get_substr(string):
    return re.findall("[@|&](.*?)[@|&]", string)

print(get_substr("@hola mora & @juli"))

#listo
#porque esta dos veces ([@|&])
#([@|&]) que tome todas las veces que aparece estos caracteres y escriba solo los substrings en el medio