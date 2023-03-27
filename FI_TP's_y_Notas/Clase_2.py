#!/bin/python3
#https://github.com/WomenBioinfoDataScLA/Workshops/blob/master/Programming/%5BES%5DScripting.md
import os, sys

#sys.argv toma los argumentos que le pasamos al script por consola
#[1] significa que siempre voy a tomar el primero 
# es decir que leo solo la primer palabra que escriben en la terminal 

usuario = sys.argv[1]

def saludador(nombre):
    return "Hola " + nombre
#print(saludador("Juli"))# PORQUE ESTO NO?

if __name__ == "__main__":
  print (saludador(usuario))
#el valor se va a pasar por la terminal, osea que yo voy a elegir que nombre quiero que me tire


"""HACER TAREA 22/03 - desafio final"""
#https://github.com/WomenBioinfoDataScLA/Workshops/blob/master/Programming/%5BES%5DScripting.md