#Este archivo es un intento por crear una clase que convierta la informacion en arrays 
# para un analisis estadistico de la informacion, aun no se termina, se necesita estudiar numpy y pandas para lograrlo.

from collections import Counter
import numpy as np


class Tabla:
    '''Clase para creacion de tablas'''

    def __init__(self, datos):
        self.datos = datos
        self.tipo_datos = type(self.datos)
        self.n = len(self.datos)
        self.frecuencias_absolutas = self.__frecuencias_absolutas__()
        self.frecuencias_relativas = self.__frecuencias_relativas__()
        self.frecuencias_absolutas_categoria = self.__frecuencias_absolutas_categoria__()
        self.fracuencias_relativas_categoria = self.__frecuencias_relativas_categoria__()

    def __str__(self):
        return f'''
        Datos: {self.__print_datos__()}
        n: {self.n}
        Frecuencias absolutas: {self.frecuencias_absolutas}
        Frecuencias relativas: {self.frecuencias_relativas}
        Frecuencias absolutas x categoria: {self.frecuencias_absolutas_categoria}
        Frecuencias relativas x categoria: {self.fracuencias_relativas_categoria}
        '''

    def __print_datos__(self):
        for id, value in self.datos.items():
            print(id, value)

    def __frecuencias_absolutas__(self):
        
        if self.tipo_datos == dict:
            
            datos = list(self.datos.values())
        else:
            
            datos = self.datos
            
        conteo_datos = Counter(datos)

        return conteo_datos

    def __frecuencias_relativas__(self):
        n = self.n
        fa = self.__frecuencias_absolutas__()
        for key in fa:
            fa[key] /= n
        
        return fa    
    
    def __frecuencias_absolutas_categoria__(self):
        
        if self.tipo_datos == dict:
            lista_categorias = []
            
            for i in self.datos.values():
                for categoria in i:
                    lista_categorias.append(categoria)
        frecuencias_absolutas_categoria = Counter(lista_categorias)
        
        return frecuencias_absolutas_categoria
        
    def __frecuencias_relativas_categoria__(self):
        n = self.n
        fr = self.__frecuencias_absolutas_categoria__()
        for key in fr:
            fr[key] /= n
        
        return fr
    
    
    
if '__main__' == __name__:

    lista = {
        1: ('F', 'MSc'), 2: ('F', 'MSc'), 3: ('F', 'MSc'), 4: ('F', 'MSc'), 
        5: ('F', 'PhD'), 6: ('M', 'MSc'), 7: ('M', 'MSc'), 8: ('M', 'MSc'), 
        9: ('M', 'MSc'), 10: ('M', 'MSc'), 11: ('M', 'MSc'), 12: ('M', 'MSc'), 
        13: ('M', 'MSc'), 14: ('M', 'MSc'), 15: ('M', 'PhD'), 16: ('M', 'PhD'), 
        17: ('M', 'PhD'), 18: ('M', 'PhD'), 19: ('M', 'PhD'), 20: ('M', 'PhD')
    }
    
    tabla1 = Tabla(lista)
    print(tabla1)
    
