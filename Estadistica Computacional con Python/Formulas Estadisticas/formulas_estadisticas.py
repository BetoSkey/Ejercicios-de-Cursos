import math
import pandas
from collections import Counter
import unittest
from busqueda_binaria import Busqueda_binaria
from formulas_especiales import ceiling_to_a_number, floor_to_a_number

# FORMULAS ESTADISTICA DESCRIPTIVA
def media(datos):
    '''
    Puede recibir:
    
    * lista (valores) = [1, 2, 3, 4]
    
    * diccionario_simple (valores: frecuencias absolutas) = {1:3, 2:1, 3:4}
    
    * diccionario_intervalos ((intervalos):frecuencias absolutas) = {(1,10):3, (10,20):4, (20,30):7}
    '''

    if type(datos) is dict:

        if type(list(datos)[0]) is tuple:

            sumatoria_ni = 0
            sumatoria_xi_ni = 0
            for intervalo, ni in datos.items():
                sumatoria_ni += ni
                marca_de_clase = (intervalo[0] + intervalo[1]) / 2
                sumatoria_xi_ni += marca_de_clase * ni
            media = sumatoria_xi_ni / sumatoria_ni

        else:
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
    '''Puede recibir:
    
    * lista.- [1, 2, 3...]
    
    * diccionario numeros y frecuencas absolutas.- {1:4, 2:10, 3:30...}
    
    * diccionario intervalos y frecuencias absolutas.- {(1,5):3, (5,10):10, (10,15):20...}
    '''
    if type(datos) is dict:
        if type(list(datos)[0]) is tuple:
            # Creacion de tabla con marcas de clase y frecuencias absolutas acumuladas
            lista_intervalos = [(intervalo,fa) for intervalo, fa in datos.items()]
            tabla_datos = []
            sumatoria_fa = 0
            
            for intervalo in lista_intervalos:
                
                rango_intervalo = intervalo[0]
                li_intervalo = intervalo[0][0]
                ls_intervalo = intervalo[0][1]
                fa_intervalo = intervalo[1]
                marca_clase = (li_intervalo + ls_intervalo) / 2
                
                sumatoria_fa += fa_intervalo
                faa_intervalo = sumatoria_fa
                
                tabla_datos.append((rango_intervalo, marca_clase ,fa_intervalo, faa_intervalo))
                
            mitad_faa = sumatoria_fa / 2
            
            # Encontrar intervalo de mitad de datos
            index_clase_mediana = 0
            while True:
                if tabla_datos[index_clase_mediana][3] < mitad_faa:
                    index_clase_mediana +=1
                else:
                    clase_mediana = tabla_datos[index_clase_mediana]
                    break
            
            li_clase_mediana = clase_mediana[0][0]
            ls_clase_mediana = clase_mediana[0][1]
            fa_clase_mediana = clase_mediana[2]
            faa_clase_anterior_mediana = 0 if index_clase_mediana == 0 else tabla_datos[(index_clase_mediana-1)][3]
            tamano_intervalo_clase_mediana = ls_clase_mediana - li_clase_mediana
            
            mediana = li_clase_mediana + (((mitad_faa - faa_clase_anterior_mediana) / fa_clase_mediana) * tamano_intervalo_clase_mediana)
        
        else:
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
            
            # si n no es par
            if total_n % 2 > 0:
                
                numero_medio = int(round(total_n/2, 0))
                ubicacion_mediana = fa_acumulada_list[Busqueda_binaria(
                    fa_acumulada_list).ubicacion_binaria(numero_medio)+1]
                
                mediana = dict_xi_fa_acumulada[ubicacion_mediana]
            else:
                
                fa_acumulada_list_binaria = Busqueda_binaria(fa_acumulada_list)
                
                numero_medio1 = int(round(total_n/2, 0)-1)
                
                numero_medio2 = int(round(total_n/2, 0))
                
                ubicacion_numero_medio1 = fa_acumulada_list[fa_acumulada_list_binaria.ubicacion_binaria(numero_medio1)]
                
                ubicacion_numero_medio2 = fa_acumulada_list[fa_acumulada_list_binaria.ubicacion_binaria(numero_medio2)]
                
                if ubicacion_numero_medio1 == ubicacion_numero_medio2:
                    numero_medio = media([numero_medio1, numero_medio2])
                    ubicacion_mediana = fa_acumulada_list[fa_acumulada_list_binaria.ubicacion_binaria(numero_medio)]
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
    '''Puede recibir:
    
    * lista.- [1, 2, 3...]
    
    * diccionario numeros y frecuencas absolutas.- {1:4, 2:10, 3:30...}
    
    * diccionario intervalos y frecuencias absolutas.- {(1,5):3, (5,10):10, (10,15):20...}
    '''
    # Si los datos son un diccionario
    if type(datos) is dict:
        
        # Si los datos son un diccionario con intervalos
        if type(list(datos)[0]) is tuple:
            # Creacion de tabla con marcas de clase y frecuencias absolutas acumuladas
            lista_intervalos = [(intervalo,fa) for intervalo, fa in datos.items()]
            tabla_datos = []
            tabla_fa = []
            sumatoria_fa = 0
            
            for intervalo in lista_intervalos:
                
                index_intervalo = lista_intervalos.index(intervalo)
                rango_intervalo = intervalo[0]
                li_intervalo = intervalo[0][0]
                ls_intervalo = intervalo[0][1]
                fa_intervalo = intervalo[1]
                marca_clase = (li_intervalo + ls_intervalo) / 2
                
                sumatoria_fa += fa_intervalo
                faa_intervalo = sumatoria_fa
                
                tabla_datos.append((rango_intervalo, marca_clase ,fa_intervalo, faa_intervalo))
                
                tabla_fa.append((index_intervalo, fa_intervalo))

            max_fa = max(dict(tabla_fa).values())
            index_intervalo_modal = [index for index, values in dict(tabla_fa).items() if values == max_fa][0]
            intervalo_modal =   tabla_datos[index_intervalo_modal]  
            li_intervalo_modal = intervalo_modal[0][0]
            ls_intervalo_modal = intervalo_modal[0][1]
            fa_intervalo_modal = intervalo_modal[2]
            fa_intervalo_modal_anteror = 0 if index_intervalo_modal == 0 else tabla_datos[(index_intervalo_modal-1)][2]
            fa_intervalo_modal_siguiente = tabla_datos[(index_intervalo_modal+1)][2]
            tamano_intervalo_modal = ls_intervalo_modal - li_intervalo_modal
            
            moda = li_intervalo_modal + (((fa_intervalo_modal - fa_intervalo_modal_anteror) / ((fa_intervalo_modal - fa_intervalo_modal_anteror) + (fa_intervalo_modal - fa_intervalo_modal_siguiente))) * tamano_intervalo_modal)
                
            
        # Si los datos son un diccionario de numeros y frecuencias absolutas
        else:        
            maximo = max(datos.values())
            moda = [id for id, value in datos.items()if value == maximo]

    # Si los datos son una lista
    else:
        conteo_elementos = Counter(datos)
        maximo = max(conteo_elementos.values())
        moda = [id for id, value in conteo_elementos.items()
                if value == maximo]
    # Se analiza si las modas encontradas son mas de 1 regresa una lista o solo 1 regresa un valor
    try:
        if len(moda) == 1:
            moda = moda[0]
    finally:
        return moda


