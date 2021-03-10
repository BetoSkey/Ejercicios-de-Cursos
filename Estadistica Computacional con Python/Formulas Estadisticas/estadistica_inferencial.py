from analisis_estadistico2 import Analisis_estadistico
from busqueda_binaria2 import Busqueda_binaria
import math
import pandas
import unittest

class Analisis_inferencial(Analisis_estadistico,Busqueda_binaria):

    def __init__(self, datos, titulo=None):
        super().__init__(datos, titulo)
    

    def valores_z(self, valor_a_convertir=None, media_lista=None, sigma=None):
        '''Regresa un diccionario de valrores z, 'z' es el alejamiento de la media en "veces desviacion estandar",
        la formula tambien puede convertir un valor dando la media de datos y sigma.'''
        datos = self.datos

        if valor_a_convertir == None:
            media_lista = Analisis_estadistico.media()
            desviacion_estandar_poblacion_lista = self.desviacion_estandar()
            valores_z = {}

            for i in range(len(datos)):
                valor_z = (datos[i] - media_lista) / \
                    desviacion_estandar_poblacion_lista
                valores_z[datos[i]] = round(valor_z, 2)

        else:
            valores_z = round(
                (valor_a_convertir - media_lista) /
                sigma, 2
            )

        return valores_z

    def valores_x_y_distribucion_normal(self):
        '''Regresa listas de "x" y "y" a partir de una datos, para graficar su distribucion normal'''
        datos = self.datos
        media_lista = self.media()
        sigma_lista = self.desviacion_estandar()
        valores_x = datos
        valores_y = []
        for i in datos:
            y = (1/(sigma_lista*math.sqrt(2*math.pi))) * \
                math.exp(-1/2*((i-media_lista)/(sigma_lista))**2)
            valores_y.append(y)
        return valores_x, valores_y

    def probabilidades_z_distribucion_normal_estandar(self):
        '''Regresa las probabilidades de z en la distribucion normal estandar'''
        df = pandas.read_csv('fdp.csv')
        z = df['z']
        probabilidad = df['prob']
        probabilidades_z = dict(
            [(z[i], probabilidad[i])
                for i in range(len(z))]
        )
        return probabilidades_z

    def buscar_z_probabilidad_intermedia(self, probabilidad):
        '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
        probabilidad_dns = round(1-((1-probabilidad)/2), 5)
        lista_probabilidades_dns = [
            val for val in self.probabilidades_z_distribucion_normal_estandar().values()]
        lista_z = {
            val: key for key,
            val in self.probabilidades_z_distribucion_normal_estandar().items()
        }
        if Busqueda_binaria(lista_probabilidades_dns).busqueda_binaria(probabilidad_dns):
            z = lista_z[probabilidad_dns]
        else:
            ubicacion1 = Busqueda_binaria(
                lista_probabilidades_dns).ubicacion_binaria(probabilidad_dns) - 1
            ubicacion2 = Busqueda_binaria(
                lista_probabilidades_dns).ubicacion_binaria(probabilidad_dns)
            z = (
                lista_z[lista_probabilidades_dns[ubicacion1]] +
                lista_z[lista_probabilidades_dns[ubicacion2]]
            ) / 2
        return z

    def buscar_z_probabilidad_izquierda(self, probabilidad):
        '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
        probabilidad_dns = round(probabilidad, 5)
        lista_probabilidades_dns = [
            val for val in self.probabilidades_z_distribucion_normal_estandar().values()]
        lista_z = {
            val: key for key,
            val in self.probabilidades_z_distribucion_normal_estandar().items()
        }

        if Busqueda_binaria(lista_probabilidades_dns).busqueda_binaria(probabilidad_dns):
            z = lista_z[probabilidad_dns]

        else:
            ubicacion1 = Busqueda_binaria(
                lista_probabilidades_dns).ubicacion_binaria(probabilidad_dns) - 1

            ubicacion2 = Busqueda_binaria(
                lista_probabilidades_dns).ubicacion_binaria(probabilidad_dns)

            z = (
                lista_z[lista_probabilidades_dns[ubicacion1]] +
                lista_z[lista_probabilidades_dns[ubicacion2]]
            ) / 2

        return z

    def buscar_z_probabilidad_derecha(self, probabilidad):
        '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
        probabilidad_dns = round((1-probabilidad), 5)

        lista_probabilidades_dns = [
            val for val in self.probabilidades_z_distribucion_normal_estandar().values()]

        lista_z = {
            val: key for key,
            val in self.probabilidades_z_distribucion_normal_estandar().items()
        }

        if Busqueda_binaria(lista_probabilidades_dns).busqueda_binaria(probabilidad_dns):
            z = lista_z[probabilidad_dns]

        else:
            ubicacion1 = Busqueda_binaria(
                lista_probabilidades_dns).ubicacion_binaria(probabilidad_dns) - 1

            ubicacion2 = Busqueda_binaria(
                lista_probabilidades_dns).ubicacion_binaria(probabilidad_dns)

            z = (
                lista_z[lista_probabilidades_dns[ubicacion1]] +
                lista_z[lista_probabilidades_dns[ubicacion2]]
            ) / 2

        return round(z, 3)

  
