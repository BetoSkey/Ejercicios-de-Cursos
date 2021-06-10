import random


class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre


class BorrachoTradicional(Borracho):
    '''Esta clase desciende de la clase borracho 
    y es tracicional ya que se mueve a la misma distancia en cualquier direccion'''

    def __init__(self, nombre):
        super().__init__(nombre)

    def generar_nueva_ubicacion(self):
        # Genera coordenadas aleatorias con la misma probabilidad (x,y)
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class BorrachoGarza(Borracho):
    '''Esta clase desciende de la clase borracho 
    y es Garza porque avanza hacia arriba mucho mas que cualquier otra direccion'''

    def __init__(self, nombre):
        super().__init__(nombre)

    def generar_nueva_ubicacion(self):
        # Genera coordenadas aleatorias con la misma probabilidad (x,y)
        return random.choice([(0, 7), (0, -1), (1, 0), (-1, 0)])


class BorrachoEnano(Borracho):
    '''Esta clase desciende de la clase borracho 
    y es Enano porque avanza abajo mucho mas que cualquier otra direccion'''

    def __init__(self, nombre):
        super().__init__(nombre)

    def generar_nueva_ubicacion(self):
        # Genera coordenadas aleatorias con la misma probabilidad (x,y)
        return random.choice([(0, 1), (0, -7), (1, 0), (-1, 0)])
