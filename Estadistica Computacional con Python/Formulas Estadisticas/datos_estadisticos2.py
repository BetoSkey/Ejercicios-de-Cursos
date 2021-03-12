import pandas


class Datos_estadisticos:
    '''
    **kwargs (fecha_registro, titulo, descripcion, datos, archivo)

    --muestra:
        este parametro permite calcular su estadistica basada en una muestra

    Recibe lista, diccionario o el url de un  archivo en el parametro "datos"

    En caso de recibir el url de un archivo, lo convierte a diccionario "dict(columna1: columna2)"
    '''

    def __init__(self, datos, muestra=True, **kwargs):
        accepted_kwargs = [
            'fecha_registro', 'titulo', 'descripcion', 'fecha_inicial_datos',
            'fecha_final_datos', 'archivo']
        self.datos = datos
        self.muestra = muestra
        self.attributes = kwargs

        if type(self.datos) == str:
            self.__setattr__('archivo', pandas.read_csv(self.datos))
            self.__setattr__(
                'dict_datos', self.archivo.to_dict(orient='list'))
            columna1 = [i for i in enumerate(
                self.dict_datos.values())][0][1]
            columna2 = [i for i in enumerate(
                self.dict_datos.values())][1][1]
            self.__setattr__('datos',  dict(zip(columna1, columna2)))

        for kwarg in self.attributes.keys():

            if kwarg in accepted_kwargs:
                self.__setattr__(kwarg, kwargs[kwarg])

            else:
                raise NameError(f'"{kwarg}" is not a valid attribute')

    def __str__(self):

        return f'''
-----------------------------------------------------------------------------------------------------------
Titulo: {self.titulo if 'titulo' in self.attributes else 'Sin Titulo'}
{'Fecha de registro: ' if 'fecha_registro' in self.attributes else ''}{self.attributes['fecha_registro'] if 'fecha_registro' in self.attributes else ''}
Descripcion: {
    self.descripcion if 'descripcion' in self.attributes else 'Sin Descripcion'}

{'Muestra' if self.muestra else 'Poblacion'}:
{'Fecha inicial: ' if 'fecha_inicial_datos' in self.attributes else ''}{self.attributes['fecha_inicial_datos'] if 'fecha_inicial_datos' in self.attributes else ''}
{'Fecha final: ' if 'fecha_final_datos' in self.attributes else ''}{self.attributes['fecha_final_datos'] if 'fecha_final_datos' in self.attributes else ''}
{'Archivo: ' if 'archivo' in self.attributes else ''}{self.attributes['archivo'] if 'archivo' in self.attributes else ''}
{self.archivo if 'archivo' in self.attributes else self.datos}
------------------------------------------------------------------------------------------------------------
'''


if '__main__' == __name__:

    datos1 = Datos_estadisticos('fdp.csv', titulo='Datos 1',
                                descripcion='Estudiantes de 2° grado', muestra=False)

    datos2 = Datos_estadisticos({'Diva': 28, 'Gilberto': 42, 'Jessica': 27, 'Connie': 30}, muestra=True, fecha_registro='2021-03-10', titulo='Edades de compradores',
                                descripcion='Compradores del departamento en los ultimos 5 años', fecha_inicial_datos='2020-05-01', fecha_final_datos='2021-01-01')

    datos3 = Datos_estadisticos([30, 59, 200, 29, 234, 33], fecha_registro='2021-03-10',
                                descripcion='Consumos de los ultimos 6 meses', titulo='Consumos de almacen')
    print(datos1)
    print(datos2)
    print(datos3)
