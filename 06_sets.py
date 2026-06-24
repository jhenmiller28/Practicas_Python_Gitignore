# sets de datos
# de base tiene a las listas, vevctor, array 
# no admite repetidos, no son ordenadas, 

#creacion de sets
my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set))

my_other_set = {"jhenmiller", "samaniego", "31"} # se edfine como set, por la fomra de ingresar datos
print(type(my_other_set))
print(len(my_other_set))
# print(my_other_set[2])

my_other_set.add("sistemas")
print(my_other_set) ## los set no son estructuras ordendas

my_other_set.add("sistemas")
print(my_other_set) # un set no ADMITE ELEMENTOS REPETIDOS

print("jhenmiller" in my_other_set)
print("jhenmillerr" in my_other_set) ## para poder cmpronbar si un dato existe en el set de datos

my_other_set.remove("jhenmiller") # remueve el elemento especificado
print(my_other_set)

my_other_set.clear() # vacia el set de datos
print(len(my_other_set))

del my_other_set # la palbra reservada del, elimina el set de datos
# print(my_other_set) # da error porque elimina el set coomo estructura

my_set = {"jhenmiller", "samaniego", 31}
my_list = list(my_set)
print(my_list)
print(my_list[1])

my_other_set = {"python","GitHub", "Docker", "jhenmiller"}

my_new_set = my_set.union(my_other_set) ## une los set de datos, pero no aepta los elementos repetidos
print(my_new_set.union(my_new_set).union(my_new_set).union({"CCNA","PostgreSQL"}))

print(my_new_set.difference(my_set))# muestra los elemntos que son diferentes comparando otro set

###### practicas de set
set_practica = {}
set_parc2 = set()

print(set_practica)
set_practica = {"miller"} # antes de agregar elementos al set, minimo debe tener un elemento
set_practica.add("jhen")
print(set_practica)
set_practica.add("jhe")
print(set_practica)
set_parc2 = {"jhen", "millerrrr", 31, "japon" }
print(set_parc2)

## INGRESAR NUEVOS ELEMNETOS POR TECLADO Y AGREGARLOS A UN SET DE DATOS
nuevo_dato = input("ingresa dato: ")
print(f"el nuevo dato ingresado por teclado es: {nuevo_dato}")

if nuevo_dato.isdigit():
    set_practica.add(int(nuevo_dato)) # PARA AGREGAR NUKMEROS DEBEMOS APLICAR EL METODO INT
else: 
    set_practica.add(nuevo_dato)
print(set_practica)
print(f"se agrego un nuevo dato a set practica {nuevo_dato}")
datos_cruzados = set_practica.intersection(set_parc2)
print(f"los datos que son iguales en ambos set son: {datos_cruzados}")