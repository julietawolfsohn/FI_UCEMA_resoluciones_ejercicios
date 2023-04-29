#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def _init_(self, la_marca, el_modelo, un_precio):
        self.marca = la_marca
        self.modelo = el_modelo
        self.precio = un_precio

    def aplicar_descuento (self, descuento):
        self.precio -= (self.precio * (descuento/100))

compu_mora = (Notebook("asus", "harman", 1000))
     
(compu_mora.aplicar_descuento(5))
print(compu_mora.precio)