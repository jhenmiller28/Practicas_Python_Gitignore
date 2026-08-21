edad = int(input("ingrese edad a calcualr: "))

if (edad >= 18):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")


if edad > 40:
    edad = edad + 20
    print("es de la tercera edad")
else:
    edad = edad - 20
    print("es joven de 20 a 40 años")
print("ingrese nueva edad a calcular")

edad = int(input("ingrese edad a calcular: "))

list_edad = [edad, "jhen", 31, "devsecops"]
nuevo_dato = input("ingresa el nuevo dato")
if nuevo_dato is int:
    print("el nuevo dato es entero")
elif nuevo_dato is str:
    print("el nuevo dato es string")
else:
    print("el nuevo datos es otro tipo de dato")
list_edad.append(nuevo_dato )
print(f"el nuevo dato ingresado a la lista es:{nuevo_dato}")
print(f" la nuea lista es: {list_edad}")


tupla_datos = (edad, "jhen", 31,"dota" )
nuevo_dato_tupla = input("ingresa nuevo dato a tupla: ")
if nuevo_dato_tupla is int:
    print(f"el nuevo datoe es enteo : {nuevo_dato_tupla}")
else:
    print(f"el nuevo dato es strinf: {nuevo_dato_tupla}")
tupla_datos = tupla_datos + (nuevo_dato_tupla,)
print(f"la tupla es: {tupla_datos}")