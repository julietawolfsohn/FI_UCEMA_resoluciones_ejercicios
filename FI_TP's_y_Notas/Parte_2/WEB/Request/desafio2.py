"""
Desafío II "https://jsonplaceholder.typicode.com/todos"

a) ¿Cuál es el dominio al que estamos consultando?
jsonplaceholder.typicode.com

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?
200, application/json; charset=utf-8

c) Agregar un contenido cuyo user Id es 11 y su id es 2 con un nuevo título e indicando que está completo (completed).

d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?
"""

import requests
dato = requests.get("https://jsonplaceholder.typicode.com/todos")

datos = dato.json()


print(dato.status_code) #B
print(dato.headers["Content-Type"]) #B

#C
#hay que definir data y headers (foto)
a = requests.post("https://jsonplaceholder.typicode.com/todos", data = json.dumps(data), headers=headers) #cuando agrego un nuevo elemento a una API, se actualiza el ID para reconocer qeu es algo nuevo