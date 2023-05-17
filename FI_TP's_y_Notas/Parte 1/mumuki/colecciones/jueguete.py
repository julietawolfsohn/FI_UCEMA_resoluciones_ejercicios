class Juguete:
  def __init__(self, nombre, precio_minorista, precio_mayorista, partes):
    self.nombre = nombre
    self.precio_minorista = precio_minorista
    self.precio_mayorista = precio_mayorista
    self.partes = partes
   
  def es_barato(self):
    return self.precio_minorista < 1000 and self.precio_mayorista < 600
    
  def precios_con_iva (self):
    return self.precio_minorista * 1.21, self.precio_mayorista *1.21
  
  def es_electronico (self):
    return "bateria" in self.partes
  
  class Jugueteria:
    def __init__(self):
      self.productos=[]
    
  def adquirir_producto(self, producto):
    return self.productos.append(producto)
  
  def catalogo_de_oferta(self):
    return [Juguete.nombre for Juguete in self.productos if Juguete.es_barato()]
  