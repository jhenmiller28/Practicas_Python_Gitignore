## strings 

my_string = "cadenas de texno entre comillas"
my_other_string = "mi otra string"

print(len(my_string)) # len es metodo para contar caracteres de una cadena
print(len(my_other_string)) # aca al nio colocar un saltop de linea, se muestra el resultado en la misma linea

print(my_string + " " + my_other_string) # concatenar cadenas de texto, se puede usar el operador + para unir dos o mas cadenas de texto, en este caso se agrega un espacio entre las dos cadenas

my_new_line_string = "esto es un string\ncon salto de linea" # \n es un caracter de escape que se utiliza para indicar un salto de linea, al imprimir esta cadena, se mostrara en dos lineas diferentes
print(my_new_line_string) 

my_tab_string = "esto es ubn string con \t de tabulacion" # \t se usa para agregar una tabulacion al imprimir una cadena, se mostrara un espacio mas grande entre las palabras
print (my_tab_string) # aca se notara la tabulacion entre las palabras "con" y "de"my_string_with_quotes = "el otro dia me dijo: \"hola, como estas?\"" # para incluir comillas dentro de una cadena de texto, se puede usar el caracter de escape \ antes de las comillas, esto le indica a python que las comillas forman parte de la cadena y no son el final de la misma

my_escape_string = "\\tEste es un sting con un caracter de escape al inicio" # para incluir el caracter de escape \ en una cadena de texto, se debe usar \\ para que python lo interprete como un caracter literal y no como el inicio de un caracter de escape
print (my_escape_string) # aca se notara el caracter de escape \ al inicio de la cadena, ya que se ha escapado correctamente con \\

## formatear cadeans de texto, para poder incluir variables dentro de una cadena de texto, se pueden usar diferentes metodos de formateo, como el metodo format() o las f-strings
# formato con format()

name, surname,age = "jhenmiller", "samaniego", 30
print("mi nombre es {} {} y tengo {} años de edad".format(name,surname,age)) ## el metodo format() permite insertar valores en una cadena de texto utilizando llaves {} como marcadores de posicion, los valores se pasan como argumentos al metodo format() en el orden correspondiente a las llaves
print ("mi nombre es %s %s y tengo %d años de edad" %(name,surname,age)) # este es otro metodo de formateo para incluir variables en una cadena de texto, se utilizan los simbolos %s para cadenas de texto y %d para numeros enteros, los valores se pasan como una tupla despues del simbolo % al final de la cadena

print ("mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años de edad") # este es un metodo mas tradicional para concatenar cadenas de texto con variables, se utiliza el operador + para unir las cadenas y se convierte la variable age a string con str() para poder concatenarla correctamente
print (f"mi nombre es {name}{surname} y tengo {age} años de edad") # f "" es una forma mas moderna y legible de formatear cadenas de texto, se coloca una f antes de las comillas y se pueden incluir las variables directamente dentro de las llaves {}, lo que hace que el codigo sea mas limpio y facil de leer

# desempaquetado de caracteres, se puede desempaquetar una cadena de texto en varias variables utilizando el operador de desempaquetado *, esto permite asignar cada caracter de la cadena a una variable diferente
nombre = "jhenmiller"
a, b, c, d, e, f, g, h, i, j = nombre # en este caso se asigna cada caracter de la cadena "jhenmiller" a una variable diferente (a,b,c,d,e,f,g,h,i,j)
print(a) # se imprime la primera variable, que contiene el primer caracter de la cadena "j"
print (i) # aca se imprime la novena variable que contine el nomveno cararcter de la cadena llamada jhenmiller, que es "l"  

# division de cadenas de texto, se divide la cadena de texto en una lista de subcadenas utilizando el metodo split(),
# este metodo toma un separador como argumento y divide la cadena en cada ocurrencia de ese separador, si no se especifica un separador
# se utiliza el espacio por defecto

nombre_slice = nombre [1:3]
print (nombre_slice) # se imprime la subcadena que es de indice 1 a 3, en este caso se muestra "he" ya que el indice 1 corresponde a la letra "h" y el indice 2 corresponde a la letra "e",
                     # el indice 3 no se incluye en la subcadena
nombre_slice = nombre [1:] # solo se especifica el indice de inicio, se obtiene la subcadena desde ese indice hasta el final de la cadena 
print (nombre_slice) # se imprime la subcadena que comienza en el indice 1 y se extiende hasta el final de la cadena, en este caso se muestra "henmiller" ya que el indice 1 corresponde a la letra "h" y se incluye todo lo que sigue hasta el final de la cadena

nombre_slice = nombre[-2] # se usa para acceder a la penultima letra de la cadena, el indice -2 se refiere al segundo caracter desde el final de la cadena, en este caso se muestra "l" ya que es la penultima letra de la cadena "jhenmiller"

## reverse de una cadena de texto, se puede inertir una cadenad de txto utilizando slicing con un paso negativo, esto permite obtener la cadena en orden invers
reverse_nombre = nombre [::-1] # el slicing con un paso negativo se indica con -1, lo que hace que se recorra la cadena de derecha a izquierda, obteniendo asi la cadena invertida
print (reverse_nombre) # aca se obtinee el nombre "jhenmiller" en orden inverso, mostrando "rellimnehj" ya que se ha recorrido la cadena desde el final hasta el principio

## funciones del sistema, python proporciona varias funciones integradas para trabajar con cadenas de texto, como upper() para convertir una cadena a mayusculas, lower() para convertir a minusculas, strip() para eliminar espacios en blanco al inicio y al final de la cadena, entre otras

print (nombre.capitalize()) # el metodo capitalize() convierte la primera letra de la cadena a mayuscula y el resto a minuscula, en este caso se muestra "Jhenmiller" ya que la primera letra "j" se ha convertido a mayuscula y el resto de las letras se han convertido a minuscula
print (nombre.upper()) # el metodo upper() convierte todas las letras de la cadena a mayusculas, en este caso se muestra "JHENMILLER" ya que todas las letras de la cadena se han convertido a mayusculas
print (nombre.count("e")) # el metodo count() se utiliza para contar el numero de ocurrencias de un caracter o una subcadena en una cadena de texto, se debe especificar el caracter o la subcadena que se desea contar como argumento del metodo count(), en este caso se muestra 2 ya que la letra "e" aparece 2 veces en la cadena "jhenmiller"
print (nombre.isnumeric()) # el metodo isnumeric() se utiliza para verificar si una cadena de texto contiene solo caracteres numericos, devuelve True si la cadena es numerica y False en caso contrario, en este caso se muestra False ya que la cadena "jhenmiller" contiene letras y no es numerica
print ("1".isnumeric())# en este caso se muestra True ya que la cadena "1" contiene solo un caracter numerico y no contiene letras ni otros caracteres, por lo tanto es considerada una cadena numerica
print (nombre.lower())# el metodo lower() convierte todas las letras de la cadena a minusculas, en este caso se muestra "jhenmiller" ya que todas las letras de la cadena se han convertido a minusculas
print (nombre.upper().isupper())# el metodo upper() convierte todas las letras de la cadena a mayusculas, y luego el metodo isupper() verifica si todas las letras de la cadena son mayusculas, devuelve True si todas las letras son mayusculas y False en caso contrario, en este caso se muestra True ya que despues de convertir la cadena a mayusculas, todas las letras son mayusculas y el metodo isupper() devuelve True




