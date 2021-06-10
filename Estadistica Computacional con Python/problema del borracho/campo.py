
class Campo:
    '''Un Campo es una lista que contiene las coordenadas de los borrachos y puede
    añadir borrachos, mover al borracho a una nueva ubicacion y nos puede dar su ubicacion'''
    def __init__(self):
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self, borracho, coordenada):
        # Añade el borracho y su coordenada al diccionario 'coordenadas de borrachos {borracho:coordenada}'
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        # Se llama a la funcion generar_nueva_ubicacion del borracho para obtener aleatoriamente una nueva coordenada en
        # tupla que se asigna a 'nueva_x' y 'nueva_y'
        nueva_x, nueva_y = borracho.generar_nueva_ubicacion()
        # coordenada actual nos trae del diccionario las coordenadas del borracho
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        # nueva coordenada utiliza el metodo mover de la clase coordenada y recibe las coordenadas del metodo generar_nueva_ubicacion del borracho
        # nos da una nueva coordenada sumando la actual con la nueva
        nueva_coordenada = coordenada_actual.mover(nueva_x, nueva_y)

        # asigna la nueva coordenada al mismo borracho dentro del diccionario de coordenadas de borrachos
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]
