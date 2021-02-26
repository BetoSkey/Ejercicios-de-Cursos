import random
from formulas_estadisticas import modas


def aventar_agujas(agujas):
    dentro_del_circulo = 0

    for aguja in range(agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        # hipotenusa es la discancia desde el centro (teorema de pitagoras)
        distancia_desde_centro = (x**2 + y**2)**.5

        if distancia_desde_centro <= 1:
            dentro_del_circulo += 1

    return (4 * dentro_del_circulo/agujas)


if '__main__' == __name__:
    largo_lista = int(input('Largo de lista: '))
    lista = [random.randint(1, largo_lista) for i in range(largo_lista)]
    print(lista)
    moda_lista = modas(lista)
    print(moda_lista)
