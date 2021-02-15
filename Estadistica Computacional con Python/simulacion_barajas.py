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

    ESCALERA_REAL = {0:['10',	'Jota',	'Reina',	'Rey', 'As']}

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
    color = 0
    full = 0
    escalera_color = 0
    escalera_real = 0

    for simulacion in range(simulaciones):
        mano = baraja.obtener_mano(baraja, tamano_mano)
        manos.append(mano)

    for mano in manos:
        numeros_mano = []
        palos_mano = []
        par_mano = 0
        tercia_mano = 0
        escalera_mano = 0
        poquer_mano = 0
        color_mano = 0
        escalera_real_mano = 0

        # Agregar numeros de la mano a lista de numeros para analisis
        for carta in mano:
            numeros_mano.append(carta[0])
            palos_mano.append(carta[1])
        #print(palos_mano)
        #---------------------------------------------------------------

        # Analisis de escaleras en mano
        dict_numeros = dict(
                          [(id, value) for id, value in enumerate(numeros_mano)]
        )

        for escalera in range(len(escaleras)):
            # *** Los diccionarios solo aceptan llaves unicas asi que para remover numeros duplicados, se crea una vairable temporal para revertir los valores a llaves y despues se vuelve a regresar las llaves como valores.
            # *** temp = {val : key for key, val in test_dict.items()}
            # *** res = {val : key for key, val in temp.items()}
            temp = {val: key for key, val in dict_numeros.items()}
            dict_numeros_unicos = {val: key for key, val in temp.items()}
            if len(dict_numeros_unicos) == 5 and all(
                dict_numeros[k] in escaleras[escalera].values()
                for k in dict_numeros
            ):
                escalera_mano += 1
                #print(f'Escalera encontrada,\nnumeros: {numeros_mano}\nEscalera: {escaleras[escalera].values()}')
        #----------------------------------------------------------------------
        # Analisis de Color (Palos) en mano
        dict_palos = dict(
                          [(id, value) for id, value in enumerate(palos_mano)]
        )
        
        temp = {val: key for key, val in dict_palos.items()}
        dict_palos_unicos = {val: key for key, val in temp.items()}

        if len(dict_palos_unicos) == 1:
          color_mano += 1
          #print(dict_palos_unicos.values())
        #----------------------------------------------------------------------

        # Analisis de los numeros
        for numero in numeros_mano:
            # Contar las jugadas
            if numeros_mano.count(numero) == 4:
                poquer_mano += 1
                for i in range(3):
                    numeros_mano.remove(numero)

            elif numeros_mano.count(numero) == 3:
                tercia_mano += 1
                for i in range(2):
                    numeros_mano.remove(numero)

            elif numeros_mano.count(numero) == 2:
                par_mano += 1
                for i in range(1):
                    numeros_mano.remove(numero)
        
        #-------------------------------------------------------------

        # Probabilidades
        
        # analisis "escalera de color":
        if color_mano >= 1 and escalera_mano >= 1:
          escalera_color += 1
          color += 1
          escalera += 1
        # analisis de "solo" color
        elif color_mano >= 1:
            color += 1
        # analisis de solo "escalera", como todos los numeros deben ser consecutivos, no se repiten y por tal en una escalera no existen par de cartas
        elif escalera_mano >= 1:
            escalera += 1
        # si hay un poquer es porque hay 4 cartas iguales que se puede analizar como sigue: 
        # (un cuarteto y una carta) o (una tercia y dos carta) o (dos_pares y una carta) o (un par y un par y una carta)

        if poquer_mano >= 1:
            poquer += 1
            tercia += 1
            dos_pares += 1
            par += 1
        # si hay un full es porque hay (tercia y par) o (tecia y dos cartas) o (par y tres cartas)
        elif tercia_mano >= 1 and par_mano >= 1:
            full += 1
            par += 1
            tercia += 1
        # si hay una tercia es porque hay (tercia y dos cartas)
        elif tercia_mano == 1:
            par += 1
            tercia += 1
        # si hay un dos_pares es porque hay (dos_pares y una carta) o (un par y un par y una carta)
        elif par_mano == 2:
            dos_pares += 1
            par += 1
        # si hay un par es porque hay (un par y tres cartas)
        elif par_mano == 1:
            par += 1

    probabilidad_par = par/simulaciones
    probabilidad_dos_pares = dos_pares/simulaciones
    probabilidad_tercia = tercia/simulaciones
    probabilidad_escalera = escalera/simulaciones
    probabilidad_color = color/simulaciones
    probabilidad_full = full/simulaciones
    probabilidad_poquer = poquer/simulaciones
    probabilidad_escalera_color = escalera_color/simulaciones
    #---------------------------------------------------------------------------------------

    # Return de formula
    print(f'Probabilidades:\nPar: {probabilidad_par}\nDos pares: {probabilidad_dos_pares}\nTercia: {probabilidad_tercia}\nEscalera: {probabilidad_escalera}\nColor: {probabilidad_color}\nFull: {probabilidad_full}\nPoquer: {probabilidad_poquer}\nEscalera de color: {probabilidad_escalera_color}')


if '__main__' == __name__:
    #print(baraja, f'\n\n Cantidad de cartas: {len(baraja)}')
    #print(f'Mano: {obtener_mano(baraja,5)}')
    tamano_mano = int(input('Tamaño de mano: '))
    intentos = int(input('Cuantas simulaciones: '))

    main(tamano_mano, intentos)
