### Sets ###

my_set = set()
my_other_set = {} #-> en principio es un diccionario

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Sebastián", "Laos", 19}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Zhare") # -> guarda elementos de manera desordenada
my_other_set.add(20) # -> un set no admite repetidos

print(my_other_set)

print("Sebastián" in my_other_set) # -> Busqueda de elementos 
print("Sebas" in my_other_set)

my_other_set.remove("Sebastián") # -> opcion a eliminar elementos
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set = {"Sebas", "Laos", 19}
my_new_list = list(my_set)
print(my_new_list)
print(my_new_list[0])

my_other_set = {"Java","JavaScript","Python","Rust"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"Typescript","C#"}))

print(my_new_set.difference(my_set))
