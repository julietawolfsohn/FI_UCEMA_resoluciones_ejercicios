#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$"
    if re.search(patron,string) is not None:
        return "Patron encontrado"
    else:
        return "Patron no encontrado"

#$ --> simoboliza el finde la linea
#+ --> una o mas veces
#_ --> string guion bajo