import random

class Baraja:
  PALOS = ['Diamantes', 'Corazones', 'Espadas', 'Treboles']
  VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']
  
  def __init__(self):
    self.baraja = [(palo, valor) for palo in self.PALOS for valor in self.VALORES]

  def obtener_mano(self, baraja, tamano_mano):
    baraja = self.baraja
    mano = random.sample(baraja, tamano_mano)

    return mano


def main(tamano_mano, simulaciones=1):
  baraja = Baraja()
  manos = []
  for simulacion in range(simulaciones):
    mano = baraja.obtener_mano(baraja, tamano_mano)
    manos.append(mano)
  
  return manos




if '__main__' == __name__:
  #print(baraja, f'\n\n Cantidad de cartas: {len(baraja)}')
  #print(f'Mano: {obtener_mano(baraja,5)}')
  tamano_mano = int(input('Tamaño de mano: '))
  intentos = int(input('Cuantas simulaciones: '))

  print(main(tamano_mano, intentos))


