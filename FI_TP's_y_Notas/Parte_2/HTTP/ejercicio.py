
import requests
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

datos = respuesta.json()

print(respuesta.status_code) 
print(datos.keys()) 
print(respuesta.headers["Content-Type"])
print(f'Tiene {len(datos["abilities"])} habilidades')

"""
EJERCICIO: https://pokeapi.co/api/v2/pokemon/ditto
1- Describir las partes de la URL
resuelto abajo 

2- ¿Qué respuesta puede obtener al hacer un GET en esa URL?
	.keys → dict_keys(['abilities', 'base_experience', 'forms', 'game_indices', 'height', 'held_items', 'id', 'is_default', 'location_area_encounters', 'moves', 'name', 'order', 'past_types', 'species', 'sprites', 'stats', 'types', 'weight']) → print(datos.keys())

3- Cual es el content type de esa respuesta?
application/json; charset=utf-8 → print(respuesta.headers["Content-Type"])


4- Cual es el estatus code de la respuesta?
200 → print(respuesta.status_code)

5- ¿Cuántas habilidades tiene este pokemon? 
Tiene 2 habilidades → print(f'Tiene {len(datos["abilities"])} habilidades')

PARTES DE LA URL ⇒ 

https://www.mercadolibre.com/aros-de-plata

Protocolo → https (para conectarnos de una compu a otra)
Dominio → Nombre con el que voy a ubicar una IP (ej:se le pone mercado libre porque la gente lo va a saber más que un número)
Recursos → Las cosas que puedes consultar en la base de datos y me va a ir combinado cada vez que le pido una cosa distinta

"""

