import random

def tirar_dado(): 
  resultado = random.randint(1,6)
  return resultado

def main(dados, tiros, repeticiones):
  
  for repeticion in range(repeticiones):
    probabilidad_x_repeticion ={}
    
    for tiro in range(tiros):
      lista_numeros_obtenidos = []
      
      for dado in range(dados):
        numero_obtenido = tirar_dado()
        lista_numeros_obtenidos.append(numero_obtenido)
      
      probabilidad_x_tiro = dict(zip([num for num in range(1,7)], [lista_numeros_obtenidos.count(num)/len(lista_numeros_obtenidos)for num in range(1, 7)]))
      
      print(probabilidad_x_tiro)
      '''Formula para sumar dos diccionarios:
      new_dict = {}
      for key, value in dict1.items():
        sum_array = [(dict1[key][i] + dict2[key][i]) for i, ele in enumerate(value)]
        new_dict.setdefault(key, sum_array)'''

      #probabilidad_x_repeticion = dict(zip([num for num in range(1,7)],[lista_numeros_obtenidos.count(num)/len(lista_numeros_obtenidos) for num in range(1,7)]))

  return probabilidad_x_repeticion

if '__main__' == __name__:
  dados = int(input('Cuantos dados: '))
  tiros = int(input('Cuantos tiros: '))
  repeticiones = int(input('Cuantas repeticiones: '))

  print(main(dados, tiros, repeticiones))