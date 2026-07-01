###
# EJERCICIOS
###

import os

os.system("cls")  # Limpiar la consola (en Windows)

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# nueva_lista = mensaje[7:14] # Extraer los elementos desde el índice 7 hasta el 13 (excluyendo el 14)
# print("Mensaje secreto:", nueva_lista) # Resultado: ['s', 'e', 'c', 'r', 'e', 't', 'o']

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# numeros = [10, 20, 30, 40, 50]
# # Guardar el primer elemento en una variable temporal
# numeros_temp = numeros[:] # Crear una copia de la lista original para evitar modificarla directamente
# numeros_temp [0] = numeros[-1]
# numeros_temp [-1] = numeros[0]
# print("Lista original:", numeros) # Resultado: [10, 20, 30, 40, 50]
# print("Lista después del intercambio:", numeros_temp) # Resultado: [50, 20, 30, 40, 10]

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# sandwich = pan + ingredientes + pan_abajo # Concatenar las listas para crear el sándwich
# print("Sandwich de listas:", sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

# lista = [1, 2, 3]
# nueva_lista = lista + lista # Concatenar la lista consigo misma para duplicar los elementos
# print("Lista original:", lista) # Resultado: [1, 2, 3]
# print("Lista duplicada:", nueva_lista) # Resultado: [1, 2, 3, 1, 2, 3]

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

# lista = [10, 20, 30, 40, 50]
# centro = lista[len(lista) // 2] # Calcular el índice del elemento central
# print("Elemento central:", centro) # Resultado: 30

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista = [1, 2, 3, 4, 5, 6]
print("Lista original:", lista)  # Resultado: [1, 2, 3, 4, 5, 6]
mitad = len(lista) // 2  # Calcular el índice de la mitad de la lista
print(mitad)
# lista_nueva = lista[mitad-1::-1] + lista[mitad::]  # Invertir la primera mitad de la lista y concatenarla con la segunda mitad sin modificar
# print(
#     "Lista con la primera mitad invertida:", lista_nueva
# )  # Resultado: [3, 2, 1, 4, 5, 6]
lista_nueva = lista[:mitad][::-1] + lista[mitad:]  # Invertir la primera mitad de la lista y concatenarla con la segunda mitad sin modificar
print("Lista con la primera mitad invertida:", lista_nueva)  # Resultado: [3, 2, 1, 4, 5, 6]