#Creá un programa que verifique las siguientes condiciones:


#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de cero o una e.

#si un string dado tiene una h seguida de dos o tres e.

#A
import re
def encontrar_patron(string):
    patron = "he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
print(encontrar_patron("juu"))
print(encontrar_patron("he"))

#si quiero que me agarre la h y la e tengo que ponerlo = "(he)*"
# El caracter que usemos nos afecta a lo que tengamos a la izquierda

#B
import re
def encontrar_patron1(string1):
    patron1 = "he+"
    if re.search(patron1, string1) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
print(encontrar_patron1("hi"))
print(encontrar_patron1("hee"))


#C 
import re
def encontrar_patron2(string2):
    patron2 = "he?$"
    if re.search(patron2, string2) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
    
print(encontrar_patron2("a")) #no se cumple
print(encontrar_patron2("h"))
print(encontrar_patron2("he"))
print(encontrar_patron2("heeeee")) 

#se puede hacer una unica busqueda por patron
#no sirve hacer "he*?" --> porq ? no estraia actuando sobre nada (CHEQUEAR)

#D
import re
def encontrar_patron3(string3):
    patron3 = "he{2,3}"   #es lo que deberia hacer (2 - es el minimo pero puede tener 3 o mas porq no aclaramos hasta cuando)
    if re.search(patron3, string3) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

print(encontrar_patron3("he"))  #no lo encuentra
print(encontrar_patron3("heeeey")) #lo encuentra