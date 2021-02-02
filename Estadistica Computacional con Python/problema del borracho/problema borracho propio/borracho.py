import random


class Borracho:
    def __init__(self, ubicacion_inicial=(0, 0)):
        self.ubicacion_inicial = ubicacion_inicial
        self.ubicaciones = [self.ubicacion_inicial]

    def obtener_nueva_coordenada(self):
        nueva_coordenada = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
        return nueva_coordenada

    def mover_borracho(self):
        nueva_ubicacion = (self.ubicaciones[-1][0] + self.obtener_nueva_coordenada(
        )[0], + self.ubicaciones[-1][1] + self.obtener_nueva_coordenada()[1])
        self.ubicaciones.append(nueva_ubicacion)

    def caminar_borracho(self, pasos):
        for i in range(pasos):
            self.mover_borracho()

    def calcular_alejamiento(self):
        delta_x = self.ubicaciones[-1][0] - self.ubicaciones[0][0]
        delta_y = self.ubicaciones[-1][1] - self.ubicaciones[0][1]

        return (round((delta_x**2 + delta_y**2)**.05, 3))


if __name__ == '__main__':
    borracho1 = Borracho()
    borracho1.caminar_borracho(20)
    print(borracho1.ubicaciones)
    print(borracho1.calcular_alejamiento())
