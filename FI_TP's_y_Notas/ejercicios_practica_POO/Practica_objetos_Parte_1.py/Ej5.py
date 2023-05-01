#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".
class Contador:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
        valor_inicial = 0
        self.ultimo_comando = None
        
    def inc(self):
        self.valor += 1
        self.ultimo_comando = "incremento"
        
    def dis(self):
        self.valor -= 1
        self.ultimo_comando = "disminucion"
        
    def reset(self):
        self.valor = 0
        self.ultimo_comando = "reset"
        
    def valorActual(self):
        return self.valor
    
    def valorNuevo(self, valorNuevo):
        self.valor = valorNuevo
        self.ultimo_comando = "actualizacion"
    
    def last_comando(self):
        return self.ultimo_comando


contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
print(contador.valorActual())
print(contador.last_comando())
contador.valorNuevo(27)
contador.dis()
contador.dis()
print (contador.valorActual())
print(contador.last_comando())