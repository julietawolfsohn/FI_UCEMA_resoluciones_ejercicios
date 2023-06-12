#Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:

class Calculadora:
    def __init__(self):
        self.valor = 0

    def cargar(self, numero):
        self.valor = numero    
    def sumar(self, numero):
        self.valor += numero
    def restar(self, numero):
        self.valor -= numero
    def multiplicar(self, numero):
        self.valor *= numero
    def valor_actual(self):
        return self.valor

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
print("el valor actual es", calculadora.valor_actual())

        
        