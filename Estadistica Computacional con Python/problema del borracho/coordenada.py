
class Coordenada:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def mover(self, delta_x, delta_y):
    #Recibe las distancias nuevas de 'x', 'y' y las suma a la actual
    return Coordenada(self.x + delta_x, self.y + delta_y)
  
  def distancia(self, otra_coordenada):
    # Caldulo de distancia con teorema de Pitagoras la 
    # raiz cuadrada de la suma del cuadrado de las diferencias
    delta_x = self.x - otra_coordenada.x
    delta_y = self.y - otra_coordenada.y

    return (delta_x**2 + delta_y**2)**.05

