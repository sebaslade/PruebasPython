### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [30,19,17,18,20]

print(my_list)
print(len(my_list))

my_other_list = [19, 1.70,"Sebastián", "Laos"]

print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-1])

print(my_other_list.count("Laos"))

edad, altura, nombre, apellido = my_other_list

print(edad)

print(my_list + my_other_list)