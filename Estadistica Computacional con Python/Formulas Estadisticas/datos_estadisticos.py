import pandas


class Datos_estadisticos:
    '''**kwargs (fecha, titulo, descripcion, datos, archivo)'''

    def __init__(self, muestra=True, **kwargs):
        accepted_kwargs = ['fecha', 'titulo',
                           'descripcion', 'datos', 'archivo', 'x', 'y']

        self.muestra = muestra
        self.attributes = kwargs

        for kwarg in self.attributes.keys():
            if kwarg == 'archivo':
                self.__setattr__('archivo', pandas.read_csv(kwargs[kwarg]))
            elif kwarg == 'x':
                self.__setattr__('x', self.archivo[kwargs[kwarg]])
            elif kwarg == 'y':
                self.__setattr__('y', self.archivo[kwargs[kwarg]])
            elif kwarg in accepted_kwargs:
                self.__setattr__(kwarg, kwargs[kwarg])
            else:
                raise NameError(f'"{kwarg}" is not a valid attribute')

    def __str__(self):
        return f'''
Titulo: {self.titulo if 'titulo' in self.attributes else 'Sin Titulo'}
Descripcion: {
    self.descripcion if 'descripcion' in self.attributes else 'Sin Descripcion'}
Datos de {'muestra' if self.muestra else 'poblacion'}:
{self.archivo if 'archivo' in self.attributes else self.datos}
{('y=', self.y) if 'y' in self.attributes else None}
        '''


if '__main__' == __name__:

    datos1 = Datos_estadisticos(archivo='fdp.csv', x='z', y='prob', titulo='Datos 1',
                                descripcion='Muestra de datos de la poblacion de estudiantes de 2° grado')

    datos2 = Datos_estadisticos(datos={'Diva': 28, 'Gilberto': 42, 'Jessica': 27, 'Connie': 30}, muestra=False,
                                titulo='Edades de compradores', descripcion='Compradores del departamento en los ultimos 5 años')
    print(datos1)
    print(datos2)
