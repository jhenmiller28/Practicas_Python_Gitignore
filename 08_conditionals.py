##CONDICIONALES 
# las condiciones con IF solo se ejecutan si es que son verdaderas, si son falasa no se ejecuten
# las condicionales empiezan en if , no puede empezar en elif
my_condition = False

if my_condition:
    print("se ejecuta la condicion del if")

print("la ejecucion continua")

##########################

my_condition = 5 * 2 

if my_condition == 10:
    print("se ejecuta la condicion del segundo if donde my_condition es =10") # se ejcuta solo si la condicion es verdadera

if my_condition >10 and my_condition < 20: #    
    print("se ejecuta la condicion del tercer if si my_condition es mayor a 10 y si es menor a 20") # si es falsa la condicion o no se cumple. no se ejecuta

elif my_condition == 1: # es como sino se cumple la condiciona anterior, prueba con esta nueva condicion
    print("se ejecuta si es igual a 1 ")
else: ## si la condicion inicial es falsa o no se cumple, por defecto esta se ejecuta, caso  por defecto, sino se cumple nada se ejecuta
    print(" se ejecuta solo si my_condition es menor igual a 10")

print("la ejecucion continua")

#####################
## praticas de condicionales

print("============================")
print("PRACTICAS DE IF , ELIF Y ELSE")
print("============================")
my_string = "mi cadena de textooo"

if my_string == "mi cadena de textooo" : 
    print("mi cadena de texto no es vacia y si coincide")

if my_string == "mi cadena de texto":
    print("esta cadena de texto no es de la condicion")
print("============================")
print ("PRACTICA DE IF,ELIF Y ELSE")
print("=============================")

if not my_string: ## la condicion niega la cadena, entonces niega que tiene un valor, y eso es falso..no ejecuta la primera ejecucion 
    print("la cadena de texto si esta vacia")

elif my_string == "mi cadena de textooo": ## aca el sino dice que el el valor es igual a la palabra textooo, lo cual es falso
    print(f"este es la ejecucioin del elif, ya que el primer if fue negado y es flasa la negacion,mi cadena de texto no esta vacia y el valor es: {my_string}")

else :  ## el else al final imprime por defecto que la cadena esta vacia
    print ("my_strinf esta vacia") ## esta no se llega a ejecutar, ya que por defecto en este caso, la condicion solo puede ser 2 estados, y se cumple entre las priimeras 2





## PRACTICA NR 2
# LISTA DE INVTADOS,CON PASE VIP, MAYOR DE 18 AÑOS 
#primero se pasa a si es mayor de edad, luego a si esta en lista, y finalmente si tiene pase vip

edad = int(input("ingrese edad: "))
if edad >= 18:
    ## ingrseo de valores por teclado

    print("\n PASA AL FILTRO 2 ")
    opcion_lista = input("se encuentra en la lista de invitados? ingrese 1 para true  y 0 para false: ")# sera la opcion true o false(0 y 1)
    esta_en_lista = (opcion_lista == "1" )# el uno es true y 0 es false
    
    print("tiene pase vip?")
    opcion_vip = input("ingrese 1 o 0 para verificar si tiene pase vip: ") #se le asigan la condicion de true y false
    tiene_vip = (opcion_vip == "1") 

    # ya tenemos los ingresos, ahora las ecisiones o filtros
    
    if esta_en_lista and tiene_vip:
        print("esta en la lista de invitados y tiene pase vip")# se ejcuta solo si ambas son verdadero, si solo uno es verdadero, pasara ala siguiente linea de codigo 
    elif esta_en_lista:
        print("si esta en la lista,no tiene pase vip")
    elif tiene_vip:
        print("si accede, tiene pase vip")# esto se ejecuta solo si tiene vip 
    else: 
        print("no tiene pase vip ni esta en la lista de invitados, solo es un mayor de 18 que quizo colarse") ## este es el mensaje de defecto, solo paso el filtro de edad

    
else:
    print("acceso denegado por ser menor de edad")

## ejercicio 2
## ahora sera si tenemos leche y cafe molido para un caffe late y chocolate 
# para un moka
# primer filtro,, si tenemos cafe... luego leche(porque se puede hacer late pero no moka)}
# leugo chocolate(poorque si hay leche y no chocolate podemos hacer un late)

hay_cafe = input("hay cafe molido:ingresa si o no ")


if hay_cafe == "si":
    print("podemos preparar cafe")
    print()
    opcion_hay_leche = input("hay leche para un latte: ") ## escribir si o no
    hay_leche = (opcion_hay_leche == "si") # compara la respuesta ingresada por teclado
    print()
    opcion_hay_chocolate  = input("hay choclolate para un moka: ")## ingresamos la palabra de confirmacion
    hay_chocolate = (opcion_hay_chocolate == "si") ## comparamos los vlaores para el true o false
    print()
    if hay_leche and hay_chocolate:
        print("podemos preparar un moka!!")
    elif hay_leche:
        print("podemos preparar un latte!")
    else:
        print("solo hay cafe molido, podemos preparar un expreso o un americano")
else: 
    print("no hay cafe, debemos ir a comprar")

