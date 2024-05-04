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

print("Sebastián" in my_dict)
print("Nombre" in my_dict)
print("Matias" in my_dict["Nombre"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre",1,"Piso"))
print(my_new_dict)

#lista -> diccionario
my_list = ["Nombre",1,"Piso"]
list_to_dict = dict.fromkeys(my_list)
print(list_to_dict)

#creacion de la copia del diccionario
my_new_dict = dict.fromkeys(my_dict, "uno")
print(my_new_dict)

#diccionario de valores
my_values = my_new_dict

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))
