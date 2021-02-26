import random
from formulas_estadisticas import ordenamiento_insercion, media, desviacion_estandar_poblacion, distribucion_normal
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models.annotations import Span, BoxAnnotation

def grafica_distribucion_estandar(lista,file="index.html"):
    
    lista_ordenada = ordenamiento_insercion(lista)

    mu = media(lista_ordenada)
    sigma = desviacion_estandar_poblacion(lista_ordenada)

    x, y = distribucion_normal(lista_ordenada)

    output_file(file)

    f = figure()

    f.line(x, y)

    # Creating span annotation for mu
    span = Span(
        location=mu, dimension='height',
        line_color='blue', line_width=2
    )
    f.add_layout(span)

    # Creating a box annotations for sigmas
    sigma_1 = BoxAnnotation(
        left=mu-1*sigma, right=mu+sigma, line_width=1,
        fill_color='grey', fill_alpha=0.3
    )
    f.add_layout(sigma_1)

    sigma_2_left = BoxAnnotation(
        left=mu-2*sigma, right=mu-1*sigma, line_width=1,
        fill_color='grey', fill_alpha=0.2
    )
    f.add_layout(sigma_2_left)

    sigma_2_right = BoxAnnotation(
        left=mu+sigma, right=mu+2*sigma, line_width=1,
        fill_color='grey', fill_alpha=0.2
    )
    f.add_layout(sigma_2_right)

    show(f)

if '__main__' == __name__:
    largo_lista = int(input('Largo de lista: '))
    lista = [random.randint(1, largo_lista) for i in range(largo_lista)]
    lista_ordenada = ordenamiento_insercion(lista)
    print(f'Lista Original: {lista}\nLista Ordenada: {lista_ordenada}')

    print(f'''
Media: {media(lista_ordenada)}
sigma: {round(desviacion_estandar_poblacion(lista),2)}

Distribucion normal: 
x={distribucion_normal(lista)[0]}

y={[round(i,3) for i in distribucion_normal(lista)[1]]}
''')
    grafica_distribucion_estandar(lista)