import random


def tirar_dado():
    resultado = random.randint(1, 6)
    return resultado


def main(dados, tiros, repeticiones):
    '''Simulacion de tiro de dados'''
    probabilidades_totales = dict(zip(
            [num for num in range(1, 7)],
            [[None] for num in range(1, 7)]
        ))
    # Pör cada repeticion
    for repeticion in range(repeticiones):
        probabilidad_x_repeticion = dict(zip(
            [num for num in range(1, 7)],
            [[None] for num in range(1, 7)]
        ))

        # Por cada tiro
        for tiro in range(tiros):
            #lista_numeros_obtenidos = []
            probabilidad_x_tiro = dict(zip(
            [num for num in range(1, 7)],
            [[None] for num in range(1, 7)]
        ))
            # Por cada dado
            for dado in range(dados):
                numero_obtenido = tirar_dado()
                #lista_numeros_obtenidos.append(numero_obtenido)
                probabilidad_x_dado = dict(zip(
                [num for num in range(1, 7)],
                [(1/(dados*6) if num == numero_obtenido else 0.0) for num in range(1, 7)]
            ))
                print(f'Probabilidad x dado: {probabilidad_x_dado}')
                # Agregar probabilidades de cada numero obtenidas por cada tiro, a cada intento:
                for key, value in probabilidad_x_dado.items():

                    if probabilidad_x_tiro[key] == [None]:
                        probabilidad_x_tiro[key] = [value]
                    else:
                        probabilidad_x_tiro[key].append(value) 
            print(f'Probabilidad x tiro: {probabilidad_x_tiro}')            
            #probabilidad_x_tiro = dict(zip(
            #    [num for num in range(1, 7)],
            #    [lista_numeros_obtenidos.count(
            #        num)/len(lista_numeros_obtenidos) for num in range(1, 7)]
            #))
            for key in probabilidad_x_tiro:
                #average = round(sum(probabilidad_x_tiro[key]) /
                #                len(probabilidad_x_tiro[key]), 3)
                #probabilidad_x_tiro[key] = average

                average = sum(probabilidad_x_tiro[key]) / tiros
                probabilidad_x_tiro[key] = average
            print(f'Promedio de probabilidades x tiro: {probabilidad_x_tiro}')
            # Agregar probabilidades de cada numero obtenidas por cada tiro, a cada intento:
            for key, value in probabilidad_x_tiro.items():

                if probabilidad_x_repeticion[key] == [None]:
                    probabilidad_x_repeticion[key] = [value]
                else:
                    probabilidad_x_repeticion[key].append(value)
    
        # Promedio de las probabilidades x repeticion obtenidas por cada numero
        for key in probabilidad_x_repeticion:
            #average = round(sum(probabilidad_x_repeticion[key]) /
            #                len(probabilidad_x_repeticion[key]), 3)
            #probabilidad_x_repeticion[key] = average
            
            average = sum(probabilidad_x_repeticion[key]) / repeticiones
            probabilidad_x_repeticion[key] = average

        # Agregar probabilidades de cada repeticion a la lista de probabilidades totales
        for key, value in probabilidad_x_repeticion.items():

                if probabilidades_totales[key] == [None]:
                    probabilidades_totales[key] = [value]
                else:
                    probabilidades_totales[key].append(value)
    # Promedio de las probabilidades totales de todos los intentos
    print(probabilidades_totales)
    for key in probabilidades_totales:
            average = round(sum(probabilidades_totales[key]) /
                            len(probabilidades_totales[key]), 3)
            probabilidades_totales[key] = average
                
    return probabilidades_totales


if '__main__' == __name__:
    dados = int(input('Cuantos dados: '))
    tiros = int(input('Cuantos tiros: '))
    repeticiones = int(input('Cuantas repeticiones: '))

    prueba = main(dados, tiros, repeticiones)
    for key, value in prueba.items():
        print(f'Probabilidad de {key}: {value}')
