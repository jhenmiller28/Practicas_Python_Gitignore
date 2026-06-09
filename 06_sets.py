# sets de datos
# de base tiene a las listas, vevctor, array 
# noadmite repetidos, no son ordenadas, 

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
