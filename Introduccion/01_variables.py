# Variables
variable_string = "Sebastián"
print(variable_string)

variable_int = 1
print(variable_int)

variable_boolean = True
print(variable_boolean)

my_int_to_str_variable = str(variable_int)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print
print(variable_string, variable_int, variable_boolean)

# funcion len
print(len(variable_string))

# Variables en una sola línea

name, surname, alias, age = 'Sebastián','Laos','Zhare',19
print("Me llamo:", name, surname,", mi edad es",age ,"y mi alias es",alias)

# Inputs
first_name = input('Cual es tu nombre: ')
age = input('Cuantos años tienes: ')

print(first_name)
print(age)

# tipado dinamico
address: str = 'String'
address = 32 # Este valor prevalece
print(type(address))

# Otros tipos de variables
print(type(3.14))                                   # float
print(type(1 + 1j))                                 # complex
print(type(True))                                   # boolean
print([1,2,3,4])                                    # list
print(type({'name': 'Sebastian', 'age':250}))       # dict
print(type((1,2)))                                  # tuple
print(type(zip([1,2],[3,4])))                       # set
print(type(print('Nonetype')))                      # Nonetype