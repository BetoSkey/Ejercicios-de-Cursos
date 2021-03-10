from datos_estadisticos import Datos_estadisticos
import unittest



class Analisis_estadistico(Datos_estadisticos):
    '''Analiza estadisticamente datos de una datos o un diccionario
    '''

    def __init__(self, datos, titulo=None):
        super().__init__()
        self.titulo = titulo

    


if '__main__' == __name__:

    analisis1=Analisis_estadistico([1,2,3,4])
    print(analisis1)