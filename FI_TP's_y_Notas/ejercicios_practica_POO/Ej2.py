#Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

#NO ME DEJA PRINTIAR
#esta hecho en la carpeta de POO (aves y main)

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if (self.energia <= 0

  def esta_feliz(self):
    return self.energia > 50

pepita = Golondrina
