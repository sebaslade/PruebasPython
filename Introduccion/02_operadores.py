# Operadores

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(3 % 4)
print(3 // 4)   # Divide aproximando al número entero
print(2 ** 3)   # Exponente

print('Hola ' * 5)
print('Hola ' * (2 ** 3))

my_float = 2.5 * 2
print('Hola ' * int(my_float))

# Operadores comparativos

print(5 > 4)
print(3 < 4)
print(3 >= 4)
print(5 <= 4)
print(3 == 4)
print(3 != 4)

# Comparación de caracteres
print('Comparación de caracteres:')
print("hola" > "Python")
print("hola" < "Python")
print("aaaa" >= "abaa")             # Ordenación alfabetica por ASCII
print(len("aaaa") >= len("abaa"))   # Por cantidad de caracteres
print("hola" <= "Python")
print("hola" == "hola")
print("hola" != "Python")

# Operadores Lógicos
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 or "Hola" > "Python" and 4 == 4)
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # Dando prioridad de comparacion
print(not(5 > 4))