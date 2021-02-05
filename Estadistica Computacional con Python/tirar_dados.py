import random


def tirar_dado():
    resultado = random.randint(1, 6)
    return resultado


def main(dados, tiros, repeticiones):
    '''Simulacion de tiro de dados'''

    # Pör cada repeticion
    for repeticion in range(repeticiones):
        probabilidad_x_repeticion = dict(zip(
            [num for num in range(1, 7)],
            [[None] for num in range(1, 7)]
        ))

        # Por cada tiro
        for tiro in range(tiros):
            lista_numeros_obtenidos = []

            # Por cada dado
            for dado in range(dados):
                numero_obtenido = tirar_dado()
                lista_numeros_obtenidos.append(numero_obtenido)

            probabilidad_x_tiro = dict(zip(
                [num for num in range(1, 7)],
                [lista_numeros_obtenidos.count(
                    num)/len(lista_numeros_obtenidos) for num in range(1, 7)]
            ))

            # Agregar probabilidades de cada numero obtenidas por cada tiro, a cada intento:
            for key, value in probabilidad_x_tiro.items():

                if probabilidad_x_repeticion[key] == [None]:
                    probabilidad_x_repeticion[key] = [value]
                else:
                    probabilidad_x_repeticion[key].append(value)

        # Promedio de las probabilidades totales obtenidas por cada numero
        for key in probabilidad_x_repeticion:
            average = round(sum(probabilidad_x_repeticion[key]) /
                            len(probabilidad_x_repeticion[key]), 3)
            probabilidad_x_repeticion[key] = average

    return probabilidad_x_repeticion


if '__main__' == __name__:
    dados = int(input('Cuantos dados: '))
    tiros = int(input('Cuantos tiros: '))
    repeticiones = int(input('Cuantas repeticiones: '))

    prueba = main(dados, tiros, repeticiones)
    for key, value in prueba.items():
        print(f'Probabilidad de {key}: {value}')
