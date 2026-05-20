## LISTAS, ARRAYS O VECTORES###
# Las listas son una estructura de datos que permite almacenar una colección de elementos, los cuales pueden ser de diferentes tipos (números, cadenas, objetos, etc.). Las listas son mutables, lo que significa que se pueden 
#modificar después de su creación. Se definen utilizando corchetes [] y los elementos se separan por comas.

my_list = list() # se crea una lista vacia utilizando la funcion list(), esta es una forma de crear una lista sin elementos, tambien se puede crear una lista vacia utilizando corchetes [] como my_list = []
my_other_list = list() # se crea una segunda lista vacia utilizando la funcion list()

print (len(my_list)) # se utiliza la funcion len() para obtener el numero de elementos en la lista my_list, en este caso se muestra 0 ya que la lista esta vacia

my_list = [35, 25, 69, 35, 15, 45]
print (my_list) # se imprime la lista my_list, mostrando los elementos que contiene, en este caso se muestra [35, 25, 69, 35, 15, 45]
print (len(my_list)) # se utiliza la funcion len() para obtener el numero de elementos en la lista my_list, en este caso se muestra 6 ya que la lista contiene 6 elementos
my_other_list = [31, 1.70, "jhenmiller", "samaniego"]
print (type(my_other_list)) # se utiliza la funcion type() para verificar el tipo de dato de la variable my_other_list, en este caso se muestra <class 'list'> ya que my_other_list es una lista

print (my_other_list) # se imprime la lista my_other_list, mostrando los elementos que contiene, en este caso se muestra [31, 1.70, "jhenmiller", "samaniego"] ya que la lista contiene un numero entero, un numero decimal y dos cadenas de texto
print (my_other_list[3]) # se accede al cuarto elemento de la lista my_other_list utilizando el indice 3, en este caso se muestra "samaniego" ya que es el cuarto elemento de la lista
print ()
