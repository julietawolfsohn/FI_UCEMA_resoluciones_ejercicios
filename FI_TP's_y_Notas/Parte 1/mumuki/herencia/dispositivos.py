class Dispositivo:
  def __init__(self,bateria):
    self.bateria = bateria
    
  def tiene_bateria(self):
    return self.bateria >20

  def cargar_a_tope(self):
    self.bateria = 100

  def tiene_bateria_maxima(self):
    return self.bateria == 0   
    
  def sin_carga(self):
    return not self.tiene_bateria()  

class Notebook(Dispositivo):
  
  def utilizar(self, minutos):
    self.bateria -= minutos

  
class Tablet(Dispositivo):

  def utilizar(self, minutos):
    self.bateria -= minutos/2