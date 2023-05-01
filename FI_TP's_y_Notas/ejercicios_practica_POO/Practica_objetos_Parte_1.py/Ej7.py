#Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

class Gorrión:
    def __init__(self):
        self.kilometros_volados = 0
        self.gramos_comida_consumidos = 0
        self.max_kilometros_vuelo = 0
        self.max_gramos_comida = 0
        self.cant_vuelos = 0
        self.cant_comidas = 0

    def volar(self, km):
        self.kilometros_volados += km
        self.cant_vuelos += 1
        if km > self.max_kilometros_vuelo:
            self.max_kilometros_vuelo = km

    def comer(self, gramos):
        self.gramos_comida_consumidos += gramos
        self.cant_comidas += 1
        if gramos > self.max_gramos_comida:
            self.max_gramos_comida = gramos

    def css(self):
        if self.gramos_comida_consumidos == 0:
            return None
        return self.kilometros_volados / self.gramos_comida_consumidos

    def cssp(self):
        if self.max_gramos_comida == 0:
            return None
        return self.max_kilometros_vuelo / self.max_gramos_comida

    def cssv(self):
        if self.cant_comidas == 0 or self.cant_vuelos == 0:
            return None
        return self.cant_vuelos / self.cant_comidas
    