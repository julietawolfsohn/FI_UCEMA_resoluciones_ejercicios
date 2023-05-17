"""
Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. 
También puede resetear este valor y al hacerlo se pone en cero. 
Además es posible indicar directamente un número nuevo que reemplace al valor actual. 
Este objeto debe entender los siguientes mensajes:

inc()
dis()
reset()
valorActual()
valorNuevo(nuevoValor)
"""
class Contador:
    def __init__(self, numero):
        self.numero = numero
        numero = 0
        
    def valor_actual(self):
        return self.numero
        
    def inc(self):
        self.numero +=1
        
    def dis(self):
        self.numero -=1
        
    def reset(self):
        self.numero = 0
    
    def valor_nuevo(self,contador):
        self.numero = contador



contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valor_actual())
contador.valor_nuevo(27)
contador.dis()
contador.dis()
print(contador.valor_actual())

