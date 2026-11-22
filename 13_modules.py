## modulos en python ## codigo que podamos reusar en otras ficheros
## usar ficheros desde otros ficheros
# una libreria que tenemos codigo en funciones y 
# modulo una saerie de utilidades para resolver operaciones, para resolver problemas puntuales

import mi_modulo  ## importamos el fichero con lass funiones a importar
from mi_modulo import sum

mi_modulo.sum(5,9,15)
print("la suma es {sum}")
mi_modulo.printValue("Hola python")

from mi_modulo import sum, printValue
sum(5,3,1)
printValue("hola python")

import math ##  importamos del modulo math con todas las funcinones del modlo

math.pi      ## 
print(math.pi)
print(math.log(100))
print(math.pow(4,3))

from math import pi as PI_VALUE  ## del modulo math importamos la funcion pi renombrada como pi_value
print(PI_VALUE)