class Pruebas_caja_cristal(unittest.TestCase):

  def test_valor_z_muchos_datos(self):
      formula_valor_z = analisis_lista.valores_z()

      self.assertEqual(
          formula_valor_z, {
              55: -1.34, 87: 1.55, 74: 0.37, 70: 0.01, 82: 1.1, 62: -0.71, 59: -0.98}
      )

  def test_valor_z_un_dato(self):
      valor_a_convertir = 55
      formula_valor_z = analisis_lista.valores_z(
          valor_a_convertir=valor_a_convertir, media_lista=69.86, sigma=11.08)

      self.assertEqual(formula_valor_z, -1.34)

  def test_valores_x_y_distribucion_normal(self):
      formula_valores_x_y_distribucion_normal = analisis_lista.valores_x_y_distribucion_normal()[
          1]

      self.assertEqual(
          formula_valores_x_y_distribucion_normal, [
              0.014649940215369783, 0.010873903333325743, 0.03358323798357501, 0.028005203898067346, 0.02227796183372684, 0.03601326534529145, 0.01974872533379657]
      )

  def test_probabilidades_z_distribucion_normal_estandar(self):
      probabilidades_z = analisis_lista.probabilidades_z_distribucion_normal_estandar()

      self.assertEqual(probabilidades_z[2.71], 0.9966)

  def test_buscar_z_probabilidad_intermedia(self):
      probabilidad = 0.9966
      formula_buscar_z_probabilidad_intermedia = analisis_lista.buscar_z_probabilidad_intermedia(
          probabilidad)

      self.assertEqual(formula_buscar_z_probabilidad_intermedia, 2.93)

  def test_buscar_z_probabilidad_izquierda(self):
      probabilidad = 0.9115
      formula_buscar_z_probabilidad_izquierda = analisis_lista.buscar_z_probabilidad_izquierda(
          probabilidad)

      self.assertEqual(formula_buscar_z_probabilidad_izquierda, 1.35)

  def test_buscar_z_probabilidad_derecha(self):
      probabilidad = 0.9115
      formula_buscar_z_probabilidad_derecha = analisis_lista.buscar_z_probabilidad_derecha(
          probabilidad)

      self.assertEqual(formula_buscar_z_probabilidad_derecha, -1.35)


if '__main__' == __name__:

    analisis_lista = Analisis_inferencial(
        datos=[55, 87, 74, 70, 82, 62, 59], titulo='Analisis 1')

    analisis_dict = Analisis_inferencial(datos=dict(
        [(6, 3), (7, 16), (8, 20), (9, 10), (10, 1)]), titulo='Analisis 2')

    print(analisis_lista)
    print(analisis_dict)

    unittest.main()
