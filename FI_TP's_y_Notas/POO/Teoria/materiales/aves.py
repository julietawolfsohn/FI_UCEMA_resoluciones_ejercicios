class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if (self.energia - (10 + kms)) < 1:
      return "no puede volar"
    else: 
      self.energia -= 10 + kms

  def esta_feliz(self):
    return self.energia > 50
  
  def esta_en_equilibrio(self):
    if self.energia >=150 or self.energia <=300:
      return "esta en equilibrio"
    else:
      return "no esta en equilibrio"
    


class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

 #es un metodo
 #la funcion no esta dentro de una clase y el metodo si lo esta 
 
  def esta_feliz(self):
    return self.energia > 500
  

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)