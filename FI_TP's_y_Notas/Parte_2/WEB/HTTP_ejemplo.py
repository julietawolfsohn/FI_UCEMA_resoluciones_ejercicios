import requests

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs")  #get -- verbo HTTP asociado a las consultas 
datos = respuesta.json()    #guardo en una variable la respuesta en formato json
#1) en cuantas org. esta involucrado el usuario 
print(len(datos))
#2) lista de nombres de las org. en la que esta involucrado   "HACER"


print(respuesta)   #<Response [403]>  --- es un objeto esto que me aparece en la terminal (el numero 403 es estado, STATUS CODE)
print(respuesta.headers)   #headers me da una info sobre el propio pedido -- cuando, a que servidor (formato), a que hora, etc
print (respuesta.status_code)  #codigo asosiado a esa respuesta -- me dice como funciono esa conexion 

#Lo que obtengo cuando imprimo es una lista 
#en login esta el nombre de la organizacion