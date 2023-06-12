"""
Los estudiantes (como ustedes) son como cualquier persona, las cuales recuperan energía si duermen o si comen, o la gastan al hacer ejercicio, sin embargo en particular los estudiantes también gastan energía al estudiar y se sienten felices al aprobar algún exámen. Resumiendo, las personan pueden:
Decirnos cuánta energía tienen.
Recuperar el máximo de energía (100) al dormir 8 horas, o el proporcional si duermen menos (si duermen 4 ganan la mitad de energía, es decir 50).
Recuperar energía al comer, ganando de esta manera 10 puntos.
Gastar energía al hacer ejercicio, siendo un gasto de 25 puntos por cada media hora de ejercicio.
Como estado de ánimo pueden estar felices o no, pero por defecto no están felices.
Además los estudiantes tienen el siguiente comportamiento:

Al estudiar su energía disminuye 20 puntos por cada hora de estudio.
Si aprueban su estado de ánimo pasa a ser "Feliz".
Definí las clases Persona y Estudiante con los atributos y métodos correspondientes y hacé que esta última herede de la primera. Además instanciá a un Estudiante y ejecutá las siguientes líneas:
"""
            
class Persona:
    def _init_(self, la_energia):
        self.energia = la_energia
        self.feliz = False

    def energia_actual(self):
        return self.energia
    
    def dormir (self, horas):
        if self.energia + horas <= 100:
            self.energia += horas * 12.5
        else:
            self.energia = 100
    
    def comer(self):
        if self.energia + 10 <=100:
            self.energia += 10
        else:
            self.energia = 100
    
    def hacer_ejercicio(self, minutos):
        if (self.energia - minutos * (25/30)) >= 0:
            self.energia -=minutos * (25/30)
        else:
            self.energia=0
    

class Estudiante(Persona):
    def estudiar(self, horas):
        if (self.energia - 20 * horas) >= 0:
            self.energia -= 20 * horas
        else:
            self.energia=0
    
    def aprobar(self):
        return not self.feliz 

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())
        
        
    
    
        
        
    
    
