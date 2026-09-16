### BUCLES O LOOPS / ciclos
## SON condicoonales que se repiten una y ptra vez o hasta que lo decidamos
## son como if pero en lugar de escrinbir varias veces un si.. escbribbimos un bucle que se ejecutte 
## minetras se cumpla la condicion

## --- WHILE MIENTRAS... SEA VERDADERO EJECUTA LO SIGUIENTE

my_condition = 0

while my_condition < 10: # mientrass se cumpla la condicion, imprimmira siempre
    print(my_condition) # le asignamos el argumento, una variable
    my_condition +=2

else: ## es opcional para avisar que se acabbo el bucle, ya que ell bucle seimpre debe terminar
    print("mi condicion es mayor a 10")
print("el bucle se acabo")


while my_condition < 20: ## mientrass la condicion sea menora 20 
    my_condition += 2   ## la condicion ira sumando mas 2
    if my_condition == 15: ## si la condicion llega a 15 imprime lo siguiente(pero salta de 14 a 16 por ende no se cumple
        print("mi condicion es 15")
    if my_condition == 16:
        print("se detiene la ejcucion en 16")
        break
print(my_condition)

print("la ejecucion se detuvo antes por un break") ## imprmie la condicion cada vez hasta qye sea 20


print("------------BUCLE FORR ----------")

## bucle for se repite tantas veces como elemntos tienen iterados
## en listas se ejecuta tanto como elemntos tenga
## y accede a los elemntos de cada lista
print("-----FOR EN LIST")
my_list = [30, 1.70 ,"jhenmiller", "Samaniego", 30]
for element in my_list: ## crea la variable element y lo corre en la lista, asugna el valor actual en la lista
    print (element) ## imprmie el valor actual en el mmomento cada vez qye el for se da la vuelta


print("------FOR EN TUPPLE----")
my_tuple = (31,27,24,"MILLER","JHEN" )
for element in my_tuple:
    print (element)

print("-----FOR EN SETS---")
my_set = {"jhenmiller", "samaniego", "31"}
for element in my_set:
    print (element)

print("----FOR EN DICT----")
my_dict = {"nombre":"jhenmiller", "apellido":"merge","edad":31, 1:"pyhton"}
for element in my_dict:
    print (element)









