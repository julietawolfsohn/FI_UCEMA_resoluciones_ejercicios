"""Ya conocimos tres tipos de colecciones: las listas, los diccionarios y los sets. 
Solo nos queda uno por descubrir, las tuplas. 
Las tuplas son similares a las listas pero tienen una particularidad, son inmutables. 
En criollo, las tuplas no se pueden modificar por lo que:

- no podemos agregarles ni quitarles elementos;
- no podemos modificar el valor de sus elementos.
Es por este motivo que las tuplas se utilizan en aquellos casos donde
quisiéramos usar una lista pero ya sabemos de antemano cuántos y qué elementos va a tener."""

#Las tuplas se pueden representar de tres formas:

tupla_1 = ("Violeta", "Amarillo")
tupla_2 = "Naranja", "Azul"
tupla_3 = tuple((22, 22, True))

#--------------------------------------------------------------------------
"""Definí en la clase Persona, el método iniciales que nos retorne una tupla con la 
primera letra del nombre, la primera letra del segundo nombre y la letra del apellido.
"""

class Persona:
  def __init__(self, un_nombre, un_segundo_nombre, un_apellido):
    self.nombre = un_nombre
    self.segundo_nombre = un_segundo_nombre
    self.apellido = un_apellido

  def iniciales(self):
    return (self.nombre[0], self.segundo_nombre[0], self.apellido[0])

borges = Persona("Jorge", "Luis", "Borges")
borges.iniciales()
("J", "L", "B")