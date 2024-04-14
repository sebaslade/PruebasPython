### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [30,19,17,18,20,16,20,25]

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

print([1,2,3,4])

my_other_list.append("sebasladev")
print(my_other_list)

my_other_list.insert(1, "Red")
print(my_other_list)

my_other_list.remove('Red') #->> solo elimina el primer elemento que encuentre en la lista
print(my_other_list)

print(my_list)
my_list.pop() #-->> solo extrae el último elemento agregado a la lista
print(my_list.pop())

print(my_list.pop(2)) #->>
print(my_list)

#Eliminar el elemento de la lista
del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear() # ->>Vacía toda la lista 
print(my_list)
print(my_new_list) # -> copio la lista

my_new_list.reverse()
print(my_new_list)

my_new_list.sort() # -> ordena de menor a mayor
print(my_new_list)

print(my_new_list[1:3]) # -> sublistas
