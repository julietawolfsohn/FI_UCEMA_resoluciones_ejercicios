class MedioDeTransporte:
  def __init__(self, combustible):
    self.combustible = combustible

  def entran_personas(self, cantidad_personas):
    return cantidad_personas <= self.maximo_personas()

  def cargar_combustible(self, cargar_combustible):
    self.combustible += cargar_combustible


class Auto(MedioDeTransporte):

  def maximo_personas(self):
    return 5

  def recorrer(self, kilometros):
    self.combustible -= kilometros /2

class Moto(MedioDeTransporte):

  def maximo_personas(self):
    return 2

  def recorrer(self, kilometros):
    self.combustible -= kilometros

class Colectivo(MedioDeTransporte):
 
  def __init__(self):
    self.pasajeros = 0
    self.combustible = 100
    
  def entran_personas(self, cantidad_personas):
    return cantidad_personas

Colectivo=MedioDeTransporte
