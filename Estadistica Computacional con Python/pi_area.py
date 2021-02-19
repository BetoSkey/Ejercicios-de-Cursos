import random


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
