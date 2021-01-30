
class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self, borracho, coordenada):
        # Añade el borracho y su coordenada al diccionario 'coordenadas de borrachos {borracho:coordenada}'
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        # Se llama a la funcion camina del borracho para obtener aleatoriamente una nueva coordenada en
        # tupla que se asigna a 'delta_x' y 'delta_y'
        delta_x, delta_y = borracho.camina()
        # coordenada actual nos trae del diccionario las coordenadas del borracho
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        # nueva coordenada utiliza el metodo mover de la clase coordenada y recibe las coordenadas del metodo camina del borracho
        # nos da una nueva coordenada sumando la actual con la nueva
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        # asigna la nueva coordenada al mismo borracho dentro del diccionario de coordenadas de borrachos
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]
