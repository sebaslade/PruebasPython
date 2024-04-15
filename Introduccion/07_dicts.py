### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Sebastián",
    "Apellido": "Laos",
    "Edad": 19,
    1: "Python"
}

my_dict = {
    "Nombre": "Sebastián",
    "Apellido": "Laos",
    "Edad": 19,
    "Lenguages": {"Python","Java","Kotlin","JavaScript"}
}

print(my_dict["Nombre"])

my_dict["Nombre"] = "Matias"
print(my_dict["Nombre"])

my_dict["Calle"] = "Av. X"
print(my_dict)

del my_dict["Calle"] #-> elimina un campo del diccionario
print(my_dict)
