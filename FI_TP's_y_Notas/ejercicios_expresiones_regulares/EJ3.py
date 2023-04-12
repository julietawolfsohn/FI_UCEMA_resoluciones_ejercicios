#Creá un programa que verifique las siguientes condiciones:


#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de cero o una e.

#si un string dado tiene una h seguida de dos o tres e.

#A
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

#si quiero que me agarre la h y la e tengo que ponerlo = "(he)*"
# El caracter que usemos somo afecta a lo que tengamos a la izquierda

#B
def encontrar_patron(string):
    patron = "he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
#C
def encontrar_patron(string):
    patron = "he?"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
print(encontrar_patron("a")) #no se cumple
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeee"))

#se puede hacer una unica busqueda por patron
#no sirve hacer "he*?" --> porq ? no estraia actuando sobre nada

#D
def encontrar_patron(string):
    patron = "he{2,3}"   #es lo que deberia hacer (2 - es el minimo pero puede tener 3 o mas porq no aclaramos hasta cuando)
    if re.search(atron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

print(encontrar_patron("he"))  #no lo encuentra
print(encontrar_patron("heeeey")) #lo encuentra