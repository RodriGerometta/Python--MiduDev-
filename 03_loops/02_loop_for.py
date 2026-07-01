###
# 02 - Bucles (for)
# Permiten iterar sobre una secuencia de elementos (como listas, tuplas, diccionarios, etc.) o sobre un rango de números.
###

import os

os.system("cls")

# print("Bucle for:")
# # Bucle for con una lista
# frutas = ["manzana", "banana", "naranja"]
# for fruta in frutas:
#     print(fruta)

# Bucle for en cualquier cosa que sea iterable
# for letra in "Python":
#     print(letra)

# Recuperar el indice con enumerate()
# frutas = ["manzana", "banana", "naranja"]
# for i, fruta in enumerate(frutas):
#     print(f"El indice de la fruta {fruta} es: {i}")
    
# Bucles anidados
# letras = ["A", "B", "C"]
# numeros = [1, 2, 3]

# for letra in letras:
#     for numero in numeros:
#         print(f"{letra}{numero}")


# Break
# print("Break:")
# animales = ["perro", "gato", "conejo", "hamster"]
# for i, animal in enumerate(animales):
#     if animal == "conejo":
#         print(f"¡Encontré un {animal}, estaba en el indice {i}! Deteniendo el bucle.")
#         break  # Salimos del bucle cuando encontramos el conejo
#     print(f"Revisando el animal: {animal}")
    
# Continue
# print("Continue:")
# animales = ["perro", "gato", "conejo", "hamster", "pez", "pajaro"]
# for i, animal in enumerate(animales):
#     if animal == "conejo":
#         continue  # Saltamos el resto del código en esta iteración y continuamos con la siguiente
#     print(f"Revisando el animal: {animal}")

# Comprension de listas (List comprehensions)
# animales = ["perro", "gato", "conejo", "hamster", "pez", "pajaro"]
# print("Animales originales:\n", animales)
# animales_mayusculas = [animal.upper() for animal in animales]  # Creamos una nueva lista con los nombres de los animales en mayúsculas
# print("Animales en mayúsculas:\n", animales_mayusculas)

# Ejemplo. Muestra los numeros pares de una lista usando una comprension de listas
pares = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]
print("Números pares:\n", pares)