#https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/Practica/Requests_Ejercicios.md

"""
Desafío III En base al siguiente enlace "https://pokeapi.co/api/v2/pokemon/", crear una clase llamada Pokemon, que tome como parámetro el nombre de un pokemon y realice lo siguiente:

a) Obtenga los datos completos del pokemon en cuestión (en caso de no existir, que devuelva un mensaje diciendo esto).

b) Muestre las estadísticas (stats) de ese pokemon.

c) Nos diga qué movimientos tiene.

d) Obtenga el/los tipo/s del mismo.

f) Devuelva la/s habilidad/es que tenga.

g) Nos diga el número (id) en la pokedex.

h) Obtenga el peso del pokemon

i) Guarde en un archivo la información básica del pokemon: número, nombre, tipos y movimientos. Este archivo tiene que ir juntando la información de cada pokemon que instanciemos.

j) Guarde en otro archivo la información para el competitivo (todo lo obtenido, menos el número). Nuevamente, este archivo tiene que ir acumulando la información.

 """
 
import requests, os, re, glob

#A
class Pokemon():
    def __init__(self, nombre):
        self.nombre = nombre
        self.data = self.data_del_pokemon()

    def data_del_pokemon(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.nombre}" #para que es la f?
        respuesta = requests.get(url)
        if respuesta.status_code == 200:  #esto no me queda claro
            return respuesta.json()
        else:
            return None
        
    def info_completa(self):
        if self.data:  #no entiendo esta parte
            return self.data
        else:
            return "El pokemon (self.nombre) no existe"
    
#F

    def cant_habilidades(self):
        ("https://pokeapi.co/api/v2/abilities")
        return (f'Tiene {(datos["abilities"])} habilidades')

  """def get_abilities(self):
        if self.data:
            abilities = self.data.get("abilities", [])
            ability_names = [ability["ability"]["name"] for ability in abilities]
            return ability_names
        else:
            return []"""

        
        
        
        
nombre_pokemon = "pikachu"
pokemon = Pokemon(nombre_pokemon)
data_completa = pokemon.info_completa()

print(data_completa)
