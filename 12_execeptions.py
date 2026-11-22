# excepciones handling##3

number1= 5
number2= "4"
number3= 50

try:  ## se ejecuta el codigo del primer bloque,al primer error salta directamente al execept
    print(number1 + number2)
    print("no ocurrio ningun error")
except: ## se ejecuta inmediatamente luego de que ocurra el error en el primer bloque
    print("atrapamos error con except")

else: # opcioonal y se ejeuta sino se cumple el execept
    print("la ejecucion continua correctamente con el else")

finally:
    print("la ejecucino continua con finally") ## una vez declarado se ejecuta siempre

#print(number1 + number2)

### captura de execepciones por tipo de datos#####
try:
    print(number1 + number2)

except TypeError:  ##captura errores por tipo de datos diferente
    print("se atrapo un error de tipo de variable")
except ValueError: # atrapa errores de valor, sino se da el tipo de value,lo ignora
    print("atrapa errores de valor")

    ### captura de la informacion del error para saber que salio mal#####
    ## para informar al usuario, por logs, analiticas que nos diga donde ocurrio un error
print("imprimiendo informacion del error")
try:
    print(number1 + number2)
    print("no se ha producido un error")
except ValueError as error: # objeto error que nos dara informacion del error,que es lo que ha pasado
    print(error)            ## que es lo que ha provocado el error


except Exception as ExceptionError:  ## atrapa cualquier error y se puede declarar con cualquier nombre as error, execeptionError
    print(ExceptionError)            ##error es un nombre de variable que conytine la info del error atrapado



