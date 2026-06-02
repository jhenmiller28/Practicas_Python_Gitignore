## LISTAS DE PYTHON
# las listas son unua estructura de datos la cual nos permite
# almacenar una coleccion de elementos, las listas son mutables, eso quiere decir
# que podremos modificar su contenido luego de crearlas, las listas 
# se definen utilizando corchetes [] y los elementos se separan por comas

my_list = list()
my_other_list = [] # estas son dos formas de crear una lista vacia, la primera utilizando la funcion list() y la segunda utilizando los corchetes []
my_primera_lista = [30, 1.70 ,"jhenmiller", "Samaniego"] # esta es una lista que contiene diferentes tipos de datos, como numeros enteros, cadenas de texto, booleanos y numeros decimales
print(my_primera_lista)# se imprime la lita completa, mostrando todos los elementos que contiene

## funciones de las listas
print(len(my_list)) # esta funcion nos devuelve la cantidad de elementos que tiene la lista, en este caso 0 porque es una lista vacia
print(type(my_primera_lista)) # esta funcion nos devuelve el tipo de dato de la variable, en este caso <class 'list'> porque es una lista
## accediendo a los elementos o variables de la lista
print(my_primera_lista[2]) # esta es la forma de acceder a un elemento de la lista utilizando su indice, en este caso se accede al elemento en la posicion 2, que es el numero 3
print(my_primera_lista[-2]) # esta forma nos da el elemtno de atras hacia adelante , en reversa     

print (my_primera_lista[0:3]) # de esta manera podemos acceder a un rango determinado en la lista, en este caso se accede a los elementos desde la posicion 0 hasta la posicion 2, es decir, los elementos 1, 2 y 3
print (my_primera_lista[my_primera_lista.count(3)]) # esta forma nos devuelve el elemento que se encuentra en la posicion del indice que se obtiene al contar cuantas veces aparece el numero 3 en la lista, en este caso el numero 3 aparece una vez, por lo tanto se accede al elemento en la posicion 1, que es el numero 2
print (my_primera_lista.count(1.70)) # esta funcion nos devuelve la cantidad de veces que aparece el numero 1.70 en la lista, en este caso aparece una vez, por lo tanto el resultado es 1

age, height, name, surname = my_primera_lista
print(age,height,name,surname) # esta forma nos permite asignar cada elemento de la lista a una variable, en este caso se asigna el primer elemento de la lista a la variable age, el segundo elemento a la variable height, el tercer elemento a la variable name y el cuarto elemento a la variable surname, es importante que el numero de variables sea igual al numero de elementos en la lista para evitar errores

print(my_primera_lista + my_other_list) # esta forma nos permite concatenar dos listas, en este caso se concatena la lista my_primera_lista con la lista my_other_list, el resultado es una nueva lista que contiene todos los elementos de ambas listas, en este caso como my_other_list es una lista vacia, el resultado es la misma lista my_primera_lista   

my_list = "hola python"
print(my_list) # esta variable ya no es una lista, ahora es una cadena de texto, esto se debe a que las variables en python son dinamicas, lo que significa que pueden cambiar de tipo de dato durante la ejecucion del programa, en este caso se le asigna una cadena de texto a la variable my_list, por lo tanto ya no es una lista sino una cadena de texto
print(type(my_list)) # esta funcion nos devuelve el tipo de dato de la variable my_list, en este caso <class 'str'> porque es una cadena de texto  


