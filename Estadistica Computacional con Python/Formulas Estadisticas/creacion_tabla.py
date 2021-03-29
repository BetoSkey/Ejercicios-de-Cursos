#Este archivo es un intento por crear una clase que convierta la informacion en arrays 
# para un analisis estadistico de la informacion, aun no se termina, se necesita estudiar numpy y pandas para lograrlo.

import numpy as np
from collections import Counter


class Tabla_bivariada:
    '''Clase para crear un array de datos'''
    
    def __init__(self, datos):
        self.datos = datos
        self.type = type(self.datos)
        self.np_datos = self.__create_array__()
        self.n = self.np_datos.shape[0]
        self.columns_count = self.np_datos.shape[1]
        self.columnas = self.__separar_columnas__()
        self.valores_unitarios_columnas = self.__valores_unitarios_columnas__()
        

    
    def __create_array__(self):
        if self.type == dict:
            columns = []
            for key, val in self.datos.items():
                columns_by_key = [key]
                for column in val:
                    columns_by_key.append(column)
                columns.append(columns_by_key)
            np_datos = np.array(columns)
        return np_datos

    def __separar_columnas__(self):
        columnas = []
        
        for i in range(self.columns_count):
            columnas.append(list(self.np_datos[:,i]))
        
        return columnas
        
    def __valores_unitarios_columnas__(self):
        valores_unitarios =[]
        for column in self.columnas[1:]:
            valores_unitarios_columna = [list(set(column))]
            for valor in valores_unitarios_columna[0]:
                valores_unitarios.append(valor)
        return valores_unitarios

    def tabla_frecuencias_absolutas(self, row_index, column_index):
        tabla = np.array(self.np_datos[ : , 1: ])
        tabla_tuples = []
        for i in tabla:
            tabla_tuples.append(tuple(i))
            
        contar_datos_tabla = Counter(tabla_tuples)
        # por cada columna que se quiere considerar
        #for valor_row in self.valores_unitarios_columnas[row_index]:
        #    for valor_column in self.valores_unitarios_columnas[column_index]:
        #        combinaciones.append([valor_row,valor_column])
        
        
        
        return contar_datos_tabla
                
            

        
    def frecuencias_absolutas(self):
        columnas = []
        
        #iterand por el total de columnas
        for i in range(1, self.columns_count):
            columnas.append(list(self.np_datos[:,i]))
        
        union_columnas = []
        for columna in columnas:
            for valor in columna:
                union_columnas.append(valor)
                
        fa = Counter(union_columnas)
        
        return fa


    def __str__(self):
        return f'''
n: {self.n}

Datos:
{self.np_datos}

Valores Unitarios Columnas:
{self.valores_unitarios_columnas}

Frecuencias absolutas:
{self.frecuencias_absolutas()}
                '''
                
                
                
                
if '__main__' == __name__:
    
    lista1 = {
        1: ('F', 'MSc'), 2: ('F', 'MSc'), 3: ('F', 'MSc'), 4: ('F', 'MSc'), 
        5: ('F', 'PhD'), 6: ('M', 'MSc'), 7: ('M', 'MSc'), 8: ('M', 'MSc'), 
        9: ('M', 'MSc'), 10: ('M', 'MSc'), 11: ('M', 'MSc'), 12: ('M', 'MSc'), 
        13: ('M', 'MSc'), 14: ('M', 'MSc'), 15: ('M', 'PhD'), 16: ('M', 'PhD'), 
        17: ('M', 'PhD'), 18: ('M', 'PhD'), 19: ('M', 'PhD'), 20: ('M', 'PhD')
    }
    
    tabla1 = Tabla_bivariada(lista1)
    tabla1_combinaciones = tabla1.tabla_frecuencias_absolutas(1,2)
    
    print(tabla1)
    print(tabla1_combinaciones)