def varianza(datos, muestra=False):
    '''Puede recibir:
    
    * lista.- [1, 2, 3...]
    
    * diccionario numeros y frecuencas absolutas.- {1:4, 2:10, 3:30...}
    
    * diccionario intervalos y frecuencias absolutas.- {(1,5):3, (5,10):10, (10,15):20...}
    '''
    
    if muestra == False:
        if type(datos) is dict:
            
            # Si es diccionario de datos agrupados con intervalos
            if type(list(datos)[0]) is tuple:

                # Creacion de tabla con marcas de clase y frecuencias absolutas
                lista_intervalos = [(intervalo,fa) for intervalo, fa in datos.items()]
                tabla_datos = []
                
                for intervalo in lista_intervalos:
                    
                    rango_intervalo = intervalo[0]
                    li_intervalo = intervalo[0][0]
                    ls_intervalo = intervalo[0][1]
                    fa_intervalo = intervalo[1]
                    marca_clase = (li_intervalo + ls_intervalo) / 2
                    
                    tabla_datos.append((marca_clase ,fa_intervalo))
                datos = dict(tabla_datos)
                
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


def coeficiente_variacion(datos):
    '''
    Porcentaje de la desviacion estandar frente a la media.

    * Todos los valores deben ser positivos para poder determinar el coheficiente.

    * Si el coeficiente es ***<= 0.80*** el conjunto de datos es ***homogeneo***, por lo tanto
        la ***media es representativa*** del conjunto de datos.


    * Si el coeficiente es ***> 0.80*** el conjunto de datos es ***heterogeneo***, por lo tanto
        la ***media "no" es representativa*** del conjunto de datos.
    '''
    s = desviacion_estandar(datos)
    media_datos = media(datos)

    cv = s / media_datos

    return cv


