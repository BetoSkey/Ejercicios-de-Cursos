import unittest


class Busqueda_binaria:
    def __init__(self, lista):
        self.lista = lista

    def __ubicacion_binaria__(self, lista, comienzo, final, objetivo, ubicacion_meta=0):

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
            return self.__ubicacion_binaria__(lista, medio + 1, final, objetivo, ubicacion_meta)

        else:  # Si el objetivo es menor que la mitad
            return self.__ubicacion_binaria__(lista, comienzo, medio - 1, objetivo, ubicacion_meta)

    def ordenamiento_insercion(self):
        lista = self.lista
        lista_ordenada = [lista[0]]
        lista_desordenada = lista[1:]
        n_lista_ordenada = len(lista_ordenada)-1
        n_lista_desordenada = len(lista_desordenada)-1

        # Por cada ubicacion de la lista desordenada
        for ubicacion_en_lista_desordenada in range(n_lista_desordenada+1):

            # Encuentra la ubicacion en la lista ordenada
            ubicacion = self.__ubicacion_binaria__(
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

    def busqueda_binaria(self, objetivo, comienzo=0, final=None):
        if final == None:
            final = len(self.lista)

        lista_ordenada = self.ordenamiento_insercion()

        if comienzo > final:
            return False
        medio = (comienzo + final) // 2
        if lista_ordenada[medio] == objetivo:
            return medio
        elif lista_ordenada[medio] < objetivo:
            return self.busqueda_binaria(objetivo, comienzo=medio + 1, final=final)
        else:
            return self.busqueda_binaria(objetivo, comienzo=comienzo, final=medio - 1)


class Pruebas_caja_cristal(unittest.TestCase):

    def test_ordenar_lista(self):
        formula_ordenar_lista = busqueda1.ordenamiento_insercion()

        self.assertEqual(formula_ordenar_lista, [55, 59, 62, 70, 74, 82, 87])

    def test_buscar_ubicacion(self):
        formula_buscar_ubicacion = busqueda1.busqueda_binaria(87)

        self.assertEqual(formula_buscar_ubicacion, 6)


if '__main__' == __name__:

    lista1 = [55, 87, 74, 70, 82, 62, 59]
    busqueda1 = Busqueda_binaria(lista1)

    unittest.main()
