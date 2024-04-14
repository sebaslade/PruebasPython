### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (19, 1.70,"Sebastián", "Laos")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Laos"))
print(my_tuple.index(19))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Laos Company"
my_tuple.insert(1, "Red")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
