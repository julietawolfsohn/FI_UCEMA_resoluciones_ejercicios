class Chef:
  def __init__(self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
    
  def picantear(self):
      try:
        self.plato_del_dia.ser_picanteado()
      except Exception as e:
        raise Exception ("El plato ya está demasiado picante")
    
class AyudanteDeCocina:
  def suavizar(self, plato):
      plato.ser_suavizado()
    
    
class Pasta:
  def __init__(self):
    self.ajies = 0
    
  def ser_picanteado(self):
    if self.ajies > 10:
      raise Exception ("El plato ya está demasiado picante")
    self.ajies += 5
    
  def ser_suavizado(self):
    self.ajies -= 1
    
    
class Pizza:
  def __init__(self):
    self.condimento = "adobo"

  def ser_suavizado(self):
    self.condimento = "orégano"
    
  def ser_picanteado(self):
    if self.condimento == "cayena":
      raise Exception ("El plato ya está demasiado picante")
    self.condimento = "cayena"