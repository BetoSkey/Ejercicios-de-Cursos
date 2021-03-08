import random
import math
import pandas
from collections import Counter
import unittest


class Analisis_estadistico:
    '''Analiza estadisticamente datos de una lista o un diccionario
    '''

    def __init__(self, titulo, datos):
        self.titulo = titulo
        self.datos = datos

    def __str__(self):
        return f'''
    -----------------------------------------------------------------------------
    {self.titulo}
        Medidas de tendencia central:
            Media: {round(self.media(), 3)}
            Mediana: {self.mediana()}
            Moda: {self.moda()}
        
        Medidas de dispercion:
            Varianza: {round(self.varianza(self.datos), 3)}
            Desviacion estandar: {round(self.desviacion_estandar(self.datos), 3)}
    -----------------------------------------------------------------------------
    '''

    def ubicacion_binaria(self, lista, comienzo, final, objetivo, ubicacion_meta=0):

        if final-comienzo == 1:  # Si la lista se acoto a dos ubicaciones
            if objetivo > lista[final]:

                if final + 1 > len(lista)-1:
                    ubicacion_meta = len(lista)-1
                else:
                    ubicacion_meta = final

                return ubicacion_meta
            elif objetivo < lista[comienzo]:
                ubicacion_meta = comienzo

                return ubicacion_meta

        if comienzo == final:  # Si la lista llego al final de su acote y solo nos indica una ubicacion

            # Si el objetivo no se encontro y es mayor que el acotamiento final
            if objetivo > lista[final]:
                # Si la ubicacion meta es mas grande que la lista completa
                if final + 1 > len(lista)-1:
                    ubicacion_meta = len(lista)-1

                else:
                    ubicacion_meta = final + 1

            # Si estamos al principio de la lista o el objetivo es igual que el acotamiento final
            elif comienzo == 0 or objetivo == lista[final]:
                pass

            else:
                ubicacion_meta += 1

            return ubicacion_meta

        # Aqui empieza a acotar la busqueda
        medio = (comienzo + final) // 2  # Se acota la lista a la mitad

        if objetivo == lista[medio]:  # Si el objetivo se encontro en la mitad
            return medio

        elif objetivo > lista[medio]:  # Si el objetivo es mayor que la mitad
            ubicacion_meta = medio
            return self.ubicacion_binaria(lista, medio + 1, final, objetivo, ubicacion_meta)

        else:  # Si el objetivo es menor que la mitad
            return self.ubicacion_binaria(lista, comienzo, medio - 1, objetivo, ubicacion_meta)

    def ordenamiento_insercion(self, lista):
        lista_ordenada = [lista[0]]
        lista_desordenada = lista[1:]
        n_lista_ordenada = len(lista_ordenada)-1
        n_lista_desordenada = len(lista_desordenada)-1

        # Por cada ubicacion de la lista desordenada
        for ubicacion_en_lista_desordenada in range(n_lista_desordenada+1):

            # Encuentra la ubicacion en la lista ordenada
            ubicacion = self.ubicacion_binaria(
                lista_ordenada, 0, n_lista_ordenada, lista_desordenada[ubicacion_en_lista_desordenada])

            # Si el numero desordenado es mayor que el de la ubicacion encontrada
            if lista_desordenada[ubicacion_en_lista_desordenada] > lista_ordenada[ubicacion]:

                # Si la ubicacion encontrada es igual que el final de la lista, se agrega al final
                if ubicacion == n_lista_ordenada:
                    lista_ordenada.append(
                        lista_desordenada[ubicacion_en_lista_desordenada])

                # Si el numero no esta al final de la lista, se inserta en la siguiente ubicacion encontrada
                else:
                    lista_ordenada.insert(
                        ubicacion + 1, lista_desordenada[ubicacion_en_lista_desordenada])
                n_lista_ordenada += 1

            # Si el numero desordenado es menor o igual que el de la ubicacion encontrada
            else:
                lista_ordenada.insert(
                    ubicacion, lista_desordenada[ubicacion_en_lista_desordenada])
                n_lista_ordenada += 1

        return lista_ordenada

    def busqueda_binaria(self, lista, comienzo, final, objetivo, ordenar=True):
        lista_ordenada = []
        if ordenar == True:
            lista_ordenada = self.ordenamiento_insercion(lista)

        if comienzo > final:
            return False
        medio = (comienzo + final) // 2
        if lista_ordenada[medio] == objetivo:
            return True
        elif lista_ordenada[medio] < objetivo:
            return self.busqueda_binaria(lista_ordenada, medio + 1, final, objetivo)
        else:
            return self.busqueda_binaria(lista_ordenada, comienzo, medio - 1, objetivo)

    def media(self, datos=None):
        if datos == None:
            datos = self.datos
        '''Puede recibir una lista o un diccionario'''
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
        '''Puede recibir una lista o un diccionario'''
        datos = self.datos
        if type(datos) is dict:
            lista_xi_ordenada = self.ordenamiento_insercion(
                [xi for xi in datos.keys()])

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
                ubicacion_mediana = fa_acumulada_list[self.ubicacion_binaria(
                    fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio)+1]
                mediana = dict_xi_fa_acumulada[ubicacion_mediana]
            else:
                numero_medio1 = int(round(total_n/2, 0)-1)
                numero_medio2 = int(round(total_n/2, 0))
                ubicacion_numero_medio1 = fa_acumulada_list[self.ubicacion_binaria(
                    fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio1)+1]
                ubicacion_numero_medio2 = fa_acumulada_list[self.ubicacion_binaria(
                    fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio2)+1]
                if ubicacion_numero_medio1 == ubicacion_numero_medio2:
                    numero_medio = self.media([numero_medio1, numero_medio2])
                    ubicacion_mediana = fa_acumulada_list[self.ubicacion_binaria(
                        fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio)+1]
                    mediana = dict_xi_fa_acumulada[ubicacion_mediana]
                else:
                    mediana = self.media([
                        dict_xi_fa_acumulada[ubicacion_numero_medio1], dict_xi_fa_acumulada[ubicacion_numero_medio2]])

        else:
            lista_ordenada = self.ordenamiento_insercion(datos)

            if len(lista_ordenada) % 2 > 0:
                mediana = lista_ordenada[int(
                    round(len(lista_ordenada)/2, 0)-1)]
            else:
                numero_medio1 = lista_ordenada[int(
                    round(len(lista_ordenada)/2, 0)-1)]
                numero_medio2 = lista_ordenada[int(
                    round(len(lista_ordenada)/2, 0))]

                mediana = self.media([numero_medio1, numero_medio2])

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
                media_dict_xi_fa = self.media(datos)
                total_n = sum(datos.values())
                xi2_fa = []
                for xi, fa in datos.items():
                    xi2_fa.append((xi**2)*fa)
                varianza = (
                    (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)

            else:
                media_lista = self.media(datos)
                diferencias_vs_media = []
                for i in range(len(datos)):
                    diferencia = (datos[i] - media_lista)**2
                    diferencias_vs_media.append(diferencia)

                varianza = self.media(diferencias_vs_media)

        else:
            if type(datos) is dict:
                media_dict_xi_fa = self.media(datos)
                total_n = sum(datos.values())-1
                xi2_fa = []
                for xi, fa in datos.items():
                    xi2_fa.append((xi**2)*fa)
                varianza = (
                    (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)

            else:
                media_lista = self.media(datos)
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

    def valores_z(self, valor_a_convertir=None, media_lista=None, sigma=None):
        '''Regresa un diccionario de valrores z, 'z' es el alejamiento de la media en "veces desviacion estandar",
        la formula tambien puede convertir un valor dando la media de lista y sigma.'''
        datos = self.datos

        if valor_a_convertir == None:
            media_lista = self.media()
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
        '''Regresa listas de "x" y "y" a partir de una lista, para graficar su distribucion normal'''
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
        if self.busqueda_binaria(lista_probabilidades_dns, 0, len(lista_probabilidades_dns), probabilidad_dns):
            z = lista_z[probabilidad_dns]
        else:
            ubicacion1 = self.ubicacion_binaria(lista_probabilidades_dns, 0, len(
                lista_probabilidades_dns), probabilidad_dns) - 1
            ubicacion2 = self.ubicacion_binaria(lista_probabilidades_dns, 0, len(
                lista_probabilidades_dns), probabilidad_dns)
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

        if self.busqueda_binaria(lista_probabilidades_dns, 0, len(lista_probabilidades_dns), probabilidad_dns):
            z = lista_z[probabilidad_dns]

        else:
            ubicacion1 = self.ubicacion_binaria(lista_probabilidades_dns, 0, len(
                lista_probabilidades_dns), probabilidad_dns) - 1

            ubicacion2 = self.ubicacion_binaria(lista_probabilidades_dns, 0, len(
                lista_probabilidades_dns), probabilidad_dns)

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

        if self.busqueda_binaria(lista_probabilidades_dns, 0, len(lista_probabilidades_dns), probabilidad_dns):
            z = lista_z[probabilidad_dns]

        else:
            ubicacion1 = self.ubicacion_binaria(lista_probabilidades_dns, 0, len(
                lista_probabilidades_dns), probabilidad_dns) - 1

            ubicacion2 = self.ubicacion_binaria(lista_probabilidades_dns, 0, len(
                lista_probabilidades_dns), probabilidad_dns)

            z = (
                lista_z[lista_probabilidades_dns[ubicacion1]] +
                lista_z[lista_probabilidades_dns[ubicacion2]]
            ) / 2

        return round(z, 3)


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

    analisis_lista = Analisis_estadistico(
        datos=[55, 87, 74, 70, 82, 62, 59], titulo='Analisis 1')

    analisis_dict = Analisis_estadistico(datos=dict(
        [(6, 3), (7, 16), (8, 20), (9, 10), (10, 1)]), titulo='Analisis 2')

    print(analisis_lista)
    print(analisis_dict)

    unittest.main()
