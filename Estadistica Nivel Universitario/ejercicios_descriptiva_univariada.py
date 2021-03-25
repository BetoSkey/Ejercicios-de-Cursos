import sys
sys.path.append(
    '../Estadistica Computacional con Python/Formulas Estadisticas/')
from formulas_estadisticas import calculo_frecuencias_absolutas, media, mediana, moda, \
    medidas_posicion, Diagrama_caja_bigotes, varianza, desviacion_estandar, \
    coeficiente_variacion, asimetria_pearson, calculo_frecuencias_absolutas, Busqueda_binaria



if '__main__' == __name__:

    lista1 = [
        60, 66, 77, 70, 66, 68, 57, 70, 66, 52, 75, 65, 69, 71, 58, 66, 67, 74,
        61, 63, 69, 80, 59, 66, 70, 67, 78, 75, 64, 71, 81, 62, 64, 69, 68, 72,
        83, 56, 65, 74, 67, 54, 65, 65, 69, 61, 67, 73, 57, 62, 67, 68, 63, 67,
        71, 68, 76, 61, 62, 63, 76, 61, 67, 67, 64, 72, 64, 73, 79, 58, 67, 71,
        68, 59, 69, 70, 66, 62, 63, 66
    ]

    iva = [.16, .20, .06, .06, .07, .17, .06, .22]

    
    fa = calculo_frecuencias_absolutas(lista1, 5)
    print(fa)

    media_iva = media(iva)
    mediana_iva = mediana(iva)
    moda_iva = moda(iva)
    cuartiles_iva = medidas_posicion(iva, k=4)
    diagrama_caja_bigotes_iva = Diagrama_caja_bigotes(iva)
    rango_intercuartilico_iva = diagrama_caja_bigotes_iva.rango_intercuartilico


    print(f'''
    Media: {media_iva}
    
    Mediana: {mediana_iva}
    
    Moda: {moda_iva}
    
    Cuartiles: {cuartiles_iva}
    
    Rango intercuartilico: {rango_intercuartilico_iva}

    Datos Boxplot: {diagrama_caja_bigotes_iva}
    ''')

    dict_intervalos = {(60, 63): 5, (63, 66): 18, (66, 69): 42, (69, 72): 27, (72, 75): 8}

    #lista_dict = list(dict_intervalos)
    media_dict_intervalos = media(dict_intervalos)
    mediana_dict_intervalos = mediana(dict_intervalos)
    moda_dict_intervalos = moda(dict_intervalos)
    varianza_dict_intervalos = varianza(dict_intervalos)
    desviacion_estandar_intervalos = desviacion_estandar(dict_intervalos)
    
    #print(lista_dict)
    print(f'Media: {media_dict_intervalos}\n')
    
    print(f'Mediana: {mediana_dict_intervalos}\n')
    
    print(f'Moda: {moda_dict_intervalos}\n')
    
    print(f'Varianza: {varianza_dict_intervalos}\n')
    
    print(f'Desviacion Estandar {desviacion_estandar_intervalos}\n')
    
    print('''
    Ejerccios Descriptiva Univariada
    ____________________________________________________________________
    
    Ejercicio: 1 Minutos de pubilidad vistos diariamente por espectadores en el mes de marzo del año pasado:
    
    ''')
    
    minutos_espectadores = {(0,20):45, (20,40):10, (40,60):5, (60,80):2}
    
    media_minutos_espectadores = media(minutos_espectadores)
    mediana_minutos_espectadores = mediana(minutos_espectadores)
    moda_minutos_espectadores = moda(minutos_espectadores)
    varianza_minutos_espectadores = varianza(minutos_espectadores)
    desviacion_estaminutos_espectadores = desviacion_estandar(minutos_espectadores)
    coeficiente_variacion_espectadores= coeficiente_variacion(minutos_espectadores)
    asimetria_espectadores = asimetria_pearson(minutos_espectadores)
    
    
    print(minutos_espectadores)
    print(f'Media: {media_minutos_espectadores}')
    print(f'Mediana: {mediana_minutos_espectadores}')
    print(f'Moda: {moda_minutos_espectadores}')
    print(f'Varianza: {varianza_minutos_espectadores}')
    print(f'Desviacion Estandar {desviacion_estaminutos_espectadores}')
    print(f'Coeficiente de Variacion {coeficiente_variacion_espectadores}')
    print(f'Asimetria Pearson {asimetria_espectadores}')
    
    print('''
    _________________________________________________________________________________
    Ejercicio 2: Evaluaciones de clientes sobre el servicio de atencion al cliente puntadas entre 0 y 10
    
    ''')
    
    evaluaciones_clientes = [3,6,6,8,2,5,7,3,8,1,5,6,4,4,2,5,6,2,9,4,2,3,7,7,7]
    
    calculo_frecuencias_absolutas_evaluaciones_clientes = calculo_frecuencias_absolutas(evaluaciones_clientes, 1)
    desviacion_estandar_clientes = desviacion_estandar(evaluaciones_clientes)
    cyb = Diagrama_caja_bigotes(evaluaciones_clientes)
    cyb_q1 = cyb.q1
    cyb_q2 = cyb.q2
    cyb_q3 = cyb.q3
    
    print(f'Frecuencias absolutas: {calculo_frecuencias_absolutas_evaluaciones_clientes}')
    print(f'Desviacion estandar: {desviacion_estandar_clientes}')
    print(f'Cuartil 1: {int(cyb_q1)}, cuartil 2: {int(cyb_q2)}, cuartil 3: {int(cyb_q3)}')
    
    
    print('''
    _______________________________________________________________
    Ejercicio 3: numero de ordenadores de 200 familias de una ciudad española en 2016
    
    ''')
    ordenadores_familia = {0:8, 1:102, 2:85, 3:5}
    
    media_ordenadores = media(ordenadores_familia)
    mediana_ordenadores = mediana(ordenadores_familia)
    moda_ordenadores = moda(ordenadores_familia)
    desviacion_estandar_ordenadores = desviacion_estandar(ordenadores_familia)
    coeficiente_variacion_ordenadores = coeficiente_variacion(ordenadores_familia)
    asimetria_pearson_ordenadores = asimetria_pearson(ordenadores_familia)
    
    print(ordenadores_familia)
    print(f'Media: {media_ordenadores}, mediana: {mediana_ordenadores}, moda: {moda_ordenadores}, stdev: {desviacion_estandar_ordenadores}, cv: {coeficiente_variacion_ordenadores}, pearson: {asimetria_pearson_ordenadores}')