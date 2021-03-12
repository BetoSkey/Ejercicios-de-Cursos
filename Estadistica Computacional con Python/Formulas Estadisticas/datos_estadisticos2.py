import pandas as pd
from formulas_estadisticas import media, mediana, moda, varianza, desviacion_estandar

class Dictionary_data_maker:
    '''Crea un diccionario de datos agrupados a partir de un archivo; el archivo
  debe contener:\n 
  columna1 = Agrupaciones\n  (deben ser Intervalos de numeros)
  columna2 = (FA) Frecuencias absolutas
    '''
    def __init__(self, archivo):
      self.df = pd.read_csv(archivo)
      self.dict_datos = self.df.to_dict(orient='list')
    
    def create_data_dictionary(self):
      columns_qty = len(self.df.columns)
      columns_info = []

      for i in range(columns_qty):
            columns_info.append([i for i in enumerate(self.dict_datos.values())][i][1])

      datos = dict(zip(columns_info[0], columns_info[1]))

      return datos


class Datos_estadisticos:
    '''
    **kwargs (fecha_registro, descripcion, observaciones, datos, archivo)

    --muestra:
        este parametro permite calcular su estadistica basada en una muestra

    Recibe lista, diccionario o el url de un  archivo en el parametro "datos"

    En caso de recibir el url de un archivo, lo convierte a diccionario "dict(columna1: columna2)"

    *** ojo *** solo recibe diccionarios con intervalos de numeros en la primer columna de agrupaciones
    '''

    def __init__(self, datos, muestra=True, **kwargs):
        accepted_kwargs = [
            'fecha_registro', 'descripcion', 'observaciones', 'fecha_inicial_datos',
            'fecha_final_datos']
        self.datos = datos
        self.muestra = muestra
        self.attributes = kwargs
        self.archivo = None
        

        if type(self.datos) == str:
            dictionary_maker = Dictionary_data_maker(self.datos)
            dict_archivo = dictionary_maker.create_data_dictionary()
            self.archivo = dictionary_maker.df
            self.datos = dict_archivo
            

        for kwarg in self.attributes.keys():

            if kwarg in accepted_kwargs:
                self.__setattr__(kwarg, kwargs[kwarg])

            else:
                raise NameError(f'"{kwarg}" is not a valid attribute')

        self.media = media(self.datos)
        self.mediana = mediana(self.datos)
        self.moda = moda(self.datos)
        self.varianza = varianza(self.datos)
        self.desviacion_estandar = desviacion_estandar(self.datos)

    def __str__(self):

        return (f'''
-------------------------------------
Descripcion: {self.descripcion if 'descripcion' in self.attributes else 'Sin descripcion'}
{'Fecha de registro: ' if 'fecha_registro' in self.attributes else ''}{self.attributes['fecha_registro'] if 'fecha_registro' in self.attributes else ''}
Observaciones: {
    self.observaciones if 'observaciones' in self.attributes else 'Sin observaciones'}

{'Muestra' if self.muestra else 'Poblacion'}:
{'Fecha inicial: ' if 'fecha_inicial_datos' in self.attributes else ''}{self.attributes['fecha_inicial_datos'] if 'fecha_inicial_datos' in self.attributes else ''}
{'Fecha final: ' if 'fecha_final_datos' in self.attributes else ''}{self.attributes['fecha_final_datos'] if 'fecha_final_datos' in self.attributes else ''}

MEDIDAS DE TENDENCIA CENTRAL
Media: {self.media}
Mediana: {self.mediana}
Moda(s): {self.moda}

MEDIDAS DE DISPERCION
Varianza: {self.varianza}
Desviacion estandar: {self.desviacion_estandar}

{'Archivo: ' if 'archivo' in self.attributes else ''}{self.attributes['archivo'] if 'archivo' in self.attributes else ''}
{self.datos if self.archivo is None else self.archivo}
''')


if '__main__' == __name__:

    # Prueba con archivo
    datos1 = Datos_estadisticos(
      'fdp.csv', descripcion='Datos 1', observaciones='Estudiantes de 2° grado', muestra=False
      )

    # Prueba con diccionario
    datos2 = Datos_estadisticos(
      {3: 28, 5: 42, 10: 27, 15: 30}, muestra=True, fecha_registro='2021-03-10', descripcion='Edades de compradores', observaciones='Compradores del departamento en los ultimos 5 años', fecha_inicial_datos='2020-05-01', fecha_final_datos='2021-01-01'
      )
    
    # Prueba con lista
    datos3 = Datos_estadisticos(
      [30, 59, 200, 29, 234, 33], fecha_registro='2021-03-10', observaciones='Consumos de los ultimos 6 meses', descripcion='Consumos de almacen'
      )

    print(datos1)
    print(datos2)
    print(datos3)


