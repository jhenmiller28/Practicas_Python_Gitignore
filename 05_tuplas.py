# Tuplas, son inmutables, no se modifican
# ideales si no se requiere cambiar los datos
# se pueden usar como claves, no pueden contener listas 
# u otras tuplas, pero si pueden contener diccionarios

my_tuple = tuple() # se puede crear una tupla vacía utilizando la función tuple() o utilizando paréntesis sin elementos
my_other_tuple = () # también se puede crear una tupla vacía utilizando paréntesis sin elementos


my_other_tuple = (31,27,24)
print(my_other_tuple)
my_tuple = (31,1.70,"Jhenmiller" , "Samaniego", "Jhenmiller") # se pueden crear tuplas con diferentes tipos de datos, como enteros, flotantes y cadenas de texto
print(my_tuple)
print(type(my_tuple)) # <class 'tuple'>

# acceder a los datps de la tupla por medio de sus indices
print(my_tuple[1]) 
print(my_tuple[-1])
print (my_tuple[-4])

print(my_tuple.count("Jhenmiller"))# no se puede modificar la tupla, por lo tanto no se pueden contar los elementos de la tupla
print(my_tuple.index("Jhenmiller"))# se puede usar el método index() para encontrar la posición de un elemento en la tupla, pero no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla

# my_tuple[5] = "20"
# print(my_tuple) # TypeError: 'tuple' object does not support item assignment, no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla

print(my_tuple + my_other_tuple) # se pueden concatenar tuplas utilizando el operador +, pero no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla

sum_tuple = my_tuple + my_other_tuple
print (sum_tuple)# se pueden concatenar tuplas utilizando el operador +, pero no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla
print(sum_tuple[3:6])# se pueden acceder a los elementos de la tupla utilizando índices y también se pueden utilizar slicing para obtener un rango de elementos
my_tuple = list(my_tuple) # se puede convertir una tupla en una lista utilizando la función list(), pero no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla
print(type(my_tuple))

my_tuple.insert(1,"python")# se puede insertar un elemento en una lista utilizando el método insert(), pero no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla
print(my_tuple)  
del my_tuple 
# print (my_tuple) # NameError: name 'my_tuple' is not defined, se puede eliminar una variable utilizando la palabra clave del, pero no se pueden modificar los elementos de la tupla, por lo tanto no se pueden contar los elementos de la tupla