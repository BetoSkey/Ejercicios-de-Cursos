import random


class Baraja:
    PALOS = [
        'Diamantes Rojo', 'Corazones Rojo',
        'Espadas Negra', 'Treboles Negro'
    ]
    VALORES = [
        'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina',
        'Rey'
    ]
    ESCALERAS = [
        ['As',	'2',	'3',	'4',	'5'],
        ['2',	'3',	'4',	'5',	'6'],
        ['3',	'4',	'5',	'6',	'7'],
        ['4',	'5',	'6',	'7',	'8'],
        ['5',	'6',	'7',	'8',	'9'],
        ['6',	'7',	'8',	'9',	'10'],
        ['7',	'8',	'9',	'10',	'Jota'],
        ['8',	'9',	'10',	'Jota',	'Reina'],
        ['9',	'10',	'Jota',	'Reina',	'Rey'],
        ['10',	'Jota',	'Reina',	'Rey', 'As'],
        ['Jota',	'Reina',	'Rey', 'As', '2'],
        ['Reina',	'Rey', 'As', '2', '3'],
        ['Rey', 'As', '2', '3', '4']
    ]

    def __init__(self):
        self.baraja = [
            (valor, palo) for palo in self.PALOS
            for valor in self.VALORES
        ]

    def obtener_mano(self, baraja, tamano_mano):
        baraja = self.baraja
        mano = random.sample(baraja, tamano_mano)

        return mano


def main(tamano_mano, simulaciones=1):
    baraja = Baraja()
    # Creacion de diccionarios dentro de un diccionario de escaleras.
    escaleras = [
        (dict([(id, value) for id, value in enumerate(list)]))
        for list in baraja.ESCALERAS
    ]
    manos = []
    par = 0
    dos_pares = 0
    tercia = 0
    poquer = 0
    escalera = 0
    full = 0

    for simulacion in range(simulaciones):
        mano = baraja.obtener_mano(baraja, tamano_mano)
        manos.append(mano)

    for mano in manos:
        numeros = []
        par_mano = 0
        tercia_mano = 0
        escalera_mano = 0
        poquer_mano = 0

        # Agregar numeros de la mano a lista de numeros para analisis
        for carta in mano:
            numeros.append(carta[0])
        numeros_coincidentes_escalera = 0

        # Analisis de los numeros
        if all(
            dict(
                [(id, value) for id, value in enumerate(numeros)]
            )[k] in escaleras[0].values()
            for k in dict([(id, value) for id, value in enumerate(numeros)])
        ):
            escalera_mano += 1
            print(f'True numeros en escalera {numeros}, {escaleras[0]}')

        for numero in numeros:
            # Contar las jugadas
            if numeros.count(numero) == 4:
                poquer_mano += 1
                for i in range(3):
                    numeros.remove(numero)

            elif numeros.count(numero) == 3:
                tercia_mano += 1
                for i in range(2):
                    numeros.remove(numero)

            elif numeros.count(numero) == 2:
                par_mano += 1
                for i in range(1):
                    numeros.remove(numero)

        # Probabilidades
        if poquer_mano >= 1:
            poquer += 1
            tercia += 1
            par += 1
        elif tercia_mano >= 1 and par_mano >= 1:
            full += 1
            par += 1
            tercia += 1
        elif tercia_mano == 1:
            par += 1
            tercia += 1
        elif par_mano == 2:
            dos_pares += 1
            par += 1
        elif par_mano == 1:
            par += 1

    probabilidad_par = par/simulaciones
    probabilidad_dos_pares = dos_pares/simulaciones
    probabilidad_tercia = tercia/simulaciones
    probabilidad_full = full/simulaciones
    probabilidad_poquer = poquer/simulaciones

    print(f'Probabilidades:\nPar: {probabilidad_par}\nDos pares: {probabilidad_dos_pares}\nTercia: {probabilidad_tercia}\nFull: {probabilidad_full}\nPoquer: {probabilidad_poquer}')


if '__main__' == __name__:
    #print(baraja, f'\n\n Cantidad de cartas: {len(baraja)}')
    #print(f'Mano: {obtener_mano(baraja,5)}')
    tamano_mano = int(input('Tamaño de mano: '))
    intentos = int(input('Cuantas simulaciones: '))

    main(tamano_mano, intentos)
