
class Campo:

  def __init__(self):
    self.coordenadas_de_borrachos = {}
  
  def anadir_borracho(self, borracho, coordenada):
    # Añade el borracho y su coordenada al diccionario 'coordenadas de borrachos {borracho:coordenada}'
    self.coordenadas_de_borrachos[borracho] = coordenada
  
  def mover_borracho(self, borracho):
    # Se llama a la funcion camina del borracho para obtener aleatoriamente una nueva tupla que se asigna a 'delta_x' y 'delta_y'
    delta_x, delta_y = borracho.camina()
    coordenada_actual = self.coordenadas_de_borrachos[borracho]
    nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)


    self.coordenadas_de_borrachos[borracho] = nueva_coordenada
  
  def obtener_coordenada(self, borracho):
    return self.coordenadas_de_borrachos[borracho]
