ESCALERAS = [
    ['As',    '2',    '3',    '4',    '5'],
    ['2',     '3',    '4',    '5',    '6'],
    ['3',     '4',    '5',    '6',    '7'],
    ['4',     '5',    '6',    '7',    '8'],
    ['5',     '6',    '7',    '8',    '9'],
    ['6',     '7',    '8',    '9',    '10'],
    ['7',     '8',    '9',    '10',   'Jota'],
    ['8',     '9',    '10',   'Jota', 'Reina'],
    ['9',     '10',   'Jota', 'Reina', 'Rey'],
    ['10',    'Jota', 'Reina', 'Rey',  'As']
]

escaleras = [
    (dict([(id, value) for id, value in enumerate(list)]))
    for list in ESCALERAS
]

numeros = ['10',    'Jota', 'Reina', 'Rey',  'As']

dict_numeros = dict(
    [(id, value) for id, value in enumerate(numeros)]
)

if '__main__' == __name__:
    print(f'Numeros: {numeros}')
    for escalera in range(len(escaleras)):
        print(f'escaleras[escalera] = {escaleras[escalera]}')
        # *** Intentar remover numeros duplicados en vairable temporal la cual se evaluara solo para las escaleras.
        # *** temp = {val : key for key, val in test_dict.items()}
        # *** res = {val : key for key, val in temp.items()}
        temp = {val: key for key, val in dict_numeros.items()}
        dict_numeros_unicos = {val: key for key, val in temp.items()}
        if len(dict_numeros_unicos) == 5 and all(
            dict_numeros[k] in escaleras[escalera].values()
            for k in dict_numeros
        ):
            print(True)
        else:
            print(False)

        # for k in dict_numeros:
        #    print(dict_numeros[k])
