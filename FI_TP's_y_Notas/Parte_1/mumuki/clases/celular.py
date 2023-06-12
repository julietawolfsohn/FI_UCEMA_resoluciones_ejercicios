class Celular:
  def __init__(self, una_bateria, un_saldo, el_sistema_operativo):
    self.bateria = una_bateria
    self.saldo = un_saldo
    self.sistema_operativo = el_sistema_operativo
    
  def tiene_bateria_maxima(self):
    return self.bateria == 100
  
  def cargar_a_tope(self):
    self.bateria = 100
    
  def necesita_saldo(self):
    return self.saldo <= 0
  
  def cargar_saldo(self, un_saldo):
    self.saldo += un_saldo