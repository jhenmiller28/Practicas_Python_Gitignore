## LISTAS DE PYTHON
# las listas son unua estructura de datos la cual nos permite
# almacenar una coleccion de elementos, las listas son mutables, eso quiere decir
# que podremos modificar su contenido luego de crearlas, las listas 
# se definen utilizando corchetes [] y los elementos se separan por comas

my_list = list()
my_other_list = [] # estas son dos formas de crear una lista vacia, la primera utilizando la funcion list() y la segunda utilizando los corchetes []
my_primera_lista = [30, 1.70 ,"jhenmiller", "Samaniego", 30] # esta es una lista que contiene diferentes tipos de datos, como numeros enteros, cadenas de texto, booleanos y numeros decimales
print(my_primera_lista)# se imprime la lita completa, mostrando todos los elementos que contiene

## funciones de las listas
print(len(my_list)) # esta funcion nos devuelve la cantidad de elementos que tiene la lista, en este caso 0 porque es una lista vacia
print(type(my_primera_lista)) # esta funcion nos devuelve el tipo de dato de la variable, en este caso <class 'list'> porque es una lista
## accediendo a los elementos o variables de la lista
print(my_primera_lista[2]) # esta es la forma de acceder a un elemento de la lista utilizando su indice, en este caso se accede al elemento en la posicion 2, que es el numero 3
print(my_primera_lista[-2]) # esta forma nos da el elemtno de atras hacia adelante , en reversa     

print (my_primera_lista[1:3]) # de esta manera podemos acceder a un rango determinado en la lista, en este caso se accede a los elementos desde la posicion 1 hasta la posicion 3, es decir, los elementos 2, 3 y 4
print (my_primera_lista[my_primera_lista.count(3)]) # esta forma nos devuelve el elemento que se encuentra en la posicion del indice que se obtiene al contar cuantas veces aparece el numero 3 en la lista, en este caso el numero 3 aparece una vez, por lo tanto se accede al elemento en la posicion 1, que es el numero 2
print (my_primera_lista.count(1.70)) # esta funcion nos devuelve la cantidad de veces que aparece el numero 1.70 en la lista, en este caso aparece una vez, por lo tanto el resultado es 1

# age, height, name, surname = my_primera_lista
# print(age,height,name,surname) # esta forma nos permite asignar cada elemento de la lista a una variable, en este caso se asigna el primer elemento de la lista a la variable age, el segundo elemento a la variable height, el tercer elemento a la variable name y el cuarto elemento a la variable surname, es importante que el numero de variables sea igual al numero de elementos en la lista para evitar errores

print(my_primera_lista + my_other_list) # esta forma nos permite concatenar dos listas, en este caso se concatena la lista my_primera_lista con la lista my_other_list, el resultado es una nueva lista que contiene todos los elementos de ambas listas, en este caso como my_other_list es una lista vacia, el resultado es la misma lista my_primera_lista   

my_list = "hola python"
print(my_list) # esta variable ya no es una lista, ahora es una cadena de texto, esto se debe a que las variables en python son dinamicas, lo que significa que pueden cambiar de tipo de dato durante la ejecucion del programa, en este caso se le asigna una cadena de texto a la variable my_list, por lo tanto ya no es una lista sino una cadena de texto
print(type(my_list)) # esta funcion nos devuelve el tipo de dato de la variable my_list, en este caso <class 'str'> porque es una cadena de texto  


# operaciones de las listas
my_primera_lista.append("souschef") # nos agrega un elemento al final de la lista
print(my_primera_lista)

my_primera_lista.insert(1, "motos clasicas") # nos permite agregar un elemtno en una posicion especifica
print(my_primera_lista)

my_primera_lista[1] = "motos electricas coustom" # esta forma nos permite modificar un elemento de la lista utilizando su indice, en este caso se modifica el elemento en la posicion 1, que es el numero 2, por el numero 3
print(my_primera_lista)

my_primera_lista.remove("motos electricas coustom") # nos permite eliminar un elemnto de la lista,solo uno
print(my_primera_lista)

my_primera_lista.pop(3) #nos permite eliminar un elemento de la lista utilizando su indice Y PODER USARLO EN OTRA PARTE DEL PROGRAMA
print(my_primera_lista)
my_pop_element = my_primera_lista.pop(3) #nos permite eliminar un elemento de la lista utilizando su indice Y PODER USARLO EN OTRA PARTE DEL PROGRAMA
print(my_pop_element) # esta variable contiene el elemento que se elimino de la lista utilizando la funcion pop()

my_primera_lista.reverse() # esta funcion nos permite invertir el orden de los elementos de la lista, es decir, el primer elemento se convierte en el ultimo y el ultimo elemento se convierte en el primero
print(my_primera_lista)

