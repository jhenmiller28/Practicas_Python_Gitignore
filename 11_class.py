## practicas de clases en POO

class Person: ## definicion de una clase
    pass
    print("esto es una clase")
    pass 

print(Person)
print(Person())

class Person1: #definimos la clase, con la fucinon _init_ un constructor de clase
    def __init__(self, name, surname, alias= "sin alias"): # donde agreamos valores asociados a personas
      # pass ## el pass se deja para cuando creamos un bloque de cpodigo que no tiene valores, en este caso constructor
        self.__name = name  ## uso de self al mmismo, instancia creada luego de definir la plantialla de la clase persona
        self.__surname = surname # se le da el valor surname a la propiedad definida con  self.surname 
        self.full_name = f"{name} {surname} {alias}" ## propiedad publica
    def walk (self):
        print(f"{self.full_name} esta caminando")
    
    def get_name (self):
        return self.__name

my_person = Person1("jhenmiller","samaniego")
# print(f"{my_person.name} {my_person.surname}")
print("primera funcion")
print(my_person.full_name)
print("segunda funcion")
my_person.walk()
print("111111111111111")
print(my_person.get_name)
print("2211111111111")
print("otra persona")
my_otra_persona = Person1("jhenmiller", "samaniegom","jhen")
print(my_otra_persona.full_name)
my_otra_persona.walk()
my_otra_persona.full_name= "hector (de leon)"
print(my_otra_persona.full_name) 
print("uso de la segunda fucnion de la clase perosna")
my_otra_persona.walk()
## dandole el valir 666 al atributo de full_name
print("cambiando de valor al atributo full name")
my_otra_persona.full_name = 666
print(my_otra_persona.full_name)
print(my_otra_persona.get_name)
my_otra_persona.walk() 