def creacion_intervalos(datos, rango_intervalos):
    '''
    Crea intervalos de los datos proporcionados de acuerdo al rango requerido para los
    intervalos.

    *** solo acepta listas***
    '''
    maximo_numero_en_rangos = ceiling_to_a_number(max(datos), rango_intervalos)
    minimo_numero_en_rangos = floor_to_a_number(min(datos), rango_intervalos)

    distancia_minimo_numero_vs_maximo_numero_en_rangos = maximo_numero_en_rangos - \
        minimo_numero_en_rangos

    cantidad_intervalos = int(
        distancia_minimo_numero_vs_maximo_numero_en_rangos / rango_intervalos)

    intervalos = [[
        minimo_numero_en_rangos,
        minimo_numero_en_rangos + rango_intervalos
    ]]

    for intervalo in range(cantidad_intervalos - 1):
        intervalos.append(
            [intervalos[-1][1], (intervalos[-1][1]) + rango_intervalos])

    return intervalos


def calculo_frecuencias_absolutas(datos, rango_intervalos):
    '''
    Crea intervalos y regresa sus frecuencias absolutas y frecuencias relativas.

    *** El ultimo numero de cada intervalo no es considerado hasta su siguiente intervalo,
    el ultimo intervalo considera el ultimo numero dentro del intervalo***
    
    *** Regresa una lista [[intervalo], fa, faa]***
    '''

    intervalos = creacion_intervalos(datos, rango_intervalos)
    ultimo_intervalo = intervalos[len(intervalos)-1]
    contar_datos = Counter(datos)

    faa = 0
    fa = []

    for intervalo in intervalos:
        conteo = 0

        if intervalo == ultimo_intervalo:
            for key, value in contar_datos.items():

                if key in range(intervalo[0], intervalo[1]+1):
                    conteo += value

        else:

            for key, value in contar_datos.items():

                if key in range(intervalo[0], intervalo[1]):
                    conteo += value
        faa += conteo

        fa.append((intervalo, conteo, faa))

    return fa


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
        valor_ubicacion_entero_siguiente = valor_ubicacion_entero if ubicacion_entero == len(
            datos)-1 else datos_ordenados[ubicacion_entero + 1]

        if ubicacion_decimal == 0:
            valor_ubicaciones_k[medida_de_posicion] = (
                ubicacion, round(valor_ubicacion_entero, 3))

        else:
            valor_ubicaciones_k[medida_de_posicion] = (ubicacion, round(
                ((valor_ubicacion_entero_siguiente - valor_ubicacion_entero) * ubicacion_decimal) + valor_ubicacion_entero, 3))

    return valor_ubicaciones_k


def asimetria_bowley(datos):
    '''
    Utiliza la medida de Yule Bowley
    
    Acepta: listade datos no agrupados, pueden estar desordenados

    Regresa: Negativa (<0), Simetrica (=0), Positiva (>0)
    '''
    cuartiles = medidas_posicion(datos, k=4)
    q1 = cuartiles['Q1'][1]
    q2 = cuartiles['Q2'][1]
    q3 = cuartiles['Q3'][1]

    medida_yule_bowley = ((q1 + q3) - (2 * q2)) / (q3 - q1)

    asimetria_bowley = 'Asimetrica negativa' if medida_yule_bowley < 0 else 'Asimetrica positiva' if medida_yule_bowley > 0 else 'Simetrica'

    return asimetria_bowley


def asimetria_pearson(datos):
    '''Puede recibir:
    
    * lista.- [1, 2, 3...]
    
    * diccionario numeros y frecuencas absolutas.- {1:4, 2:10, 3:30...}
    
    * diccionario intervalos y frecuencias absolutas.- {(1,5):3, (5,10):10, (10,15):20...}
    
    *** Resultados de asimetria: 
    (< 0 : asimetrica negativa 'hacia izquierda'), (= 0 : simetrica), (> 0 : asimetrica positiva 'hacia derecha')***
    '''
    
    media_datos = media(datos)
    mediana_datos = mediana(datos)
    desviacion_estandar_datos = desviacion_estandar(datos)
    
    asimetria_pearson = (3*(media_datos - mediana_datos)) / desviacion_estandar_datos
    
    return asimetria_pearson


