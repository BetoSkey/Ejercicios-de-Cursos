from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    # Nos da las coordenadas iniciales del borracho
    inicio = campo.obtener_coordenada(borracho)

    # Por cada paso nos da la nueva coordenada del borracho simulando que se mueve de lugar
    for _ in range(pasos):
        campo.mover_borracho(borracho)

    # Regresa la distancia entre las coordenadas de inicio y la ultima coordenada del borracho
    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    # Crea una instancia de un borracho
    borracho = tipo_de_borracho(nombre='David')
    # Crea una instancia de coordenada
    origen = Coordenada(0, 0)
    # Lista para almacenar las distancias en cada movimiento del borracho
    distancias = []

    for _ in range(numero_de_intentos):
        # Se crea una instancia de campo que nos regresa las coordenadas de los borrachos
        campo = Campo()
        # Se añade el borracho con su coordenada de origen al campo
        campo.anadir_borracho(borracho, origen)
        # Nos regresa la distancia de caminata del borracho a la cantidad de pasos
        simulacion_caminata = caminata(campo, borracho, pasos)
        # Se agrega la distancia a la lista de distancias redondeandolo para que no tenga ningun decimal
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def graficar(x, y):
    f = figure(
        title='Camino aleatorio',
        x_axis_label='pasos',
        y_axis_label='distancia')

    f.circle(x, y, legend='distancia media')

    show(f)


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_medias_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(
            pasos, numero_de_intentos, tipo_de_borracho)
        print(distancias)
        # Calcular los datos estadisticos
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        distancias_medias_por_caminata.append(distancia_media)

        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

    graficar(x=distancias_de_caminata, y=distancias_medias_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)
