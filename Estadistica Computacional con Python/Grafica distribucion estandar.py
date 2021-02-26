from formulas_estadisticas import ordenamiento_insercion, distribucion_normal, media, desviacion_estandar_poblacion, valor_z, modas
import random
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models.annotations import Span, BoxAnnotation


largo_lista = 1000
lista = [random.randint(1, largo_lista) for i in range(largo_lista)]
lista_ordenada = ordenamiento_insercion(lista)

mu = media(lista_ordenada)
sigma = desviacion_estandar_poblacion(lista_ordenada)
modas_lista = modas(lista_ordenada)
valores_z = valor_z(lista_ordenada)

x, y = distribucion_normal(lista_ordenada)

output_file("distribucion_normal.html")

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

print(f'''
mu = {mu}
sigma = {sigma}
modas = {modas_lista}
''')
