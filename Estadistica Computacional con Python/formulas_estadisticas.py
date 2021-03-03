import random
import math
import pandas
from collections import Counter
import unittest


def ubicacion_binaria(lista, comienzo, final, objetivo, ubicacion_meta=0):

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
        return ubicacion_binaria(lista, medio + 1, final, objetivo, ubicacion_meta)

    else:  # Si el objetivo es menor que la mitad
        return ubicacion_binaria(lista, comienzo, medio - 1, objetivo, ubicacion_meta)


def ordenamiento_insercion(lista):
    lista_ordenada = [lista[0]]
    lista_desordenada = lista[1:]
    n_lista_ordenada = len(lista_ordenada)-1
    n_lista_desordenada = len(lista_desordenada)-1

    # Por cada ubicacion de la lista desordenada
    for ubicacion_en_lista_desordenada in range(n_lista_desordenada+1):

        # Encuentra la ubicacion en la lista ordenada
        ubicacion = ubicacion_binaria(
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


def busqueda_binaria(lista, comienzo, final, objetivo, ordenar=True):
    lista_ordenada = []
    if ordenar == True:
        lista_ordenada = ordenamiento_insercion(lista)

    if comienzo > final:
        return False
    medio = (comienzo + final) // 2
    if lista_ordenada[medio] == objetivo:
        return True
    elif lista_ordenada[medio] < objetivo:
        return busqueda_binaria(lista_ordenada, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista_ordenada, comienzo, medio - 1, objetivo)


def media(datos):
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


def mediana(datos):
    '''Puede recibir una lista o un diccionario'''
    if type(datos) is dict:
        lista_xi_ordenada = ordenamiento_insercion(
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
                xi_fa_acumulada.append((fa_xi + xi_fa_acumulada[-1][0], xi))
                fa_acumulada_list.append(fa_xi + fa_acumulada_list[-1])

        total_n = xi_fa_acumulada[-1][0]
        dict_xi_fa_acumulada = dict(xi_fa_acumulada)

        if total_n % 2 > 0:
            numero_medio = int(round(total_n/2, 0))
            ubicacion_mediana = fa_acumulada_list[ubicacion_binaria(
                fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio)+1]
            mediana = dict_xi_fa_acumulada[ubicacion_mediana]
        else:
            numero_medio1 = int(round(total_n/2, 0)-1)
            numero_medio2 = int(round(total_n/2, 0))
            ubicacion_numero_medio1 = fa_acumulada_list[ubicacion_binaria(
                fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio1)+1]
            ubicacion_numero_medio2 = fa_acumulada_list[ubicacion_binaria(
                fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio2)+1]
            if ubicacion_numero_medio1 == ubicacion_numero_medio2:
                numero_medio = media([numero_medio1, numero_medio2])
                ubicacion_mediana = fa_acumulada_list[ubicacion_binaria(
                    fa_acumulada_list, 0, len(fa_acumulada_list), numero_medio)+1]
                mediana = dict_xi_fa_acumulada[ubicacion_mediana]
            else:
                mediana = media([
                    dict_xi_fa_acumulada[ubicacion_numero_medio1], dict_xi_fa_acumulada[ubicacion_numero_medio2]])
    
    else:
      lista_ordenada = ordenamiento_insercion(datos)

      if len(lista_ordenada) % 2 > 0:
          mediana = lista_ordenada[int(round(len(lista_ordenada)/2, 0)-1)]
      else:
          numero_medio1 = lista_ordenada[int(round(len(lista_ordenada)/2, 0)-1)]
          numero_medio2 = lista_ordenada[int(round(len(lista_ordenada)/2, 0))]

          mediana = media([numero_medio1, numero_medio2])

    return mediana


def moda(datos):
    if type(datos) is dict:
      maximo = max(datos.values())
      moda = [id for id, value in datos.items()if value == maximo]
    
    else:
      conteo_elementos = Counter(datos)
      maximo = max(conteo_elementos.values())
      moda = [id for id, value in conteo_elementos.items()if value == maximo]
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
        
        varianza = sum(diferencias_vs_media) / (len(diferencias_vs_media)-1)

    return varianza


def desviacion_estandar_datos_agrupados(datos):
    media_dict_xi_fa = media(datos)
    total_n = sum(datos.values())
    xi2_fa = []
    for xi, fa in datos.items():
        xi2_fa.append((xi**2)*fa)
    desviacion_estandar_datos_agrupados = (
        (sum(xi2_fa)/total_n) - media_dict_xi_fa**2)**.5
    return desviacion_estandar_datos_agrupados


def desviacion_estandar_poblacion(lista):
    varianza_lista = varianza(lista)
    sigma = varianza_lista**0.5
    return sigma


def varianza_datos_agrupados(datos):
    desviacion_estandar_datos_agrupados_dict = desviacion_estandar_datos_agrupados(
        datos)
    sigma_datos_agrupados = desviacion_estandar_datos_agrupados_dict**2
    return sigma_datos_agrupados


def varianza_muestra(lista):
    media_lista = media(lista)
    diferencias_vs_media = []
    for i in range(len(lista)):
        diferencia = (lista[i] - media_lista)**2
        diferencias_vs_media.append(diferencia)
    varianza = media(diferencias_vs_media,muestra=True)
    return varianza


def desviacion_estandar_muestra(lista):
    varianza_lista = varianza_muestra(lista)
    sigma = varianza_lista**0.5
    return sigma


def lista_valores_z(lista):
    '''Regresa de cada numero dentro de una lista, el alejamiento de la media en "veces desviacion estandar"'''
    media_lista = media(lista)
    desviacion_estandar_poblacion_lista = desviacion_estandar_poblacion(lista)
    lista_valor_z = {}
    for i in range(len(lista)):
        valor_z = (lista[i] - media_lista) / \
            desviacion_estandar_poblacion_lista
        lista_valor_z[lista[i]] = round(valor_z, 2)
    return lista_valor_z


def valores_x_y_distribucion_normal(lista):
    '''Regresa listas de "x" y "y" a partir de una lista, para graficar su distribucion normal'''
    media_lista = media(lista)
    sigma_lista = desviacion_estandar_poblacion(lista)
    valores_x = lista
    valores_y = []
    for i in lista:
        y = (1/(sigma_lista*math.sqrt(2*math.pi))) * \
            math.exp(-1/2*((i-media_lista)/(sigma_lista))**2)
        valores_y.append(y)
    return valores_x, valores_y


def diccionario_probabilidades_z_distribucion_normal_estandar():
    '''Regresa las probabilidades de z en la distribucion normal estandar'''
    df = pandas.read_csv('fdp.csv')
    z = df['z']
    probabilidad = df['prob']
    probabilidad_z = dict([(z[i], probabilidad[i]) for i in range(len(z))])
    return probabilidad_z


def buscar_z_dada_una_probabilidad_intermedia(probabilidad):
    '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
    probabilidad_dns = round(1-((1-probabilidad)/2), 5)
    lista_probabilidades_dns = [
        val for val in diccionario_probabilidades_z_distribucion_normal_estandar().values()]
    lista_z = {
        val: key for key,
        val in diccionario_probabilidades_z_distribucion_normal_estandar().items()
    }
    if busqueda_binaria(lista_probabilidades_dns, 0, len(lista_probabilidades_dns), probabilidad_dns):
        z = lista_z[probabilidad_dns]
    else:
        ubicacion1 = ubicacion_binaria(lista_probabilidades_dns, 0, len(
            lista_probabilidades_dns), probabilidad_dns) - 1
        ubicacion2 = ubicacion_binaria(lista_probabilidades_dns, 0, len(
            lista_probabilidades_dns), probabilidad_dns)
        z = (
            lista_z[lista_probabilidades_dns[ubicacion1]] +
            lista_z[lista_probabilidades_dns[ubicacion2]]
        ) / 2
    return round(z, 3)


def buscar_z_dada_una_probabilidad_izquierda(probabilidad):
    '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
    probabilidad_dns = round(probabilidad, 5)
    lista_probabilidades_dns = [
        val for val in diccionario_probabilidades_z_distribucion_normal_estandar().values()]
    lista_z = {
        val: key for key,
        val in diccionario_probabilidades_z_distribucion_normal_estandar().items()
    }

    if busqueda_binaria(lista_probabilidades_dns, 0, len(lista_probabilidades_dns), probabilidad_dns):
        z = lista_z[probabilidad_dns]

    else:
        ubicacion1 = ubicacion_binaria(lista_probabilidades_dns, 0, len(
            lista_probabilidades_dns), probabilidad_dns) - 1

        ubicacion2 = ubicacion_binaria(lista_probabilidades_dns, 0, len(
            lista_probabilidades_dns), probabilidad_dns)

        z = (
            lista_z[lista_probabilidades_dns[ubicacion1]] +
            lista_z[lista_probabilidades_dns[ubicacion2]]
        ) / 2

    return round(z, 3)


def buscar_z_dada_una_probabilidad_derecha(probabilidad):
    '''Busca Z en la tabla de probabilidades de la distribucion normal estandar dada una probabilidad'''
    probabilidad_dns = round((1-probabilidad), 5)

    lista_probabilidades_dns = [
        val for val in diccionario_probabilidades_z_distribucion_normal_estandar().values()]

    lista_z = {
        val: key for key,
        val in diccionario_probabilidades_z_distribucion_normal_estandar().items()
    }

    if busqueda_binaria(lista_probabilidades_dns, 0, len(lista_probabilidades_dns), probabilidad_dns):
        z = lista_z[probabilidad_dns]

    else:
        ubicacion1 = ubicacion_binaria(lista_probabilidades_dns, 0, len(
            lista_probabilidades_dns), probabilidad_dns) - 1

        ubicacion2 = ubicacion_binaria(lista_probabilidades_dns, 0, len(
            lista_probabilidades_dns), probabilidad_dns)

        z = (
            lista_z[lista_probabilidades_dns[ubicacion1]] +
            lista_z[lista_probabilidades_dns[ubicacion2]]
        ) / 2

    return round(z, 3)


class Pruebas_caja_cristal(unittest.TestCase):
  
  LISTA_PARA_PRUEBAS = [55, 87, 74, 70, 82, 62, 59]
  DICT_PARA_PRUEBAS = dict([(6, 3), (7, 16), (8, 20), (9, 10), (10,1)])

  def test_media(self):
      datos = Pruebas_caja_cristal.LISTA_PARA_PRUEBAS
      formula_media = round(media(datos),2)
      
      self.assertEqual(formula_media, 69.86)
  
  def test_media_datos_agrupados(self):
      datos = Pruebas_caja_cristal.DICT_PARA_PRUEBAS
      formula_media = media(datos)
     
      self.assertEqual(formula_media, 7.8)
  
  def test_mediana(self):
      datos = Pruebas_caja_cristal.LISTA_PARA_PRUEBAS
      formula_mediana = mediana(datos)
      
      self.assertEqual(formula_mediana, 70)
  
  def test_mediana_datos_agrupados(self):
      datos = Pruebas_caja_cristal.DICT_PARA_PRUEBAS
      formula_mediana = mediana(datos)
      
      self.assertEqual(formula_mediana, 8)

  def test_moda(self):
      datos = Pruebas_caja_cristal.LISTA_PARA_PRUEBAS
      datos.append(70)
      formula_moda = moda(datos)

      self.assertEqual(formula_moda, [70])
      datos.remove(70)
  
  def test_moda_datos_agrupados(self):
      datos = Pruebas_caja_cristal.DICT_PARA_PRUEBAS
      formula_moda = moda(datos)

      self.assertEqual(formula_moda, [8])
  
  def test_varianza(self):
      datos = Pruebas_caja_cristal.LISTA_PARA_PRUEBAS
      formula_varianza = round(varianza(datos),2)

      self.assertEqual(formula_varianza, 122.69)
  
  def test_varianza_muestral(self):
      datos = Pruebas_caja_cristal.LISTA_PARA_PRUEBAS
      formula_varianza = round(varianza(datos, muestra=True), 2)

      self.assertEqual(formula_varianza, 143.14)
  
  def test_varianza_datos_agrupados(self):
      datos = Pruebas_caja_cristal.DICT_PARA_PRUEBAS
      formula_varianza = round(varianza(datos),3)

      self.assertEqual(formula_varianza, 0.8)
  
  def test_varianza_muestral_datos_agrupados(self):
      datos = Pruebas_caja_cristal.DICT_PARA_PRUEBAS
      formula_varianza = round(varianza(datos,muestra=True), 3)

      self.assertEqual(formula_varianza, 2.058)

if '__main__' == __name__:
    '''largo_lista = int(input('Largo de lista: '))

    lista = [random.randint(1, largo_lista) for i in range(largo_lista)]

    #lista = [26, 33, 65, 28, 34, 55, 25, 44, 50, 36, 26, 37, 43, 62, 35, 38, 45, 32, 28, 34]

    #lista = [i for i in range(largo_lista)]

    lista_ordenada = ordenamiento_insercion(lista)

    print(f'Lista Original: {lista}\nLista Ordenada: {lista_ordenada}')

    probabilidad_a_buscar = float(input('Probabilidad a buscar: '))'''

    '''print(f#
Media: {media(lista_ordenada)}
Media muestra: {media(lista_ordenada, muestra=True)}
Media muestra original: media_muestra(lista_ordenada)
Mediana: {mediana(lista_ordenada)}
Modas: {moda(lista)}

Varianza Poblacion: {round(varianza(lista),2)}
sigma Poblacion: {round(desviacion_estandar_poblacion(lista),2)}

Varianza Muestra: {round(varianza_muestra(lista),2)}
sigma Muestra: {round(desviacion_estandar_muestra(lista),2)}

Valores z: {lista_valores_z(lista)}

Distribucion normal: 
x={valores_x_y_distribucion_normal(lista)[0]}

y={[round(i,3) for i in valores_x_y_distribucion_normal(lista)[1]]}

Probabilidad intermedia a {float(probabilidad_a_buscar*100)}% : z= {buscar_z_dada_una_probabilidad_intermedia(probabilidad_a_buscar)}
P(-z>= X <=z) = P({-buscar_z_dada_una_probabilidad_intermedia(probabilidad_a_buscar)} >= {float(probabilidad_a_buscar*100)}% <= {buscar_z_dada_una_probabilidad_intermedia(probabilidad_a_buscar)})

Probabilidad izquierda a {float(probabilidad_a_buscar*100)}% : z= {buscar_z_dada_una_probabilidad_izquierda(probabilidad_a_buscar)}
P(X <=z) = P({float(probabilidad_a_buscar*100)}% <= {buscar_z_dada_una_probabilidad_izquierda(probabilidad_a_buscar)})

Probabilidad derecha a {float(probabilidad_a_buscar*100)}% : z= {buscar_z_dada_una_probabilidad_derecha(probabilidad_a_buscar)}
P(z >= X) = P({buscar_z_dada_una_probabilidad_derecha(probabilidad_a_buscar)} >= {float(probabilidad_a_buscar*100)}% )
#)'''

    '''print('--------------------------------------------------------------')
    dict1 = {6: 3, 7: 16, 8: 20, 9: 10, 10: 1}

    print(f'media datos agrupados: {media(dict1)}')
    print(f'mediana datos agrupados: {mediana_datos_agrupados(dict1)}')
    print(f'moda datos agrupados: {moda(dict1)}')
    print(
        f'sigma datos agrupados {desviacion_estandar_datos_agrupados(dict1)}')
    print(
        f'varianza datos agrupados: {varianza_datos_agrupados(dict1)}')'''
    
    unittest.main()
    