import random

def ubicacion_binaria(lista, comienzo, final, objetivo, ubicacion_meta=0):

    if final-comienzo == 1:  # Si la lista se acoto a dos ubicaciones
        if objetivo > lista[final]:

            if final + 1 > len(lista)-1:
                ubicacion_meta = len(lista)-1
            else:
                ubicacion_meta = final

            return ubicacion_meta
        elif objetivo < lista[comienzo]:
            ubicacion_meta = comienzo

            return ubicacion_meta

    if comienzo == final:  # Si la lista llego al final de su acote y solo nos indica una ubicacion

        # Si el objetivo no se encontro y es mayor que el acotamiento final
        if objetivo > lista[final]:
            # Si la ubicacion meta es mas grande que la lista completa
            if final + 1 > len(lista)-1:
                ubicacion_meta = len(lista)-1

            else:
                ubicacion_meta = final + 1

        # Si estamos al principio de la lista o el objetivo es igual que el acotamiento final
        elif comienzo == 0 or objetivo == lista[final]:
            pass

        else:
            ubicacion_meta += 1

        return ubicacion_meta

    # Aqui empieza a acotar la busqueda
    medio = (comienzo + final) // 2  # Se acota la lista a la mitad

    if objetivo == lista[medio]:  # Si el objetivo se encontro en la mitad
        return medio

    elif objetivo > lista[medio]:  # Si el objetivo es mayor que la mitad
        ubicacion_meta = medio
        return ubicacion_binaria(lista, medio + 1, final, objetivo, ubicacion_meta)

    else:  # Si el objetivo es menor que la mitad
        return ubicacion_binaria(lista, comienzo, medio - 1, objetivo, ubicacion_meta)

def ordenamiento_insercion(lista):
    lista_ordenada = [lista[0]]
    lista_desordenada = lista[1:]
    n_lista_ordenada = len(lista_ordenada)-1
    n_lista_desordenada = len(lista_desordenada)-1

    # Por cada ubicacion de la lista desordenada
    for ubicacion_en_lista_desordenada in range(n_lista_desordenada+1):

        # Encuentra la ubicacion en la lista ordenada
        ubicacion = ubicacion_binaria(
            lista_ordenada, 0, n_lista_ordenada, lista_desordenada[ubicacion_en_lista_desordenada])

        # Si el numero desordenado es mayor que el de la ubicacion encontrada
        if lista_desordenada[ubicacion_en_lista_desordenada] > lista_ordenada[ubicacion]:

            # Si la ubicacion encontrada es igual que el final de la lista, se agrega al final
            if ubicacion == n_lista_ordenada:
                lista_ordenada.append(
                    lista_desordenada[ubicacion_en_lista_desordenada])

            # Si el numero no esta al final de la lista, se inserta en la siguiente ubicacion encontrada
            else:
                lista_ordenada.insert(
                    ubicacion + 1, lista_desordenada[ubicacion_en_lista_desordenada])
            n_lista_ordenada += 1

        # Si el numero desordenado es menor o igual que el de la ubicacion encontrada
        else:
            lista_ordenada.insert(
                ubicacion, lista_desordenada[ubicacion_en_lista_desordenada])
            n_lista_ordenada += 1

    return lista_ordenada


def media(lista):
    return sum(lista) / len(lista)

def media_muestra(lista):
    return sum(lista) / (len(lista)-1)

def mediana(lista):
  lista_ordenada = ordenamiento_insercion(lista)

  if len(lista_ordenada)%2 >0:
    mediana = lista_ordenada[int(round(len(lista_ordenada)/2,0)-1)]
  else:
    numero_medio1 = lista_ordenada[int(round(len(lista_ordenada)/2,0)-1)]
    numero_medio2 = lista_ordenada[int(round(len(lista_ordenada)/2,0))]

    mediana = media([numero_medio1,numero_medio2])
  
  return mediana

def varianza_poblacion(lista):
  media_lista = media(lista)
  diferencias_vs_media = []
  
  for i in range(len(lista)):
    diferencia = (lista[i] - media_lista)**2
    diferencias_vs_media.append(diferencia)
  
  varianza = media(diferencias_vs_media)

  return varianza

def desviacion_estandar_poblacion(lista):
  varianza_lista = varianza_poblacion(lista)
  sigma = varianza_lista**0.5
  return sigma

def varianza_muestra(lista):
  media_lista = media(lista)
  diferencias_vs_media = []
  
  for i in range(len(lista)):
    diferencia = (lista[i] - media_lista)**2
    diferencias_vs_media.append(diferencia)
  
  varianza = media_muestra(diferencias_vs_media)

  return varianza

def desviacion_estandar_muestra(lista):
  varianza_lista = varianza_muestra(lista)
  sigma = varianza_lista**0.5
  return sigma

def valor_z_poblacion(lista):
  media_lista = media(lista)
  desviacion_estandar_poblacion_lista = desviacion_estandar_poblacion(lista)
  lista_valor_z = []

  for i in range(len(lista)):
    valor_z = (lista[i] - media_lista) / desviacion_estandar_poblacion_lista 
    lista_valor_z.append((lista[i], round(valor_z,2)))

  return lista_valor_z

if '__main__' == __name__:
  largo_lista = int(input('Largo de lista: '))
  lista = [random.randint(1, largo_lista) for i in range(largo_lista)]
  #lista = [26, 33, 65, 28, 34, 55, 25, 44, 50, 36, 26, 37, 43, 62, 35, 38, 45, 32, 28, 34]
  lista_ordenada = ordenamiento_insercion(lista)
  print(f'Lista Original: {lista}\nLista Ordenada: {lista_ordenada}')

  print(f'Media: {media(lista_ordenada)}\nMediana: {mediana(lista_ordenada)}\nVarianza Poblacion: {round(varianza_poblacion(lista),2)}\nsigma Poblacion: {round(desviacion_estandar_poblacion(lista),2)}\nVarianza Muestra: {round(varianza_muestra(lista),2)}\nsigma Muestra: {round(desviacion_estandar_muestra(lista),2)}\nValores z: {valor_z_poblacion(lista)}')
  