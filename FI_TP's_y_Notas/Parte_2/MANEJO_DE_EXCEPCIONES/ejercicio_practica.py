#Desafio II: Creá una función denominada eneavo que tenga como argumento un número e imprima el resultado de la división de 1 por ese número
#Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except

def eneavo(numero):
    try:
        print(1/numero)
    except ZeroDivisionError:         #agregar que tipo de error va a ser -- tipo si aparece el tipo de error que dije que me aparezca lo otro
        print("No se puede dividir por", numero)
    except TypeError:
        print("")
eneavo(9)
eneavo(0)

