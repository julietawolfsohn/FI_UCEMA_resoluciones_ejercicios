"""
Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), 
CSSP y CSSV (como el CSS pero “pico” y “veces”). 
El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. 
El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. 
El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. 
Si un gorrión nunca comió, los coeficientes deben ser None. 
Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.
"""

class Gorrion:
    def __init__(self):
        self.kilometro = [] #una lista ya que no sabemos los valores iniciales y de esa manera va a poder identificar cual es el numero mas grande de esa lista para ver cuando fue la vez que mas comio y volo
        self.gramos = []
        #self.kilometro_actual = 0      esto podria ser para que tenga un atributo con cant total y despues otro con cada valor
        #self.gramos_actuales = 0
        
    def volar(self, km):
      self.kilometro.append(km)
        
    def comer(self, gramos):
      self.gramos.append(gramos)  
      
    def css(self):
        if self.gramos != []: #la lista self.gramos es distinta a una lista vacia?
        #if len(self.gramos) > 0: (podria ser otra opcion)
            return sum(self.kilometro) / sum(self.gramos)
        else:
            return None
        
    def cssp(self):
        if self.gramos != []:
            return max(self.kilometro) / max(self.gramos)
        else:
            return None 

    def cssv(self):
        if self.gramos != []:
            return len(self.kilometro) / len(self.gramos)
        else:
            return None
        
    def esta_equilibrio(self):
        return 0.5 < self.css() < 2 #te lee primero el 0.5 y despues entiende que es hasta 2
        return self.css
    
self.kilometro = [5, 10, 56, 124]
self.gramos = [1, 5, 40]

