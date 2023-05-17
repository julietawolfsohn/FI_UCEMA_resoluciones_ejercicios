#TEORIA
"""Al utilizar SUPER en el método de una subclase, se evalúa el método con el mismo nombre 
de su superclase y además lo que se está redefiniendo. Por ejemplo:"""

class Saludo:
  def saludar(self):
    return "Buen día"

class SaludoDocente(Saludo):
  def saludar(self):
    return super().saludar() + " estudiantes"
"""De esta forma, al enviar el mensaje saludar a SaludoDocente, 
super invoca el método saludar de su superclase, 
Saludo y agrega la particularidad de SaludoDocente sumando " estudiantes". """

mi_saludo = SaludoDocente()
mi_saludo.saludar()
"Buen día estudiantes"

#---------------------------------------------------------------------------------------
from colectivo import MedioDeTransporte
class Colectivo(MedioDeTransporte):
  def __init__(self):
    super().__init__(100)
    self.pasajeros = 0
  def entran_personas(self, pasajeros):
    return self
  def cargar_combustible(self, cantidad_combustible):
    super().cargar_combustible(cantidad_combustible)
    self.pasajeros=0