# FORMULAS PARA GRAFICAR
class Diagrama_caja_bigotes:
    '''
    Obtiene informacion para grafica de caja y bigotes:
    * datos_ordenados
    * q1 
    * q2
    * q3
    * bigote_inferior
    * bigote_superior
    * rango_intercuartilico
    * barrera_superior
    * barrera_inferior
    * datos_atipicos
    '''

    def __init__(self, datos):
        self.datos = datos
        self.datos_ordenados = Busqueda_binaria(
            self.datos).ordenamiento_insercion()

        self.n = len(self.datos)

        self.cuartiles = medidas_posicion(self.datos, k=4)

        self.q1 = self.cuartiles['Q1'][1]
        self.q2 = self.cuartiles['Q2'][1]
        self.q3 = self.cuartiles['Q3'][1]

        self.rango_intercuartilico = self.q3 - self.q1

        self.barrera_inferior = self.q1 - (1.5 * self.rango_intercuartilico)
        self.barrera_superior = self.q3 + (1.5 * self.rango_intercuartilico)

        ubicacion_barrera_inferior = 0
        ubicacion_barrera_superior = 1

        while True:
            self.bigote_inferior = self.datos_ordenados[ubicacion_barrera_inferior]
            if self.bigote_inferior < self.barrera_inferior:
                ubicacion_barrera_inferior += 1
            else:
                break

        while True:
            self.bigote_superior = self.datos_ordenados[self.n -
                                                        ubicacion_barrera_superior]
            if self.bigote_superior > self.barrera_superior:
                ubicacion_barrera_superior += 1
            else:
                break

        self.datos_atipicos = [
            i for i in datos if i <
            self.barrera_inferior or i > self.barrera_superior
        ]

    def __str__(self):
        return f'''
    Datos ordenados: {self.datos_ordenados}

    Cuartiles = Q1:{self.q1}, Q2:{self.q2}, Q3:{self.q3}
    Bigote inferior = {self.bigote_inferior}
    bigote superior = {self.bigote_superior}

    Rango intercuartilico: {self.rango_intercuartilico}

    Barrera inferior: {self.barrera_inferior}
    Barrera superior: {self.barrera_superior}

    Datos atipicos: {self.datos_atipicos}
            '''


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


# FORMULAS ESTADISTICA INFERENCIAL
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

    def test_coeficiente_variacion(self):
        formula_coeficiente_variacion = coeficiente_variacion(analisis_lista)

        self.assertEqual(round(formula_coeficiente_variacion, 3), 0.159)

    def test_creacion_intervalos(self):
        formula_creacion_intervalos = creacion_intervalos(analisis_lista2, 5)

        self.assertEqual(formula_creacion_intervalos, [
            [50, 55], [55, 60], [60, 65], [65, 70], [70, 75], [75, 80], [80, 85]
        ])

    def test_calculo_frecuencias_absolutas(self):
        formula_calculo_frecuencias_absolutas = calculo_frecuencias_absolutas(
            analisis_lista2, 5)

        self.assertEqual(formula_calculo_frecuencias_absolutas, [
            ([50, 55], 2, 2), ([55, 60], 7, 9), ([
                60, 65], 17, 26), ([65, 70], 30, 56),
            ([70, 75], 14, 70), ([75, 80], 7, 77), ([80, 85], 3, 80)
        ])

    def test_medidas_posicion(self):
        formula_medidas_posicion = medidas_posicion(analisis_lista)

        self.assertEqual(
            formula_medidas_posicion, {'Q1': (1.0, 59), 'Q2': (3.0, 70), 'Q3': (5.0, 82)})

    def test_rango_intercuartilico(self):
        formula_rango_intercuartilico = Diagrama_caja_bigotes(
            analisis_lista).rango_intercuartilico

        self.assertEqual(formula_rango_intercuartilico, 23)

    def test_asimetria(self):
        formula_asimetria = asimetria_bowley(analisis_lista)

        self.assertEqual(formula_asimetria, 'Asimetrica positiva')

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


# INFORMACION PARA PRUEBAS
if '__main__' == __name__:

    analisis_lista = [55, 87, 74, 70, 82, 62, 59]

    analisis_dict = dict(
        [(6, 3), (7, 16), (8, 20), (9, 10), (10, 1)]
    )

    analisis_lista2 = [
        60, 66, 77, 70, 66, 68, 57, 70, 66, 52, 75, 65, 69, 71, 58, 66, 67, 74,
        61, 63, 69, 80, 59, 66, 70, 67, 78, 75, 64, 71, 81, 62, 64, 69, 68, 72,
        83, 56, 65, 74, 67, 54, 65, 65, 69, 61, 67, 73, 57, 62, 67, 68, 63, 67,
        71, 68, 76, 61, 62, 63, 76, 61, 67, 67, 64, 72, 64, 73, 79, 58, 67, 71,
        68, 59, 69, 70, 66, 62, 63, 66
    ]

    unittest.main()
