import random


class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    '''Esta clase desciende de la clase borracho 
    y es tracicional ya que se mueve a la misma distancia en cual quier direccion'''

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        # Genera coordenadas aleatorias con la misma probabilidad (x,y)
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
