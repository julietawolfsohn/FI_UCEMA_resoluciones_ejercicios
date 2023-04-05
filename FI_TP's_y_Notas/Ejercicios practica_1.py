"""def ayp(numero):
    return numero +1, numero -1
print (ayp (2))

def doble_numero (numero):
    return numero*2
print (doble_numero (2))

def ayps(numero):
    return (numero +1)*2,(numero -1)*2
print (ayps(7))"""
#link ejercicio https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_de_introducci%C3%B3n_a_Python_Parte1.md
#ej1
def siguiente(num):
    return num +1
print (siguiente(6))
#ej1
def anterior(num):
    return num -1
print (anterior(6))
#ej2
def doble(num):
    return num*2
#ej3
def doble2(num):
    return str(doble(anterior(num))) + ' ' + str(doble(siguiente(num)))
print(doble2(2))
#ej4 (opcion1)
def retirar_dinero(saldo, monto):
    while saldo > monto:
        return saldo - monto
    else: 
        saldo < monto
        return 0
print (retirar_dinero(10,2))
#ej4 (opcion2)
def retirar_dinero1(saldo, monto):
    return max(saldo-monto, 0)
print(retirar_dinero(10, 2))
#ej5
def dia_de_la_semana_favorito (dia):
    return dia == "Sabado" 
print(dia_de_la_semana_favorito("Sabado"))
print (dia_de_la_semana_favorito("Lunes"))


#ej11
#opcion 1
def funcion (palabra):
    if palabra.startswith("H"):
        return len(palabra)
print (funcion("Hola"))
print (funcion("Juli"))

#opcion 2
def funcion (palabra):
    if str.startswith(palabra, "H"):
        return len(palabra)
print (funcion("Hola"))
print (funcion("Juli"))

#opcion3
def empieza_con_H(palabra):
    if palabra[0]== "H":
        return len(palabra)
    else:
        return "la palabra no empieza con H"
print (empieza_con_H("Hola"))
print (empieza_con_H("Buenos dias"))

#ej12 (opcion1)
def funcion1 (palabra):
    if str.startswith(palabra, "Buenas") or str.startswith(palabra,"Buenos"):
        return True
    else: 
        return False
print (funcion1("Buenos dias"))
print (funcion1("Soy Juli"))

#opcion2
def funcion1 (palabra):
    return str.startswith(palabra, "Buenas") or str.startswith(palabra,"Buenos")

print (funcion1("Buenos dias"))
print (funcion1("Soy Juli"))

#ej6
"""
#ej6 -- (porq esta mal?) y como es la funcion max?
def long_radio (onda):
    return onda in min(223) or onda in max(586)
print (long_radio(250))
"""
#porque no puedo usar la coma?
rango_longitud = range(223,586)
def long_onda (longitud):
    return longitud in rango_longitud
print (long_onda(250))
print (long_onda(660))

#ej7
def long_de_la_onda(longitud):
    return longitud in rango_longitud and not longitud == 314
print (long_de_la_onda(250))
print (long_de_la_onda(314))
print (long_de_la_onda(660))

#ej8
def tiene_descuento (edad):
    return edad<=12 or edad>=60
print (tiene_descuento(15))

#ej9 (CHEQUEAR SI NO HAY UNA FORMA MEJOR O SI EL XOR ESTA BIEN USADO)
def xor(A,B):
    return A == True and B == False or B == True and A == False 
print (xor(True, False))
print (xor(False, False))
print (xor(False, True))
print (xor(True, True))

#ej10
def saludo (nombre, apellido):
    return "Hola" + " " + nombre + " " + apellido + " " + "bienvenida al grupo"
print (saludo("Juli", "Wolfsohn"))

#ej13
def es_multiplo (n1, n2):
    return n1%n2 == 0
print (es_multiplo (5, 10))
print (es_multiplo (6, 3))

#ej14
def funcion(numero):
    if numero%2 == 0 and not numero == 0:
        return "es par"
    elif numero%2 != 0:
        return "es impar"
    else:
        return "es cero"
print (funcion(4))
print (funcion(5))
print (funcion(0))

"""
#ej15 (COMO SE HACE? NO ME SALE)s
def cuantas_a_A (frase):
    contar = 0
    for a in frase or A in frase:
        return contar + A or a
print (cuantas_a_A("A cuantas cuadras estamos"))

def cuantas_a(frase):
    for a or A in [frase]:  
"""

#ej15
frase = "Soy MoraaaaA"
MiLetra= "a" """LA A MAYUSCULA"""
contador = 0

for letra in frase:
    if letra == MiLetra:
        contador += 1
print(("La letra " + MiLetra + " se repite " + str(contador) + "veces"))

#ej16 (NO ME SALE)
def dinero(dinero_por_mes):
    pesos_por_mes == 60000
    if pesos_por_mes == 60000
        return 1
    else:
        return dinero_por_mes


