# FUNCTIONS ###          
# como definir una funcion , palabra reservada DEF

def my_function (): ## funcion 
    print ("es mi primera funcion") ## la funcino puede resibir codigo

my_function()  ## llamar a my_function
my_function()   ## podemos llamar la funcion con todos sus operacinoes( x lineas de codigo)
my_function()  ## odnde podemos llamar blucles, diccionearios procesados etc



def sum_two_values (first_number, second_number): ## esta fucnion le pasamos parametros(variables,valores fijos)
    print(first_number + second_number)
sum_two_values(4,10)  ## imprime la suma de los dos parametros qye se le dieron

sum_two_values(456,589) #la funcino es imprimir la suma de los dos parametros
print("funcinoes con ingreso de valores por teclado") ## ingresando los valors por tecladoS
first_number = int(input("ingresa los parametrso a sumar " )) ## partiedno de aca solicitammos el ingreeso de valores
second_number = int(input("ingresa los parametrso a sumar"))#fomateamos pra que recoonozca que son enteros, int y no concatene, sino que sume#
sum_two_values (first_number,second_number)  ## imprime la suma de los valroes ingresados

print("funcniones con return")
def sum_two_values_whit_return (first_number, second_number): ##

   return first_number+second_number
my_result = sum_two_values_whit_return(50,40)
print(my_result)
my_result = sum_two_values_whit_return(1.5,4.5)
print(my_result)

print(" funcniones con formateo de string e int")
def print_datos(name,edad, apellido):
    print(f"{name} {edad} {apellido}")
print_datos(name="jhenmiller", edad= 31, apellido= "samaniego")  


print("funcio con parametros por dfecto")
def print_whit_name (name, apodo, edad = "sin eddad"):
    print(f"{name} {apodo} {edad}")
print_whit_name("Jhenmiller", "samaniegom")


def print_texts(*text): ## el asterisco nos permite agrrgar diferentes parametros, le podeos masar N datos
    print(text)

print("hola mundo", "desde", "pyhton", "jhenmiller")
print("hola mundo DevSecOps")

print("def FUNCION CON BUCLE Y CONVERTIR TEXTO A MAYUS.. CON la fucnnion upper")
def print_text_mayuscula(*texts): # definido asi podemos pasarle N valoes string o int
    for text in texts:
        print(text.upper())
print_text_mayuscula("Jhenmiller", "samaniegom","bbva")