## DICTIONARIES####
## constructores de diccionarios
# creadno variables y dandoles valor de diccionarios con metodos

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

## CLAVE VALOR, SIMILAR A ARCHIVOS JSON
my_other_dict = {"nombre":"jhenmiller", "apellido":"merge","edad":31, 1:"pyhton"}

my_dict= {
    "nombre":"jhenmiller",
    "apellido":"merge",
    "edad":31,
    "lenguajes":{"pyhton","dart","java"},
    1:1.77
    }
print(my_dict)
print(my_other_dict)

print(f"el valor de la clave nombre es: {my_dict["nombre"]}") # PASAMOS EL NOMBRE DE UNA CLAVE E IMPRIME SU VALOR
my_dict["nombre"] = "albert" # actualizamos el valor de la clave nombre
print(my_dict["nombre"])

print(my_dict["lenguajes"])# PASAMOS LA CLAVE LENGUAJES E IMPRIME LOS VALORES QUE TIENE LA LISTA DENTRO DEL DICT

my_dict["calle"] = "calle Santa Rosa" ## AGREGAMOS UNA NUEVA CLAVE Y VALOR AL DICT
print(f"se agrego la nueva clave calle y su valor es: {my_dict["calle"]}")

print("jhenmiller" in my_dict) ## busca e imprime la clave si es que se encuentra en el diccionario
print("nombre" in my_dict)

print(my_dict.items)# listado de claves en formato lista
print(my_dict.keys)
print(my_dict.values) #nos da los valores del diccionario 

my_list = ["nombre",1, "piso"]
## el uso de fromkyes nos pasa las claves de otro diccionario o agregamos mas claves para hacer el diccionario mas grande
my_new_dict = dict.fromkeys((my_list))# creamos un dict dandole claves en base a una lista
print(my_new_dict)
my_new_dict = dict.fromkeys(("escuela",1,"piso"))  #creamos un dict dandole claves con el metodo fromkyes
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict) # creamos otro dict a base de las mismas claves del dict base
print(f"my nuevo diccionario es una copia de my_dict: {my_new_dict}")
my_new_dict = dict.fromkeys(my_dict, "jhen") #le da a toddas las claves el valor que se esta agregando
print(f"mi nuevo diccionario es: {my_new_dict}")

print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))

print(f" mi diccinoario final es:  {my_dict}")

print(f"la nueva lsita es {list(my_new_dict.values())}") #nuevmente se le agrega los vañores a cada clave"jhen""
print(f"el nuevo set es {set(my_new_dict)}")
print(f"la nueva tupla es {tuple(my_new_dict)}")

#dato_nuevo = input("ingresa nuevo dato: ")
#print(f"el dato nuevo es: {dato_nuevo}")
#print(f"el nuevo dato es:{dato_nuevo}")

print("\n * 5")
##AGREGANDO NUEVAS CLAVES Y VALORES POR TECLADO###
new_clave = input("ingresa nueva clave: ")
new_valor = input("ingresa nuevo valor: ")

if new_valor.isdigit():
    new_valor = int(new_valor)
my_dict[new_clave] = new_valor
print(my_dict)

print (f"la nueva clave es {new_clave} y su valor es {new_valor}")