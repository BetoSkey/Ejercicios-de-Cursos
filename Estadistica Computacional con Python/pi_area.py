import random
from formulas_estadisticas import desviacion_estandar_poblacion, media


def aventar_agujas(agujas):
    dentro_del_circulo = 0

    for aguja in range(agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        # hipotenusa es la discancia desde el centro (teorema de pitagoras), ya que generaremos triangulos cuadrados desde algun punto de "x" y "y" aleatoriamente
        distancia_desde_centro = (x**2 + y**2)**.5

        if distancia_desde_centro <= 1:
            dentro_del_circulo += 1

    return dentro_del_circulo

def estimacion_pi(agujas):
    agujas_dentro_de_circulo = aventar_agujas(agujas)

    estimacion_pi = (4*agujas_dentro_de_circulo)/agujas

    return estimacion_pi

def simulaciones_estimacion_pi(agujas, intentos):
  '''Regresa la media y desviacion estandar de los resultados de las estimaciones de pi de cada intento'''
  estimaciones_pi = []
  
  for intento in range(intentos):
    intento_estimacion_pi = estimacion_pi(agujas)
    estimaciones_pi.append(intento_estimacion_pi)

  media_estimaciones_pi = media(estimaciones_pi)
  sigma_estimaciones_pi = desviacion_estandar_poblacion(estimaciones_pi)

  print(f'''
    Estimado de pi={round(media_estimaciones_pi, 5)}, 
    sigma de pi={round(sigma_estimaciones_pi, 5)}
    ''')

  return(media_estimaciones_pi, sigma_estimaciones_pi)

def precision_estimacion_pi(sigma_meta, intentos):
    agujas = 1000
    sigma = sigma_meta


    while sigma >= precision / 1.96:
        media_estimaciones_pi, sigma_estimaciones_pi = simulaciones_estimacion_pi(agujas, intentos)
        agujas *= 2
    
    return media_estimaciones_pi
 
if '__main__' == __name__:
  precision_estimacion_pi(.01, 1000)





if '__main__' == __name__:
    largo_lista = int(input('Largo de lista: '))
    lista = [random.randint(1, largo_lista) for i in range(largo_lista)]
    print(lista)
    moda_lista = modas(lista)
    print(moda_lista)
