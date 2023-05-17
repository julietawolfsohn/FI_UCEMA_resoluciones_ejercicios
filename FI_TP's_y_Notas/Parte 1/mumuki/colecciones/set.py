"""Hasta acá usamos dos tipos de colecciones, las listas y los diccionarios. 
Ahora vamos a conocer los sets (en castellano conjuntos).

Los sets son muy parecidos a las listas, pero tienen dos particularidades 
que los diferencian:

- no tienen elementos repetidos;
- sus elementos no están ordenados."""

class Biblioteca:
    def __init__(self):
        self.libros = set()

    def agregar_libro(self, libro):
        self.libros.add(libro)
    
    def libros_largos(self):
        libros_largos = [libro for libro in self.libros if libro.es_largo()]
        return libros_largos

    def titulos_disponibles(self):
        return [libro.titulo for libro in self.libros]
      
      
class Libro:
  def __init__(self, titulo, paginas, genero, autoria={"nombre": "Desconocido", "apellido": "Desconocido", "nacionalidad": "Desconocida"}):
        self.titulo = titulo
        self.paginas = paginas
        self.genero = genero
        self.autoria = autoria
        
    
    
  def es_largo(self):
    if self.paginas > 300:
      return True
    
  def nacionalidad (self):
    return self.autoria["nacionalidad"]