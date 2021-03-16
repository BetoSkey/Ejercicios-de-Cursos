from busqueda_binaria import Busqueda_binaria
from formulas_estadisticas import media
import unittest


def medidas_posicion(datos, k=4):
    '''Calcula la posicion para la agrupacion de los datos en cuartiles, deciles y percentiles'''

    n = len(datos)
    if k != 4 and k != 10 and k != 100:
        raise NameError('"k" solo puede ser 4, 10 o 100')

    tipo = 'Q' if k == 4 else 'D' if k == 10 else 'P' if k == 100 else 'error'
    par = True if n % 2 == 0 else False
    analisis_binario = Busqueda_binaria(datos)
    datos_ordenados = analisis_binario.ordenamiento_insercion()

    ubicaciones_k = []
    valor_ubicaciones_k = {}

    # Si es par
    if par == True:
        for q in range(k-1):

            ubicaciones_k.append(
                ((tipo + str(q + 1)), round((((q+1)*n) / k) - 1, 3)))

        for i in ubicaciones_k:
            print(i[1])
            # si n= par y la ubicacion encontrada no tiene decimales,
            # quiere decir que se encontraron dos ubicaciones intermedias y se deberan promediar
            if i[1] < 0:
                valor_ubicaciones_k[i[0]] = datos_ordenados[0]

            elif i[1] - int(i[1]) == 0:

                valor_ubicaciones_k[i[0]] = media(
                    [
                        datos_ordenados[int(i[1])],
                        datos_ordenados[int((i)[1] + 1)]
                    ]
                )

            else:
                valor_ubicaciones_k[i[0]] = datos_ordenados[round(i[1])]

    # Si no es par
    else:
        for q in range(k-1):
            ubicaciones_k.append(
                ((tipo + str(q + 1)), round((((q+1) * (n + 1)) / k) - 1, 3)))

        print(ubicaciones_k)

        for i in ubicaciones_k:
            print(i)

            if i[1] < 0:
                valor_ubicaciones_k[i[0]] = datos_ordenados[0]

            elif i[1] - int(i[1]) == 0:

                valor_ubicaciones_k[i[0]] = media(
                    [
                        datos_ordenados[int(i[1])],
                        datos_ordenados[int((i)[1] + 1)]
                    ]
                )

            else:
                valor_ubicaciones_k[i[0]] = datos_ordenados[round(i[1])]

    print(valor_ubicaciones_k)
    return valor_ubicaciones_k


class Pruebas_caja_cristal(unittest.TestCase):

    def test_cuartiles_lista1(self):
        formula_agrupar_datos = medidas_posicion(lista1)

        self.assertEqual(
            formula_agrupar_datos, {
                'Q1': 3.0, 'Q2': 6.0, 'Q3': 9.0
            }
        )

    def test_cuartiles_lista2(self):
        formula_agrupar_datos = medidas_posicion(lista2)

        self.assertEqual(formula_agrupar_datos, {
            'Q1': 1.0, 'Q2': 3.0, 'Q3': 5.0})

    def test_deciles_lista1(self):
        formula_agrupar_datos = medidas_posicion(lista1, k=10)

        self.assertEqual(formula_agrupar_datos, {})

    def test_percentiles_lista1(self):
        self.maxDiff = None
        formula_agrupar_datos = medidas_posicion(lista1, k=100)

        self.assertEqual(formula_agrupar_datos, {})


if '__main__' == __name__:

    lista1 = [33, 26, 66, 45, 28, 59, 33, 36, 26, 45, 62, 45]
    lista2 = [55, 87, 74, 70, 82, 62, 59, 65]
    lista3 = [
        1000, 1000, 2500, 2500, 2500, 3500, 4000,
        5300, 9000, 12500, 13500, 24500, 27500, 30300, 41000
    ]

    lista4 = [
        27, 22, 19, 46, 41, 16, 28, 35, 33, 39, 54,
        60, 53, 48, 65, 76, 68, 83, 89, 92, 103, 85, 57, 43, 59
    ]

    lista5 = [
        15, 17, 16, 16, 15, 17, 15, 18, 14, 16, 15
    ]

    # print(Busqueda_binaria(lista1).ordenamiento_insercion())

    print(Busqueda_binaria(lista5).ordenamiento_insercion())
    # datos_agrupados = medidas_posicion(lista1)
    # print(datos_agrupados)

    # unittest.main()
    medidas_posicion(lista5, k=100)
