#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números
import re
def contenga(string):
    patron = ".[a-zA-Z0-9\s]$"
    if re.search(patron, string) is not None:
        return "Encontro"
    else:
        return "No encontro"

print(contenga("Juli la 1"))
print(contenga("Juli_gana!"))
    