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
    def __str__(self):
        return str(self.baraja)

    def obtener_mano(self, baraja, tamano_mano):
        baraja = self.baraja
        mano = random.sample(baraja, tamano_mano)
        for i in mano:
          self.baraja.remove(i)
        return mano

if '__main__' == __name__:
    baraja = Baraja()

    print(f'\nBaraja ({len(baraja.baraja)}cartas):\n {baraja}')

    mano = baraja.obtener_mano(baraja, 5)
    
    print(f'\nMano:\n {mano}')

    print(f'\nBaraja ({len(baraja.baraja)}cartas):\n {baraja}')

    mano = baraja.obtener_mano(baraja, 5)

    print(f'\nMano:\n {mano}')

    print(f'\nBaraja ({len(baraja.baraja)}cartas):\n {baraja}')
    mano = baraja.obtener_mano(baraja, 5)
    print(f'\nMano:\n {mano}')
    mano = baraja.obtener_mano(baraja, 5)
    print(f'\nMano:\n {mano}')
    mano = baraja.obtener_mano(baraja, 5)
    print(f'\nMano:\n {mano}')

    print(f'\nBaraja ({len(baraja.baraja)}cartas):\n {baraja}')