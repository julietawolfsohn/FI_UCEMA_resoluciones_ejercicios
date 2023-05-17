#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
import re
def reemplzar(string):
    patron = "[\s\t]"
    return re.sub(patron, ";",  string)

print(reemplzar("juli wolfsohn  va a la     cancha"))