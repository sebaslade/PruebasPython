### Strings

my_string = 'My String'
my_other_string = "My String"

print(len(my_string))
print(len(my_other_string))


my_new_line_string = "Texto con \nsalto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un texto con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un texto \nescapado"
print(my_scape_string)

# Formateo

# %s -> Strings
# %d -> integers
# %f -> floating
# %.number of digitsf -> floatings con precicion fija

# Solo texto
name, surname, age = 'Sebastián','Laos',19
print("Mi primer nombre es " + name + " " + surname +" y mi edad es " + str(age)) # <- al de siempre
print("Mi primer nombre es {} {} y mi edad es {}".format(name, surname,age)) # <- extrae con el tipo de dato
print("Mi primer nombre es %s %s y mi edad es %d" %(name, surname, age)) # <- formatea el tipo de dato a string
print(f"Mi primer nombre es {name} {surname} y mi edad es {age}") # <- inferencia el tipo de dato

# texto y numeros
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'El area del circulo con radio %d es %.2f.' %(radius, area) # <- Se podría usar mas para los precios
print(formated_string)

# desempaquetadod de caracteres
language = 'Python'
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2] # desde el índice 0 hasta el índice 5 (inclusive), con un paso de 2
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# funciones

language = 'java'
print(language.capitalize()) # -> mayuscula el primer caracter
print(language.upper())
print(language.lower())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.upper().isupper())
print(language.lower().islower())
print(language.startswith("ja"))
