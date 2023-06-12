# Escribir funciones que, dado un String, permitan responder lo siguiente:

# a) obtener la lista de los substrings delimitados entre '<' y '>' que no incluyan ninguna 'o'.

# b) Onomatopopih, que aún no sabe mucho de expresiones regulares,
# nos mandó una función que debería ser capaz de decirnos si un string incluye o no un substring de 3 letras,
# cada una de las cuales debe ser a, b ó c. Esto es, alcanza con incluir, p.ej, 'abc', 'cbc', 'aac', 'ccc'.

# En base a la función que definió respondé:
"""
delimitados_piquitos_sin_o("ds<hola>hsb<hhj>sdk<469>nkd")
"""
# ¿Qué error/es tiene? (justificando la respuesta).
"""
Los errores que tiene es que no indica en ninguna parte que el sub sting tiene que ser de 3 letras y tambein cuales son esas letras.

"""

# Uno de los errores esta en el patron, el metacaracter {3} solo influye en la c; y tampoco da lugar a que haya match con las 3 letras en otro orden
# Tendria que usar re.search para que la funcion nos diga SI INCLUYE O NO el substring. Con el findall, si la funcion esta escrita correctamente, devolvera la lista de coincidencias. 

# Modificá la función para que cumpla lo requerido correctamente.



#A
import re
def lista_substrings(string):
    patron = "<([^o]*?)>"   #el . significa todos los caracteres 
    return re.findall(patron, string)


print(lista_substrings("river<el mejor de la historia> por siempre<juli>"))

#B opcion 1
import re
def triples(string1):
    patron = "abc{3}"
    return re.findall(patron, string1)

triples("svsslkvabckjsv")

#opcion 2
def triples_correcta(string):
    print(bool(re.search("[a-c]{3}", string)))

triples_correcta("svsslkvkjabcuhjv")
triples_correcta("svsslkvkjbbcuhjv")
triples_correcta("svsslkvkjabuhjv")
triples_correcta("svssalkvbkjcuhjv")
