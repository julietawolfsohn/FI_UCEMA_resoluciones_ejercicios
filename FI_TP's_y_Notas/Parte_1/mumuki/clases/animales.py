class Caballo:
  def __init__(self, una_energia, una_raza):
    self.energia = una_energia
    self.raza = una_raza

  def comer(self, gramos):
    self.energia += gramos*2 

  def galopar(self, kms):
    self.energia -= kms

class Golondrina:
  def __init__(self, una_energia, una_ciudad):
    self.energia = una_energia
    self.ciudad = una_ciudad

  def comer(self, gramos):
    self.energia += gramos /2

  def volar_hacia(self, una_ciudad):
    self.energia /=2 
    self.ciudad = una_ciudad 

class Gato:
  def __init__(self, una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad
    
  def comer(self, gramos):
    self.energia += gramos
    
  def cumplir_anios(self):
    self.edad += 1 