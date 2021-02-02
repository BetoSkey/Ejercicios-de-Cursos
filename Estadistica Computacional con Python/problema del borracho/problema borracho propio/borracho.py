import random


class Borracho:
    '''Clase padre de borrachos, puede:
    * Recibir ubicacion inicial
    * Caminar al borracho
    * Calcular la distancia que se alejo desde el inicio'''

    def __init__(self, ubicacion_inicial=(0, 0)):
        self.ubicacion_inicial = ubicacion_inicial
        self.ubicaciones = [self.ubicacion_inicial]

    def obtener_nueva_coordenada(self):
        nueva_coordenada = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        return nueva_coordenada

    def mover_borracho(self):
        nueva_ubicacion = (self.ubicaciones[-1][0] + self.obtener_nueva_coordenada(
        )[0], + self.ubicaciones[-1][1] + self.obtener_nueva_coordenada()[1])
        self.ubicaciones.append(nueva_ubicacion)

    def caminar_borracho(self, pasos):
        for i in range(pasos):
            self.mover_borracho()

    def calcular_alejamiento(self):
        delta_x = self.ubicaciones[-1][0] - self.ubicaciones[0][0]
        delta_y = self.ubicaciones[-1][1] - self.ubicaciones[0][1]
        
        return (round(((delta_x**2) + (delta_y**2))**.5, 3))

class Borracho_crudo(Borracho):
  '''Este borracho caminara aleatoriamente y con la misma probabilidad,
  un paso hascia cualquier punto cardinal.
  * Puede recibir una ubicacion inicial'''

  def __init__(self, ubicacion_inicial):
    super().__init__(ubicacion_inicial)
  
  def obtener_nueva_coordenada(self):
        nueva_coordenada = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        return nueva_coordenada

class Borracho_drogado(Borracho):
  '''Este borracho caminara aleatoriamente un rango entre 0 y 10 con la misma
  probabilidad en cualquier punto cardinal.
  * Puede recibir una ubicacion inicial'''

  def __init__(self, ubicacion_inicial):
    super().__init__(ubicacion_inicial)
  
  def obtener_nueva_coordenada(self):
        nueva_coordenada = random.choice([(random.randint(0, 10),0), (0, random.randint(0, 10)), (random.randint(-10, 0), 0), (0, random.randint(-10, 0))])
        return nueva_coordenada
    
class Prueba_estocastica:
  '''La prueba estocastica camina al borracho por cada intento, el numero de pasos indicado.
  * Nos realiza un analisis estadistico de las distancias recorridas por cada intento.'''

  def __init__(self, borracho, intentos, pasos):
    self.borracho = borracho
    self.intentos = intentos
    self.pasos = pasos
    self.distancias = []
    self.distancia_media = None
    self.distancia_minima = None
    self.distancia_maxima = None

  def correr_prueba(self):
    for intento in range(self.intentos):
      self.borracho.caminar_borracho(self.pasos)
      self.distancias.append(self.borracho.calcular_alejamiento())
    self.distancia_media = (round(sum(self.distancias) / len(self.distancias), 3))
    self.distancia_minima = min(self.distancias)
    self.distancia_maxima = max(self.distancias)
  
  def analisis_estadistico(self):
    print(f'Numero de pasos del borracho: {self.pasos}\n',
    f'Intentos: {self.intentos}\n',
    f'Distancias: {self.distancias}\n',
    f'Distancia Minima: {self.distancia_minima}\n',
    f'Distancia Media: {self.distancia_media}\n',
    f'Distancia maxima: {self.distancia_maxima}')
    

if __name__ == '__main__':
    borracho1 = Borracho_drogado((0, 0))
    intentos = int(input('Intentos: '))
    pasos_del_borracho = int(input('Pasos del borracho: '))
    prueba1 = Prueba_estocastica(borracho1, intentos, pasos_del_borracho)
    prueba1.correr_prueba()
    prueba1.analisis_estadistico()
    print(len(borracho1.ubicaciones))

    #El programa esta añadiendo y calculando la distancia inicial con la ultima, esto esta mal se tiene que revisar
