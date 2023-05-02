"""
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:

implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

comprobar el código que se escribió con esta secuencia:

definir un ornitólogo, dos golondrinas y dos gorriones,
inicializar las aves con valores conocidos,
decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
decirle al ornitólogo que realice su rutina sobre aves,
verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.
"""
#ver como resolver

class Ornitologo:
    def __init__(self):
        self.aves = []
        
    def estudiar_ave(self,ave):
        self.aves.append(ave)
        
    def aves_en_estudio(self):
        return self.aves
    
    def realizar_rutina_sobre_aves(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]
        
    def aves_en_equilibrio(self):
        return [self.aves[i].esta_en_equilibrio() for i in range(len(self.aves))]
    #se pone prinero la accion y despues el for
    #recorrer la lista de aves -- la idea es hacer un for en una misma linea -- me va a generar lista de booleanos (True or False)
    #recorro por cada indice
    
    #opcion 2 (ver como era en la clase grabada)
"""
lista = []
for aves
        """

ornitologo = Ornitologo
golondrina1 = Golondrina(80)
