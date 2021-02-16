import random


class Baraja:
    PALOS = [
        'Diamantes Rojo', 'Corazones Rojo', 'Espadas Negra', 'Treboles Negro'
    ]
    VALORES = [
        'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina',
        'Rey'
    ]
    ESCALERAS = [['As', '2', '3', '4', '5'], ['2', '3', '4', '5', '6'],
                 ['3', '4', '5', '6', '7'], ['4', '5', '6', '7', '8'],
                 ['5', '6', '7', '8', '9'], ['6', '7', '8', '9', '10'],
                 ['7', '8', '9', '10', 'Jota'],
                 ['8', '9', '10', 'Jota', 'Reina'],
                 ['9', '10', 'Jota', 'Reina', 'Rey'],
                 ['10', 'Jota', 'Reina', 'Rey', 'As']]

    def __init__(self):
        self.baraja = [(valor, palo) for palo in self.PALOS
                       for valor in self.VALORES]

    def obtener_mano(self, baraja, tamano_mano):
        baraja = self.baraja
        mano = random.sample(baraja, tamano_mano)

        return mano


def main(tamano_mano, simulaciones=1):
    
# Creacion de baraja y diccionarios dentro de un diccionario de escaleras para comparacion.
    baraja = Baraja()
    escaleras = [(dict([(id, value) for id, value in enumerate(list)]))
              for list in baraja.ESCALERAS]

    #Lista de manos obtenidas en cada simulacion
    manos = []

    # Contadores Totales
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
        escalera_mayor_valor_mano = 0

        # Agregar numeros de la mano a lista de numeros para analisis
        for carta in mano:
            numeros_mano.append(carta[0])
            palos_mano.append(carta[1])

        # ---------------------------------------------------------------

        # conversion de lista de numeros a diccionario para comparacion con diccionario de escaleras
        dict_numeros = dict([(id, value)
                             for id, value in enumerate(numeros_mano)])

        #----------------------------------------------------------------

        #Analisis de "Escalera"
        for escaleramano in range(len(escaleras)):
            # *** Los diccionarios solo aceptan llaves unicas asi que para remover numeros duplicados, se crea una vairable temporal para revertir los valores a llaves y despues se vuelve a regresar las llaves como valores.

            temp = {val: key for key, val in dict_numeros.items()}
            dict_numeros_unicos = {val: key for key, val in temp.items()}
            if len(dict_numeros_unicos) == 5 and all(
                    dict_numeros[k] in escaleras[escaleramano].values()
                    for k in dict_numeros):
                escalera_mano += 1
        #---------------------------------------------------------------------

        # Analisis de Color (Palos) en mano
        dict_palos = dict([(id, value) for id, value in enumerate(palos_mano)])

        temp = {val: key for key, val in dict_palos.items()}
        dict_palos_unicos = {val: key for key, val in temp.items()}

        if len(dict_palos_unicos) == 1:
            color_mano += 1

        # ----------------------------------------------------------------------

        # Analisis de "Escalera de mayor valor"
        if all(dict_numeros[k] in escaleras[9].values() for k in dict_numeros):
            escalera_mayor_valor_mano += 1

        # ----------------------------------------------------------------------

        # Analisis de los numeros en la mano
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

        # -------------------------------------------------------------

        # Analisis de JUGADAS de acuerdo a ESCALERAS
        # (si existe escalera no pueden existir cartas duplicadas)

        # analisis "Escalera Real o Flor Imperial":
        if escalera_mayor_valor_mano >= 1 and color_mano >= 1:
            escalera_real += 1
            escalera_color += 1
            color += 1
            escalera += 1
        # analisis "Escalera de Color"
        elif color_mano >= 1 and escalera_mano >= 1:
            escalera_color += 1
            color += 1
            escalera += 1
        # analisis "Color"
        elif color_mano >= 1:
            color += 1
        # analisis "Escalera"
        elif escalera_mano >= 1:
            escalera += 1

        #--------------------------------------------------------------------------

        # Analisis de JUGADAS de acuerdo a la repeticion de sus NUMEROS

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

    #-----------------------------------------------------------------------------------------------

    # Probabilidades
    probabilidad_par = par / simulaciones
    probabilidad_dos_pares = dos_pares / simulaciones
    probabilidad_tercia = tercia / simulaciones
    probabilidad_escalera = escalera / simulaciones
    probabilidad_color = color / simulaciones
    probabilidad_full = full / simulaciones
    probabilidad_poquer = poquer / simulaciones
    probabilidad_escalera_color = escalera_color / simulaciones
    probabilidad_escalera_real = escalera_real / simulaciones
    # ---------------------------------------------------------------------------------------

    # Return de formula
    print(
        f'Probabilidades:\nPar: veces= {par} | probabilidad= {probabilidad_par}\nDos pares: veces= {dos_pares} | probabilidad= {probabilidad_dos_pares}\nTercia: veces={tercia} | probabilidad= {probabilidad_tercia}\nEscalera: veces= {escalera} | probabilidad= {probabilidad_escalera}\nColor: veces= {color} | probabilidad= {probabilidad_color}\nFull: veces= {full} | probabilidad= {probabilidad_full}\nPoquer: veces= {poquer} | probabilidad= {probabilidad_poquer}\nEscalera de color: veces={escalera_color} | probabilidad= {probabilidad_escalera_color}\nEscalera Real (Flor Imperial): veces= {escalera_real} | probabilidad= {probabilidad_escalera_real}'
    )


if '__main__' == __name__:
    #print(baraja, f'\n\n Cantidad de cartas: {len(baraja)}')
    #print(f'Mano: {obtener_mano(baraja,5)}')
    tamano_mano = int(input('Tamaño de mano: '))
    intentos = int(input('Cuantas simulaciones: '))

    main(tamano_mano, intentos)
