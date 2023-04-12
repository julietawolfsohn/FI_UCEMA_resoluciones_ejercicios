#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

#la primer letra del patron tiene que ser P y lo que siga tiene que ser 0 o caracteres especiales (CREO)


import re
def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())

