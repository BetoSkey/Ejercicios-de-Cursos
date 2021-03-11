from analisis_estadistico2 import Analisis_estadistico
from busqueda_binaria2 import Busqueda_binaria
from collections import Counter
import unittest


class Analisis_descriptivo(Analisis_estadistico, Busqueda_binaria):

    def __init__(self, datos):
        super().__init__(datos)
        datos = self.datos.datos

    def __str__(self):
        return f'''
    -----------------------------------------------------------------------------
    {self.datos.titulo}
        Medidas de tendencia central:
            Media: {round(self.media(), 3)}
            Mediana: {self.mediana()}
            Moda: {self.moda()}
        
        Medidas de dispercion:
            Varianza: {round(self.varianza(self.datos), 3)}
            Desviacion estandar: {round(self.desviacion_estandar(self.datos), 3)}
    -----------------------------------------------------------------------------
    '''

    def media(self):
        '''Puede recibir una datos o un diccionario'''

        datos = self.datos

        if type(datos) is dict:
            total_n = sum(datos.values())
            lista_ni_xi = []

            for xi, ni in datos.items():
                lista_ni_xi.append(xi * ni)

            suma_lista_ni_xi = sum(lista_ni_xi)
            media = suma_lista_ni_xi / total_n

        else:
            media = sum(datos) / len(datos)

        return media

    def mediana(self):
        '''Puede recibir una datos o un diccionario'''
        datos = self.datos
        if type(datos) is dict:
            lista_xi_ordenada = Busqueda_binaria(
                [xi for xi in datos.keys()]).ordenamiento_insercion()

            # faa= frecuencias absolutas acumuladas (FAA)
            xi_fa_acumulada = []
            fa_acumulada_list = []

            for xi in lista_xi_ordenada:
                fa_xi = datos[xi]
                if len(xi_fa_acumulada) == 0:
                    xi_fa_acumulada.append((fa_xi, xi))
                    fa_acumulada_list.append(fa_xi)
                else:
                    xi_fa_acumulada.append(
                        (fa_xi + xi_fa_acumulada[-1][0], xi))
                    fa_acumulada_list.append(fa_xi + fa_acumulada_list[-1])

            total_n = xi_fa_acumulada[-1][0]
            dict_xi_fa_acumulada = dict(xi_fa_acumulada)

            if total_n % 2 > 0:
                numero_medio = int(round(total_n/2, 0))
                ubicacion_mediana = fa_acumulada_list[Busqueda_binaria(
                    fa_acumulada_list).ubicacion_binaria(numero_medio)+1]
                mediana = dict_xi_fa_acumulada[ubicacion_mediana]
            else:
                numero_medio1 = int(round(total_n/2, 0)-1)
                numero_medio2 = int(round(total_n/2, 0))
                ubicacion_numero_medio1 = fa_acumulada_list[Busqueda_binaria(
                    fa_acumulada_list).ubicacion_binaria(numero_medio1)+1]
                ubicacion_numero_medio2 = fa_acumulada_list[Busqueda_binaria(
                    fa_acumulada_list).ubicacion_binaria(numero_medio2)+1]
                if ubicacion_numero_medio1 == ubicacion_numero_medio2:
                    numero_medio = Analisis_descriptivo(
                        [numero_medio1, numero_medio2]).media()
                    ubicacion_mediana = fa_acumulada_list[Busqueda_binaria(
                        fa_acumulada_list).ubicacion_binaria(numero_medio)+1]
                    mediana = dict_xi_fa_acumulada[ubicacion_mediana]
                else:
                    mediana = Analisis_descriptivo([
                        dict_xi_fa_acumulada[ubicacion_numero_medio1], dict_xi_fa_acumulada[ubicacion_numero_medio2]]).media()

        else:
            lista_ordenada = Busqueda_binaria(datos).ordenamiento_insercion()

            if len(lista_ordenada) % 2 > 0:
                mediana = lista_ordenada[int(
                    round(len(lista_ordenada)/2, 0)-1)]
            else:
                numero_medio1 = lista_ordenada[int(
                    round(len(lista_ordenada)/2, 0)-1)]
                numero_medio2 = lista_ordenada[int(
                    round(len(lista_ordenada)/2, 0))]

                mediana = Analisis_descriptivo(
                    [numero_medio1, numero_medio2]).media()

        return mediana

    def moda(self):
        datos = self.datos

        if type(datos) is dict:
            maximo = max(datos.values())
            moda = [id for id, value in datos.items()if value == maximo]

        else:
            conteo_elementos = Counter(datos)
            maximo = max(conteo_elementos.values())
            moda = [id for id, value in conteo_elementos.items()
                    if value == maximo]

        if len(moda) == 1:
            moda = moda[0]

        return moda

    def varianza(self, muestra=False):
        datos = self.datos

        if muestra == False:
            if type(datos) is dict:
                media_dict_xi_fa = self.media()
                total_n = sum(datos.values())
                xi2_fa = []
                for xi, fa in datos.items():
                    xi2_fa.append((xi**2)*fa)
                varianza = (
                    (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)

            else:
                media_lista = self.media()
                diferencias_vs_media = []
                for i in range(len(datos)):
                    diferencia = (datos[i] - media_lista)**2
                    diferencias_vs_media.append(diferencia)

                varianza = Analisis_descriptivo(diferencias_vs_media).media()

        else:
            if type(datos) is dict:
                media_dict_xi_fa = self.media()
                total_n = sum(datos.values())-1
                xi2_fa = []
                for xi, fa in datos.items():
                    xi2_fa.append((xi**2)*fa)
                varianza = (
                    (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)

            else:
                media_lista = self.media()
                diferencias_vs_media = []
                for i in range(len(datos)):
                    diferencia = (datos[i] - media_lista)**2
                    diferencias_vs_media.append(diferencia)

                varianza = sum(diferencias_vs_media) / \
                    (len(diferencias_vs_media)-1)

        return varianza

    def desviacion_estandar(self, muestra=False):
        formula_varianza = self.varianza(muestra=muestra)
        desviacion_estandar = formula_varianza ** 0.5

        return desviacion_estandar


class Pruebas_caja_cristal(unittest.TestCase):

    def test_media(self):
        formula_media = round(analisis_lista.media(), 2)

        self.assertEqual(formula_media, 69.86)

    def test_media_datos_agrupados(self):
        formula_media = analisis_dict.media()

        self.assertEqual(formula_media, 7.8)

    def test_mediana(self):
        formula_mediana = analisis_lista.mediana()

        self.assertEqual(formula_mediana, 70)

    def test_mediana_datos_agrupados(self):
        formula_mediana = analisis_dict.mediana()

        self.assertEqual(formula_mediana, 8)

    def test_muchas_modas(self):
        analisis_lista.datos.append(70)
        analisis_lista.datos.append(82)
        formula_moda = analisis_lista.moda()
        try:
            self.assertEqual(formula_moda, [82, 70])
        except:
            self.assertEqual(formula_moda, [70, 82])
        finally:
            analisis_lista.datos.remove(70)
            analisis_lista.datos.remove(82)

    def test_moda(self):
        analisis_lista.datos.append(70)
        formula_moda = analisis_lista.moda()

        try:
            self.assertEqual(formula_moda, 70)
        finally:
            analisis_lista.datos.remove(70)

    def test_moda_datos_agrupados(self):
        formula_moda = analisis_dict.moda()

        self.assertEqual(formula_moda, 8)

    def test_varianza(self):
        formula_varianza = round(analisis_lista.varianza(), 2)

        self.assertEqual(formula_varianza, 122.69)

    def test_varianza_muestral(self):
        formula_varianza = round(
            analisis_lista.varianza(muestra=True), 2)

        self.assertEqual(formula_varianza, 143.14)

    def test_varianza_datos_agrupados(self):
        formula_varianza = round(analisis_dict.varianza(), 3)

        self.assertEqual(formula_varianza, 0.8)

    def test_varianza_muestral_datos_agrupados(self):
        formula_varianza = round(
            analisis_dict.varianza(muestra=True), 3)

        self.assertEqual(formula_varianza, 2.058)

    def test_desviacion_estandar(self):
        formula_desviacion_estandar = round(
            analisis_lista.desviacion_estandar(), 2)

        self.assertEqual(formula_desviacion_estandar, 11.08)

    def test_desviacion_estandar_datos_agrupados(self):
        formula_desviacion_estandar = round(
            analisis_dict.desviacion_estandar(), 4)

        self.assertEqual(formula_desviacion_estandar, 0.8944)

    def test_desviacion_estandar_muestral(self):
        formula_desviacion_estandar = round(
            analisis_lista.desviacion_estandar(muestra=True), 4)

        self.assertEqual(formula_desviacion_estandar, 11.9642)

    def test_desviacion_estandar_muestral_datos_agrupados(self):
        formula_desviacion_estandar = round(
            analisis_dict.desviacion_estandar(muestra=True), 4)

        self.assertEqual(formula_desviacion_estandar, 1.4346)

    def test_valor_z_muchos_datos(self):
        formula_valor_z = analisis_lista.valores_z()

        self.assertEqual(
            formula_valor_z, {
                55: -1.34, 87: 1.55, 74: 0.37, 70: 0.01, 82: 1.1, 62: -0.71, 59: -0.98}
        )


if '__main__' == __name__:

    analisis_lista = Analisis_descriptivo(
        datos=[55, 87, 74, 70, 82, 62, 59])

    analisis_dict = Analisis_descriptivo(datos=dict(
        [(6, 3), (7, 16), (8, 20), (9, 10), (10, 1)]))

    print(analisis_lista)
    print(analisis_dict)

    unittest.main()
