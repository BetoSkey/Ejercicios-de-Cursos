import sys
sys.path.append('../Estadistica Computacional con Python/Formulas Estadisticas/')

from formulas_estadisticas import calculo_frecuencias_absolutas, media, mediana, moda, medidas_posicion, Diagrama_caja_bigotes


if '__main__' == __name__:

    lista1 = [
        60, 66, 77, 70, 66, 68, 57, 70, 66, 52, 75, 65, 69, 71, 58, 66, 67, 74, 
        61, 63, 69, 80, 59, 66, 70, 67, 78, 75, 64, 71, 81, 62, 64, 69, 68, 72, 
        83, 56, 65, 74, 67, 54, 65, 65, 69, 61, 67, 73, 57, 62, 67, 68, 63, 67, 
        71, 68, 76, 61, 62, 63, 76, 61, 67, 67, 64, 72, 64, 73, 79, 58, 67, 71, 
        68, 59, 69, 70, 66, 62, 63, 66
    ]

    iva = [.16, .20, .06, .06, .07, .17, .06, .22]

    #fa = calculo_frecuencias_absolutas(lista1, 5)
    #print(fa)

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

