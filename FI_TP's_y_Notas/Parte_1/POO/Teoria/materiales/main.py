#importo una libreria --> ave

from aves import pepita, anastasia, roberta
#pepita sabe volar xq lo hace
#print(pepita.volar_en_circulos())
#pepita no sabe hablar --> nos tira un error xq esa caracterista no la tienen las aves (es una golondrina)
#print(pepita.hablar())
#A pepita le gusta comer alpiste
#print(pepita.comer_alpiste(200))

#NONE siganifica que no rompio(porq lo sabe hacer) y po eso me devulve None xq es como que ya lo hizo
#pepita es un objeto

"""
Sabemos que pepita es un objeto individual/unico, 
en particular es un objeto de la clase Golondrinas
Que entiende mensajes (llo que las golondrinas entienden) 
y que tienen las caracteristicas de una Golondrina (atributos)
"""
"""print("Pepita al comiendo:", pepita.energia)
pepita.volar_en_circulos()
print("Pepita despues de volar:", pepita.energia)
print(pepita.esta_feliz())
pepita.comer_alpiste(200)
print("despues de comer:", pepita.energia)
print(pepita.esta_en_equilibrio())
print("hasta aca pepita ..")"""

""" Pepita tiene una energia basal.
Ahora sabemos que pepita cuando le damos ordenes, esta haciendo algo.
Y algo en su estado cambia(la energia).
Entonces ahora sabemos que el estado de pepita esta dado por su energis 
- Pepita tiene como atributos o caracteristicas sabe volar y comer alpiste
- El estado de los obejtos de alguna forma puede cambiar o modificarse
"""
#ESTADO --> IMP

print("En el caso de anastasia tiene de energia: ", anastasia.energia)
(anastasia.volar_en_circulos())
print(anastasia.energia)
print(anastasia)
(anastasia.comer_alpiste(200))
print(anastasia.energia)

""" Aprendimos que los objetos pueden tener distintos estados basales, uno propio cada uno
Aun con distintos estados, los objetos pueden entender los mismos mensajes (los mensajes se llaman metodos)
"""

print("Llamemos a Roberta")
print ("Roberta al cominzo tiene de energia: ", roberta.energia)
(roberta.volar_en_circulos())
print("Energia despues de volar: ", roberta.energia)
#(roberta.comer_alpiste(200))
#print("Energia despues de comer alpiste: ", roberta.energia)
#Roberta es un dragon, no come alpiste
roberta.escupir_fuego()
print("Energia despues de sacar fuego: ", roberta.energia)
roberta.comer_peces(200)
print("Energia despues de comer peces: ", roberta.energia)

""" A prendimos que hay obejtos que entienden 
los mismos mensajes aunque no sean de la misma clase
Esos mensajes se llaman interfaz(el conjunto de mensajes que entiende)
"""
#Teoria
"""
Los objetos no sabes si son o no polimorficos 
Los objetos que comparten su interfaz son polimorficos. 
En este caso vemos un polimorfismo parcial.
Para ver polimorfismo necesitamos un observador u otro actor

"""
from aves import pepita
print(pepita.volar(1))

from aves import pepita
pepita.energia = 180
print(pepita.esta_en_equilibrio())