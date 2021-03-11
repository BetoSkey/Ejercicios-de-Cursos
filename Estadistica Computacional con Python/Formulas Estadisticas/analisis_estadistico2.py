from datos_estadisticos import Datos_estadisticos
import unittest


class Analisis_estadistico:
    '''Recibe un objeto "Datos_estadisticos"
    '''

    def __init__(self, datos):
        self.datos = datos

    def __str__(self):
        return f'''
Datos: {self.datos.datos}
'''


if '__main__' == __name__:

    datos1 = Datos_estadisticos(datos=[1, 2, 3, 4])
    analisis1 = Analisis_estadistico(datos1)
    print(analisis1)
