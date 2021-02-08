import random


def tirar_dado():
    resultado_tiro = random.randint(1, 6)
    return resultado_tiro


def secuencias_tiros(dados, tiros, secuencias):
    secuencias_tiros = []

    for i in range(secuencias):
        listado_tiros = []

        for i in range(tiros):
            for k in range(dados):
                resultado_tiro = tirar_dado()
                listado_tiros.append(resultado_tiro)

        secuencias_tiros.append(listado_tiros)

    return secuencias_tiros


def determinar_probabilidad(dados, tiros, secuencias):
    secuencias_de_tiros = secuencias_tiros(dados, tiros, secuencias)
    cantidad_de_1 = 0
    cantidad_de_no_1 = 0

    for secuencia in secuencias_de_tiros:
        if 1 in secuencia:
            cantidad_de_1 += 1
        else:
            cantidad_de_no_1 += 1

    probabilidad_de_1 = cantidad_de_1 / secuencias
    probabilidad_de_no_1 = cantidad_de_no_1 / secuencias

    print(
        f'Probabilidades con {dados} dado(s) realizando {tiros} tiros en {secuencias} secuencias:\n'
        f'Probabilidad de 1 = {probabilidad_de_1}\n'
        f'Probabilidad de "no" 1 = {probabilidad_de_no_1}'
    )


if '__main__' == __name__:
    dados = int(input('Cuantos dados: '))
    tiros = int(input('Cuantos tiros: '))
    secuencias = int(input('Cuantos secuencias: '))

    determinar_probabilidad(dados, tiros, secuencias)
