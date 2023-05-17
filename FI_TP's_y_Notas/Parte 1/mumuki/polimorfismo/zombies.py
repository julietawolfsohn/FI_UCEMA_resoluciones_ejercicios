class Zombi:
  def __init__(self, hambre):
    self.hambre = hambre 

  def sabe_correr(self):
    return self

  def es_un_peligro(self):
    return self.hambre >50

  def recibir_danio(self, hambre):
    self.hambre -= hambre * 2


class SuperZombi:
  def __init__(self, hambre):
    self.hambre = hambre

  def sabe_correr(self):
    return self

  def es_un_peligro(self):
    return self

  def recibir_danio(self, hambre):
    self.hambre -= hambre 

  def regenerarse(self):
    self.hambre = 100

class Sobreviviente:
  def __init__(self, adrenalina):
    self.adrenalina = adrenalina 
    
  def atacar(self, contrincante):
    if not contrincante.es_un_peligro():
      self.recibir_danio = self.adrenalina/2 
      contrincante.recibir_danio(self.recibir_danio)
      self.adrenalina += 20
      return "ataque exitoso"
    else:
      raise Exception ("Es peligroso atacar a este zombi")
    
class PlantaCarnivoraZombi:
  def __init__(self, clorofila):
    self.clorofila = clorofila
    
  def es_un_peligro(self):
    return self.clorofila > 40
    
  def hacer_fotosintesis(self,minutos):
    self.clorofila += minutos
    
  def recibir_danio(self, clorofila):
    self.clorofila -=10