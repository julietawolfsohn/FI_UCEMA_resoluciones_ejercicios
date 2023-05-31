"""
🧗‍♀️ Desafío I "https://pokeapi.co/api/v2/pokemon/pikachu"

a) ¿Cuál es el dominio al que estamos consultando? #NOMBRE + EXTENSION  
pokeapi.co

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".
status_code = 200 (es que esta funcionando), Content-type = application/json; charset=utf-8, [{'name': 'pikachu', 'url': 'https://pokeapi.co/api/v2/pokemon-form/25/'}]

c) Averigüá cuántos Pokemones almacena la API.
1281

d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?

f) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

g) Describí la arquitectura cliente-servidor y los roles de cada parte
"""

import requests
pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

datos = pikachu.json()


print(pikachu.status_code) #B
print(pikachu.headers["Content-Type"]) #B

print(pikachu.json().keys()) #te devuelve las claves tipo diccionario para poder buscar el forms #B
print(pikachu.json()["forms"]) #BUSCRA EL FORMS #B
 
respuesta_n = requests.get("https://pokeapi.co/api/v2/pokemon") #C
datos_1 = respuesta_n.json() #C
print((datos_1)) #C     #hay que hacerlo sin el LEN para que me cuente en total, en cambio si pongo el LEN me van a dar los headers que hay (4) -- es asi aca porq la API esta mal

("https://pokeapi.co/api/v2/abilities") #D #URL que tenga sentido para buscar las habilidades (tendria que estar antes de el pokemon o despues pero no desp del pikachu) -- son como ramas de arbol

sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon") #F
datos_2 = sylveon.json() #F

with open("ficha_tecnica_pokemos.txt", "ab") as ficha: #wb = ab #F
    ficha.write(pikachu.content)
    ficha.write(b'\n')
    ficha.write(sylveon.content)