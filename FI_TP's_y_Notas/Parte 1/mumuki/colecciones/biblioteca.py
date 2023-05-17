class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if libro not in self.libros:
          self.libros.append(libro)
    
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

biblioteca_de_emma = Biblioteca()

autor_contacto = {"nombre": "Carl", "apellido": "Sagan", "nacionalidad": "Estados Unidos"}
contacto = Libro("Contacto", 400, "Ciencia ficción", autor_contacto)
biblioteca_de_emma.agregar_libro(contacto)

autor_socorro = {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina"}
socorro = Libro("Socorro", 250, "Terror", autor_socorro)
biblioteca_de_emma.agregar_libro(socorro)
