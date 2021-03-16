import math
import pandas
from collections import Counter
import unittest
from busqueda_binaria import Busqueda_binaria


def media(datos):
    '''Puede recibir un datos o un diccionario'''

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


def mediana(datos):
    '''Puede recibir una datos o un diccionario'''
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
                numero_medio = media([numero_medio1, numero_medio2])
                ubicacion_mediana = fa_acumulada_list[Busqueda_binaria(
                    fa_acumulada_list).ubicacion_binaria(numero_medio)+1]
                mediana = dict_xi_fa_acumulada[ubicacion_mediana]
            else:
                mediana = media([
                    dict_xi_fa_acumulada[ubicacion_numero_medio1], dict_xi_fa_acumulada[ubicacion_numero_medio2]])

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

            mediana = media([numero_medio1, numero_medio2])

    return mediana


def moda(datos):

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


def varianza(datos, muestra=False):

    if muestra == False:
        if type(datos) is dict:
            media_dict_xi_fa = media(datos)
            total_n = sum(datos.values())
            xi2_fa = []
            for xi, fa in datos.items():
                xi2_fa.append((xi**2)*fa)
            varianza = (
                (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)

        else:
            media_lista = media(datos)
            diferencias_vs_media = []
            for i in range(len(datos)):
                diferencia = (datos[i] - media_lista)**2
                diferencias_vs_media.append(diferencia)

            varianza = media(diferencias_vs_media)

    else:
        if type(datos) is dict:
            media_dict_xi_fa = media(datos)
            total_n = sum(datos.values())-1
            xi2_fa = []
            for xi, fa in datos.items():
                xi2_fa.append((xi**2)*fa)
            varianza = (
                (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)

        else:
            media_lista = media(datos)
            diferencias_vs_media = []
            for i in range(len(datos)):
                diferencia = (datos[i] - media_lista)**2
                diferencias_vs_media.append(diferencia)

            varianza = sum(diferencias_vs_media) / \
                (len(diferencias_vs_media)-1)

    return varianza


def desviacion_estandar(datos, muestra=False):
    formula_varianza = varianza(datos, muestra=muestra)
    desviacion_estandar = formula_varianza ** 0.5

    return desviacion_estandar


def medidas_posicion(datos, k=4):
    '''Ubica las posiciones para la agrupacion de los datos en cuartiles (k=4), deciles (k=10) y percentiles (k=100)

    Entrada: lista de datos no agrupados (pueden no estar ordenados)
    
    Regresa un diccionario {Posicion: (ubicacion, valor)}'''

    n = len(datos)
    if k != 4 and k != 10 and k != 100:
        raise NameError('"k" solo puede ser 4, 10 o 100')

    tipo = 'Q' if k == 4 else 'D' if k == 10 else 'P' if k == 100 else 'error'
   
    analisis_binario = Busqueda_binaria(datos)
    datos_ordenados = analisis_binario.ordenamiento_insercion()

    ubicaciones_k = []
    valor_ubicaciones_k = {}

    for q in range(k-1):
        ubicaciones_k.append(
            ((tipo + str(q + 1)), round((((q+1) * (n + 1)) / k) - 1, 3)))

    for i in ubicaciones_k:

        medida_de_posicion = i[0]
        ubicacion = i[1]
        ubicacion_entero = int(ubicacion)
        ubicacion_decimal = ubicacion - int(ubicacion)
        valor_ubicacion_entero = datos_ordenados[ubicacion_entero]
        valor_ubicacion_entero_siguiente = valor_ubicacion_entero if ubicacion_entero == len(datos)-1 else datos_ordenados[ubicacion_entero + 1]


        if ubicacion_decimal == 0:
            valor_ubicaciones_k[medida_de_posicion] = (ubicacion, round(valor_ubicacion_entero, 2))

        else:
            valor_ubicaciones_k[medida_de_posicion] = (ubicacion, round(((valor_ubicacion_entero_siguiente - valor_ubicacion_entero) * ubicacion_decimal) + valor_ubicacion_entero, 2))

    
    return valor_ubicaciones_k


def valores_z(datos, valor_a_convertir=None, media_lista=None, sigma=None):
    '''Regresa un diccionario de valrores z, 'z' es el alejamiento de la media en "veces desviacion estandar",
    la formula tambien puede convertir un valor dando la media de datos y sigma.'''

    if valor_a_convertir == None:
        media_lista = media(datos)
        desviacion_estandar_poblacion_lista = desviacion_estandar(datos)
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


def valores_x_y_distribucion_normal(datos):
    '''Regresa listas de "x" y "y" a partir de una datos, para graficar su distribucion normal'''
    media_lista = media(datos)
    sigma_lista = desviacion_estandar(datos)
    valores_x = datos
    valores_y = []

    for i in datos:
        y = (1/(sigma_lista*math.sqrt(2*math.pi))) * \
            math.exp(-1/2*((i-media_lista)/(sigma_lista))**2)
        valores_y.append(y)

    return valores_x, valores_y


def probabilidades_z_distribucion_normal_estandar():
    '''Regresa las probabilidades de z en la distribucion normal estandar'''
    df = pandas.read_csv('fdp.csv')
    z = df['z']
    probabilidad = df['prob']
    probabilidades_z = dict(
        [(z[i], probabilidad[i])
            for i in range(len(z))]
    )
    return probabilidades_z


def buscar_z_probabilidad_intermedia(probabilidad):
    '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
    probabilidad_dns = round(1-((1-probabilidad)/2), 5)
    lista_probabilidades_dns = [
        val for val in probabilidades_z_distribucion_normal_estandar().values()]
    lista_z = {
        val: key for key,
        val in probabilidades_z_distribucion_normal_estandar().items()
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


def buscar_z_probabilidad_izquierda(probabilidad):
    '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
    probabilidad_dns = round(probabilidad, 5)
    lista_probabilidades_dns = [
        val for val in probabilidades_z_distribucion_normal_estandar().values()]
    lista_z = {
        val: key for key,
        val in probabilidades_z_distribucion_normal_estandar().items()
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


def buscar_z_probabilidad_derecha(probabilidad):
    '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
    probabilidad_dns = round((1-probabilidad), 5)

    lista_probabilidades_dns = [
        val for val in probabilidades_z_distribucion_normal_estandar().values()]

    lista_z = {
        val: key for key,
        val in probabilidades_z_distribucion_normal_estandar().items()
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

    def test_media_lista(self):
        formula_media = round(media(analisis_lista), 2)

        self.assertEqual(formula_media, 69.86)

    def test_media_diccionario(self):
        formula_media = round(media(analisis_dict), 2)

        self.assertEqual(formula_media, 7.8)

    def test_mediana(self):
        formula_mediana = mediana(analisis_lista)

        self.assertEqual(formula_mediana, 70)

    def test_mediana_datos_agrupados(self):
        formula_mediana = mediana(analisis_dict)

        self.assertEqual(formula_mediana, 8)

    def test_moda(self):
        analisis_lista.append(70)
        formula_moda = moda(analisis_lista)

        try:
            self.assertEqual(formula_moda, 70)
        finally:
            analisis_lista.remove(70)

    def test_muchas_modas(self):
        analisis_lista.append(70)
        analisis_lista.append(82)
        formula_moda = moda(analisis_lista)
        try:
            self.assertEqual(formula_moda, [82, 70])
        except:
            self.assertEqual(formula_moda, [70, 82])
        finally:
            analisis_lista.remove(70)
            analisis_lista.remove(82)

    def test_varianza(self):
        formula_varianza = round(varianza(analisis_lista), 2)

        self.assertEqual(formula_varianza, 122.69)

    def test_varianza_muestral(self):
        formula_varianza = round(
            varianza(analisis_lista, muestra=True), 2)

        self.assertEqual(formula_varianza, 143.14)

    def test_varianza_datos_agrupados(self):
        formula_varianza = round(varianza(analisis_dict), 3)

        self.assertEqual(formula_varianza, 0.8)

    def test_varianza_muestral_datos_agrupados(self):
        formula_varianza = round(
            varianza(analisis_dict, muestra=True), 3)

        self.assertEqual(formula_varianza, 2.058)

    def test_desviacion_estandar(self):
        formula_desviacion_estandar = round(
            desviacion_estandar(analisis_lista), 2)

        self.assertEqual(formula_desviacion_estandar, 11.08)

    def test_desviacion_estandar_datos_agrupados(self):
        formula_desviacion_estandar = round(
            desviacion_estandar(analisis_dict), 4)

        self.assertEqual(formula_desviacion_estandar, 0.8944)

    def test_desviacion_estandar_muestral(self):
        formula_desviacion_estandar = round(
            desviacion_estandar(analisis_lista, muestra=True), 4)

        self.assertEqual(formula_desviacion_estandar, 11.9642)

    def test_desviacion_estandar_muestral_datos_agrupados(self):
        formula_desviacion_estandar = round(
            desviacion_estandar(analisis_dict, muestra=True), 4)

        self.assertEqual(formula_desviacion_estandar, 1.4346)

    def test_medidas_posicion(self):
        formula_medidas_posicion = medidas_posicion(analisis_lista)

        self.assertEqual(
            formula_medidas_posicion, {'Q1': (1.0, 59), 'Q2': (3.0, 70), 'Q3': (5.0, 82)})

    def test_valor_z_muchos_datos(self):
        formula_valor_z = valores_z(analisis_lista)

        self.assertEqual(
            formula_valor_z, {
                55: -1.34, 87: 1.55, 74: 0.37, 70: 0.01, 82: 1.1, 62: -0.71, 59: -0.98}
        )

    def test_valor_z_un_dato(self):
        valor_a_convertir = 55
        formula_valor_z = valores_z(analisis_lista,
                                    valor_a_convertir=valor_a_convertir, media_lista=69.86, sigma=11.08)

        self.assertEqual(formula_valor_z, -1.34)

    def test_valores_x_y_distribucion_normal(self):
        formula_valores_x_y_distribucion_normal = valores_x_y_distribucion_normal(analisis_lista)[
            1]

        self.assertEqual(
            formula_valores_x_y_distribucion_normal, [
                0.014649940215369783, 0.010873903333325743, 0.03358323798357501, 0.028005203898067346, 0.02227796183372684, 0.03601326534529145, 0.01974872533379657]
        )

    def test_probabilidades_z_distribucion_normal_estandar(self):
        probabilidades_z = probabilidades_z_distribucion_normal_estandar()

        self.assertEqual(probabilidades_z[2.71], 0.9966)

    def test_buscar_z_probabilidad_intermedia(self):
        probabilidad = 0.9966
        formula_buscar_z_probabilidad_intermedia = buscar_z_probabilidad_intermedia(
            probabilidad)

        self.assertEqual(formula_buscar_z_probabilidad_intermedia, 2.93)

    def test_buscar_z_probabilidad_izquierda(self):
        probabilidad = 0.9115
        formula_buscar_z_probabilidad_izquierda = buscar_z_probabilidad_izquierda(
            probabilidad)

        self.assertEqual(formula_buscar_z_probabilidad_izquierda, 1.35)

    def test_buscar_z_probabilidad_derecha(self):
        probabilidad = 0.9115
        formula_buscar_z_probabilidad_derecha = buscar_z_probabilidad_derecha(
            probabilidad)

        self.assertEqual(formula_buscar_z_probabilidad_derecha, -1.35)


if '__main__' == __name__:

    analisis_lista = [55, 87, 74, 70, 82, 62, 59]
    analisis_dict = dict(
        [(6, 3), (7, 16), (8, 20), (9, 10), (10, 1)])

    unittest.main()
