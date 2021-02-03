
class Coordenada:
    '''Una Coordenada (x, y) nos muestra la ubicacion, 
    puede trasladarse (mover) a una nueva ubicacion y 
    puede calcular la distancia recorrida'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, nueva_x, nueva_y):
        # Recibe las distancias nuevas de 'x', 'y' y las suma a la actual para recibir la nueva ubicacion
        return Coordenada(self.x + nueva_x, self.y + nueva_y)

    def distancia(self, otra_coordenada):
        # Caldulo de distancia con teorema de Pitagoras la
        # raiz cuadrada de la suma del cuadrado de las diferencias
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**.5