my_primera_lista.sort(key=str)# nos ayuda cuadno hay tipoos de datos mixtos, trata todo como string y los ordena
print(my_primera_lista) # esta es la lista my_primera_lista despues de ordenar los elementos utilizando la funcion sort() con el parametro key=str, esto hace que todos los elementos se traten como cadenas de texto y se ordenen alfabeticamente, en este caso el resultado es una lista ordenada alfabeticamente, aunque contiene diferentes tipos de datos, como numeros enteros, cadenas de texto y booleanos, todos se tratan como cadenas de texto para poder ordenarlos sin generar un error debido a la mezcla de tipos de datos.

print("\n" * 5)

print("ESPACIO DE PRACTICAS DE LISTAS/n")
print(40 * "=")

my_list_copiada = my_primera_lista.copy()
my_primera_lista.clear() # esta forma nos permite eliminar todos los elementos de la lista
print(my_primera_lista)
print(my_list_copiada) # esta variable contiene una copia de la lista my_primera_lista antes de ser limpiada, por lo tanto contiene todos los elementos que tenia la lista antes de ser limpiada


my_list_copiada.reverse() # nos muestra los elementos ordenados ulitmo a prinmero
print(my_list_copiada)

# my_list_copiada.sort() # nos ayuda a ordernar los elementos de la lista de menor a mayor, en este caso como la lista contiene diferentes tipos de datos, no se puede ordenar, por lo tanto se genera un error, para evitar esto se pueden ordenar solo los elementos que sean del mismo tipo de dato, por ejemplo, si queremos ordenar solo los numeros enteros de la lista, podemos utilizar una comprension de listas para crear una nueva lista que contenga solo los numeros enteros y luego ordenar esa nueva lista.
print(my_list_copiada) # solo fuunciona con elementos del mismo tipo de dato, en este caso como la lista contiene diferentes tipos de datos, no se puede ordenar, por lo tanto se genera un error, para evitar esto se pueden ordenar solo los elementos que sean del mismo tipo de dato, por ejemplo, si queremos ordenar solo los numeros enteros de la lista, podemos utilizar una comprension de listas para crear una nueva lista que contenga solo los numeros enteros y luego ordenar esa nueva lista.

print(my_list_copiada[1:4]) # de esta manera accedemos a un rango determinado de la lista
print (my_list_copiada[2])  # nos impriime el elemento del indice 2
print(my_list_copiada.count(30)) # cuenta cuantas veces aparece el elemneto 30 en la lista

palabra = "hola mundo"
my_list_copiada.insert(2, palabra) # de estab manera agrego na variable creada a un indice en la lista
print(my_list_copiada)

numero = 100
my_list_copiada.append(numero) # agregoo el elemento 100 al funakl de la lista copiada
print(my_list_copiada)

my_list_copiada.remove(numero) # elimino el elemto 100, con el nomnre de la varriable que le di al inicio
my_list_copiada.remove(palabra) # aca elimino con el valor de la varaible palabra, que es "hola mundo" 
print(my_list_copiada)

print(len(my_list_copiada)) # esra funcion me permite saber el tamaño de la lista, es decir, la cantidad de elementos que contiene la lista copiada, en este caso el resultado es 4 porque la lista copiada contiene 4 elementos despues de eliminar el numero 100 y la palabra "hola mundo"


elemento_pop = my_list_copiada.pop(2) # esta forma nos permite eliminar un elemento de la lista utilizando su indice y guardar ese elemento en una variable, en este caso se elimina el elemento en la posicion 2, que es el numero 30, y se guarda en la variable elemento_pop
print(elemento_pop) # esta variable contiene el elemento que se elimino de la lista utilizando la funcion pop(), en este caso el numero 30
print(my_list_copiada) # esta es la lista copiada despues de eliminar el elemento
# se pede usar para poder quitar de una lista un elemneto
# y poder tenerla en una papelara, por decirlo asi y y poder usarala luego
my_list_copiada.insert(2, elemento_pop) # asi podemos agregarla luego a la misma u optra lista, en este caso se agrega el elemento que se elimino anteriormente, que es el numero 30, en la posicion 2 de la lista copiada
print(my_list_copiada)

my_list_copiada.reverse() # esta funcion nos permite invertir el orden de los elementos de la lista copiada, es decir, el primer elemento se convierte en el ultimo y el ultimo elemento se convierte en el primero
print(my_list_copiada) # esta es la lista copiada despues de invertir el orden

rango_elemtos = my_list_copiada[1:4] # esta variable contiene un rango de elementos de la lista copiada, en este caso se accede a los elementos desde la posicion 1 hasta la posicion 4, es decir, los elementos en las posiciones 1, 2 y 3
print(rango_elemtos) # esta variable contiene el rango de elementos que se accedio de la lista copiada, en este caso el resultado es una nueva lista que contiene los elementos en las posiciones 1, 2 y 3 de la lista copiada

my_list_copiada.append(rango_elemtos) # esta fomra agregamos una lista como si una variable se tratara, por medio de 2 fucniones, serviria para pasar de una lista a otra,
print(my_list_copiada) # esta es la lista copiada despues de agregar el rango de elementos como un nuevo elemento, en este caso el resultado es una lista que contiene los elementos originales de la lista copiada y un nuevo elemento que es una lista con los elementos en las posiciones 1, 2 y 3 de la lista copiada